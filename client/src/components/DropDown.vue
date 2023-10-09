<template>
  <label>{{ label }}</label>
  <div class="relative">
    <div
      class="p-1 mt-2 border border-solid rounded-md text-black w-full bg-white hover:cursor-pointer hover:border-gray-400"
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
        <div class="ml-auto">
          <svg-icon
            type="mdi"
            size="20"
            :path="mdiChevronDown"
            :class="{ 'rotate-180': isOpen, 'rotate-0': !isOpen }"
          ></svg-icon>
        </div>
      </div>
      <div
        v-if="isOpen"
        class="z-10 absolute top-full left-0 w-full mt-1 rounded-md bg-white shadow-md overflow-hidden"
      >
        <ul>
          <li
            v-for="(item, index) in menuOptions"
            :key="index"
            class="px-4 py-2 text-xs text-black leading-5 hover:bg-chip-color hover:text-black focus:outline-none focus:bg-gray-50 hover:cursor-pointer"
            @click="handleClick(item)"
            :class="{
              'font-bold': isSelected(item),
              'bg-slate-300': isSelected(item),
            }"
          >
            {{ item }}
          </li>
        </ul>
      </div>
    </div>
    <p v-if="error" class="text-red-500 text-sm">{{ error }}</p>
  </div>
</template>

<script setup>
import { defineProps, defineEmits, ref, watch } from "vue";
import SvgIcon from "@jamescoyle/vue-icon";
import { mdiChevronDown } from "@mdi/js";
import Chip from "./Chip.vue";

const props = defineProps({
  label: { type: String, default: "" },
  placeholder: { type: String, default: "" },
  menuOptions: { type: Array, default: () => [] },
  modelValue: { type: [Array, String], default: () => [] },
  error: { type: String, default: "" },
  multiSelect: { type: Boolean, default: false },
  maxSelection: { type: Number, default: 0 },
});

const emit = defineEmits(["update:modelValue"]);

const isOpen = ref(false);
const selectedItems = ref([]);

watch(
  () => props.modelValue,
  (newVal) => {
    selectedItems.value = Array.isArray(newVal) ? [...newVal] : [newVal];
  },
);

const handleClick = (item) => {
  if (props.multiSelect) {
    if (selectedItems.value.includes(item)) {
      selectedItems.value = selectedItems.value.filter((i) => i !== item);
    } else if (selectedItems.value.length < props.maxSelection) {
      selectedItems.value.push(item);
      if (selectedItems.value.length == props.maxSelection) {
        isOpen.value = false;
      }
    }
    emit("update:modelValue", selectedItems.value);
  } else {
    emit("update:modelValue", item);
    isOpen.value = false;
  }
};

const handleChipRemove = (itemToRemove) => {
  selectedItems.value = selectedItems.value.filter(
    (item) => item !== itemToRemove,
  );
  emit("update:modelValue", selectedItems.value);
};

const isSelected = (item) => selectedItems.value.includes(item);
</script>

<style scoped>
.rotate-180 {
  transform: rotate(180deg);
  transition: transform 0.25s ease-in-out;
}

.rotate-0 {
  transform: rotate(0deg);
  transition: transform 0.25s ease-in-out;
}
</style>
