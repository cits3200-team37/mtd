import { defineStore } from "pinia";
import axios from "axios";
const BACKEND_URL = "https://mtd-sim-api-u5ffcbdh3q-ts.a.run.app/";

export const useSimulationStore = defineStore("simulation", {
  state: () => ({
    parameters: null,
    network: null,
    attackRecord: null,
    mtdRecord: null,
    compromiseMetrics: null,
    strategies: null,
  }),
  actions: {
    async simulate(simulateFormValues) {
      this.parameters = { ...simulateFormValues };
      const reqBody = {
        scheme:
          this.parameters.scheme !== "None" ? this.parameters.scheme : null,
        mtdInterval: Number(this.parameters.mtdInterval),
        finishTime: Number(this.parameters.finishTime),
        totalNodes: Number(this.parameters.totalNodes),
      };
      if (this.parameters.strategies) {
        reqBody.strategies = this.parameters.strategies;
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
        reqBody.seed = parseInt(this.parameters.seed);
      }
      if (this.parameters.totalLayers) {
        reqBody.totalLayers = Number(this.parameters.totalLayers);
      }
      if (this.parameters.targetLayer) {
        reqBody.targetLayer = Number(this.parameters.targetLayer);
      }
      if (this.parameters.seed) {
        reqBody.seed = parseInt(this.parameters.seed);
      }

      const { data } = await axios.post(`${BACKEND_URL}/simulate`, reqBody);
      const { network, attack_record, mtd_record, compromise_metrics } = data;
      this.network = network;
      this.attackRecord = attack_record;
      this.mtdRecord = mtd_record;
      this.compromiseMetrics = compromise_metrics;
    },
    async getStrategies() {
      const { data } = await axios.get(`${BACKEND_URL}/strategies`);
      this.strategies = data;
    },
    reset() {
      this.parameters = null;
      this.network = null;
      this.attackRecord = null;
      this.mtdRecord = null;
      this.compromiseMetrics = null;
    },
  },
});
