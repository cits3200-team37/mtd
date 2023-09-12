<template>
    <div>
        <button @click="toggleMenu" class="bg-white text-black">{{ heading }}</button>
        <ul v-if="menuOpen" class="bg-white text-black">
            <li @click="selectOption(option)" v-for="option in props.menuOptions" :key="option.id">
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
const optionSelected = ref("");

const toggleMenu = () => {
    menuOpen.value = !menuOpen.value;
    console.log(menuOpen.value);
};

const selectOption = (option) => {
    optionSelected.value = option;
    console.log(optionSelected.value);
};
</script>
  
<style scoped></style>
  