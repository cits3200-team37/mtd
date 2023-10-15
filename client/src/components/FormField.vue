<template>
  <div class="flex items-center justify-between">
    <label>{{ label }}</label>
    <div v-if="info != null" @mouseover="showInfo = true" @mouseleave="showInfo = false">
      <svg-icon type="mdi" size="18" :path="mdiInformationOutline" />
    </div>
  </div>
  <input
    :type="type"
    :placeholder="placeholder"
    class="p-1 mt-2 mb-2.5 pl-2.5 border border-solid rounded-md text-black w-full text-sm"
    :class="{ 'border-red-500 border-4': error }"
    @input="updateInput"
    :value="modelValue"
  />
  <div class="relative">
    <div v-if="info && showInfo" class="border border-[2px] rounded p-[2px] max-w-[155px] z-75 bg-background-color absolute top-full left-0 w-full mt-[5px]">
      <div v-html="info" class="text-xs"></div>
    </div>
  </div>
  <p v-if="error" class="text-red-500 text-xs mt-[5px] max-w-[178px]">{{ error }}</p>
</template>

<script setup>
import { ref } from "vue";
import SvgIcon from "@jamescoyle/vue-icon";
import {mdiInformationOutline} from "@mdi/js";
const props = defineProps({
  label: { type: String, default: "" },
  modelValue: { type: [String, Number], default: "" },
  placeholder: { type: String, default: "" },
  type: { type: String, default: "text" },
  error: { type: String, default: "" },
  info: {type: String, default: null},
});
const emit = defineEmits(["update:modelValue", "update"]);

const showInfo = ref(false)

const updateInput = (e) => {
  emit("update:modelValue", e.target.value);
  emit("update");
};
</script>
