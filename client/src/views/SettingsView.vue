<template>
  <div class="h-[calc(100vh-36px)]">
    <p class="text-2xl pb-2">Settings page</p>
    <p class="text-md">Customise your experience, make it more enjoyable and easier to work!</p>
    <div class="flex flex-col">
      <div class="flex flex-row">
        <div v-for="theme in themes" :key="theme">
          <ThemeCard :theme="theme" />
        </div>
        <!-- <button @click="setTheme('dark')">Dark Theme</button>
      <button @click="setTheme('light')">Light Theme</button> -->
      </div>
    </div>
  </div>
</template>

<script setup>
import ThemeCard from '../components/ThemeCard.vue';
const setTheme = (theme) => {
  localStorage.setItem("user-theme", theme);
  window.dispatchEvent(
    new CustomEvent("theme-changed", {
      detail: { storage: localStorage.getItem("user-theme") },
    }),
  );
};
const themes = ["dark", "light"];
</script>
