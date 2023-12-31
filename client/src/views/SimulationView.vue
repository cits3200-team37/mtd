<script setup>
import { onMounted, ref, nextTick } from "vue";
import FormField from "../components/FormField.vue";
import DropDown from "../components/DropDown.vue";
import ToolTip from "../components/ToolTip.vue";
import Scenario from "../components/Scenario.vue";
import * as d3 from "d3";
import { useSimulationStore } from "../stores/simulation.js";
import Modal from "../components/Modal.vue";
import SvgIcon from "@jamescoyle/vue-icon";
import { mdiChevronDown, mdiLoading } from "@mdi/js";

const simulationStore = useSimulationStore();
const isAbleToSwap = ref(false);

const graph = ref(true);
const isOpen = ref(false);
const loading = ref(false);

const Schemes = ref([
  "None",
  "random",
  "single",
  "simultaneous",
  "alternative",
]);

const showTooltip = ref(false);

const showModal = ref(false);

const isInputView = ref(true);
const toolTipOffsetX = ref(0);
const tooltipOffsetY = ref(0);

const modalServiceGraph = ref(null);
const compromisedServiceIds = ref(null);

const defaultForm = ref({
  startTime: null,
  finishTime: null,
  mtdInterval: null,
  scheme: null,
  strategies: [],
  totalNodes: null,
  totalLayers: null,
  totalEndpoints: null,
  totalSubnets: null,
  totalDatabase: null,
  targetLayer: null,
  seed: null,
  strategies: [],
});

const activeGraphOption = ref("layer");

const serviceNetworkHost = ref(null);

// for tooltip
const currentHost = ref({
  ip: "",
  osType: "",
  osVersion: "",
  totalUsers: 0,
  totalServices: 0,
});

const form = ref({ ...defaultForm.value });
const strategies = ref(null);

const resetStrategy = () => {
  form.value.strategies = [];
};

const toggleDropDown = () => {
  isOpen.value = !isOpen.value;
};

const maxSelection = (scheme) => {
  switch (scheme) {
    case "None":
    case "random":
      return 0;
    case "single":
      return 1;
    case "alternative":
      return 2;
    case "simultaneous":
      return strategies.value.length;
    default:
      return 0;
  }
};

onMounted(async () => {
  // load past state of network and form
  if (!simulationStore.strategies) {
    loading.value = true;
    await simulationStore.getStrategies();
    loading.value = false;
  }
  strategies.value = [...simulationStore.strategies];
  if (simulationStore.network && simulationStore.parameters) {
    plotNetwork(simulationStore.network);
    // NOTE: could use pinia's storeToRefs, but i think using this
    // and copying objects will be easier for everyone to understand
    form.value = { ...simulationStore.parameters };
  } else {
    graph.value = false;
  }
});

const closeModal = () => {
  showModal.value = false;
  serviceNetworkHost.value = null;
};
const isValid = ref(true);
const errors = ref({
  scheme: "",
  mtdInterval: "",
  finishTime: "",
  totalNodes: "",
  totalLayers: "",
  totalEndpoints: "",
  totalSubnets: "",
  totalDatabase: "",
  targetLayer: "",
  seed: "",
});

