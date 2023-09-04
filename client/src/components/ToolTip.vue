<template>
  <transition
    enter-from-class="opacity-0"
    leave-to-class="opacity-0"
    enter-active-class="transition duration-200"
    leave-active-class="transition duration-200"
  >
    <!-- NOTE: use v-show here as we only want to toggle css properties. Inefficient and will not work with v-if directive  -->
    <div
      v-show="showTooltip"
      class="absolute bg-gray-700 text-center rounded-lg py-1 px-4 opacity-90"
    >
      <ul>
        <li>IP: {{ ip }}</li>
        <li>OS: {{ `${osType} ${osVersion}` }}</li>
        <li>{{ `${totalUsers} ${totalUsers == 1 ? "User" : "Users"}` }}</li>
        <li>
          {{
            `${totalServices} ${totalServices == 1 ? "Service" : "Services"}`
          }}
        </li>
        <li v-if="compromised" class="bg-red-600 rounded-full">Compromised</li>
      </ul>
    </div>
  </transition>
</template>

<script setup>
const props = defineProps({
  showTooltip: Boolean,
  ip: String,
  osType: String,
  osVersion: String,
  totalUsers: Number,
  totalServices: Number,
  compromised: Boolean,
});
</script>
