<script setup>
import NavBar from "./components/NavBar.vue";
import { RouterView } from "vue-router";
import DropDown from "./components/DropDown.vue";
import { ref } from "vue";

// const selectedOption = ref('Value');

// const handleOptionSelected = (option) => {
//   selectedOption.value = option;
// };

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
</script>

<template>
  <NavBar />
  <RouterView />
  <DropDown heading="Menu" :menuOptions="['Option 1', 'Option 2', 'Option 3']" @emitOption="handleOptionSelected" />
  <!-- <p class="text-white">{{ selectedOption }}</p>  -->
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