const handleSubmit = async () => {
  // Reset errors
  isValid.value = true;
  Object.keys(errors.value).forEach((key) => {
    errors.value[key] = "";
  });

  const finishTime = Number(form.value.finishTime);
  const mtdInterval = Number(form.value.mtdInterval);
  const totalNodes = Number(form.value.totalNodes);
  const totalLayers = Number(form.value.totalLayers);
  const totalEndpoints = Number(form.value.totalEndpoints);
  const totalSubnets = Number(form.value.totalSubnets);
  const totalDatabase = Number(form.value.totalDatabase);
  const targetLayer = Number(form.value.targetLayer);

  if (!form.value.scheme) {
    errors.value.scheme = "Please pick a Scheme";
    isValid.value = false;
  }

  if (
    form.value.scheme &&
    form.value.scheme != "None" &&
    form.value.scheme != "random"
  ) {
    const maxStrategies = maxSelection(form.value.scheme);

    if (!form.value.strategies || form.value.strategies.length == 0) {
      errors.value.strategies = "Please select at least one Strategy";
      isValid.value = false;
    } else if (
      form.value.scheme == "alternative" &&
      form.value.strategies.length != 2
    ) {
      errors.value.strategies =
        "Please select exactly 2 Strategies for the 'alternative' scheme";
      isValid.value = false;
    } else if (form.value.strategies.length > maxStrategies) {
      errors.value.strategies = `You can select up to ${maxStrategies} strategies for this scheme`;
      isValid.value = false;
    }
  }

  if (isNaN(mtdInterval) || mtdInterval <= 0) {
    errors.value.mtdInterval = "Stable test limit: MTD Interval > 0";
    isValid.value = false;
  }

  if (isNaN(finishTime) || finishTime < 10 || finishTime > 5000) {
    errors.value.finishTime = "Stable test limit: 10 <= Finish Time <= 5000";
    isValid.value = false;
  }

  if (isNaN(totalNodes) || totalNodes < 20 || totalNodes > 1000) {
    errors.value.totalNodes = "Stable test limit: 20 <= Total Nodes <= 1000";
    isValid.value = false;
  }

  if (form.value.totalEndpoints) {
    if (isNaN(totalEndpoints) || totalEndpoints <= 0) {
      errors.value.totalEndpoints = "Stable test limit: Total Endpoints > 0";
      isValid.value = false;
    } else if (isNaN(totalNodes) || totalEndpoints >= totalNodes) {
      errors.value.totalEndpoints =
        "Logical limit: Total Endpoints < Total Nodes";
      isValid.value = false;
    }
  }

  if (form.value.totalSubnets) {
    if (isNaN(totalSubnets) || totalSubnets <= 4) {
      errors.value.totalSubnets = "Stable test limit: Total Subnents > 4";
      isValid.value = false;
    } else if ((totalNodes - totalEndpoints) / (totalSubnets - 1) <= 2) {
      errors.value.totalSubnets =
        "Logical limit: (Total Nodes - Total Endpoints) / (Total Subnets - 1) > 2";
      isValid.value = false;
    }
  }

  if (form.value.totalDatabase) {
    if (isNaN(totalDatabase)) {
      errors.value.totalDatabase = "Total Database must be a number";
      isValid.value = false;
    }
  }

  if (form.value.totalLayers) {
    if (isNaN(totalLayers) || totalLayers <= 0 || totalLayers > 6) {
      errors.value.totalLayers = "Stable test limit: 0 < Total Layers <= 6";
      isValid.value = false;
    }
  }

  if (form.value.targetLayer) {
    if (isNaN(targetLayer)) {
      errors.value.targetLayer = "Logical Limit: Target Layer > 0";
      isValid.value = false;
    } else if (isNaN(totalLayers) || totalLayers < targetLayer) {
      errors.value.targetLayer = "Logical Limit: Target Layer <= Total Layers";
      if (errors.value.totalLayers == "") {
        errors.value.totalLayers = "Required";
      }
      isValid.value = false;
    }
  }

  if (!isValid.value) {
    return;
  }

  loading.value = true;
  // do not look in store for existing network graph as we run a new simulation
  await simulationStore.simulate(form.value);
  loading.value = false;
  graph.value = true;
  await nextTick();
  resetGraph();
  plotNetwork(simulationStore.network, ".network-graph");
  activeGraphOption.value = "layer";
  isAbleToSwap.value = true;
};

const resetSimulation = () => {
  // Reset the form values
  form.value = { ...defaultForm.value };

  graph.value = false;
  resetGraph();

  simulationStore.reset();
  isAbleToSwap.value = false;
};

const applyPredefinedScenario = (values) => {
  for (let key in values) {
    form.value[key] = values[key];
  }
};

const color = d3.scaleOrdinal(d3.schemeCategory10);

