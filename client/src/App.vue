<script setup>
import NavBar from "./components/NavBar.vue";
import TitleBar from "./components/TitleBar.vue";
import { RouterView } from "vue-router";
import findVersion from "./helpers/findVersion";
import { onMounted } from "vue";
// ! needs to be uncommented out for prod
// import router from "./router";
onMounted(async () => {
  console.log("mounted");
  // await router.push("/");
  console.log(findVersion(window));
});
</script>

<template>
  <TitleBar />
  <NavBar />
  <RouterView />
</template>
