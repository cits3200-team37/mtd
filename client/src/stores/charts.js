import { defineStore } from "pinia";
import axios from "axios";

export const useChartStore = defineStore("charts", {
    state: () => ({
        data: [],
    }),
    actions: {
        async requestData() {
            const server = axios.create({ baseURL: "http://localhost:8001" });
            const dummyObject = {
                "finishTime": 3000,
                "mtdInterval": 20,
                "scheme": "None",
                "totalNodes": 50
            };
            const { data, status } = await server.post("/simulate", dummyObject);
            this.data = data;
        },
    },
});