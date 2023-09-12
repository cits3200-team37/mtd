<template>
  <div
    class="flex items-center justify-center h-[calc(100vh-36px)] bg-background-color text-text-color"
  >
    <div class="text-center">
      <h1 class="text-3xl font-semibold mb-2 px-20">
        Welcome to the Moving Target Defence Simulator
      </h1>
      <p class="font-light text-text-color">
        Integrate time domain in the evaluation of Moving Target Defence
      </p>

      <div
        class="flex justify-center items-center mt-3 space-x-20 max-w-full mx-auto"
      >
        <a
          href="https://github.com/cits3200-team37"
          target="_blank"
          class="flex flex-col items-center mt-10 fill-current text-text-color"
        >
          <div class="h-12 w-12">
            <svg viewBox="0 0 24 24">
              <path :d="mdiGithub"></path>
            </svg>
          </div>
          <span class="text-xs">GitHub</span>
        </a>

        <a
          href="https://research-repository.uwa.edu.au/en/persons/jin-hong"
          target="_blank"
          class="flex flex-col items-center mt-10 fill-current text-text-color"
        >
          <div class="h-12 w-12">
            <svg viewBox="0 0 24 24">
              <path :d="mdiFileDocument"></path>
            </svg>
          </div>
          <span class="text-xs">Documentation</span>
        </a>

        <a
          @click="toSimulateView()"
          class="flex flex-col items-center mt-10 fill-current text-text-color hover:cursor-pointer"
        >
          <div class="h-12 w-12">
            <svg viewBox="0 0 24 24">
              <path :d="mdiGraphOutline"></path>
            </svg>
          </div>
          <span class="text-xs">Simulate</span>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { mdiGithub } from "@mdi/js";
import { mdiFileDocument } from "@mdi/js";
import { mdiGraphOutline } from "@mdi/js";
import { useRouter } from "vue-router";

const router = useRouter();

const toSimulateView = async () => {
  await router.push("/simulation");
};
</script>
