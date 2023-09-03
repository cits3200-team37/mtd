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
import { computed } from 'vue';
import useTheme from "../stores/useTheme.js";

const { theme, setTheme } = useTheme();

const themeClass = computed(() => {
  switch (theme.value) {
    case 'dark': return ['bg-dark-background', 'text-dark-text'];
    case 'light': return ['bg-light-background', 'text-light-text'];
    case 'blue': return ['bg-blue-background', 'text-blue-text'];
    default: return [];
  }
});
</script>
