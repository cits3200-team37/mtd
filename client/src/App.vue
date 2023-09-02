<script setup>
import { ref, watch } from 'vue';
import NavBar from "./components/NavBar.vue";
import { RouterView } from "vue-router";
// import router from "./router";
// import { onMounted } from "vue";
// ! needs to be uncommented out for prod
// onMounted(async () => {
//   console.log("mounted");
//   await router.push("/");
// });

const defaultTheme = 'dark';
const theme = ref(localStorage.getItem('user-theme') || defaultTheme);

watch(theme, (newTheme) => {
  localStorage.setItem('user-theme', newTheme);
  document.body.setAttribute('data-theme', newTheme);
});

const changeTheme = (newTheme) => {
  theme.value = newTheme;
};
</script>

<template>
  <NavBar />
  <RouterView :theme="theme" @change-theme="changeTheme" />
</template>
