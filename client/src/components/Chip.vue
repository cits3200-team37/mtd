<template>
  <div class="chip-container inline-flex bg-gray-200 rounded-full px-2 py-1">
    <span class="chip-label">{{ label }}</span>
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

<style scoped>
.chip-container {
  max-width: 100px; 
}

.chip-label {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  max-width: 100px; 
  display: inline-block;
  vertical-align: middle;
}
</style>
