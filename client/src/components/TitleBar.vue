<template>
  <div class="drag w-screen top-0 bg-navbar-primary h-9 pt-1.5">
    <div class="flex justify-center w-[calc(100vw-64px)]">
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
        class="no-drag rounded-md bg-background-secondary w-64 text-center text-text-color"
      >
        <p>{{ router.currentRoute.value.name }}</p>
      </div>
      <div v-if="os == `win32` || os == `linux`" class="absolute right-4 pt-1">
        <button
          class="no-drag hover:cursor-pointer pr-2"
          @click="handleMinimise"
        >
          <svg-icon
            type="mdi"
            :path="mdiWindowMinimize"
            size="24"
            class="text-white"
          ></svg-icon>
        </button>
        <button
          class="no-drag hover:cursor-pointer pr-2"
          @click="handleMaximise"
        >
          <svg-icon
            type="mdi"
            :path="mdiWindowMaximize"
            size="24"
            class="text-white"
          ></svg-icon>
        </button>
        <button class="no-drag hover:cursor-pointer" @click="handleClose">
          <svg-icon
            type="mdi"
            :path="mdiWindowClose"
            size="24"
            class="text-white"
          ></svg-icon>
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
  mdiWindowMaximize,
} from "@mdi/js";
import router from "../router";
import { ref, onMounted } from "vue";
import { handleMinimise, handleClose, handleMaximise } from "../renderer";
const os = ref("");

onMounted(async () => {
  try {
    os.value = await window.electronAPI?.operatingSystem();
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
