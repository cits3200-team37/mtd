<template>
  <div v-if="!isLoading">
    <div class="h-[calc(100vh-36px)] flex flex-col px-10 pt-12">
      <p class="text-3xl pb-4">Downloads</p>
      <p class="text-xl">
        Latest <span class="">{{ version }}</span>
      </p>
      <p class="text-xl pt-6">
        Click one of the options to download your desired platforms package.
      </p>
      <div class="grid grid-cols-3 pt-12">
        <div v-for="(os, index) in osVersions" :key="os.name">
          <a :href="os.link" :download="os.name" target="_blank">
            <div
              class="bg-gray-500 py-12 hover:bg-gray-600 hover:cursor-pointer"
              :class="{
                'rounded-l-md': index == 0,
                'rounded-r-md': index == 2,
              }"
            >
              <div class="flex flex-col items-center">
                <svg-icon type="mdi" :path="os.icon" size="48" />
                <p class="pt-2">{{ os.name }}</p>
              </div>
            </div>
          </a>
        </div>
        <div>
          <p class="text-3xl py-4">Release Notes</p>
          <span>{{ data.body }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import getTag from "../helpers/getTag";
import { siApple, siWindows11, siLinux } from "simple-icons";
import SvgIcon from "@jamescoyle/vue-icon";
import { ref, onMounted } from "vue";
const version = ref(null);
const data = ref(null);
const isLoading = ref(true);
const osVersions = ref();

onMounted(async () => {
  try {
    data.value = await getTag();
    version.value = data.value.tag_name;
    await manageAssets();
  } catch (error) {
    console.log(error);
  }
  isLoading.value = false;
});

const manageAssets = async () => {
  const releases = [];
  data.value.assets.forEach((os) => {
    const obj = {
      link: os.browser_download_url,
      packageName: os.name,
    };
    if (os.content_type.includes("zip")) {
      obj.name = "Mac";
      obj.icon = siApple.path;
    } else if (os.content_type.includes("msdos")) {
      obj.name = "Windows";
      obj.icon = siWindows11.path;
    } else if (os.content_type.includes("debian")) {
      obj.name = "Linux";
      obj.icon = siLinux.path;
    }
    releases.push(obj);
  });
  osVersions.value = releases;
};
</script>
