<template>
  <div class="flex items-center justify-between">
    <label>{{ label }}</label>
    <div
      v-if="info"
      @mouseover="showInfoTooltip"
      @mouseleave="showInfo = false"
    >
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
  <p v-if="error" class="text-red-500 text-xs mt-[5px] max-w-[178px]">
    {{ error }}
  </p>
  <ToolTip :showTooltip="showInfo" :offsetX="tooltipX" :offsetY="tooltipY">{{
    info
  }}</ToolTip>
</template>

<script setup>
import { ref } from "vue";
import SvgIcon from "@jamescoyle/vue-icon";
import { mdiInformationOutline } from "@mdi/js";
import ToolTip from "./ToolTip.vue";
const props = defineProps({
  label: { type: String, default: "" },
  modelValue: { type: [String, Number], default: "" },
  placeholder: { type: String, default: "" },
  type: { type: String, default: "text" },
  error: { type: String, default: "" },
  info: { type: String, default: null },
});
const emit = defineEmits(["update:modelValue", "update"]);
const tooltipX = ref(0);
const tooltipY = ref(0);

const showInfo = ref(false);

const updateInput = (e) => {
  emit("update:modelValue", e.target.value);
  emit("update");
};
const showInfoTooltip = (e) => {
  showInfo.value = true;
  tooltipX.value = e.clientX + 25;
  tooltipY.value = e.clientY - 40;
};
</script>
