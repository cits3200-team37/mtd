<template>
    <label>{{ label }}</label>
    <input :type="type" :placeholder="placeholder" class="p-1 mt-2 mb-2.5 pl-2.5 border border-solid rounded-md text-black w-full" @input="updateInput" :value="modelValue">
</template>

<script setup>
const props = defineProps({
  label: { type: String, default: "" },
  modelValue: { type: [String, Number], default: "" },
  placeholder: { type: String, default: "" },
  type: { type: String, default: "text" },
});
const emit = defineEmits(["update:modelValue", "update"]);

const updateInput = (e) => {
  emit("update:modelValue", e.target.value);
  emit("update");
};
</script>