<template>
  <div class="h-20 p-4 bg-black text-white cursor-pointer" @click="useScenario">
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
  scenarioValues: { type: String, default: "" },
});

const emit = defineEmits(["apply-scenario"]);

const useScenario = () => {
  emit("apply-scenario", props.scenarioValues);
};
</script>
