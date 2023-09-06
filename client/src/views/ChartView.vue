<template>
  <div>
    <h1>Chart page</h1>
    <div v-if="data != null">
      Updated
      <AttackbyHost :attackRecord="data" />
      <AttackOp :attackRecord="data" />
    </div>
    <div v-else>null</div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useChartStore } from "../stores/charts";
import AttackbyHost from "../components/charts/AttackbyHostChart.vue";
import AttackOp from "../components/charts/AttackOp.vue";

const store = useChartStore();
const data = ref();

onMounted(async () => {
  try {
    await store.requestData();
    data.value = store.data.attack_record;
  } catch (error) {
    console.log(error);
  }
});
</script>
