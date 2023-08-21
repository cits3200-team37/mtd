<template>
    <navbar />
    <RouterView />
</template>

<script setup>
import navbar from './components/navbar.vue'
import { RouterView } from 'vue-router';
import router from './router'
import { onMounted } from 'vue';

onMounted(async () => {
    console.log('mounted')
    await router.push('/')
})

</script>
