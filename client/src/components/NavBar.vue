<template>
    <nav class="w-16 bg-navbar-primary h-screen border border-black border-100">
        <div class="flex flex-col items-center h-screen justify-between">
            <div class="flex flex-col flex-nowrap py-6 space-y-8 relative text-center justify-normal h-full">
                <div v-for="route in routes" :key="route.path" class="relative group">
                    <!-- Main Icon -->
                    <svg-icon type="mdi" :path="route.icon" size="36" class="text-navbar-icon hover:text-white"
                        :class="{ 'text-white': route.active }" @click="handleRoute(route)"></svg-icon>

                    <!-- Re-open Icon (next to simulation icon) -->
                    <div v-if="route.path === '/simulation' && !showParamBar" class="absolute -right-8 top-0 ">
                        <svg-icon type="mdi" :path="mdiKeyboardTab" size="36" class="text-navbar-icon hover:text-white bg-black"
                            @click="reopenParamBar"></svg-icon>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script setup>
import { ref, inject } from "vue";
import router from "../router";
import SvgIcon from "@jamescoyle/vue-icon";
import { mdiCog } from "@mdi/js";
import { mdiHomeOutline } from "@mdi/js";
import { mdiGraphOutline } from "@mdi/js";
import { mdiChartTimeline } from "@mdi/js";
import { mdiSigma } from "@mdi/js";
import { mdiKeyboardTab  } from "@mdi/js";

const routes = ref([{
    path: "/",
    active: true,
    icon: mdiHomeOutline
},
{
    path: "/simulation",
    active: false,
    icon: mdiGraphOutline
},
{
    path: "/charts",
    active: false,
    icon: mdiChartTimeline
},
{
    path: "/statistics",
    active: false,
    icon: mdiSigma
},
{
    path: "/settings",
    active: false,
    icon: mdiCog
}
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
}

// Provide/Inject mechanism for ParamBar
const showParamBar = inject('showParamBar');
const reopenParamBar = inject('reopenParamBar');
</script>