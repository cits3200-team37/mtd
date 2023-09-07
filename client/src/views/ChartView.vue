<template>
  <div>
    <h1>Chart page</h1>
    <div v-if="data != null">
      Updated
      <AttackbyHost :attackRecord="data" />
      <AttackOperation :attackRecord="data" />
    </div>
    <div v-else>null</div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useChartStore } from "../stores/charts";
import AttackbyHost from "../components/charts/AttackbyHost.vue";
import AttackOperation from "../components/charts/AttackOperation.vue";

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
