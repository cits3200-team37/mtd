import { defineStore } from "pinia";

export const useClickerStore = defineStore("clicker", {
  state: () => ({
    count: 0,
  }),
  actions: {
    async increment() {
      this.count++;
    },
  },
});
