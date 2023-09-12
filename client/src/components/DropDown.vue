<template>
    <button class="bg-white text-black">{{ heading }}</button>
</template>
  
<script setup>
import { defineProps } from "vue";
const props = defineProps({
    heading: { type: String, default: "" },
    menuOptions: { type: Array, default: [] }
})
</script>
  
<style scoped></style>
  