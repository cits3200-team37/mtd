<script setup>
import NavBar from "./components/NavBar.vue";
import { RouterView } from "vue-router";
import DropDown from "./components/DropDown.vue"
import { ref } from "vue";

const selectedOption = ref ("") // Create a ref to store the selected option

const handleOptionSelected = (option) => {
  selectedOption.value = option; // Update the selected option when emitted from the DropDown component
};
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
  <DropDown :buttonLabel="'Options'" :menuOptions="['Option 1', 'Option 2', 'Option 3']"
    @optionSelected="handleOptionSelected" />
    <p>{{ selectedOption }}</p>
</template>
