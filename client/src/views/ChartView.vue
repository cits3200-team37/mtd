<template>
  <div class="flex flex-col items-center h-[calc(100vh-36px)]">
    <div v-if="attackRecord != null && mtdRecord != null">
      <AttackbyHost :attackRecord="attackRecord" />
      <AttackOperation :attackRecord="attackRecord" />
      <MTDOperation :mtdRecord="mtdRecord" />
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
import MTDOperation from "../components/charts/MTDOperation.vue";

const store = useSimulationStore();
const attackRecord = ref();
const mtdRecord = ref();

onMounted(async () => {
  try {
    attackRecord.value = store.attackRecord;
    mtdRecord.value = store.mtdRecord
  } catch (error) {
    console.log(error);
  }
});
</script>
