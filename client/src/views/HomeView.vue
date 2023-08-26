<template>
  <div class="flex items-center justify-center h-screen bg-gray-100">
    <div class="text-center">
      <h1 class="text-3xl font-semibold mb-2 px-20">
        Welcome to the Moving Target Defence Simulator
      </h1>
      <p class="text-gray-600">
        Integrate time domain in the evaluation of Moving Target Defence
      </p>

      <div
        class="flex justify-center items-center mt-3 space-x-20 max-w-full mx-auto"
      >
        <a
          href="https://www.https://github.com/MoeBuTa/MTDSimTime.com"
          target="_blank"
          class="flex flex-col items-center mt-10 text-gray-500"
        >
          <div class="h-12 w-12">
            <svg
              viewBox="0 0 24 24"
              class="fill-current text-gray-500 hover:text-blue-500"
            >
              <path :d="mdiGithub"></path>
            </svg>
          </div>
          <span class="text-xs">GitHub</span>
        </a>

        <a
          href="https://research-repository.uwa.edu.au/en/persons/jin-hong"
          target="_blank"
          class="flex flex-col items-center mt-10 text-gray-500"
        >
          <div class="h-12 w-12">
            <svg
              viewBox="0 0 24 24"
              class="fill-current text-gray-500 hover:text-blue-500"
            >
              <path :d="mdiFileDocument"></path>
            </svg>
          </div>
          <span class="text-xs">Documentation</span>
        </a>

        <a
          href="https://www.google.com"
          target="_blank"
          class="flex flex-col items-center mt-10 text-gray-500"
        >
          <div class="h-12 w-12">
            <svg
              viewBox="0 0 24 24"
              class="fill-current text-gray-500 hover:text-blue-500"
            >
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
</script>
