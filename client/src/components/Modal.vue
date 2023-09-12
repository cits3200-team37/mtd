<template>
  <transition
    enter-from-class="opacity-0"
    leave-to-class="opacity-0"
    enter-active-class="transition duration-200"
    leave-active-class="transition duration-200"
  >
    <div
      v-if="showModal"
      @click="emit('close')"
      class="flex justify-center items-center absolute inset-0 z-10 w-screen h-screen bg-black bg-opacity-40 drop-shadow-lg"
    >
      <div
        @click.stop
        class="p-2 container bg-dark-background border border-none rounded-md"
      >
        <div class="h-6 flex flex-row-reverse">
          <svg-icon
            @click="emit('close')"
            type="mdi"
            size="30"
            class="text-navbar-icon hover:text-white hover:cursor-pointer transition"
            :path="mdiWindowClose"
          ></svg-icon>
        </div>
        <slot />
      </div>
    </div>
  </transition>
</template>
<script setup>
import SvgIcon from "@jamescoyle/vue-icon";
import { mdiWindowClose } from "@mdi/js";
const emit = defineEmits(["close"]);
const props = defineProps({
  showModal: Boolean,
});
</script>
