import { defineStore } from "pinia";
import axios from "axios";
// const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;
const BACKEND_URL = "http://localhost:8001";

const hashCode = (str) => {
  let hash = 0;
  if (str.length === 0) return hash;
  for (let i = 0; i < str.length; i++) {
    const char = str.charCodeAt(i);
    hash = (hash << 5) - hash + char;
  }
  return hash;
};

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
        scheme: this.parameters.scheme,
      };
      if (this.parameters.mtdInterval) {
        reqBody.mtdInterval = Number(this.parameters.mtdInterval);
      }
      if (this.parameters.finishTime) {
        reqBody.finishTime = Number(this.parameters.finishTime);
      }
      if (this.parameters.totalNodes) {
        reqBody.totalNodes = Number(this.parameters.totalNodes);
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
      if (this.parameters.totalLayers) {
        reqBody.totalLayers = Number(this.parameters.totalLayers);
      }
      if (this.parameters.targetLayer) {
        reqBody.targetLayer = Number(this.parameters.targetLayer);
      }
      if (this.parameters.seed) {
        reqBody.seed = hashCode(this.parameters.seed);
      }

      console.log(reqBody);

      const { data } = await axios.post(`${BACKEND_URL}/simulate`, reqBody);
      const { network, attack_record, mtd_record } = data;
      this.network = network;
      this.attackRecord = attack_record;
      this.mtdRecord = mtd_record;
      // TODO: set other response variables related to the data object from the api call
    },
  },
});
