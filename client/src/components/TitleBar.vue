<template>
    <div class="drag w-screen inset-x-0 top-0 bg-navbar-primary h-8 pl-20 pt-1">
        <div class="flex flex-row items-center justify-center">
            <div class="flex flex-row">
                <button class="hover:bg-gray-500 hover:opacity-70 rounded-md px-2">
                    <svg-icon type="mdi" color="white" size="22" :path="mdiArrowLeft" />
                </button>
                <button class="hover:bg-gray-500 hover:opacity-70 rounded-md px-2">
                    <svg-icon type="mdi" color="white" size="22" :path="mdiArrowRight" />
                </button>
            </div>
            <div class="rounded-md bg-blue-400 w-1/3 text-center">
                <p class="">{{ router.currentRoute.value.name }}</p>
            </div>
        </div>
    </div>
</template>

<script setup>
import svgIcon from '@jamescoyle/vue-icon';
import { mdiArrowLeft } from '@mdi/js';
import { mdiArrowRight } from '@mdi/js';
import router from "../router"
console.log(router);
</script>

<style >
.drag {
    -webkit-app-region: drag;
}
</style>