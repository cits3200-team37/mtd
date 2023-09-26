<script setup>
import { onMounted, ref } from "vue";
import FormField from "../components/FormField.vue";
import DropDown from "../components/DropDown.vue";
import ToolTip from "../components/ToolTip.vue";
import SvgIcon from "@jamescoyle/vue-icon";
import { mdiArrowLeft } from "@mdi/js";
import { mdiArrowRight } from "@mdi/js";
import * as d3 from "d3";
import { useSimulationStore } from "../stores/simulation.js";
import Modal from "../components/Modal.vue";

const simulationStore = useSimulationStore();

const isOpen = ref(true);
const showTooltip = ref(false);

const showModal = ref(false);

const isInputView = ref(true);
const toolTipOffsetX = ref(0);
const tooltipOffsetY = ref(0);

const modalServiceGraph = ref(null);
const compromisedServiceIds = ref(null);

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

const serviceNetworkHost = ref(null);

// for tooltip
const currentHost = ref({
  ip: "",
  osType: "",
  osVersion: "",
  totalUsers: 0,
  totalServices: 0,
});

onMounted(async () => {
  // load past state of network and form
  if (!simulationStore.strategies) {
    await simulationStore.getStrategies();
    console.log(simulationStore.strategies);
  }
  if (simulationStore.network && simulationStore.parameters) {
    plotNetwork(simulationStore.network);
    // NOTE: could use pinia's storeToRefs, but i think using this
    // and copying objects will be easier for everyone to understand
    form.value = { ...simulationStore.parameters };
  }
});

const closeModal = () => {
  showModal.value = false;
  serviceNetworkHost.value = null;
};
const isValid = ref(true);
const errors = ref({
  startTime: "",
  finishTime: "",
  mtdInterval: "",
  scheme: "",
  totalNodes: "",
});

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
    errors.value.finishTime =
      "Finish Time must be a number greater than Start Time";
    isValid.value = false;
  }

  if (
    !form.value.mtdInterval ||
    isNaN(form.value.mtdInterval) ||
    form.value.startTime < 0
  ) {
    errors.value.mtdInterval = "MTD Interval must be a non-negative number";
    isValid.value = false;
  }

  const validSchemes = [
    "random",
    "simultaneous",
    "alternative",
    "single",
    "None",
  ];
  if (
    !form.value.scheme ||
    !validSchemes.includes(form.value.scheme.toLowerCase())
  ) {
    errors.value.scheme =
      "Invalid scheme. Choose between random, simultaneous, alternative, single, or None.";
    isValid.value = false;
  }

  if (!form.value.totalNodes || isNaN(form.value.totalNodes)) {
    errors.value.totalNodes = "Total Nodes must be a number";
    isValid.value = false;
  } else if (parseInt(form.value.totalNodes) < 20) {
    errors.value.totalNodes = "Total Nodes must be 20 or greater";
    isValid.value = false;
  }

  if (!isValid.value) {
    return;
  }
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
    .attr("fill", (d) => color(d.layer))
    .on("dblclick", (e, d) => {
      compromisedServiceIds.value = d.host.compromisedServices;
      modalServiceGraph.value = d.host.graph;
      showModal.value = true;
    });

  node.append("title").text((d) => d.id);
  node.call(
    d3.drag().on("start", dragstarted).on("drag", dragged).on("end", dragended),
  );

  d3.selectAll(".node")
    .on("mouseover", (e, d) => {
      // NOTE: arbitrary px values cannot be used in runtime.
      // set manually with d3 and raw css
      toolTipOffsetX.value = e.clientX + 40;
      tooltipOffsetY.value = e.clientY - 50;
      const { host } = d;
      currentHost.value = { ...host };
      showTooltip.value = true;
    })
    .on("mouseout", () => {
      showTooltip.value = false;
    });
};

const plotServiceNetwork = (graphData) => {
  const { width, height } = d3
    .select("#service-network-graph")
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
    .select("#service-network-graph")
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .attr("viewBox", [0, 0, width, height]);

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

  d3.selectAll("#service-network-graph .node").on("click", (e, d) => {
    serviceNetworkHost.value = { ...d };
  });
};
</script>

