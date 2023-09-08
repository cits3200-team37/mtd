<script setup>
import { ref } from "vue";
import FormField from "../components/FormField.vue";
import SvgIcon from "@jamescoyle/vue-icon";
import { mdiArrowLeft } from "@mdi/js";
import { mdiArrowRight } from "@mdi/js";
const isOpen = ref(true);

const form = ref({
  network_size_list: "",
  start_time: "",
  finish_time: "",
  mtd_interval: "",
  scheme: "",
  total_nodes: "",
});

const isValid = ref(true);
const errors = ref({
  network_size_list: "",
  start_time: "",
  finish_time: "",
  mtd_interval: "",
  scheme: "",
  total_nodes: "",
});

const handleSubmit = async () => {
  // Reset errors
  Object.keys(errors.value).forEach((key) => {
    errors.value[key] = "";
  });

  const networkSizes = form.value.network_size_list.split(",");
  for (let size of networkSizes) {
    let parsedSize = parseInt(size.trim());
    if (isNaN(parsedSize)) {
      errors.value.network_size_list =
        "Network Size List must be a list of numbers separated by commas";
      isValid.value = false;
      break;
    } else if (parsedSize < 20) {
      errors.value.network_size_list =
        "Each number in Network Size List must be 20 or greater";
      isValid.value = false;
      break;
    }
  }

  if (
    !form.value.start_time ||
    isNaN(form.value.start_time) ||
    form.value.start_time < 0
  ) {
    errors.value.start_time = "Start Time must be a non-negative number";
    isValid.value = false;
  }

  if (
    !form.value.finish_time ||
    isNaN(form.value.finish_time) ||
    form.value.finish_time <= form.value.start_time
  ) {
    errors.value.finish_time =
      "Finish Time must be a number greater than Start Time";
    isValid.value = false;
  }

  if (
    !form.value.mtd_interval ||
    isNaN(form.value.mtd_interval) ||
    form.value.start_time < 0
  ) {
    errors.value.mtd_interval = "MTD Interval must be a non-negative number";
    isValid.value = false;
  }

  const validSchemes = [
    "random",
    "simultaneous",
    "alternative",
    "single",
    "None",
  ];
  if (!form.value.scheme || !validSchemes.includes(form.value.scheme)) {
    errors.value.scheme =
      "Invalid scheme. Choose between random, simultaneous, alternative, single, or None.";
    isValid.value = false;
  }

  if (!form.value.total_nodes || isNaN(form.value.total_nodes)) {
    errors.value.total_nodes = "Total Nodes must be a number";
    isValid.value = false;
  } else if (parseInt(form.value.total_nodes) < 20) {
    errors.value.total_nodes = "Total Nodes must be 20 or greater";
    isValid.value = false;
  }

  if (!isValid.value) {
    return;
  }

  console.log(form.value);
};
</script>

<template>
  <div class="flex flex-row">
    <div v-if="isOpen">
      <div
        class="w-48 bg-navbar-primary min-h-screen border border-black border-100 float-left px-5 pt-5"
      >
        <div class="flex flex-col items-center">
          <p class="text-lg pb-5 text-center">Simulation Parameters</p>
          <form class="flex flex-col space-y-2" @submit.prevent="handleSubmit">
            <div>
              <FormField
                v-model="form.network_size_list"
                label="Network Size List"
                placeholder="Network Size"
                type="text"
                :color="
                  errors.network_size_list ? 'border-red-500 border-4' : ''
                "
              />
            </div>
            <p class="text-red-500">{{ errors.network_size_list }}</p>
            <div>
              <FormField
                v-model="form.start_time"
                label="Start Time"
                placeholder="Start Time"
                type="text"
                :color="errors.start_time ? 'border-red-500 border-4' : ''"
              />
            </div>
            <p class="text-red-500">{{ errors.start_time }}</p>
            <div>
              <FormField
                v-model="form.finish_time"
                label="Finish Time"
                placeholder="Finish Time"
                type="text"
                :color="errors.finish_time ? 'border-red-500 border-4' : ''"
              />
            </div>
            <p class="text-red-500">{{ errors.finish_time }}</p>
            <div>
              <FormField
                v-model="form.mtd_interval"
                label="MTD Interval"
                placeholder="MTD Interval"
                type="text"
                :color="errors.mtd_interval ? 'border-red-500 border-4' : ''"
              />
            </div>
            <p class="text-red-500">{{ errors.mtd_interval }}</p>
            <div>
              <FormField
                v-model="form.scheme"
                label="Scheme"
                placeholder="Scheme"
                type="text"
                :color="errors.scheme ? 'border-red-500 border-4' : ''"
              />
            </div>
            <p class="text-red-500">{{ errors.scheme }}</p>
            <div>
              <FormField
                v-model="form.total_nodes"
                label="Total Nodes"
                placeholder="Total Nodes"
                type="text"
                :color="errors.total_nodes ? 'border-red-500 border-4' : ''"
              />
            </div>
            <p class="text-red-500">{{ errors.total_nodes }}</p>
            <div class="text-center">
              <button
                class="bg-gray-700 py-1 px-4 mt-3 w-full text-center rounded-md mb-4"
              >
                Submit
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div class="w-6 min-h-screen float-left z-50">
      <div class="min-h-screen flex items-center justify-center">
        <div v-if="isOpen">
          <button @click="isOpen = !isOpen" class="text-white">
            <svg-icon type="mdi" :path="mdiArrowLeft" size="24"></svg-icon>
          </button>
        </div>
        <div v-else>
          <button @click="isOpen = !isOpen" class="text-white">
            <svg-icon type="mdi" :path="mdiArrowRight" size="24"></svg-icon>
          </button>
        </div>
      </div>
    </div>
    <div class="border border-blue-200 bg-blue-200 flex-1 mr-2 my-2">
      <p>d3</p>
    </div>
  </div>
</template>
