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
                    <a href="#" class="block px-4 py-2 text-sm"
                        :class="[selectedOption === option ? 'bg-gray-100 text-gray-900' : 'text-gray-700']">
                        {{ option }}
                    </a>
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

const ChevronDownIcon = {
    template: `
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
        <path fill-rule="evenodd" d="M6.293 7.293a1 1 0 011.414 0L10 9.586l2.293-2.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z" clip-rule="evenodd" />
      </svg>
    `,
};
</script>
  
<style scoped>

</style>
  