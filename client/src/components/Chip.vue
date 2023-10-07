<template>
  <div
    class="inline-flex text-white bg-teal-600 rounded-full px-3 py-px justify-center content-center cursor-default"
  >
    <span class="truncate block max-w-xs align-middle text-xs mr-2">{{
      label
    }}</span>
    <div class="cursor-pointer">
      <svg-icon
        type="mdi"
        size="20"
        :path="mdiClose"
        @click.stop="handleRemove"
      ></svg-icon>
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from "vue";
import { mdiClose } from "@mdi/js";
import SvgIcon from "@jamescoyle/vue-icon";

const props = defineProps({
  label: String,
});

const emit = defineEmits(["remove"]);

const handleRemove = () => {
  emit("remove", props.label);
};
</script>
