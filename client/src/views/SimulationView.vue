<template>
  <div class="flex flex-row justify-between">
    <div>
      <button
        @click="executeSimulation"
        class="rounded-lg bg-red-500 text-md py-3 px-3"
      >
        Simulate
      </button>
      <button
        @click="resetGraph"
        class="rounded-lg bg-blue-500 text-md py-3 px-3"
      >
        Reset
      </button>
    </div>
    <div>
      <button
        @click="colorBySubnet"
        class="bg-gray-700 rounded-lg text-md py-3 px-3"
      >
        Subnet
      </button>
      <button
        @click="colorByLayer"
        class="bg-green-500 rounded-lg text-md py-3 px-3"
      >
        Layer
      </button>
      <button
        @click="colorByCompromised"
        class="bg-orange-600 rounded-lg text-md py-3 px-3"
      >
        Compromised
      </button>
    </div>
  </div>
  <div class=""><svg class="network-graph"></svg></div>
</template>

<script setup>
import * as d3 from "d3";
import axios from "axios";

const color = d3.scaleOrdinal(d3.schemeCategory10);
const width = 600;
const height = 500;
const svg = d3.select(".network-graph");

const colorByCompromised = () => {
  const nodes = d3.select(".network-graph").selectAll("circle");
  nodes
    .transition()
    .duration(300)
    .attr("fill", (d) => color(d.host.compromised));
};
const colorByLayer = () => {
  const nodes = d3.select(".network-graph").selectAll("circle");
  nodes
    .transition()
    .duration(400)
    .attr("fill", (d) => color(d.layer));
};

const colorBySubnet = () => {
  const nodes = d3.select(".network-graph").selectAll("circle");
  nodes
    .transition()
    .duration(400)
    .attr("fill", (d) => color(d.subnet));
};

const executeSimulation = async () => {
  const data = await axios.post("http://localhost:8001/simulate", {
    finishTime: 3000,
    mtdInterval: 200,
    scheme: "random",
    totalNodes: 100,
  });
  resetGraph();
  const graph = data.data;
  const links = graph.links.map((d) => ({ ...d }));
  const nodes = graph.nodes.map((d) => ({ ...d }));
  const simulation = d3
    .forceSimulation(nodes)
    .force(
      "link",
      d3.forceLink(links).id((d) => d.id),
    )
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(width / 2, height / 2))
    .on("tick", ticked);

  const svg = d3
    .select(".network-graph")
    .attr("width", width)
    .attr("height", height)
    .attr("viewBox", [0, 0, width, height])
    .attr("style", "max-width: 100%; height: auto;");

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
    .attr("class", "node")
    .selectAll()
    .data(nodes)
    .join("circle")
    .attr("r", 10)
    .attr("fill", (d) => color(d.layer));

  node.append("title").text((d) => d.id);
  node.call(
    d3.drag().on("start", dragstarted).on("drag", dragged).on("end", dragended),
  );

  // Set the position attributes of links and nodes each time the simulation ticks.
  function ticked() {
    link
      .attr("x1", (d) => d.source.x)
      .attr("y1", (d) => d.source.y)
      .attr("x2", (d) => d.target.x)
      .attr("y2", (d) => d.target.y);

    node.attr("cx", (d) => d.x).attr("cy", (d) => d.y);
  }

  // Reheat the simulation when drag starts, and fix the subject position.
  function dragstarted(event) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    event.subject.fx = event.subject.x;
    event.subject.fy = event.subject.y;
  }

  // Update the subject (dragged node) position during drag.
  function dragged(event) {
    event.subject.fx = event.x;
    event.subject.fy = event.y;
  }

  // Restore the target alpha so the simulation cools after dragging ends.
  // Unfix the subject position now that it’s no longer being dragged.
  function dragended(event) {
    if (!event.active) simulation.alphaTarget(0);
    event.subject.fx = null;
    event.subject.fy = null;
  }
};

const resetGraph = () => {
  d3.selectAll(".network-graph > *").remove();
};
</script>
