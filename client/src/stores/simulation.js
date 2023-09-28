import { defineStore } from "pinia";
import axios from "axios";

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
        totalLayers: Number(this.parameters.totalLayers),
        totalEndpoints: Number(this.parameters.totalEndpoints),
        totalSubnets: Number(this.parameters.totalSubnets),
        totalDatabase: Number(this.parameters.totalDatabase),
        targetLayer: Number(this.parameters.targetLayer),
        terminateCompromiseRatio: parseFloat(this.parameters.terminateCompromiseRatio),
        seed: Number(this.parameters.seed),
      };
      const { data } = await axios.post(
        "http://localhost:8001/simulate",
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
