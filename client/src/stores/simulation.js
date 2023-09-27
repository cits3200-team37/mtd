import { defineStore } from "pinia";
import axios from "axios";
const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

export const useSimulationStore = defineStore("simulation", {
  state: () => ({
    parameters: null,
    network: null,
    attackRecord: null,
    mtdRecord: null,
  }),
  actions: {
    async simulate(simulateFormValues) {
      this.parameters = { ...simulateFormValues };
      const reqBody = {
        networkSizeList: Number(this.parameters.networkSizeList),
        startTime: Number(this.parameters.startTime),
        finishTime: Number(this.parameters.finishTime),
        mtdInterval: Number(this.parameters.mtdInterval),
        scheme: this.parameters.scheme.toLowerCase(),
        totalNodes: Number(this.parameters.totalNodes),
      };
      const { data } = await axios.post(
        `${BACKEND_URL}/simulate`,
        reqBody,
      );
      const { network, attack_record, mtd_record } = data;
      this.network = network;
      this.attackRecord = attack_record;
      this.mtdRecord = mtd_record;
      // TODO: set other response variables related to the data object from the api call
    },
  },
});
