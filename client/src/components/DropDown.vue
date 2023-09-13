<template>
    <div>
        <button @click="toggleMenu" class="bg-white text-black rounded-sm">{{ header }}</button>
        <ul v-if="menuOpen" class="bg-white text-black rounded-sm h-1/4">
            <li class="w-full" @click="selectOption(option)" v-for="option in props.menuOptions" :key="option">
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
};

const emitmenuoption = () => {
    emits("emitOption", optionSelected.value); 
};
</script>
  
<style scoped></style>
  