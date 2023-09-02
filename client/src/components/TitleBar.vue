<template>
  <div class="drag w-screen inset-x-0 top-0 bg-navbar-primary h-9 pl-20 p-1.5">
    <div class="flex flex-row items-center justify-center">
      <button
        class="no-drag hover:bg-gray-500 hover:opacity-70 rounded-md px-2"
        @click="handleBack"
      >
        <svg-icon type="mdi" color="white" size="22" :path="mdiArrowLeft" />
      </button>
      <button
        class="no-drag hover:bg-gray-500 hover:opacity-70 rounded-md px-2"
        @click="handleForward"
      >
        <svg-icon type="mdi" color="white" size="22" :path="mdiArrowRight" />
      </button>
      <div class="no-drag rounded-md bg-dark-background w-1/3 text-center">
        <p>{{ router.currentRoute.value.name }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import svgIcon from "@jamescoyle/vue-icon";
import { mdiArrowLeft } from "@mdi/js";
import { mdiArrowRight } from "@mdi/js";
import router from "../router";

const handleBack = async () => {
  router.back();
};
const handleForward = async () => {
  router.forward();
};
</script>

<style scoped>
.drag {
  -webkit-app-region: drag;
}

.no-drag {
  -webkit-app-region: no-drag;
}
</style>
