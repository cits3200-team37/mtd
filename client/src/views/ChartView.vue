<template>
  <div class="flex flex-col items-center h-[calc(100vh-36px)] overflow-y-auto">
    <div v-if="attackRecord != null && mtdRecord != null">
      <AttackbyHost :attackRecord="attackRecord" />
      <AttackOperation :attackRecord="attackRecord" />
      <MTDOperation
        v-if="store.parameters['scheme'] != 'None'"
        :mtdRecord="mtdRecord"
      />
      <div
        v-if="compromiseMetrics != null && metricsItems > 0"
        id="compMetrics"
        class="m-10 border border-navbar-icon rounded p-4 flex flex-col bg-navbar-primary scrollbar max-w-[800px]"
      >
        <!-- Title Bar -->
        <div id="metricsTitleBar" class="flex items-center justify-between">
          <div class="flex space-x-5 items-center">
            <div class="text-xl border border-[--text-color] pl-2 pr-2 rounded">
              Metrics by compromise ratio
            </div>
            <div class="text-xl border border-[--text-color] pl-2 pr-2 rounded">
              Ratio:
              {{ compromiseMetrics[itemIndex].host_compromise_ratio * 100 }}%
            </div>
          </div>
          <div class="flex space-x-2">
            <svg-icon
              v-if="itemIndex > 0"
              @click="showPreviousItem"
              type="mdi"
              size="20"
              class="rotate-90 border border-[--text-color] border-[1.5px] rounded-lg hover:bg-background-secondary hover:cursor-pointer"
              :path="mdiChevronDown"
            ></svg-icon>
            <svg-icon
              v-if="itemIndex < metricsItems - 1"
              @click="showNextItem"
              type="mdi"
              size="20"
              class="rotate--90 border border-[--text-color] border-[1.5px] rounded-lg hover:bg-background-secondary hover:cursor-pointer"
              :path="mdiChevronDown"
            ></svg-icon>
          </div>
        </div>

        <!-- Metrics Data (Fill Remaining Vertical Space) -->
        <div id="metricsData" class="mt-5 overflow-x-hidden flex-grow">
          <div
            id="metricsContainer"
            class="flex space-x-3 transition-transform duration-700 ease-in-out"
          >
            <div
              v-for="item in compromiseMetrics"
              :key="item.id"
              class="inline-block min-w-full"
            >
              <div
                class="border border-[--text-color] p-2 rounded whitespace-nowrap"
              >
                Attack Success Rate:
                {{ (item.attack_success_rate * 100).toFixed(2) }}% <br />
                MTD Execution Frequency:
                {{ (item.mtd_execution_frequency * 100).toFixed(2) }}% <br />
                Time to compromise: {{ item.time_to_compromise.toFixed(4) }}s
                <br />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <p>No data available.</p>
      <p>Please run a simualation in the simulate tab.</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from "vue";
import { useSimulationStore } from "../stores/simulation";
import AttackbyHost from "../components/charts/AttackbyHost.vue";
import AttackOperation from "../components/charts/AttackOperation.vue";
import MTDOperation from "../components/charts/MTDOperation.vue";

import SvgIcon from "@jamescoyle/vue-icon";
import { mdiChevronDown } from "@mdi/js";

const store = useSimulationStore();
const attackRecord = ref();
const mtdRecord = ref();
const compromiseMetrics = ref();
const metricsItems = ref(0);
const itemIndex = ref(0);

const showNextItem = () => {
  if (itemIndex.value < metricsItems.value - 1) {
    itemIndex.value++;
  }
};

const showPreviousItem = () => {
  if (itemIndex.value > 0) {
    itemIndex.value--;
  }
};

watch(itemIndex, (newValue) => {
  const metricsContainer = document.getElementById("metricsContainer");
  if (metricsContainer) {
    metricsContainer.style.transform = `translateX(calc(${newValue} * (-100% - 12px)))`;
  }
});

onMounted(async () => {
  try {
    attackRecord.value = store.attackRecord;
    mtdRecord.value = store.mtdRecord;
    compromiseMetrics.value = store.compromiseMetrics;
    if (compromiseMetrics.value != null) {
      metricsItems.value = compromiseMetrics.value.length;
    }
  } catch (error) {
    console.log(error);
  }
});
</script>
<style scoped>
.rotate-90 {
  transform: rotate(90deg);
}

.rotate--90 {
  transform: rotate(-90deg);
}
</style>
