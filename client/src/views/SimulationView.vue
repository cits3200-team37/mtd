<script setup>
import { inject } from "vue";
import D3Chart from '../components/SimView/D3Chart.vue';
import ParamBar from '../components/SimView/ParamBar/ParamBar.vue'

// Provide/Inject mechanism for ParamBar
const showParamBar = inject('showParamBar');
console.log("showParamBar:", showParamBar.value);
</script>

<template>
    <div class="h-screen flex">
        <ParamBar v-if="showParamBar"/>
        <D3Chart />
    </div>
</template>