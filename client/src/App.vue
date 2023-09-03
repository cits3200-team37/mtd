<script setup>
import { ref, watch } from "vue";
import NavBar from "./components/NavBar.vue";
import { RouterView } from "vue-router";
import useTheme from "./stores/useTheme.js";
import { onMounted } from "vue";
import TitleBar from "./components/TitleBar.vue";
// ! needs to be uncommented out for prod
// import router from "./router";
onMounted(async () => {
  console.log("mounted");
  // await router.push("/");
});

const { theme } = useTheme();
</script>

<template>
  <TitleBar />
  <NavBar />
  <RouterView :theme="theme" />
</template>
