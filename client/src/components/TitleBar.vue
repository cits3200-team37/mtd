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
      <div
        class="no-drag rounded-md bg-dark-background w-1/3 text-center text-white"
      >
        <p>{{ router.currentRoute.value.name }}</p>
      </div>
      <div v-if="os == `win32` || os == `linux`" class="absolute right-4 pt-1">
        <!-- todo change to win32 || linux -->
        <button
          class="no-drag hover:cursor-pointer pr-2"
          @click="handleMinimise"
        >
          <svg-icon type="mdi" :path="mdiWindowMinimize" size="24"></svg-icon>
        </button>
        <button class="no-drag hover:cursor-pointer" @click="handleClose">
          <svg-icon type="mdi" :path="mdiWindowClose" size="24"></svg-icon>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import svgIcon from "@jamescoyle/vue-icon";
import {
  mdiArrowLeft,
  mdiArrowRight,
  mdiWindowClose,
  mdiWindowMinimize,
} from "@mdi/js";
import router from "../router";
import { ref, onMounted } from "vue";
import { handleMinimise, handleClose } from "../renderer";
const os = ref("");

onMounted(async () => {
  try {
    os.value = await window.electronAPI.operatingSystem();
  } catch (error) {
    console.log(error);
  }
});

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
