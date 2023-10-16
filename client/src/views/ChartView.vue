<template>
  <div class="flex flex-col items-center h-[calc(100vh-36px)] overflow-y-auto">
    <div v-if="attackRecord != null && mtdRecord != null">
      <AttackbyHost :attackRecord="attackRecord" />
      <AttackOperation :attackRecord="attackRecord" />
      <MTDOperation :mtdRecord="mtdRecord" />
    </div>
    <div v-else>
      <div
        class="flex flex-col h-[calc(100vh-36px)] items-center justify-center"
      >
        <p class="text-lg">No data available.</p>
        <p class="text-lg">Please run a simualation in the simulate tab.</p>
        <div>
          <a
            @click="toSimulateView()"
            class="flex flex-col items-center mt-5 fill-current text-text-color hover:cursor-pointer"
          >
            <div class="h-12 w-12">
              <svg viewBox="0 0 24 24">
                <path :d="mdiGraphOutline"></path>
              </svg>
            </div>
            <span class="text-xs pt-1">Simulate</span>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useSimulationStore } from "../stores/simulation";
import AttackbyHost from "../components/charts/AttackbyHost.vue";
import AttackOperation from "../components/charts/AttackOperation.vue";
import MTDOperation from "../components/charts/MTDOperation.vue";
import { mdiGraphOutline } from "@mdi/js";
import { useRouter } from "vue-router";

const store = useSimulationStore();
const attackRecord = ref();
const mtdRecord = ref();
const router = useRouter();

onMounted(async () => {
  try {
    attackRecord.value = store.attackRecord;
    mtdRecord.value = store.mtdRecord;
  } catch (error) {
    console.log(error);
  }
});

const toSimulateView = async () => {
  await router.push("/simulation");
};
</script>
