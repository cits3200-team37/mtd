<template>
    <div>
        <button @click="toggleMenu" class="bg-white text-black">{{ heading }}</button>
        <ul v-if="menuOpen" class="bg-white text-black">
            <li v-for="option in props.menuOptions" :key="option.id">
                {{ option }}
            </li>
        </ul>
    </div>
</template>
  
<script setup>
import { defineProps, ref } from "vue";

const props = defineProps({
    heading: { type: String, default: "" },
    menuOptions: { type: Array, default: [] },
});

const menuOpen = ref(false);

const toggleMenu = () => {
    menuOpen.value = !menuOpen.value;
    console.log(toggleMenu)
};
</script>
  
<style scoped></style>
  