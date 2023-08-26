<template>
  <div v-if="isLoading == false">
    <h1>Statistics page</h1>
    {{ data }}
  </div>
  <div v-else>
    <h1>Loading...</h1>
  </div>
</template>

<script setup>
import { useChartStore } from '../stores/charts';
import { onMounted, ref } from 'vue';
import * as d3 from 'd3';
// console.log(d3);
const store = useChartStore();
const data = ref();
const isLoading = ref(true);

onMounted(async () => {
  try {
    await store.requestData();
    data.value = store.data;
    await mtd_operation();
  } catch (error) {
    console.log(error);
  }
  isLoading.value = false;
  // console.log(JSON.parse(data.value[0]));

});

const mtd_operation = async () => {
  console.log(data.value);
  // const record = data.value[0];
  // const colors = ["blue", "green", "orange"];
  // const mtd_action_legend = []
  // const mtd_action_legend_name = []
  // record['executed_at'].forEach((element) => {
  //   console.log(element);
  // })
}
</script>
