<script setup>
import NavBar from './components/NavBar.vue'
import { RouterView } from 'vue-router';
import router from './router'
import { onMounted } from 'vue';

onMounted(async () => {
    console.log('mounted');
    await router.push('/');
});
</script>

<template>
    <div class = "flex">
    <NavBar />
    <RouterView /> 
    </div>
</template>


