<template>
  <div
    class="inline-flex bg-gray-200 rounded-full px-3 py-px justify-center content-center cursor-default"
  >
    <span class="truncate block max-w-xs align-middle text-xs">{{
      label
    }}</span>
    <div class="cursor-pointer">
      <svg-icon
        type="mdi"
        size="20"
        :path="mdiCloseCircleOutline"
        @click.stop="handleRemove"
      ></svg-icon>
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from "vue";
import { mdiCloseCircleOutline } from "@mdi/js";
import SvgIcon from "@jamescoyle/vue-icon";

const props = defineProps({
  label: String,
});

const emit = defineEmits(["remove"]);

const handleRemove = () => {
  emit("remove", props.label);
};
</script>
