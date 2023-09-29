<script setup>
import { onMounted, ref } from "vue";
import FormField from "../components/FormField.vue";
import DropDown from "../components/DropDown.vue";
import ToolTip from "../components/ToolTip.vue";
import Scenario from "../components/Scenario.vue";
import SvgIcon from "@jamescoyle/vue-icon";
import { mdiArrowLeft } from "@mdi/js";
import { mdiArrowRight } from "@mdi/js";
import * as d3 from "d3";
import { useSimulationStore } from "../stores/simulation.js";

const simulationStore = useSimulationStore();

const showTooltip = ref(false);

const isInputView = ref(true);

const currentHost = ref({
  ip: "",
  osType: "",
  osVersion: "",
  totalUsers: 0,
  totalServices: 0,
  compromised: false,
});

const form = ref({
  startTime: "",
  finishTime: "",
  mtdInterval: "",
  scheme: "",
  totalNodes: "",
  totalLayers: "",
  totalEndpoints: "",
  totalSubnets: "",
  totalDatabase: "",
  targetLayer: "",
  terminateCompromiseRatio: "",
  seed: "",
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

const isValid = ref(true);
const errors = ref({
  startTime: "",
  finishTime: "",
  mtdInterval: "",
  scheme: "",
  totalNodes: "",
});

const showScenario = ref(true);

const handleSubmit = async () => {
  // Reset errors
  Object.keys(errors.value).forEach((key) => {
    errors.value[key] = "";
  });

  if (
    !form.value.startTime ||
    isNaN(form.value.startTime) ||
    form.value.startTime < 0
  ) {
    errors.value.startTime = "Start Time must be a non-negative number";
    isValid.value = false;
  }

  if (
    !form.value.finishTime ||
    isNaN(form.value.finishTime) ||
    form.value.finishTime <= form.value.startTime
  ) {
    errors.value.finishTime = "Finish Time must be greater than start time";
    isValid.value = false;
  }

  if (
    !form.value.mtdInterval ||
    isNaN(form.value.mtdInterval) ||
    form.value.startTime < 0
  ) {
    errors.value.mtdInterval = "MTD Interval must be a positive number";
    isValid.value = false;
  }

  const validSchemes = [
    "random",
    "simultaneous",
    "alternative",
    "single",
    "none",
  ];
  if (
    !form.value.scheme ||
    !validSchemes.includes(form.value.scheme.toLowerCase())
  ) {
    errors.value.scheme =
      "Invalid scheme. Choose between Random, Simultaneous, Alternative, Single, or None";
    isValid.value = false;
  }

  if (!form.value.totalNodes || isNaN(form.value.totalNodes)) {
    errors.value.totalNodes = "Total Nodes must be a number";
    isValid.value = false;
  } else if (
    parseInt(form.value.totalNodes) < 20 ||
    parseInt(form.value.totalNodes) > 1000
  ) {
    errors.value.totalNodes = "Total Nodes must between 20 and 1000";
    isValid.value = false;
  }

  if (!isValid.value) {
    return;
  }

  showScenario.value = false;

  // do not look in store for existing network graph as we run a new simulation
  await simulationStore.simulate(form.value);
  resetGraph();
  plotNetwork(simulationStore.network, ".network-graph");
};

const applyPredefinedScenario = (values) => {
  for (let key in values) {
    form.value[key] = values[key];
  }
};

const color = d3.scaleOrdinal(d3.schemeCategory10);

const colorByCompromised = () => {
  const nodes = d3.select("#network-graph").selectAll("circle");
  nodes
    .transition()
    .duration(300)
    .attr("fill", (d) => color(d.host.compromised));
};

const zoom = d3.zoom().on("zoom", function () {
  d3.select("#network-zoom-area").attr("transform", d3.zoomTransform(this));
});

const resetZoom = () => {
  d3.select("#network-zoom-area")
    .transition()
    .duration(750)
    .call(zoom.transform, d3.zoomIdentity);
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
    .attr("id", "network-zoom-area")
    .call(zoom)
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
    .style("cursor", "pointer")
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
    <div>
      <div
        class="w-48 bg-simulation-color h-[calc(100vh-36px)] float-left px-5 pt-5 overflow-y-auto"
      >
        <div class="flex flex-row">
          <div
            class="text-xs p-1 pl-2 pr-1.5 text-center bg-background-secondary text-text-color rounded-l-md cursor-pointer"
            :class="{ 'bg-teal-500': isInputView }"
            @click="
              () => {
                isInputView = true;
              }
            "
          >
            Simulation
          </div>
          <div
            class="text-xs p-1 pr-2 pl-1.5 text-center bg-background-secondary text-text-color rounded-r-md cursor-pointer"
            :class="{ 'bg-teal-500': !isInputView }"
            @click="
              () => {
                isInputView = false;
              }
            "
          >
            Visualisation
          </div>
        </div>

        <div v-if="isInputView">
          <div class="flex flex-col items-center">
            <p class="text-lg pb-5 mt-4 text-center">Simulation Parameters</p>
            <form
              class="flex flex-col space-y-2"
              @submit.prevent="handleSubmit"
            >
              <div>
                <FormField
                  v-model="form.startTime"
                  label="Start Time"
                  placeholder="Start Time"
                  type="text"
                  :error="errors.startTime"
                />
              </div>
              <div>
                <FormField
                  v-model="form.finishTime"
                  label="Finish Time"
                  placeholder="Finish Time"
                  type="text"
                  :error="errors.finishTime"
                />
              </div>
              <div>
                <FormField
                  v-model="form.mtdInterval"
                  label="MTD Interval"
                  placeholder="MTD Interval"
                  type="text"
                  :error="errors.mtdInterval"
                />
              </div>
              <div>
                <DropDown
                  v-model="form.scheme"
                  label="Scheme"
                  :error="errors.scheme"
                />
              </div>
              <div>
                <FormField
                  v-model="form.totalNodes"
                  label="Total Nodes"
                  placeholder="Total Nodes"
                  type="text"
                  :error="errors.totalNodes"
                />
              </div>
              <p class="text-red-500 text-sm">{{ errors.totalNodes }}</p>
              <div>
                <FormField
                  v-model="form.totalLayers"
                  label="Total Layers"
                  placeholder="Total Layers"
                  type="text"
                />
              </div>
              <div>
                <FormField
                  v-model="form.totalEndpoints"
                  label="Total Endpoints"
                  placeholder="Total Endpoints"
                  type="text"
                />
              </div>
              <div>
                <FormField
                  v-model="form.totalSubnets"
                  label="Total Subnets"
                  placeholder="Total Subnets"
                  type="text"
                />
              </div>
              <div>
                <FormField
                  v-model="form.totalDatabase"
                  label="Total Databases"
                  placeholder="Total Databases"
                  type="text"
                />
              </div>
              <div>
                <FormField
                  v-model="form.targetLayer"
                  label="Target Layer"
                  placeholder="Target Layer"
                  type="text"
                />
              </div>
              <div>
                <FormField
                  v-model="form.terminateCompromiseRatio"
                  label="Compromise Ratio"
                  placeholder="Compromise Ratio"
                  type="text"
                />
              </div>
              <div>
                <FormField
                  v-model="form.seed"
                  label="Set Seed"
                  placeholder="Set Seed"
                  type="text"
                />
              </div>
              <div class="text-center">
                <button
                  class="bg-background-secondary py-1 px-4 mt-3 w-full text-center rounded-md mb-4"
                >
                  Submit
                </button>
              </div>
            </form>
          </div>
        </div>
        <div v-else>
          <div class="flex flex-col items-center">
            <p class="text-lg pb-5 mt-4 text-center">Network Graph Options</p>
            <button
              @click="colorByLayer"
              class="bg-background-secondary py-1 px-4 mt-3 w-full text-center rounded-md mb-4"
            >
              Color By Layer
            </button>
            <button
              @click="colorBySubnet"
              class="bg-background-secondary py-1 px-4 mt-3 w-full text-center rounded-md mb-4"
            >
              Color By Subnet
            </button>
            <button
              @click="colorByCompromised"
              class="bg-background-secondary py-1 px-4 mt-3 w-full text-center rounded-md mb-4"
            >
              Color by Compromised
            </button>
            <button
              @click="resetZoom"
              class="bg-background-secondary py-1 px-4 mt-3 w-full text-center rounded-md mb-4"
            >
              Reset Zoom
            </button>
          </div>
        </div>
      </div>
    </div>

    <div class="flex-1 flex flex-col mr-2 h-[calc(100vh-36px)]">
      <div
        id="network-graph"
        class="flex-1 mr-2 h-[calc(100vh-36px - (showScenario ? 56px : 0px))]"
      ></div>

      <div
        v-if="showScenario"
        class="w-full p-4 grid grid-cols-2 gap-3 max-h-52"
      >
        <Scenario
          :scenarioTitle="'Scenario 1'"
          :scenarioDescription="'Random Scheme'"
          :scenarioValues="{
            startTime: '0',
            finishTime: '1000',
            mtdInterval: '200',
            scheme: 'random',
            totalNodes: '20',
          }"
          @apply-scenario="applyPredefinedScenario"
        />
        <Scenario
          :scenarioTitle="'Scenario 2'"
          :scenarioDescription="'Simultaneous Scheme'"
          :scenarioValues="{
            startTime: '0',
            finishTime: '500',
            mtdInterval: '100',
            scheme: 'simultaneous',
            totalNodes: '50',
          }"
          @apply-scenario="applyPredefinedScenario"
        />
        <Scenario
          :scenarioTitle="'Scenario 3'"
          :scenarioDescription="'Alternative Scheme'"
          :scenarioValues="{
            startTime: '0',
            finishTime: '300',
            mtdInterval: '50',
            scheme: 'alternative',
            totalNodes: '100',
          }"
          @apply-scenario="applyPredefinedScenario"
        />
        <Scenario
          :scenarioTitle="'Scenario 4'"
          :scenarioValues="{
            startTime: '0',
            finishTime: '400',
            mtdInterval: '150',
            scheme: 'none',
            totalNodes: '70',
          }"
          @apply-scenario="applyPredefinedScenario"
        />
      </div>
    </div>
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
