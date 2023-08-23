<template>
    <nav class="w-20 bg-primary-navbar h-screen float-left mr-8">
        <div class="flex flex-col items-center h-screen justify-between">
            <div class="flex flex-col flex-nowrap py-6 space-y-8 relative text-center justify-normal">
                <div>
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

            </div>
            <div class="flex flex-col pb-6">
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