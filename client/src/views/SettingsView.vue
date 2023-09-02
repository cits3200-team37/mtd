<template>
  <div class="flex flex-col items-center h-screen" :class="themeClass">
    <h1>Settings page</h1>
    <h2>Theme Variants:</h2>
    <button @click="setTheme('dark')">Dark Theme</button>
    <button @click="setTheme('light')">Light Theme</button>
    <button @click="setTheme('blue')">Blue Theme</button>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';
import { computed } from 'vue';

const props = defineProps(['theme']);
const emit = defineEmits();

const setTheme = (newTheme) => {
  emit('change-theme', newTheme);
};

const themeClass = computed(() => {
  switch (props.theme) {
    case 'dark': return ['bg-dark-background', 'text-dark-text'];
    case 'light': return ['bg-light-background', 'text-light-text'];
    case 'blue': return ['bg-blue-background', 'text-blue-text'];
    default: return [];
  }
});
</script>
