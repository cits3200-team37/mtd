<template>
  <div>
    <svg ref="svg" class="border"></svg>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import * as d3 from "d3";

const svg = ref(null);
const props = defineProps(["attackRecord"]);

// Define your colors array
const colors = ["purple", "blue", "green", "yellow", "orange", "red"];

// Convert the main dictionary and its sub-dictionaries into arrays
const attackRecord = props.attackRecord;

// Derive uniqueNames and attackActionLegend (name:color)
const uniqueNames = Array.from(new Set(Object.values(attackRecord.name)));
let attackActionLegend = null;
if (colors.length >= uniqueNames.length) {
  attackActionLegend = uniqueNames.map((name, i) => ({
    name,
    color: colors[i],
  }));
}

// Derive uniqueHosts and hostToken as arrays
const uniqueHosts = Array.from(
  new Set(Object.values(attackRecord.current_host_uuid)),
);
const hostToken = uniqueHosts.map((host, i) => ({
  host,
  token: i.toString(),
}));

const attackRecordArray = Object.values(attackRecord.current_host_uuid)
  // .filter((uuid) => uuid !== -1)
  .map((uuid, i) => ({
    uuid,
    currentHostToken: hostToken.find((entry) => entry.host === uuid).token,
    attackName: attackRecord.name[i],
    start_time: attackRecord.start_time[i],
    duration: attackRecord.duration[i],
    color: attackActionLegend.find(
      (entry) => entry.name === attackRecord.name[i],
    ).color,
  }));

// Function to create the Gantt chart with legend
const createChart = () => {
  const margin = { top: 50, right: 50, bottom: 50, left: 50 };

  // const { width, height } = d3.select(svg.value).node().getBoundingClientRect();
  const width = 800 - margin.left - margin.right;
  const height = 300 - margin.top - margin.bottom;

  const svgContainer = d3
    .select(svg.value)
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);

  // Define scales for X and Y axes
  const xScale = d3
    .scaleLinear()
    .domain([
      0,
      d3.max(attackRecordArray, (d) => d.start_time + d.duration) * 1.05,
    ])
    .range([0, width]);
  const yScale = d3
    .scaleBand()
    .domain(hostToken.map((d) => d.token))
    .range([0, height])
    .padding(0.1);

  // Create X and Y axes
  const xAxis = d3.axisBottom(xScale);
  const yAxis = d3.axisLeft(yScale);

  // Append X and Y axes to the SVG
  svgContainer
    .append("g")
    .attr("class", "x-axis")
    .attr("transform", `translate(0, ${height})`)
    .call(xAxis);
  svgContainer.append("g").attr("class", "y-axis").call(yAxis);

  // X-axis label
  svgContainer
    .append("text")
    .attr("class", "x-label")
    .attr("x", width / 2)
    .attr("y", height + 35)
    .style("text-anchor", "middle")
    .text("Time")
    .attr("fill", "white");

  // Y-axis label
  svgContainer
    .append("text")
    .attr("class", "y-label")
    .attr("x", -height / 2)
    .attr("y", -40)
    .attr("dy", "1em")
    .style("text-anchor", "middle")
    .attr("transform", "rotate(-90)")
    .text("Host")
    .attr("fill", "white");

  // Gridlines
  svgContainer
    .selectAll(".gridline")
    .data(yScale.domain())
    .enter()
    .append("line")
    .attr("class", "gridline")
    .attr("x1", 0)
    .attr("x2", width)
    .attr("y1", (d) => yScale(d) + yScale.bandwidth() / 2)
    .attr("y2", (d) => yScale(d) + yScale.bandwidth() / 2)
    .attr("stroke", "gray")
    .attr("stroke-dasharray", "5,5");

  // Create Gantt bars
  svgContainer
    .selectAll(".bar")
    .data(attackRecordArray)
    .enter()
    .append("rect")
    .attr("class", "bar")
    .attr("x", (d) => xScale(d.start_time))
    .attr("y", (d) => yScale(d.currentHostToken) + yScale.bandwidth() / 2 - 4)
    .attr("width", (d) => xScale(d.duration))
    .attr("height", 8)
    .attr("fill", (d) => d.color);

  // Create a legend
  const legend = svgContainer
    .append("g")
    .attr("class", "legend")
    .attr(
      "transform",
      `translate(10, ${height - (attackActionLegend.length * 15 + 20)})`,
    );

  // Legend border
  legend
    .append("rect")
    .attr("width", 150) // Adjust the width as needed
    .attr("height", attackActionLegend.length * 15 + 10) // Adjust the height as needed
    .attr("fill", "none") // Set fill to none to make it transparent
    .attr("stroke", "white") // Set border color
    .attr("stroke-width", 2); // Set border width

  // Legend colors
  legend
    .selectAll("rect.legend-item")
    .data(attackActionLegend)
    .enter()
    .append("rect")
    .attr("class", "legend-item")
    .attr("width", 10)
    .attr("height", 10)
    .attr("x", 5)
    .attr("y", (d, i) => i * 15 + 5)
    .attr("fill", (d) => d.color);

  // Legend names
  legend
    .selectAll("text.legend-item")
    .data(attackActionLegend)
    .enter()
    .append("text")
    .attr("class", "legend-item")
    .attr("x", 20)
    .attr("y", (d, i) => i * 15 + 15)
    .text((d) => d.name)
    .attr("fill", "white");
};

// Create the chart when the component is mounted
onMounted(() => {
  createChart();
});
</script>
