<template>
    <div class="bg-gray-500 mx-6 px-16 py-16 rounded-md">
        <div class="flex flex-row justify-center items-center">
            <p>PHOTO</p>
        </div>
        <div class="bg-gray-200">
            <p>{{ theme }}</p>
        </div>
    </div>
</template>

<script setup>
defineProps({
    theme: { type: String, default: "" }
});
const emit = defineEmits(["update:theme"]);
</script>