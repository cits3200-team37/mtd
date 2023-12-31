import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SimulationView from "../views/SimulationView.vue";
import ChartView from "../views/ChartView.vue";
import SettingsView from "../views/SettingsView.vue";
import DownloadView from "../views/DownloadView.vue";

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
      path: "/settings",
      name: "Settings",
      component: SettingsView,
    },
    {
      path: "/download",
      name: "Download",
      component: DownloadView,
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
