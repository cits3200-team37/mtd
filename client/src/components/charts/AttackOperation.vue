<template>
  <div>
    <svg
      ref="svg"
      class="m-10 border border-navbar-icon rounded bg-navbar-primary"
    ></svg>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import * as d3 from "d3";

const svg = ref(null);
const props = defineProps(["attackRecord"]);

// Define your colors array
const colors = ["black", "#87FF65", "#FDCA40"];

// Convert the main dictionary and its sub-dictionaries into arrays
const attackRecord = props.attackRecord;

// Derive uniqueNames and interruptLegend (name:color)
const uniqueNames = Array.from(new Set(Object.values(attackRecord.name)));

const interruptLoc = Array.from(
  new Set(Object.values(attackRecord.interrupted_in)),
);
let interruptLegend = null;
if (colors.length >= interruptLoc.length) {
  interruptLegend = interruptLoc.map((name, i) => ({
    name,
    color: colors[i],
  }));
}

const legendData = [
  {
    name: "compromise_host",
    color: "#DF2935",
  },
  ...interruptLegend.slice(1),
];

const attackRecordArray = Object.values(attackRecord.current_host_uuid).map(
  (uuid, i) => ({
    uuid,
    attackName: attackRecord.name[i],
    start_time: attackRecord.start_time[i],
    duration: attackRecord.duration[i],
    color: "#0075F2",
  }),
);

const interruptedRecordArray = Object.values(attackRecord.interrupted_by)
  .map((interrupted_by, i) => ({
    interrupted_by,
    interrupted_in: attackRecord.interrupted_in[i],
    attackName: attackRecord.name[i],
    finish_time: attackRecord.finish_time[i],
    color: interruptLegend.find(
      (entry) => entry.name === attackRecord.interrupted_in[i],
    ).color,
  }))
  .filter((entry) => entry.interrupted_by !== "None");

const compromiseHostRecordArray = Object.values(
  attackRecord.compromise_host_uuid,
)
  .map((compromise_host_uuid, i) => ({
    compromise_host_uuid,
    compromise_host: attackRecord.compromise_host[i],
    attackName: attackRecord.name[i],
    finish_time: attackRecord.finish_time[i],
    color: "#DF2935",
  }))
  .filter((entry) => entry.compromise_host_uuid != "None");

// Function to create the Gantt chart with legend
const createChart = () => {
  const margin = { top: 75, right: 50, bottom: 50, left: 110 };
  const width = 800 - margin.left - margin.right;
  const height = 350 - margin.top - margin.bottom;
  const legendWidth = 160;

  const svgElement = window.getComputedStyle(svg.value);
  const textColor = svgElement.getPropertyValue("color");
  const bkgColor = svgElement.getPropertyValue("background-color");

  // Title
  const title = d3.select(svg.value).append("g").attr("class", "title");

  title
    .append("rect")
    .attr("x", "35%")
    .attr("y", 20)
    .attr("width", "30%")
    .attr("height", 30)
    .attr("fill", "none")
    .attr("stroke", textColor)
    .attr("stroke-width", 1)
    .attr("rx", 3)
    .attr("ry", 3);

  title
    .append("text")
    .attr("x", "50%")
    .attr("y", 40)
    .attr("text-anchor", "middle")
    .attr("fill", textColor)
    .text("Attack Operation");

  // Chart
  const chart = d3
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
    .domain(uniqueNames)
    .range([0, height])
    .padding(0.1);

  // Create X and Y axes
  const xAxis = d3.axisBottom(xScale);
  const yAxis = d3.axisLeft(yScale);

  // Append X and Y axes to the SVG
  chart
    .append("g")
    .attr("class", "x-axis")
    .attr("transform", `translate(0, ${height})`)
    .call(xAxis);
  chart.append("g").attr("class", "y-axis").call(yAxis);

  // X-axis label
  chart
    .append("text")
    .attr("class", "x-label")
    .attr("x", width / 2)
    .attr("y", height + 35)
    .style("text-anchor", "middle")
    .text("Time")
    .attr("fill", textColor);

  // Y-axis label
  chart
    .append("text")
    .attr("class", "y-label")
    .attr("x", -80)
    .attr("y", -25)
    .attr("dy", "1em")
    .style("text-anchor", "top")
    .text("Attack Type")
    .attr("fill", textColor);

  // Gridlines
  chart
    .selectAll(".gridline")
    .data(yScale.domain())
    .enter()
    .append("line")
    .attr("class", "gridline")
    .attr("x1", 0)
    .attr("x2", width)
    .attr("y1", (d) => yScale(d) + yScale.bandwidth() / 2)
    .attr("y2", (d) => yScale(d) + yScale.bandwidth() / 2)
    .attr("stroke", textColor)
    .attr("stroke-dasharray", "2,10");

  // Create Attack bars
  chart
    .selectAll(".bar")
    .data(attackRecordArray)
    .enter()
    .append("rect")
    .attr("class", "bar")
    .attr("x", (d) => xScale(d.start_time))
    .attr("y", (d) => yScale(d.attackName) + yScale.bandwidth() / 2 - 4)
    .attr("width", (d) => xScale(d.duration))
    .attr("height", 8)
    .attr("fill", (d) => d.color);

  // Create interrupt points
  chart
    .selectAll(".scatter")
    .data(compromiseHostRecordArray)
    .enter()
    .append("circle")
    .attr("class", "circle")
    .attr("cx", (d) => xScale(d.finish_time))
    .attr("cy", (d) => yScale(d.attackName) + yScale.bandwidth() / 2)
    .attr("r", 4)
    .attr("fill", "#DF2935");

  chart
    .selectAll(".scatter")
    .data(interruptedRecordArray)
    .enter()
    .append("circle")
    .attr("class", "circle")
    .attr("cx", (d) => xScale(d.finish_time))
    .attr("cy", (d) => yScale(d.attackName) + yScale.bandwidth() / 2)
    .attr("r", 4)
    .attr("fill", (d) => d.color);

  // Create a legend
  const legend = chart
    .append("g")
    .attr("class", "legend")
    .attr("transform", `translate(${width - legendWidth}, -25)`);

  // Legend border
  legend
    .append("rect")
    .attr("width", legendWidth) // Adjust the width as needed
    .attr("height", interruptLegend.length * 15 + 10) // Adjust the height as needed
    .attr("fill", bkgColor) // Set fill to none to make it transparent
    .attr("opacity", 0.8)
    .attr("stroke", textColor) // Set border color
    .attr("stroke-width", 1) // Set border width
    .attr("rx", 3)
    .attr("ry", 3);

  // Legend colors
  legend
    .selectAll("circle.legend-item")
    .data(legendData)
    .enter()
    .append("circle")
    .attr("class", "legend-item")
    .attr("width", 10)
    .attr("height", 10)
    .attr("cx", 10)
    .attr("cy", (d, i) => i * 15 + 10)
    .attr("r", 4)
    .attr("fill", (d) => d.color);

  // Legend names
  legend
    .selectAll("text.legend-item")
    .data(legendData)
    .enter()
    .append("text")
    .attr("class", "legend-item")
    .attr("x", 20)
    .attr("y", (d, i) => i * 15 + 15)
    .text((d) => d.name)
    .attr("fill", textColor);
};

// Create the chart when the component is mounted
onMounted(() => {
  createChart();
});
</script>
