<script setup>
import { onMounted, ref } from "vue";
import FormField from "../components/FormField.vue";
import ToolTip from "../components/ToolTip.vue";
import SvgIcon from "@jamescoyle/vue-icon";
import { mdiArrowLeft } from "@mdi/js";
import { mdiArrowRight } from "@mdi/js";
import * as d3 from "d3";
import { useSimulationStore } from "../stores/simulation.js";

const simulationStore = useSimulationStore();

const isOpen = ref(true);
const showTooltip = ref(false);

const currentHost = ref({
  ip: "",
  osType: "",
  osVersion: "",
  totalUsers: 0,
  totalServices: 0,
  compromised: false,
});

const form = ref({
  networkSizeList: "",
  startTime: "",
  finishTime: "",
  mtdInterval: "",
  scheme: "",
  totalNodes: "",
});

onMounted(() => {
  // load past state of network and form
  if (simulationStore.network && simulationStore.parameters) {
    plotNetwork(simulationStore.network, ".network-graph");
    // NOTE: could use pinia's storeToRefs, but i think using this
    // and copying objects will be easier for everyone to understand
    form.value = { ...simulationStore.parameters };
  }
});

const handleSubmit = async () => {
  // do not look in store for existing network graph as we run a new simulation
  await simulationStore.simulate(form.value);
  resetGraph();
  plotNetwork(simulationStore.network, ".network-graph");
};

const color = d3.scaleOrdinal(d3.schemeCategory10);

const colorByCompromised = () => {
  const nodes = d3.select("#network-graph").selectAll("circle");
  nodes
    .transition()
    .duration(300)
    .attr("fill", (d) => color(d.host.compromised));
};

const colorByLayer = () => {
  const nodes = d3.select("#network-graph").selectAll("circle");
  nodes
    .transition()
    .duration(400)
    .attr("fill", (d) => color(d.layer));
};

const colorBySubnet = () => {
  const nodes = d3.select("#network-graph").selectAll("circle");
  nodes
    .transition()
    .duration(400)
    .attr("fill", (d) => color(d.subnet));
};

const resetGraph = () => {
  d3.selectAll("#network-graph > *").remove();
};

const plotNetwork = (graphData) => {
  const { width, height } = d3
    .select("#network-graph")
    .node()
    .getBoundingClientRect();

  // Set the position attributes of links and nodes each time the simulation ticks.
  const ticked = () => {
    link
      .attr("x1", (d) => d.source.x)
      .attr("y1", (d) => d.source.y)
      .attr("x2", (d) => d.target.x)
      .attr("y2", (d) => d.target.y);

    node.attr("cx", (d) => d.x).attr("cy", (d) => d.y);
  };
  // Reheat the simulation when drag starts, and fix the subject position.
  const dragstarted = (event) => {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    event.subject.fx = event.subject.x;
    event.subject.fy = event.subject.y;
  };

  // Update the subject (dragged node) position during drag.
  const dragged = (event) => {
    event.subject.fx = event.x;
    event.subject.fy = event.y;
  };

  // Restore the target alpha so the simulation cools after dragging ends.
  // Unfix the subject position now that it’s no longer being dragged.
  const dragended = (event) => {
    if (!event.active) simulation.alphaTarget(0);
    event.subject.fx = null;
    event.subject.fy = null;
  };

  // setup graph
  const links = graphData.links.map((d) => ({ ...d }));
  const nodes = graphData.nodes.map((d) => ({ ...d }));

  const simulation = d3
    .forceSimulation(nodes)
    .force(
      "link",
      d3.forceLink(links).id((d) => d.id),
    )
    .force("charge", d3.forceManyBody().strength(-10))
    .force("center", d3.forceCenter(width / 2, height / 2))
    .on("tick", ticked);

  const svg = d3
    .select("#network-graph")
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .attr("viewBox", [0, 0, width, height])
    .append("g")
    .call(
      d3.zoom().on("zoom", function () {
        svg.attr("transform", d3.zoomTransform(this));
      }),
    )
    .on("dblclick.zoom", null);

  const link = svg
    .append("g")
    .attr("stroke", "#999")
    .attr("stroke-opacity", 0.6)
    .selectAll()
    .data(links)
    .join("line")
    .attr("stroke-width", (d) => Math.sqrt(d.value));

  const node = svg
    .append("g")
    .attr("stroke", "#fff")
    .attr("stroke-width", 1.5)
    .selectAll()
    .data(nodes)
    .join("circle")
    .attr("class", "node")
    .attr("r", 8)
    .attr("fill", (d) => color(d.layer));

  node.append("title").text((d) => d.id);
  node.call(
    d3.drag().on("start", dragstarted).on("drag", dragged).on("end", dragended),
  );

  d3.selectAll(".node")
    .on("mouseover", (e, d) => {
      // NOTE: arbitrary px values cannot be used in runtime.
      // set manually with d3 and raw css
      const left = e.clientX + 40 + "px";
      const top = e.clientY - 50 + "px";
      const { host } = d;
      currentHost.value = { ...host };
      d3.select("#node-tooltip").style("left", left).style("top", top);
      showTooltip.value = true;
    })
    .on("mouseout", () => {
      showTooltip.value = false;
    });
};
</script>

