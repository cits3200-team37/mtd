<script setup>
import { ref } from "vue";
import D3Chart from '../components/SimView/D3Chart.vue';
import ParamBar from '../components/SimView/ParamBar/ParamBar.vue'

const showParamBar = ref(true);
</script>

<template>
    <div class="h-screen flex">
        <ParamBar v-if="showParamBar" @close="showParamBar = false" />
        <D3Chart />
    </div>
</template>

<script setup>
</script>