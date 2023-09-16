<template>
  <div
    class="fixed bottom-4 right-4 p-4 bg-black text-white cursor-pointer"
    @click="useScenario"
  >
    {{ scenarioMessage }}
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from "vue";

const props = defineProps({
  scenarioMessage: {
    type: String,
    default: "Click to have a predefined scenario",
  },
  scenarioValues: { type: Object, default: () => ({}) },
});

const emit = defineEmits(["apply-scenario"]);

const useScenario = () => {
  emit("apply-scenario", props.scenarioValues);
};
</script>
