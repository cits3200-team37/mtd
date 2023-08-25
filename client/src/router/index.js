import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SimulationView from "../views/SimulationView.vue";
import ChartView from "../views/ChartView.vue";
import StatisticsView from "../views/StatisticsView.vue";
import SettingsView from "../views/SettingsView.vue";

const router = createRouter({
  // mode: process.env.IS_ELECTRON ? 'hash' : 'history',
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "Home",
      component: HomeView,
    },
    {
      path: "/simulation",
      name: "Simulation",
      component: SimulationView,
    },
    {
      path: "/charts",
      name: "Charts",
      component: ChartView,
    },
    {
      path: "/statistics",
      name: "Statistics",
      component: StatisticsView,
    },
    {
      path: "/settings",
      name: "Settings",
      component: SettingsView,
    },
    {
      path: "/:pathMatch(.*)*",
      redirect: "/",
    },
  ],
});

router.beforeEach((to, from) => {
  document.title = to.name;
});

export default router;
