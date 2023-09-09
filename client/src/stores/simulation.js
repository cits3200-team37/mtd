import { defineStore } from "pinia";
import axios from "axios";

export const useSimulationStore = defineStore("simulation", {
  state: () => ({
    parameters: null,
    network: null,
    attackRecord: null,
  }),
  actions: {
    async simulate(simulateFormValues) {
      this.parameters = { ...simulateFormValues };
      const reqBody = {
        networkSizeList: Number(this.parameters.networkSizeList),
        startTime: Number(this.parameters.startTime),
        finishTime: Number(this.parameters.finishTime),
        mtdInterval: Number(this.parameters.mtdInterval),
        scheme: this.parameters.scheme,
        totalNodes: Number(this.parameters.totalNodes),
      };
      const { data } = await axios.post(
        "http://localhost:8001/simulate",
        reqBody,
      );
      console.log(data);
      const { network, attack_record } = data;
      this.network = network;
      this.attackRecord = attack_record;
      // TODO: set other response variables related to the data object from the api call
    },
  },
});
