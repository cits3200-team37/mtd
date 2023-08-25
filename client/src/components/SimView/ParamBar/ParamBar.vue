<template>
    <div class="w-48 bg-navbar-primary h-screen border border-black border-100">
        <div class="flex flex-col items-center h-screen justify-between">
            <div class="flex flex-col flex-nowrap py-6 space-y-8 relative text-center justify-normal h-full">
                <!-- Parameter 1 becomes the form -->
                <form class="simulation-form space-y-4">
                    <label class="text-white flex flex-col">
                        Network size list:
                        <input type="text" name="network_size_list" class="mt-1">
                    </label>
                    <label class="text-white flex flex-col">
                        Start time:
                        <input type="text" name="start_time" class="mt-1">
                    </label>
                    <label class="text-white flex flex-col">
                        Finish time:
                        <input type="text" name="finish_time" class="mt-1">
                    </label>
                    <label class="text-white flex flex-col">
                        MTD Interval:
                        <input type="text" name="mtd_interval" class="mt-1">
                    </label>
                    <label class="text-white flex flex-col">
                        Scheme:
                        <input type="text" name="scheme" class="mt-1">
                    </label>
                    <label class="text-white flex flex-col">
                        Total nodes:
                        <input type="text" name="total_nodes" class="mt-1">
                    </label>
                </form>
            </div>
            <div class="flex justify-center mt-auto pb-4">
                <PBRun />
            </div>
        </div>
    </div>
</template>

<script setup>
import PBRun from './PBRun.vue'; 
</script>