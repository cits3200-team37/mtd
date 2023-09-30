<template>
  <label>{{ label }}</label>
  <div
    class="p-1 mt-2 pl-2.5 border border-solid rounded-md text-black w-full bg-white hover:cursor-pointer"
    :class="{ 'mb-2.5': !isOpen, 'border-red-500 border-4': error }"
  >
    <div class="flex items-center" @click="isOpen = !isOpen">
      <div v-if="!selected">
        <span class="text-gray-400">
          {{ placeholder }}
        </span>
      </div>
      <div v-else>
        <span class="">
          {{ selected }}
        </span>
      </div>
      <div v-if="!isOpen" class="ml-auto">
        <svg-icon type="mdi" size="20" :path="mdiArrowDown"></svg-icon>
      </div>
      <div v-else class="ml-auto">
        <svg-icon type="mdi" size="20" :path="mdiArrowUp"></svg-icon>
      </div>
    </div>
  </div>
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
        :class="{ 'hover:cursor-not-allowed text-gray-500': item != 'Random' }"
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

const props = defineProps({
  label: { type: String, default: "" },
  placeholder: { type: String, default: "Select Scheme" },
  selected: { type: String, default: "Random" },
  menuOptions: {
    type: Array,
    default: () => ["Random", "Simultaneous", "Alternative", "Single", "None"],
  },
  modelValue: { type: String, default: "" },
  error: { type: String, default: "" },
});

const emit = defineEmits(["update:modelValue"]);

const isOpen = ref(false);
const selected = ref(props.modelValue);

watch(
  () => props.modelValue,
  (val) => (selected.value = val),
);

const handleClick = (item) => {
  selected.value = item;
  isOpen.value = false;
  emit("update:modelValue", item);
};
</script>

<style scoped></style>