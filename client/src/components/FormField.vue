<template>
  <label>{{ label }}</label>
  <input
    :type="type"
    :placeholder="placeholder"
    class="p-1 mt-2 mb-2.5 pl-2.5 border border-solid rounded-md text-black w-full"
    :class="{ 'border-red-500 border-4': error }"
    @input="updateInput"
    :value="modelValue"
  />
  <p v-if="error" class="text-red-500 text-sm">{{ error }}</p>
</template>

<script setup>
const props = defineProps({
  label: { type: String, default: "" },
  modelValue: { type: [String, Number], default: "" },
  placeholder: { type: String, default: "" },
  type: { type: String, default: "text" },
  error: { type: String, default: "" },
});
const emit = defineEmits(["update:modelValue", "update"]);

const updateInput = (e) => {
  emit("update:modelValue", e.target.value);
  emit("update");
};
</script>