const colorByCompromised = () => {
  activeGraphOption.value = "compromised";
  const nodes = d3.select("#network-graph").selectAll("circle");
  nodes
    .transition()
    .duration(300)
    .attr("fill", (d) => {
      if (d.host.compromised) {
        return "#FF0000";
      } else {
        return "#50C878";
      }
    });
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
  activeGraphOption.value = "layer";
  const nodes = d3.select("#network-graph").selectAll("circle");
  nodes
    .transition()
    .duration(400)
    .attr("fill", (d) => color(d.layer));
};

const colorBySubnet = () => {
  activeGraphOption.value = "subnet";
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
      currentHost.value = { ...host, subnet: d.subnet, layer: d.layer };
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
    .force("charge", d3.forceManyBody().strength(-50))
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
const toggleView = () => {
  if (
    simulationStore.parameters == null ||
    simulationStore.network == null ||
    simulationStore.attackRecord == null
  ) {
    return;
  } else {
    isInputView.value = !isInputView.value;
  }
};
</script>

<template>
  <div class="flex flex-row">
    <div>
      <div class="w-64 bg-simulation-color h-[calc(100vh-36px)] float-left px-5 pt-5 overflow-y-scroll scrollbar">
        <div class="flex flex-row">
          <div
            class="text-xs p-1 pl-2 pr-1.5 text-center bg-background-secondary text-text-color rounded-l-md cursor-default w-1/2"
            :class="{
              'bg-sub-color': isInputView,
              'cursor-pointer': isAbleToSwap == true,
            }" @click="toggleView">
            Simulation
          </div>
          <div
            class="text-xs p-1 pr-2 pl-1.5 text-center bg-background-secondary text-text-color rounded-r-md cursor-default w-1/2"
            :class="{
              'bg-sub-color': !isInputView,
              'cursor-pointer': isAbleToSwap == true,
            }" @click="toggleView">
            Graph
          </div>
        </div>

        <div v-if="isInputView">
          <div class="flex flex-col items-center">
            <p class="text-lg pb-5 mt-4 text-center">Simulation Parameters</p>
            <form class="flex flex-col space-y-2 text-sm" @submit.prevent="handleSubmit">
              <div @click="resetSimulation"
                class="bg-background-secondary py-1 px-4 mt-3 w-full text-center rounded-md mb-4 hover:cursor-pointer">
                Reset
              </div>
              <div>
                <DropDown placeholder="Select Scheme" v-model="form.scheme" label="Scheme"
                  info="The manner in which the simulation will employ MTD strategies." :menu-options="Schemes"
                  :error="errors.scheme" @update:modelValue="resetStrategy" />
              </div>
              <div>
                <FormField v-model="form.mtdInterval" label="MTD Interval" placeholder="MTD Interval" type="text"
                  info="The frequency of applying MTD strategies." :error="errors.mtdInterval" />
              </div>
              <div>
                <FormField v-model="form.finishTime" label="Finish Time" placeholder="Finish Time" type="text"
                  info="The maximum simulation duration." :error="errors.finishTime" />
              </div>
              <div>
                <FormField v-model="form.totalNodes" label="Total Nodes" placeholder="Total Nodes" type="text"
                  info="The number of nodes in the simulated network." :error="errors.totalNodes" />
              </div>
              <div>
                <DropDown placeholder="Select Strategy" v-model="form.strategies" label="Strategy"
                  info="The MTD Strategies the simulation will utilise." :menu-options="strategies" :isStrategy="true"
                  :multi-select="true" :error="errors.strategies" :max-selection="maxSelection(form.scheme)" />
              </div>
              <!-- advanced drop down -->
              <div class="flex flex-row justify-between">
                <p class="pb-2">Advanced</p>
                <div class="hover:cursor-pointer" @click="toggleDropDown">
                  <svg-icon type="mdi" size="18" :path="mdiChevronDown"
                    :class="{ 'rotate-180': isOpen, 'rotate-0': !isOpen }" />
                </div>
              </div>
              <hr class="pb-2 text-gray-400 " />
              <div v-if="isOpen == true" class="space-y-2">
                <div>
                  <FormField v-model="form.totalEndpoints" label="Total Endpoints" placeholder="Total Endpoints"
                    type="text" info="The number of endpoints in the simulated network. Default: 5"
                    :error="errors.totalEndpoints" />
                </div>
                <div>
                  <FormField v-model="form.totalSubnets" label="Total Subnets" placeholder="Total Subnets" type="text"
                    info="The number of sub-networks in the simulated network. Default: 8" :error="errors.totalSubnets" />
                </div>
                <div>
                  <FormField v-model="form.totalDatabase" label="Total Databases" placeholder="Total Databases"
                    type="text" info="The number of databases in the simulated network. Default: 2"
                    :error="errors.totalDatabase" />
                </div>
                <div>
                  <FormField v-model="form.totalLayers" label="Total Layers" placeholder="Total Layers" type="text"
                    info="The number of layers in the simulated network. Default: 4" :error="errors.totalLayers" />
                </div>
                <div>
                  <FormField v-model="form.targetLayer" label="Target Layer" placeholder="Target Layer" type="text"
                    info="The layer where the target host will be located." :error="errors.targetLayer" />
                </div>
                <div>
                  <FormField v-model="form.seed" label="Set Seed" placeholder="Set Seed" type="text"
                    :error="errors.seed" />
                </div>
              </div>
              <div class="text-center">
                <button class="bg-background-secondary py-1 px-4 mt-3 w-full text-center rounded-md mb-4">
                  Submit
                </button>
              </div>
            </form>
          </div>
        </div>
        <div v-else>
          <div class="flex flex-col items-center">
            <p class="text-lg pb-5 mt-4 text-center">Network Graph Options</p>
            <button @click="colorByLayer"
              class="bg-background-secondary py-1 px-4 mt-3 w-full text-center rounded-md mb-4"
              :class="{ 'bg-teal-500': activeGraphOption === 'layer' }">
              Color By Layer
            </button>
            <button @click="colorBySubnet"
              class="bg-background-secondary py-1 px-4 mt-3 w-full text-center rounded-md mb-4"
              :class="{ 'bg-teal-500': activeGraphOption === 'subnet' }">
              Color By Subnet
            </button>
            <button @click="colorByCompromised"
              class="bg-background-secondary py-1 px-4 mt-3 w-full text-center rounded-md mb-4"
              :class="{ 'bg-teal-500': activeGraphOption === 'compromised' }">
              Color by Compromised
            </button>
            <button @click="resetZoom" class="bg-background-secondary py-1 px-4 mt-3 w-full text-center rounded-md mb-4">
              Reset Zoom
            </button>
          </div>
        </div>
      </div>
    </div>

    <div class="w-full flex-1 flex flex-col ml-1 mr-1 h-[calc(100vh-36px)]">
      <div
        v-if="loading"
        class="flex flex-1 h-[calc(100vh)] items-center justify-center"
      >
        <svg-icon
          type="mdi"
          size="60"
          :path="mdiLoading"
          class="animate-spin"
        />
      </div>
      <div v-else-if="graph" id="network-graph" class="flex-1 h-[calc(100vh)] justify-center"></div>
      <div v-else class="flex-row">
        <div id="sim_explanation"
          class="flex-2 m-10 border rounded p-4 h-[calc(50vh)] overflow-y-auto bg-simulation-color scrollbar">
          <div class="h-full">
            <h1 class="font-bold ml-2">Simulation quick start guide:</h1>
          </div>
        </div>
        <div class="w-full p-10 grid grid-cols-2 gap-3 max-h-52">
          <Scenario :scenarioTitle="'Scenario 1'" :scenarioDescription="'Random Scheme'" :scenarioValues="{
            finishTime: '1000',
            mtdInterval: '200',
            scheme: 'random',
            strategies: [],
            totalNodes: '20',
          }" @apply-scenario="applyPredefinedScenario" />
          <Scenario :scenarioTitle="'Scenario 2'" :scenarioDescription="'Simultaneous Scheme'" :scenarioValues="{
            finishTime: '500',
            mtdInterval: '100',
            scheme: 'simultaneous',
            strategies: ['IP Shuffle', 'OS Diversity', 'Service Diversity'],
            totalNodes: '50',
          }" @apply-scenario="applyPredefinedScenario" />
          <Scenario :scenarioTitle="'Scenario 3'" :scenarioDescription="'Alternative Scheme'" :scenarioValues="{
            finishTime: '300',
            mtdInterval: '50',
            scheme: 'alternative',
            strategies: ['IP Shuffle', 'OS Diversity'],
            totalNodes: '100',
          }" @apply-scenario="applyPredefinedScenario" />
          <Scenario :scenarioTitle="'Scenario 4'" :scenario-description="`Predefined scenario`" :scenarioValues="{
            finishTime: '400',
            mtdInterval: '150',
            scheme: 'None',
            strategies: [],
            totalNodes: '70',
          }" @apply-scenario="applyPredefinedScenario" />
        </div>
      </div>
    </div>
  </div>
  <transition enter-from-class="opacity-0" leave-to-class="opacity-0" enter-active-class="transition duration-200"
    leave-active-class="transition duration-200">
    <Modal v-if="showModal" @mounted="plotServiceNetwork(modalServiceGraph)" @close="closeModal">
      <div class="h-full divide-x-2 divide-zinc-600 flex overflow-hidden">
        <div id="service-network-graph" class="h-full w-1/2"></div>
        <div class="w-1/2 flex-col">
          <div class="flex justify-center">
            <h3 class="font-semibold text-xl">Service Explorer</h3>
          </div>
          <hr class="h-[2px] my-2 mx-8 bg-zinc-600 border-0" />
          <div class="w-full px-8 flex-1">
            <transition enter-from-class="opacity-0" leave-to-class="opacity-0" enter-active-class="transition"
              leave-active-class="transition" mode="out-in">
              <div v-if="serviceNetworkHost && serviceNetworkHost.service">
                <div class="overflow-auto shadow-md rounded-lg">
                  <table class="w-full text-sm text-left text-navbar-icon bg-gray-700 opacity-80">
                    <tbody class="divide-y divide-gray-500">
                      <tr>
                        <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap text-white">
                          Name
                        </th>
                        <td class="px-6 py-4">
                          {{ serviceNetworkHost.service.name }}
                        </td>
                      </tr>
                      <tr>
                        <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap text-white">
                          Version
                        </th>
                        <td class="px-6 py-4">
                          {{ serviceNetworkHost.service.version }}
                        </td>
                      </tr>
                      <tr>
                        <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap text-white">
                          Port
                        </th>
                        <td class="px-6 py-4">{{ serviceNetworkHost.port }}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <br />
                <div class="overflow-auto max-h-64 shadow-md rounded-lg">
                  <table class="w-full text-sm text-left text-navbar-icon bg-gray-700 opacity-80 relative">
                    <thead class="text-xs uppercase bg-gray-600 drop-shadow-md text-gray-200 sticky top-0">
                      <tr>
                        <th scope="col" class="px-6 py-3">ID</th>
                        <th scope="col" class="px-6 py-3">CVSS</th>
                        <th scope="col" class="px-6 py-3">Exploited</th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-gray-500">
                      <tr v-for="vul in serviceNetworkHost.service
                        .vulnerabilities">
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
  <ToolTip :showTooltip="showTooltip" :offsetX="toolTipOffsetX" :offsetY="tooltipOffsetY">
    <ul>
      <li>IP: {{ currentHost.ip }}</li>
      <li>OS: {{ `${currentHost.osType} ${currentHost.osVersion}` }}</li>
      <li>
        {{
          `${currentHost.totalUsers} ${currentHost.totalUsers == 1 ? "User" : "Users"
          }`
        }}
      </li>
      <li>
        {{
          `${currentHost.totalServices} ${currentHost.totalServices == 1 ? "Service" : "Services"
          }`
        }}
      </li>
      <li>Subnet: {{ currentHost.subnet }}</li>
      <li>Layer: {{ currentHost.layer }}</li>
    </ul>
  </ToolTip>
</template>

<style scoped>
.rotate-180 {
  transform: rotate(180deg);
  transition: transform 0.25s ease-in-out;
}

.rotate-0 {
  transform: rotate(0deg);
  transition: transform 0.25s ease-in-out;
}
</style>
