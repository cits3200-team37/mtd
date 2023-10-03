<template>
  <div>
    <div v-if="scheme === 'random' || scheme === 'single'">
      <DropDown
        placeholder="Select Strategy"
        v-model="Strategies[0]"
        label="Strategy"
        :menu-options="availableStrategies"
      />
    </div>

    <div v-if="scheme === 'alternative'">
      <DropDown
        placeholder="Select Strategy 1"
        v-model="Strategies[0]"
        label="Strategy"
        :menu-options="availableStrategies"
      />
      <DropDown
        placeholder="Select Strategy 2"
        v-model="Strategies[1]"
        label="Strategy"
        :menu-options="availableStrategies"
      />
    </div>

    <div v-if="scheme === 'simultaneous'">
      <DropDown
        placeholder="Select Strategy 1"
        v-model="Strategies[0]"
        label="Strategy"
        :menu-options="availableStrategies"
      />
      <DropDown
        placeholder="Select Strategy 2"
        v-model="Strategies[1]"
        label="Strategy"
        :menu-options="availableStrategies"
      />
      <DropDown
        placeholder="Select Strategy 3"
        v-model="Strategies[2]"
        label="Strategy"
        :menu-options="availableStrategies"
      />
    </div>
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
</script>
