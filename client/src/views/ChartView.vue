<template>
  <div class="flex flex-col items-center h-screen" :class="themeClass">
    <h1>Chart page</h1>
    <p>testing</p>
  </div>
</template>

<script setup>
import { computed, defineProps } from 'vue';

const props = defineProps(['theme']);

const themeClass = computed(() => {
  switch (props.theme) {
    case 'dark': return ['bg-dark-background', 'text-dark-text'];
    case 'light': return ['bg-light-background', 'text-light-text'];
    case 'blue': return ['bg-blue-background', 'text-blue-text'];
    default: return [];
  }
});
</script>
