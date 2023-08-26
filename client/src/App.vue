<script setup>
import NavBar from "./components/NavBar.vue";
import { RouterView } from "vue-router";
import router from "./router";
import { onMounted } from "vue";
// ! needs to be uncommented out for prod
// onMounted(async () => {
//   console.log("mounted");
//   await router.push("/");
// });


// /**Provide/Inject mechanism for ParamBar */
// const showParamBar = ref(true);
// provide('showParamBar', showParamBar);

// const closeParamBar = () => {
//     showParamBar.value = false;
// };
// provide('closeParamBar', closeParamBar);

// const reopenParamBar = () => {
//     showParamBar.value = true;
// };
// provide('reopenParamBar', reopenParamBar);
</script>

<template>
  <NavBar />
  <RouterView />
</template>
