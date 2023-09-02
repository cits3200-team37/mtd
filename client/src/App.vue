<script setup>
import NavBar from "./components/NavBar.vue";
import TitleBar from "./components/TitleBar.vue";
import findVersion from "./helpers/findVersion";
import { RouterView } from "vue-router";
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
