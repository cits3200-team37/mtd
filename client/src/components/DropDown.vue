<template>
  <label>{{ label }}</label>
  <div
    class="p-1 mt-2 pl-2.5 border border-solid rounded-md text-black w-full bg-white hover:cursor-pointer"
    :class="{ 'mb-2.5': !isOpen, 'border-red-500 border-4': error }"
  >
    <div class="flex items-center" @click="isOpen = !isOpen">
      <div v-if="!selectedItems[0]">
        <span class="text-gray-400">
          {{ placeholder }}
        </span>
      </div>
      <div v-else>
        <div v-if="multiSelect">
          <Chip
            v-for="item in selectedItems"
            :key="item"
            :label="item"
            @remove="handleChipRemove"
          />
        </div>
        <div v-else>
          <span>{{ selectedItems[0] }}</span>
        </div>
      </div>
      <div v-if="!isOpen" class="ml-auto">
        <svg-icon type="mdi" size="20" :path="mdiArrowDown"></svg-icon>
      </div>
      <div v-else class="ml-auto">
        <svg-icon type="mdi" size="20" :path="mdiArrowUp"></svg-icon>
      </div>
    </div>
  </div>
  <p v-if="error" class="text-red-500 text-sm">{{ error }}</p>
  <div
    v-if="isOpen"
    class="z-10 rounded-md bg-white shadow-md w-full transition overflow-hidden"
  >
    <ul class="divide-y divide-gray-200">
      <li
        v-for="(item, index) in menuOptions"
        :key="index"
        class="px-4 py-2 text-sm text-black leading-5 hover:bg-gray-50 focus:outline-none focus:bg-gray-50 hover:cursor-pointer"
        @click="handleClick(item)"
        :class="{
          'hover:cursor-not-allowed text-gray-500': item != 'Random',
          'font-bold': isSelected(item),
        }"
      >
        <!-- todo change :class when we have all methods working -->
        {{ item }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { defineProps, defineEmits, ref, watch } from "vue";
import SvgIcon from "@jamescoyle/vue-icon";
import { mdiArrowDown, mdiArrowUp } from "@mdi/js";
import Chip from "./Chip.vue";

const props = defineProps({
  label: { type: String, default: "" },
  placeholder: { type: String, default: "" },
  menuOptions: { type: Array, default: () => [] },
  modelValue: { type: Array, default: () => [] },
  error: { type: String, default: "" },
  multiSelect: { type: Boolean, default: false },
  maxSelection: { type: Number, default: Infinity },
});

const emit = defineEmits(["update:modelValue"]);

const isOpen = ref(false);
// Check whether it is string(scheme) or array(strategy)
const selectedItems = ref(
  Array.isArray(props.modelValue) ? props.modelValue : [props.modelValue]
);

watch(
  () => props.modelValue,
  (newVal) => {
    selectedItems.value = Array.isArray(newVal) ? [...newVal] : [newVal];
  }
);

const handleClick = (item) => {
  if (props.multiSelect) {
    if (selectedItems.value.includes(item)) {
      selectedItems.value = selectedItems.value.filter((i) => i !== item);
    } else if (selectedItems.value.length < props.maxSelection) {
      selectedItems.value.push(item);
    }
    emit("update:modelValue", selectedItems.value);
  } else {
    emit("update:modelValue", item);
    isOpen.value = false;
  }
};

const handleChipRemove = (itemToRemove) => {
  selectedItems.value = selectedItems.value.filter(
    (item) => item !== itemToRemove
  );
  emit("update:modelValue", selectedItems.value);
};

const isSelected = (item) => selectedItems.value.includes(item);
</script>
