<template>
  <div v-if="isLoading == false" class="h-[calc(100vh-36px)]">
    <h1>Statistics page</h1>
    {{ data }}
  </div>
  <div v-else>
    <h1>Loading...</h1>
  </div>
</template>

<script setup>
import { useChartStore } from "../stores/charts";
import { onMounted, ref } from "vue";

const store = useChartStore();
const data = ref();
const isLoading = ref(true);

onMounted(async () => {
  try {
    await store.requestData();
    data.value = store.data;
  } catch (error) {
    console.log(error);
  }
  isLoading.value = false;
});
</script>
