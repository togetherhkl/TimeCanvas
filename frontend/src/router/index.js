import { createRouter,createWebHashHistory } from "vue-router";
/* 添加 */
import CreateClassmate from '../views/CreateClassmate.vue';
import CreateInterestingEvent from "../views/CreateInterestingEvent.vue";
import CreateTravel from "../views/CreateTravel.vue";
/* 编辑 */
import UpdateClassmate from '../views/UpdateClassmate.vue';
import UpdateTravel from "../views/UpdateTravel.vue";
import UpdateEvent from "../views/UpdateEvent.vue";
/* 404页面 */
import NotFound from '../views/404.vue';
/* 测试 */
import Test from '../views/Test.vue'
import m3u8 from "../views/m3u8.vue";
/* 主要展示页面 */
import MainLayout from '../views/MainLayout.vue'
import Album from '../views/Album.vue';
import Home from '../views/Home.vue'
import AlbumType from '../views/AlbumType.vue';
import InformShowC from "../views/InformShowC.vue";
import InformShowI from "../views/InformShowI.vue";
import InformShowT from "../views/InformShowT.vue";

import axios from 'axios'
import { isProxy } from "vue";
import FileList from "../views/FileList.vue";
import M3u8 from "../views/m3u8.vue";
import m3 from "../views/m3.vue";

//创建路由
const routes = [
    {
        path: "/",
        redirect: "/home",
        component: MainLayout,
        children: [
            {
                path: "/home",
                name: "Home",
                component: Home,
            },
            {
                path: "/album",
                name: "Album",
                component: Album,
                props:(router)=>({id:router.query.id})
            },
            {
                path:"/albumtype",
                name:"AlbumType",
                component:AlbumType,
            },
            {
                path: "/test",
                name: "Test",
                component: FileList,
            },
            {
                path: "/classmates",
                children:[
                    {
                        path:"informshow",
                        name:"InformShowC",
                        component:InformShowC,
                    },
                    {
                        path:"createclassmate",
                        name:"CreateClassmate",
                        component:CreateClassmate,
                    },
                    {
                        path:"updateclassmate",
                        name:"UpdateClassmate",
                        component:UpdateClassmate,
                    },
                ],
            },
            {
                path:"/interestingevents",
                children:[
                    {
                        path:"informshow",
                        name:"InformShowI",
                        component:InformShowI,
                    },
                    {
                        path:"createinterestingevent",
                        name:"CreateInterestingEvent",
                        component:CreateInterestingEvent,
                    },
                    {
                        path:"updateinterestingevent",
                        name:"UpdateInterestingEvent",
                        component:UpdateEvent,
                    },
                ],
            },
            {
                path:"/travels",
                children:[
                    {
                        path:"informshow",
                        name:"InformShowT",
                        component:InformShowT,
                    },
                    {
                        path:"createtravel",
                        name:"CreateTravel",
                        component:CreateTravel,
                    },
                    {
                        path:"updatetravel",
                        name:"UpdateTravel",
                        component:UpdateTravel,
                    }
                ],
            },
        ],
    },
    { 
        path: '/:pathMatch(.*)*', 
        name: 'NotFound', 
        component: NotFound 
    },
]
//创建路由实例
const router = createRouter({
    history: createWebHashHistory(),
    routes: routes,
});
export default router;