<script setup>
import NavBar from "./components/NavBar.vue";
import { RouterView } from "vue-router";
import { onMounted } from "vue";
// ! needs to be uncommented out for prod
// import router from "./router";
onMounted(async () => {
  console.log("mounted");
  // await router.push("/");
});
</script>

<template>
  <NavBar />
  <RouterView />
</template>
