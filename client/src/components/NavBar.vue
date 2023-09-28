<template>
  <nav class="w-16 bg-navbar-primary h-[calc(100vh-36px)] float-left">
    <div class="flex flex-col items-center h-full justify-between">
      <div
        class="flex flex-col flex-nowrap py-4 space-y-8 relative text-center justify-normal h-full w-full"
      >
        <div
          v-for="route in routes"
          :key="route.path"
          @click="handleRoute(route)"
        >
          <div
            class="flex flex-col"
            :class="{
              'absolute inset-x-0 bottom-3': route.path == `/download`,
            }"
          >
            <div v-if="route.active">
              <div
                class="top absolute h-10 bg-white w-0.5 rounded-md"
              ></div>
            </div>
            <div class="flex flex-col items-center justify-center">
              <svg-icon
                type="mdi"
                :path="route.icon"
                size="36"
                class="text-navbar-icon hover:text-white hover:cursor-pointer"
                :class="{
                  'text-white': route.active,
                }"
              ></svg-icon>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted } from "vue";
import router from "../router";
import SvgIcon from "@jamescoyle/vue-icon";
import { mdiCog } from "@mdi/js";
import { mdiHomeOutline } from "@mdi/js";
import { mdiGraphOutline } from "@mdi/js";
import { mdiChartTimeline } from "@mdi/js";
import { mdiSigma } from "@mdi/js";
import { mdiDownload } from "@mdi/js";
import findVersion from "../helpers/findVersion";

onMounted(async () => {
  try {
    handleVersion(findVersion(window));
  } catch (error) {
    console.log(error);
  }
});

const routes = ref([
  {
    path: "/",
    active: true,
    icon: mdiHomeOutline,
  },
  {
    path: "/simulation",
    active: false,
    icon: mdiGraphOutline,
  },
  {
    path: "/charts",
    active: false,
    icon: mdiChartTimeline,
  },
  {
    path: "/statistics",
    active: false,
    icon: mdiSigma,
  },
  {
    path: "/settings",
    active: false,
    icon: mdiCog,
  },
  {
    path: "/download",
    active: false,
    icon: mdiDownload,
  },
]);

const handleRoute = async (route) => {
  routes.value.forEach((r) => {
    if (r.path != route.path) {
      r.active = false;
    } else {
      r.active = true;
    }
  });
  route.active = true;
  await router.push(route.path);
};

// ability to handle route changes not from clicking on navbar
router.afterEach(async (to, _) => {
  const active = routes.value.filter((route) => route.active);
  if (active[0].path != to.path) {
    routes.value.forEach((route) => {
      if (route.path != to.path) {
        route.active = false;
      } else {
        route.active = true;
      }
    });
  }
});

const handleVersion = async (version) => {
  // todo change this to only website when we deploy later
  // remove ! mark
  if (!version) {
    routes.value.forEach((route) => {
      if (route.path == "/download") {
        routes.value.splice(routes.value.indexOf(route), 1);
      }
    });
  }
};
</script>
