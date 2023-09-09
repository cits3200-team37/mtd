<template>
  <div class="flex flex-col items-center h-[calc(100vh-36px)]">
    <div v-if="data != null">
      <AttackbyHost :attackRecord="data" />
      <AttackOperation :attackRecord="data" />
    </div>
    <div v-else>
      <p>No data available.</p>
      <p>Please run a simualation in the simulate tab.</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useSimulationStore } from "../stores/simulation";
import AttackbyHost from "../components/charts/AttackbyHost.vue";
import AttackOperation from "../components/charts/AttackOperation.vue";

const store = useSimulationStore();
const data = ref();

onMounted(async () => {
  try {
    data.value = store.attackRecord;
  } catch (error) {
    console.log(error);
  }
});
</script>
