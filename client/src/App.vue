<script setup>
import { ref, provide } from 'vue';
import NavBar from './components/NavBar.vue'
import { RouterView } from 'vue-router';
import router from './router'
import { onMounted } from 'vue';

onMounted(async () => {
    console.log('mounted');
    await router.push('/');
});


/**Provide/Inject mechanism for ParamBar */
const showParamBar = ref(true);
provide('showParamBar', showParamBar);

const closeParamBar = () => {
    showParamBar.value = false;
};
provide('closeParamBar', closeParamBar);

const reopenParamBar = () => {
    showParamBar.value = true;
};
provide('reopenParamBar', reopenParamBar);
</script>

<template>
    <div class="flex">
      <div>
        <NavBar /> <!-- NavBar with its own size -->
      </div>
      <div class="flex-1">
        <RouterView /> <!-- RouterView takes up the remaining space -->
      </div>
    </div>
  </template>
  
  