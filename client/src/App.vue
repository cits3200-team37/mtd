<script setup>
import { ref } from "vue";
import NavBar from "./components/NavBar.vue";
import { RouterView } from "vue-router";
import { onMounted } from "vue";
import TitleBar from "./components/TitleBar.vue";
import router from "./router";
const theme = ref(null);

onMounted(async () => {
  try {
    await router.push("/");
    theme.value = localStorage.getItem("user-theme");
  } catch (error) {
    console.log(error);
  }
  // await router.push("/");
});

window.addEventListener("theme-changed", (e) => {
  theme.value = e.detail.storage;
});
</script>
<template>
  <div
    class="bg-background-color text-text-color"
    :class="{
      'theme-dark': theme == 'dark',
      'theme-light': theme == 'light',
      'theme-blue': theme == 'blue',
    }"
  >
    <TitleBar />
    <NavBar />
    <RouterView />
  </div>
</template>
