import {createRouter, createWebHistory} from 'vue-router';
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";

const router = createRouter({
    // mode: process.env.IS_ELECTRON ? 'hash' : 'history',
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'Home',
            component: HomeView
        },
        {
            path: '/about',
            name: 'About',
            component: AboutView
        }
    ]
})

// router.beforeEach((to, from) => {
//     // console.log('beforeEach', to, from)
//     console.log(to, from,process.env);
// })

export default router