<template>
  <div class="flex flex-row">
    <div v-if="isOpen">
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
    <div class="w-6 h-[calc(100vh-36px)] float-left">
      <div class="h-[calc(100vh-36px)] flex items-center justify-center">
        <div v-if="isOpen">
          <button @click="isOpen = !isOpen" class="text-text-color">
            <svg-icon type="mdi" :path="mdiArrowLeft" size="24"></svg-icon>
          </button>
        </div>
        <div v-else>
          <button @click="isOpen = !isOpen" class="text-text-color">
            <svg-icon type="mdi" :path="mdiArrowRight" size="24"></svg-icon>
          </button>
        </div>
      </div>
    </div>
    <div id="network-graph" class="flex-1 mr-2 h-[calc(100vh-36px)]"></div>
  </div>
  <transition
    enter-from-class="opacity-0"
    leave-to-class="opacity-0"
    enter-active-class="transition duration-200"
    leave-active-class="transition duration-200"
  >
    <Modal
      v-if="showModal"
      @mounted="plotServiceNetwork(modalServiceGraph)"
      @close="closeModal"
    >
      <div class="h-[40vh] divide-x-2 divide-zinc-600 flex">
        <div id="service-network-graph" class="h-full w-1/2"></div>
        <div class="h-full w-1/2">
          <div class="flex justify-center">
            <h3 class="font-semibold text-xl">Service Explorer</h3>
          </div>
          <hr class="h-[2px] my-2 mx-8 bg-zinc-600 border-0" />
          <div class="w-full px-8 h-full flex-col">
            <transition
              enter-from-class="opacity-0"
              leave-to-class="opacity-0"
              enter-active-class="transition"
              leave-active-class="transition"
              mode="out-in"
            >
              <div
                v-if="serviceNetworkHost && serviceNetworkHost.service"
                class="flex-col"
              >
                <div class="overflow-auto shadow-md rounded-lg">
                  <table
                    class="w-full text-sm text-left text-navbar-icon bg-gray-700 opacity-80"
                  >
                    <tbody class="divide-y divide-gray-500">
                      <tr>
                        <th
                          scope="row"
                          class="px-6 py-4 font-medium whitespace-nowrap text-white"
                        >
                          Name
                        </th>
                        <td class="px-6 py-4">
                          {{ serviceNetworkHost.service.name }}
                        </td>
                      </tr>
                      <tr>
                        <th
                          scope="row"
                          class="px-6 py-4 font-medium whitespace-nowrap text-white"
                        >
                          Version
                        </th>
                        <td class="px-6 py-4">
                          {{ serviceNetworkHost.service.version }}
                        </td>
                      </tr>
                      <tr>
                        <th
                          scope="row"
                          class="px-6 py-4 font-medium whitespace-nowrap text-white"
                        >
                          Port
                        </th>
                        <td class="px-6 py-4">{{ serviceNetworkHost.port }}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <br />
                <div class="overflow-auto max-h-64 shadow-md rounded-lg">
                  <table
                    class="w-full text-sm text-left text-navbar-icon bg-gray-700 opacity-80"
                  >
                    <thead class="text-xs uppercase bg-gray-600 text-gray-200">
                      <tr>
                        <th scope="col" class="px-6 py-3">ID</th>
                        <th scope="col" class="px-6 py-3">CVSS</th>
                        <th scope="col" class="px-6 py-3">Exploited</th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-gray-500">
                      <tr
                        v-for="vul in serviceNetworkHost.service
                          .vulnerabilities"
                      >
                        <td class="px-6 py-4">
                          {{ vul.id }}
                        </td>
                        <td class="px-6 py-4">
                          {{ Math.round(vul.cvss) }}
                        </td>
                        <td class="px-6 py-4">
                          {{ vul.exploited }}
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
              <div v-else-if="serviceNetworkHost">
                <p class="text-navbar-icon">
                  No information to show for node selected
                </p>
              </div>
              <div v-else>
                <p class="font-light text-navbar-icon">
                  Select a node to explore
                </p>
              </div>
            </transition>
          </div>
        </div>
      </div>
    </Modal>
  </transition>
  <ToolTip
    :showTooltip="showTooltip"
    :offsetX="toolTipOffsetX"
    :offsetY="tooltipOffsetY"
  >
    <ul>
      <li>IP: {{ currentHost.ip }}</li>
      <li>OS: {{ `${currentHost.osType} ${currentHost.osVersion}` }}</li>
      <li>
        {{
          `${currentHost.totalUsers} ${
            currentHost.totalUsers == 1 ? "User" : "Users"
          }`
        }}
      </li>
      <li>
        {{
          `${currentHost.totalServices} ${
            currentHost.totalServices == 1 ? "Service" : "Services"
          }`
        }}
      </li>
    </ul>
  </ToolTip>
</template>
