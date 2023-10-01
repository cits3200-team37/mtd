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
      const reqBody = {};
      if (this.parameters.startTime) {
        reqBody.startTime = Number(this.parameters.startTime);
      }
      if (this.parameters.finishTime) {
        reqBody.finishTime = Number(this.parameters.finishTime);
      }
      if (this.parameters.mtdInterval) {
        reqBody.mtdInterval = Number(this.parameters.mtdInterval);
      }
      if (this.parameters.networkSizeList) {
        reqBody.networkSizeList = Number(this.parameters.networkSizeList);
      }
      if (this.parameters.scheme) {
        reqBody.scheme = this.parameters.scheme.toLowerCase()
      }
      if (this.parameters.totalNodes) {
        reqBody.totalNodes = Number(this.parameters.totalNodes);
      }
      if (this.parameters.totalLayers) {
        reqBody.totalLayers = Number(this.parameters.totalLayers);
      }
      if (this.parameters.totalEndpoints) {
        reqBody.totalEndpoints = Number(this.parameters.totalEndpoints);
      }
      if (this.parameters.totalSubnets) {
        reqBody.totalSubnets = Number(this.parameters.totalSubnets);
      }
      if (this.parameters.totalDatabase) {
        reqBody.totalDatabase = Number(this.parameters.totalDatabase);
      }
      if (this.parameters.targetLayer) {
        reqBody.targetLayer = Number(this.parameters.targetLayer);
      }
      if (this.parameters.seed) {
        reqBody.seed = Number(this.parameters.seed);
      }

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
