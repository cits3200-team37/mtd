<template>
    <button @click="$emit('close')">Close</button>
</template>

<script setup>
import { defineEmits } from "vue";

const emits = defineEmits(["close"]);
</script>
