<template>
  <div class="absolute bg-gray-700 text-center rounded-lg py-1 px-4 opacity-90">
    <ul>
      <li>IP: {{ ip }}</li>
      <li>OS: {{ `${osType} ${osVersion}` }}</li>
      <li>{{ `${totalUsers} ${totalUsers == 1 ? "User" : "Users"}` }}</li>
      <li>
        {{ `${totalServices} ${totalServices == 1 ? "Service" : "Services"}` }}
      </li>
      <li v-if="compromised" class="bg-red-600 rounded-full">Compromised</li>
    </ul>
  </div>
</template>

<script setup>
const props = defineProps({
  ip: String,
  osType: String,
  osVersion: String,
  totalUsers: Number,
  totalServices: Number,
  compromised: Boolean,
});
</script>
