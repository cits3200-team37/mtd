<script setup>
import NavBar from "./components/NavBar.vue";
import { RouterView } from "vue-router";
import DropDown from "./components/DropDown.vue";
import { ref } from "vue";

// const selectedOption = ref('Value');

// const handleOptionSelected = (option) => {
//   selectedOption.value = option;
// };
</script>

<template>
  <NavBar />
  <RouterView />
  <DropDown heading="Menu" :menuOptions="['Option 1', 'Option 2', 'Option 3']" @emitOption="handleOptionSelected" />
  <!-- <p class="text-white">{{ selectedOption }}</p>  -->
</template>
