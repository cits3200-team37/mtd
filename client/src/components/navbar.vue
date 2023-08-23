<template>
    <nav class="z-0 w-20 bg-primary-navbar h-screen top-0 inset-y-0 left-0">
        <div class="flex flex-col items-center pt-8 space-y-8">
            <div>
                <!-- <p class="text-white">hello</p> -->
                <svg-icon type="mdi" :path="home" size="48" color="#A4A4A4"></svg-icon>
            </div>
            <div>
                <svg-icon type="mdi" :path="graph" size="48" color="#A4A4A4"></svg-icon>
            </div>
            <div>
                <svg-icon type="mdi" :path="chart" size="48" color="#A4A4A4"></svg-icon>

            </div>
            <div>
                <svg-icon type="mdi" :path="sigma" size="48" color="#A4A4A4"></svg-icon>

            </div>
            <div>
                <svg-icon type="mdi" :path="cog" size="48" color="#A4A4A4"></svg-icon>
            </div>

        </div>

    </nav>
</template>

<script setup>
import SvgIcon from "@jamescoyle/vue-icon";
import { mdiCog } from "@mdi/js";
import { mdiHomeOutline } from "@mdi/js";
import { mdiGraphOutline } from "@mdi/js";
import { mdiChartTimeline } from "@mdi/js";
import { mdiSigma } from "@mdi/js";
const cog = mdiCog;
const home = mdiHomeOutline;
const graph = mdiGraphOutline;
const chart = mdiChartTimeline;
const sigma = mdiSigma;
</script>