<template>
  <div
    class="inline-flex items-center text-white rounded-full bg-sub-color text-center justify-center content-center cursor-default py-1 px-3 my-0.5"
  >
    <span
      class="block max-w-xs align-middle text-xs mr-2 justify-self-center self-center"
      >{{ label }}</span
    >
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