<template>
  <div class="flex flex-row">
    <div v-if="isOpen">
      <div
        class="w-48 bg-navbar-primary min-h-screen border border-black border-100 float-left px-5 pt-5"
      >
        <div class="flex flex-col items-center">
          <p class="text-lg pb-5 text-center">Simulation Parameters</p>
          <form class="flex flex-col space-y-2" @submit.prevent="handleSubmit">
            <div>
              <FormField
                v-model="form.networkSizeList"
                label="Network Size List"
                placeholder="Network Size"
                type="text"
              />
            </div>
            <div>
              <FormField
                v-model="form.startTime"
                label="Start Time"
                placeholder="Start Time"
                type="text"
              />
            </div>
            <div>
              <FormField
                v-model="form.finishTime"
                label="Finish Time"
                placeholder="Finish Time"
                type="text"
              />
            </div>
            <div>
              <FormField
                v-model="form.mtdInterval"
                label="MTD Interval"
                placeholder="MTD Interval"
                type="text"
              />
            </div>
            <div>
              <FormField
                v-model="form.scheme"
                label="Scheme"
                placeholder="Scheme"
                type="text"
              />
            </div>
            <div>
              <FormField
                v-model="form.totalNodes"
                label="Total Nodes"
                placeholder="Total Nodes"
                type="text"
              />
            </div>
            <div class="text-center">
              <button
                class="bg-gray-700 py-1 px-4 mt-3 w-full text-center rounded-md mb-4"
              >
                Submit
              </button>
            </div>
          </form>
          <button
            @click="colorByLayer"
            class="bg-gray-700 py-1 px-4 mt-3 w-full text-center rounded-md mb-4"
          >
            Color By Layer
          </button>
          <button
            @click="colorBySubnet"
            class="bg-gray-700 py-1 px-4 mt-3 w-full text-center rounded-md mb-4"
          >
            Color By Subnet
          </button>
          <button
            @click="colorByCompromised"
            class="bg-gray-700 py-1 px-4 mt-3 w-full text-center rounded-md mb-4"
          >
            Color by Compromised
          </button>
        </div>
      </div>
    </div>
    <div class="w-6 min-h-screen float-left z-50">
      <div class="min-h-screen flex items-center justify-center">
        <div v-if="isOpen">
          <button @click="isOpen = !isOpen" class="text-white">
            <svg-icon type="mdi" :path="mdiArrowLeft" size="24"></svg-icon>
          </button>
        </div>
        <div v-else>
          <button @click="isOpen = !isOpen" class="text-white">
            <svg-icon type="mdi" :path="mdiArrowRight" size="24"></svg-icon>
          </button>
        </div>
      </div>
    </div>
    <div id="network-graph" class="flex-1 mr-2 my-2 max-h-screen"></div>
  </div>
  <!-- NOTE: have left the props this way so it is easier for someone to see what is in the host object -->
  <ToolTip
    id="node-tooltip"
    :showTooltip="showTooltip"
    :ip="currentHost.ip"
    :osType="currentHost.osType"
    :osVersion="currentHost.osVersion"
    :totalUsers="currentHost.totalUsers"
    :totalServices="currentHost.totalServices"
    :compromised="currentHost.compromised"
  />
</template>
