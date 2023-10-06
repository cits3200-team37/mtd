<template>
  <div class="inline-flex bg-gray-200 rounded-full px-3 py-1 justify-center content-center">
    <span class="truncate block max-w-[70px] align-middle">{{ label }}</span>
    <div class="">
      <svg-icon type="mdi" size="20" :path="mdiCloseCircleOutline" @click=handleRemove></svg-icon>
    </div>  
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from "vue";
import { mdiCloseCircleOutline } from '@mdi/js';
import SvgIcon from "@jamescoyle/vue-icon";

const props = defineProps({
  label: String,
});

const emit = defineEmits(["remove"]);

const handleRemove = () => {
  emit("remove", props.label);
};
</script>

<style scoped></style>
