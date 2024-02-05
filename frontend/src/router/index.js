import { createRouter,createWebHashHistory } from "vue-router";
import Home from "../views/Home.vue";
import Primary from '../views/Classmate/Primary.vue';
import Junior from '../views/Classmate/Junior.vue';
import Senior from '../views/Classmate/Senior.vue';
import University from '../views/Classmate/University.vue';
import Addinformation from '../views/AddInformation.vue';
import NotFound from '../views/404.vue'
import axios from 'axios'
import { isProxy } from "vue";
//创建路由
const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/home",
        redirect:"/",
        children:[
            {
                path:"primary",
                name:"Primary",
                component:Primary
            },
            {
                path:"junior",
                name:"Junior",
                component:Junior
            },
            {
                path:"senior",
                name:"Senior",
                component:Senior
            },
            {
                path:"university",
                name:"Universtiy",
                component:University
            },
            {
                path:"addinformation",
                name:"Addinformation",
                component:Addinformation
            },
        ],
    },
    { 
        path: '/:pathMatch(.*)*', 
        name: 'NotFound', 
        component: NotFound 
    },
    {
        path:"/test",
        name:"Main",
        component:()=>import('../views/Test.vue')
    },
]
//创建路由实例
const router = createRouter({
    history: createWebHashHistory(),
    routes: routes
});

export default router;