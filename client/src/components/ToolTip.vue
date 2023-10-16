<template>
  <transition
    enter-from-class="opacity-0"
    leave-to-class="opacity-0"
    enter-active-class="transition duration-200"
    leave-active-class="transition duration-200"
  >
    <div v-if="showTooltip">
      <div
        class="absolute transition bg-gray-700 text-center rounded-lg py-1 px-4 opacity-90"
        :style="{ left: offsetX + 'px', top: offsetY + 'px' }"
      >
        <slot />
      </div>
    </div>
  </transition>
</template>

<script setup>
const props = defineProps({
  showTooltip: Boolean,
  offsetX: Number,
  offsetY: Number,
});
</script>
