<script setup>
import NavBar from "./components/NavBar.vue";
import { RouterView } from "vue-router";
import DropDown from "./components/DropDown.vue";
// import router from "./router";
// import { onMounted } from "vue";
// ! needs to be uncommented out for prod
// onMounted(async () => {
//   console.log("mounted");
//   await router.push("/");

// });

</script>

<template>
  <NavBar />
  <RouterView />
  <DropDown heading="Menu" :menuOptions="['Option 1','Option 2','Option 3']" />
</template>


