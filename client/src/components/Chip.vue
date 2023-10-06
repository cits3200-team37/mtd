<template>
  <div class="inline-flex items-center bg-gray-200 rounded px-2 py-1 text-sm">
    <span>{{ label }}</span>
    <button @click="handleRemove" class="ml-1">×</button>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from "vue";

const props = defineProps({
  label: String,
});

const emit = defineEmits(["remove"]);

const handleRemove = () => {
  emit("remove", props.label);
};
</script>
