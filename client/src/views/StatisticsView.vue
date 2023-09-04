<template>
  <div v-if="isLoading == false">
    <div class="flex flex-col items-center h-screen">
      <h1>Statistics page</h1>
    </div>
    {{ data }}
  </div>
  <div v-else>
    <h1>Loading...</h1>
  </div>
</template>

<script setup>
// import { computed } from "vue";
// import useTheme from "../stores/useTheme.js";
import { useChartStore } from "../stores/charts";
import { onMounted, ref } from "vue";

// const { theme } = useTheme();

// const themeClass = computed(() => {
//   switch (theme.value) {
//     case "dark":
//       return ["bg-dark-background", "text-dark-text"];
//     case "light":
//       return ["bg-light-background", "text-light-text"];
//     case "blue":
//       return ["bg-blue-background", "text-blue-text"];
//     default:
//       return [];
//   }
// });

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
