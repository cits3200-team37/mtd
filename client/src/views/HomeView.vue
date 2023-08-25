<template>
  <div class="min-h-screen flex flex-col justify-center items-center">
    <h1>home page</h1>
    <p class="font-bold">count: {{ clickerStore.count }}</p>
    <button
      class="py-2 px-2 my-4 rounded-sm bg-blue-400"
      @click="incrementCount"
    >
      increment
    </button>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useClickerStore } from "../stores/clicker";

const clickerStore = useClickerStore();

const incrementCount = () => {
  clickerStore.increment();
};
</script>
