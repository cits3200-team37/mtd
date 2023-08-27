<template>
  <div class="h-screen flex">
    <!-- ParamBar component -->
    <ParamBar v-if="showParamBar" class="h-full z-50 w-16 bg-gray-200 shadow-lg"></ParamBar>
    <!-- Main content container with padding -->
    <div class="flex-1 p-4">
      <!-- Add the D3 chart container -->
      <div ref="networkContainer" class="h-full bg-white rounded-lg shadow-md"></div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, inject } from "vue";
import * as d3 from 'd3';
import ParamBar from '../components/SimView/ParamBar/ParamBar.vue'; // Import your ParamBar component

// Inject showParamBar
const showParamBar = inject('showParamBar');
console.log("showParamBar:", showParamBar.value);

const networkContainer = ref(null);

// Fetch data from localhost:8001/simulate
const fetchData = async () => {
  try {
    const response = await fetch('http://localhost:8001/simulate');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const graphData = await response.json();
    createNetworkGraph(graphData); // Pass the fetched data to createNetworkGraph
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};

// Create the D3 network graph
const createNetworkGraph = (graphData) => {
  // Access the container element
  const container = networkContainer.value;

  // Set up the D3.js SVG canvas
  const svg = d3.select(container).append('svg')
    .attr('width', '100%') // Set the width to 100% to match the container's width
    .attr('height', '100%'); // Set the height to 100% to match the container's height

  const width = container.clientWidth; // Get the container's width
  const height = container.clientHeight; // Get the container's height

  // Parse the data from the JSON
  const nodes = graphData.nodes;
  const links = graphData.links;

  // Create a force simulation for the network layout
  const simulation = d3
    .forceSimulation(nodes)
    .force('link', d3.forceLink(links).id(d => d.id))
    .force('charge', d3.forceManyBody())
    .force('center', d3.forceCenter(width / 2, height / 2));

  // Create links
  const link = svg
    .selectAll('line')
    .data(links)
    .enter()
    .append('line');

  // Create nodes
  const node = svg
    .selectAll('circle')
    .data(nodes)
    .enter()
    .append('circle')
    .attr('r', 10); // Set the radius of the nodes

  // Update the positions of nodes and links
  simulation.on('tick', () => {
    link
      .attr('x1', d => d.source.x)
      .attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x)
      .attr('y2', d => d.target.y);

    node
      .attr('cx', d => d.x)
      .attr('cy', d => d.y);
  });
};

onMounted(fetchData);
</script>

<style scoped>
/* Your component-specific styles here */
.param-bar {
  /* Adjust the styles for the ParamBar component as needed */
}

.main-container {
  flex: 1; /* Allow the container to expand and fill available space */
  padding: 20px; /* Add padding to the main container */
  position: relative; /* Position relative for child elements */
}

/* Style the D3.js SVG to fill the container */
.network-container svg {
  width: 100%;
  height: 100%;
}

/* Adjust the styles for ParamBar and other elements as needed */
</style>
