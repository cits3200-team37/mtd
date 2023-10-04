<template>
  <div>
    <DropDown
      placeholder="Select Strategy"
      v-model="Strategies"
      label="Strategy"
      :menu-options="availableStrategies"
      :multi-select="true"
      :max-selection="maxSelection()"
    />
  </div>
</template>

<script setup>
import { defineProps, ref, watch } from "vue";
import DropDown from "./DropDown.vue";

const props = defineProps({
  scheme: {
    type: String,
    default: "",
  },
  modelValue: {
    type: Array,
    default: () => [],
  },
  availableStrategies: {
    type: Array,
    default: () => [],
  },
});

const emit = defineEmits(["update:modelValue"]);

const Strategies = ref(props.modelValue);

watch(
  () => props.modelValue,
  (val) => (Strategies.value = val),
);

const maxSelection = () => {
  if (props.scheme == "None") {
    return 0;
  } else if (props.scheme == "random" || props.scheme == "single") {
    return 1;
  } else if (props.scheme == "alternative") {
    return 2;
  } else if (props.scheme == "simultaneous") {
    return 4;
  } else {
    return 9;
  }
};
</script>
