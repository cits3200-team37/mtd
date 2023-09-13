<template>
    <div class="relative" @click="toggleMenu">
        <button class="bg-white text-black rounded-sm">{{ header }}</button>
        <ul v-if="menuOpen" class="bg-white text-black rounded-sm absolute mt-2 w-36 shadow-lg">
            <li class="w-full py-2 px-4 cursor-pointer hover:bg-gray-200" @click="selectOption(option)"
                v-for="option in props.menuOptions" :key="option">
                {{ option }}
            </li>
        </ul>
    </div>
</template>
  
<script setup>
import { defineProps, defineEmits, ref } from "vue";

const props = defineProps({
    heading: { type: String, default: "" },
    menuOptions: { type: Array, default: [] },
});

const emits = defineEmits(["emitOption"]);

const header = ref(props.heading);
const menuOpen = ref(false);
const optionSelected = ref("");

const toggleMenu = () => {
    menuOpen.value = !menuOpen.value;
    console.log(menuOpen.value);
};

const selectOption = (option) => {
    optionSelected.value = option;
    console.log(optionSelected.value);
    header.value = optionSelected.value;
    menuOpen.value = false;
    emitmenuoption();
    toggleMenu()
};

const emitmenuoption = () => {
    emits("emitOption", optionSelected.value);
};
</script>
  
<style scoped>
</style>
  