import { defineStore } from "pinia";
import axios from "axios";

export const useSimulationStore = defineStore("simulation", {
  state: () => ({
    parameters: null,
    network: null,
  }),
  actions: {
    async simulate(simulateFormValues) {
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
      const { network } = data;
      this.network = network;
      // TODO: set other response variables related to the data object from the api call
    },
  },
});
