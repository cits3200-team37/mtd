<template>
    <div class="relative inline-block text-left">
        <button
            class="inline-flex w-full justify-center gap-x-1.5 rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
            @click="toggleMenu">
            {{ buttonLabel }}
            <ChevronDownIcon class="-mr-1 h-5 w-5 text-gray-400" aria-hidden="true" />
        </button>
        <transition enter-active-class="transition ease-out duration-100" enter-from-class="transform opacity-0 scale-95"
            enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75"
            leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
            <ul v-if="isMenuOpen"
                class="absolute right-0 z-10 mt-2 max-w-lg origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                <li v-for="(option, index) in menuOptions" :key="index" @click="selectOption(option)">
                </li>
            </ul>
        </transition>
    </div>
</template>
  
<script setup>
import { ref, defineProps, defineEmits } from 'vue';

const props = defineProps({
    buttonLabel: String,
    menuOptions: Array,
});

const emits = defineEmits();
const isMenuOpen = ref(false);
const selectedOption = ref(null);

const toggleMenu = () => {
    isMenuOpen.value = !isMenuOpen.value;
};

const selectOption = (option) => {
    selectedOption.value = option;
    isMenuOpen.value = false;
    emits('optionSelected', option); // Emit the selected option to the parent component
};

</script>
  
<style scoped></style>
  