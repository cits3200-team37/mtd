<template>
  <div class="flex items-center justify-between">
    <label>{{ label }}</label>
    <div v-if="info != null" @mouseover="showInfo = true" @mouseleave="showInfo = false">
      <svg-icon type="mdi" size="18" :path="mdiInformationOutline"/>
    </div>
  </div>
  <div class="relative">
    <div v-if="info && showInfo" class="border border-[2px] rounded p-[2px] max-w-[155px] z-75 bg-background-color absolute top-full left-0 w-full mt-[5px]">
      <div v-html="info" class="text-xs"></div>
    </div>
    <div
      class="p-1 mt-2 mb-2.5 pl-2.5 border border-solid rounded-md text-black w-full bg-white hover:cursor-pointer"
      :class="{
        'border-red-500 border-4': error,
        'bg-slate-100 hover:cursor-not-allowed':
          maxSelection == 0 && isStrategy,
      }"
    >
      <div class="flex items-center" @click="toggleDropdown">
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
        class="z-50 absolute top-full left-0 w-full mt-1 rounded-md bg-white shadow-md overflow-y-auto"
      >
        <ul>
          <li
            v-for="(item, index) in menuOptions"
            :key="index"
            class="px-4 py-2 text-xs text-black leading-5 hover:bg-sub-color hover:text-black hover:cursor-pointer"
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
    <p v-if="error" class="text-red-500 text-xs mt-[5px] max-w-[178px]">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";
import SvgIcon from "@jamescoyle/vue-icon";
import { mdiChevronDown, mdiInformationOutline} from "@mdi/js";
import Chip from "./Chip.vue";

const props = defineProps({
  label: { type: String, default: "" },
  placeholder: { type: String, default: "" },
  menuOptions: { type: Array, default: () => [] },
  modelValue: { type: [Array, String], default: () => [] },
  error: { type: String, default: "" },
  isStrategy: { type: Boolean, default: false },
  multiSelect: { type: Boolean, default: false },
  maxSelection: { type: Number, default: 0 },
  info: {type: String, default: null}
});

const emit = defineEmits(["update:modelValue"]);

const showInfo = ref(false);
const isOpen = ref(false);
const selectedItems = ref([]);

watch(
  // close on new max selection value
  () => props.maxSelection,
  () => {
    isOpen.value = false;
  },
);

watch(
  () => props.modelValue,
  (newVal) => {
    selectedItems.value = Array.isArray(newVal) ? [...newVal] : [newVal];
  },
);

const toggleDropdown = () => {
  if (!props.isStrategy || (props.isStrategy && props.maxSelection != 0)) {
    isOpen.value = !isOpen.value;
  }
};

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
