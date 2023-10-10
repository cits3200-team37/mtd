<template>
  <div
    class="bg-navbar-primary overflow-hidden shadow-lg rounded-md hover:cursor-pointer"
    @click="toggleTheme(theme)"
  >
    <div
      class="w-48 h-32 bg-background-secondary flex flex-row items-center justify-center"
    >
      <img class="h-24 w-32" :src="link" />
    </div>
    <div class="px-6 py-4 flex flex-row items-center">
      <input
        :checked="active"
        id="default-radio-2"
        type="radio"
        name="default-radio"
        class="w-4 h-4 bg-gray-100 border-gray-300 hover:cursor-pointer"
      />
      <label class="hover:cursor-pointer pl-2">{{ theme }}</label>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  theme: { type: String, default: "" },
  active: { type: Boolean, default: false },
  link: { type: String, default: "" },
});
const emit = defineEmits(["update:modelValue"]);

const toggleTheme = (theme) => {
  emit("update:modelValue", theme);
};
</script>
