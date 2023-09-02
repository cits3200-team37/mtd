<script setup>
import { ref } from 'vue';
import NavBar from "./components/NavBar.vue";
import { RouterView } from "vue-router";
// import router from "./router";
// import { onMounted } from "vue";
// ! needs to be uncommented out for prod
// onMounted(async () => {
//   console.log("mounted");
//   await router.push("/");
// });

const theme = ref('dark');
const changeTheme = (newTheme) => {
  theme.value = newTheme;
};
</script>

<template>
  <NavBar />
  <RouterView :theme="theme" @change-theme="changeTheme" />
</template>
