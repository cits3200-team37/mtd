<template>
  <div
    class="h-20 p-4 border border-solid rounded-lg hover:bg-hover-theme hover:cursor-pointer"
    @click="useScenario"
  >
    <h3 class="text-base font-semibold mb-2">{{ scenarioTitle }}</h3>
    <p class="text-sm">{{ scenarioDescription }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  scenarioTitle: {
    type: String,
    default: "Scenario",
  },
  scenarioDescription: {
    type: String,
    default: "Click to have a predefined scenario",
  },
  scenarioValues: { type: Object, default: {} },
});

const emit = defineEmits(["apply-scenario"]);

const useScenario = () => {
  emit("apply-scenario", props.scenarioValues);
};
</script>
