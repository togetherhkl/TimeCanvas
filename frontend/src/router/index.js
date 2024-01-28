import { createRouter,createWebHashHistory } from "vue-router";
import Home from "../views/Home.vue";
import axios from 'axios'
//创建路由
const routes = [
    {
        path: "/",
        name: "Home",
        component: Home
    }, 
]
//创建路由实例
const router = createRouter({
    history: createWebHashHistory(),
    routes: routes
});

export default router;