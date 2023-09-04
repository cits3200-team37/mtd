<script setup>
import { ref, watch } from "vue";
import NavBar from "./components/NavBar.vue";
import { RouterView } from "vue-router";
import { onMounted } from "vue";
import TitleBar from "./components/TitleBar.vue";
const theme = ref(null);
// ! needs to be uncommented out for prod
// import router from "./router";
onMounted(async () => {
  try {
    theme.value = localStorage.getItem("user-theme");
  } catch (error) {
    console.log(error);
  }
  console.log("mounted");
  // await router.push("/");
});

window.addEventListener('theme-changed', (e) => {
  // console.log(e.detail.storage);
  theme.value = e.detail.storage;
});

</script>

<template>
  <div class="text-text-color bg-background-color">
    {{ theme }}
    <TitleBar />
    <NavBar />
    <RouterView />
  </div>
</template>
