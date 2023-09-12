<template>
    <button @click="menu" class="bg-white text-black">{{ heading }}</button>
    <ul v-if="menuOpen" class="bg-white text-black">
        <li v-for="option in props.menuOptions" :key="option.id">
            <a :href="option.link">{{ option.name }}</a>
        </li>
    </ul>
</template>
  
<script setup>
import { defineProps, ref } from "vue";

const props = defineProps({
    heading: { type: String, default: "" },
    menuOptions: { type: Array, default: [] }
})

const menu = () => {
    console.log("menu clicked");
    console.log(props.menuOptions)
    if (menuOpen == true) {
        menuOpen.value = false
    } else {
        menuOpen.value = true
    }
    console.log(menuOpen)
}

const menuOpen = ref(false)


</script>
  
<style scoped></style>
  