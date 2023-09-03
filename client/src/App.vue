<script setup>
import { ref, watch } from "vue";
import NavBar from "./components/NavBar.vue";
import { RouterView } from "vue-router";
import useTheme from "./stores/useTheme.js";
// import router from "./router";
// import { onMounted } from "vue";
// ! needs to be uncommented out for prod
// onMounted(async () => {
//   console.log("mounted");
//   await router.push("/");
// });

const { theme } = useTheme();
</script>

<template>
  <NavBar />
  <RouterView :theme="theme" />
</template>
