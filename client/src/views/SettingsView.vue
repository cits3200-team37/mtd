<template>
  <div class="h-[calc(100vh-36px)] flex flex-col pl-8 pt-8">
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
  </div>
</template>

<script setup>
import ThemeCard from "../components/ThemeCard.vue";
import { ref, onMounted } from "vue";
import dark from "../public/screens/Dark.png";
import light from "../public/screens/Light.png";
const currentTheme = ref();
onMounted(async () => {
  try {
    currentTheme.value = localStorage.getItem("user-theme");
    console.log(currentTheme.value);
    await setTheme(currentTheme.value);
  } catch (e) {
    console.log(e);
  }
});

const setTheme = async (theme) => {
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
