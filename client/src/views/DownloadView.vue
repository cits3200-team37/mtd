<template>
  <div class="min-h-screen flex flex-col px-10 pt-12">
    <p class="text-3xl pb-4">Downloads</p>
    <p class="text-xl">
      Latest Version <span class="">{{ version }}</span>
    </p>
    <p class="text-xl pt-6">
      Click one of the options to download your desired platforms package.
    </p>
    <div class="grid grid-cols-3 pt-12">
      <div v-for="(os, index) in osVersions" :key="os.name">
        <!-- todo change this to real download link -->
        <a :href="os.link" target="_blank">
          <div
            class="bg-gray-500 py-12 hover:bg-gray-600 hover:cursor-pointer"
            :class="{ 'rounded-l-md': index == 0, 'rounded-r-md': index == 2 }"
          >
            <div class="flex flex-col items-center">
              <svg-icon type="mdi" :path="os.icon" size="48" />
              <p class="pt-2">{{ os.name }}</p>
            </div>
          </div>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
// todo replace these os logos with real ones that wont expire
import { mdiApple, mdiPenguin, mdiMicrosoftWindows } from "@mdi/js";
import SvgIcon from "@jamescoyle/vue-icon";
import { ref } from "vue";
const version = ref("2.0.0");
const osVersions = ref([
  {
    name: "Windows",
    icon: mdiMicrosoftWindows,
    link: "http://www.google.com",
  },
  {
    name: "Mac",
    icon: mdiApple,
    link: "http://www.google.com",
  },
  {
    name: "Linux",
    icon: mdiPenguin,
    link: "http://www.google.com",
  },
]);
</script>
