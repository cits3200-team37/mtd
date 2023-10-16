<template>
  <div v-if="!isLoading" class="h-[calc(100vh-36px)] flex flex-col pl-8 pt-8">
    <div>
      <p class="text-2xl pb-4">Settings page</p>
      <p class="text-md">
        Customise your experience, make it more enjoyable and easier to work!
      </p>
      <div class="flex flex-row py-4 space-x-5">
        <div v-for="theme in themes" :key="theme">
          <ThemeCard
            :theme="theme.theme"
            :active="theme.active"
            :link="theme.link"
            @update:model-value="setTheme(theme.theme)"
          />
        </div>
      </div>
      <div v-if="isElectron">
        <p class="text-2xl pb-2">Current Version</p>
        <p class="text-md pb-4">{{ currentVersion }}</p>
        <div v-if="LatestVersion.name.replace('v', '') != currentVersion">
          <p class="text-md">
            There is a new update available, please close and reopen your app
          </p>
        </div>
      </div>
    </div>
  </div>
  <div
    v-else
    class="flex flex-1 h-[calc(100vh-36px)] items-center justify-center"
  >
    <svg-icon type="mdi" size="60" :path="mdiLoading" class="animate-spin" />
  </div>
</template>

<script setup>
import ThemeCard from "../components/ThemeCard.vue";
import { ref, onMounted } from "vue";
import dark from "../public/screens/Dark.png";
import light from "../public/screens/Light.png";
import getTag from "../helpers/getTag";
import findVersion from "../helpers/findVersion";
import { mdiLoading } from "@mdi/js";
import SvgIcon from "@jamescoyle/vue-icon";
const LatestVersion = ref();
const currentVersion = ref();
const currentTheme = ref();
const isLoading = ref(true);
const isElectron = ref();
onMounted(async () => {
  try {
    currentTheme.value = localStorage.getItem("user-theme");
    LatestVersion.value = await getTag();
    isElectron.value = findVersion(navigator.userAgent);
    currentVersion.value = await window.electronAPI?.processVersion();
    await setTheme(currentTheme.value);
  } catch (e) {
    console.log(e);
  }
  isLoading.value = false;
});

const setTheme = async (theme) => {
  if (theme == null) {
    theme = "Dark";
  }
  localStorage.setItem("user-theme", theme.toLowerCase());
  window.dispatchEvent(
    new CustomEvent("theme-changed", {
      detail: { storage: localStorage.getItem("user-theme") },
    }),
  );
  themes.value.forEach((presetTheme) => {
    if (presetTheme.theme.toUpperCase() === theme.toUpperCase()) {
      presetTheme.active = true;
    } else {
      presetTheme.active = false;
    }
  });
};
const themes = ref([
  { theme: "Dark", link: dark, active: false },
  { theme: "Light", link: light, active: false },
]);
</script>
