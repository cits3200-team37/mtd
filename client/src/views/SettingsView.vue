<template>
  <div class="flex flex-col items-center h-[calc(100vh-36px)]">
    <h1>Settings page</h1>
    <h2>Theme Variants:</h2>
    <button @click="setTheme('dark')">Dark Theme</button>
    <button @click="setTheme('light')">Light Theme</button>
  </div>
</template>

<script setup>
const setTheme = (theme) => {
  localStorage.setItem("user-theme", theme);
  window.dispatchEvent(
    new CustomEvent("theme-changed", {
      detail: { storage: localStorage.getItem("user-theme") },
    }),
  );
};
</script>
