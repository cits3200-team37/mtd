import { defineStore } from "pinia";
import axios from "axios";

export const useSimulationStore = defineStore("simulation", {
  state: () => ({
    parameters: null,
    network: null,
  }),
  actions: {
    async simulate(simulateFormValues) {
      console.log("fetching...");
      this.parameters = {
        networkSizeList: Number(simulateFormValues.networkSizeList),
        startTime: Number(simulateFormValues.startTime),
        finishTime: Number(simulateFormValues.finishTime),
        mtdInterval: Number(simulateFormValues.mtdInterval),
        scheme: simulateFormValues.scheme,
        totalNodes: Number(simulateFormValues.totalNodes),
      };
      const { data } = await axios.post(
        "http://localhost:8001/simulate",
        this.parameters,
      );
      this.network = data;
      return this.network;
    },
  },
});
