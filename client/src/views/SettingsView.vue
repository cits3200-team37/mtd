<template>
  <div class="flex flex-col items-center h-screen">
    <h1>Settings page</h1>
    <h2>Theme Variants:</h2>
    <button @click="setTheme('dark')">Dark Theme</button>
    <button @click="setTheme('light')">Light Theme</button>
    <button @click="setTheme('blue')">Blue Theme</button>
  </div>
</template>

<script setup>
import { computed, onMounted, ref, watch } from "vue";
// import useTheme from "../stores/useTheme.js";

// const { theme, setTheme } = useTheme();

onMounted(async () => {
  try {
    // console.log(findTheme());
  } catch (error) {
    console.log(error);
  }
})

const theme = ref(localStorage.getItem("user-theme"));

// watch(theme, (newTheme) => {
//   console.log(newTheme);
//   // localStorage.setItem("user-theme", newTheme);
//   // document.body.setAttribute("data-theme", newTheme);
// });

const setTheme = (theme) => {
  console.log(theme);
  localStorage.setItem("user-theme", theme);
  // document.body.setAttribute("data-theme", theme);
  window.dispatchEvent(new CustomEvent('theme-changed', { detail: { storage: localStorage.getItem('user-theme') } }));
  // setTheme(theme);
};

// const themeClass = computed(() => {
//   switch (theme.value) {
//     case "dark":
//       return ["bg-dark-background", "text-dark-text"];
//     case "light":
//       return ["bg-light-background", "text-light-text"];
//     case "blue":
//       return ["bg-blue-background", "text-blue-text"];
//     default:
//       return [];
//   }
// });
</script>
