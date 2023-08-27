<script setup>
import { ref } from "vue";
import FormField from "../components/FormField.vue";
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiArrowLeft } from '@mdi/js';
import { mdiArrowRight } from '@mdi/js';
const isOpen = ref(true);

const form = ref({
    network_size_list: "",
    start_time: "",
    finish_time: "",
    mtd_interval: "",
    scheme: "",
    total_nodes: "",
});

const handleSubmit = async () => {
    console.log(form.value);
};

</script>

<template>
    <div class="flex flex-row">
        <div v-if="isOpen">
            <div class="w-48 bg-navbar-primary min-h-screen border border-black border-100 float-left px-5 pt-5">
                <div class="flex flex-col items-center">
                    <p class="text-lg pb-5 text-center">Simulation Parameters</p>
                    <form class="flex flex-col space-y-2" @submit.prevent="handleSubmit">
                        <div>
                            <FormField v-model="form.network_size_list" label="Network Size List" placeholder="Network Size"
                                type="text" />
                        </div>
                        <div>
                            <FormField v-model="form.start_time" label="Start Time" placeholder="Start Time" type="text" />
                        </div>
                        <div>
                            <FormField v-model="form.finish_time" label="Finish Time" placeholder="Finish Time"
                                type="text" />
                        </div>
                        <div>
                            <FormField v-model="form.mtd_interval" label="MTD Interval" placeholder="MTD Interval"
                                type="text" />
                        </div>
                        <div>
                            <FormField v-model="form.scheme" label="Scheme" placeholder="Scheme" type="text" />
                        </div>
                        <div>
                            <FormField v-model="form.total_nodes" label="Total Nodes" placeholder="Total Nodes"
                                type="text" />
                        </div>
                        <div class="text-center">
                            <button class="bg-gray-700 py-1 px-4 mt-3 w-full text-center rounded-md mb-4">Submit</button>
                        </div>
                    </form>
                </div>
            </div>

        </div>
        <div class="w-6 min-h-screen float-left z-50">
            <div class="min-h-screen flex items-center justify-center">
                <div v-if="isOpen">
                    <button @click="isOpen = !isOpen" class="text-white">
                        <svg-icon type="mdi" :path="mdiArrowLeft" size="24"></svg-icon></button>
                </div>
                <div v-else>
                    <button @click="isOpen = !isOpen" class="text-white">
                        <svg-icon type="mdi" :path="mdiArrowRight" size="24"></svg-icon></button>
                </div>
            </div>
        </div>
        <div class="border border-blue-200 bg-blue-200 flex-1 mr-2 my-2">
            <p>d3</p>
        </div>

    </div>
</template>