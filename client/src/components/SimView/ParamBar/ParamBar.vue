<template>
  <div class="w-48 bg-navbar-primary h-screen border border-black border-100">
    <div class="flex flex-col items-center h-screen justify-between">
      <div
        class="flex flex-col flex-nowrap py-6 space-y-8 relative text-center justify-normal h-full"
      >
        <div
          class="flex flex-col text-white bg-gray-700 hover:bg-gray-800 py-1 px-4 mt-3"
        >
          <button @click="closeParamBar">Close</button>
        </div>

        <form class="simulation-form space-y-4">
          <label class="text-white flex flex-col">
            Network size list:
            <input type="text" name="network_size_list" class="mt-1" />
          </label>
          <label class="text-white flex flex-col">
            Start time:
            <input type="text" name="start_time" class="mt-1" />
          </label>
          <label class="text-white flex flex-col">
            Finish time:
            <input type="text" name="finish_time" class="mt-1" />
          </label>
          <label class="text-white flex flex-col">
            MTD Interval:
            <input type="text" name="mtd_interval" class="mt-1" />
          </label>
          <label class="text-white flex flex-col">
            Scheme:
            <input type="text" name="scheme" class="mt-1" />
          </label>
          <label class="text-white flex flex-col">
            Total nodes:
            <input type="text" name="total_nodes" class="mt-1" />
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
import { inject } from "vue";
import PBRun from "./PBRun.vue";

// Provide/Inject mechanism for ParamBar
const closeParamBar = inject("closeParamBar");
</script>
