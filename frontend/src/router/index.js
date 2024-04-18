import { createRouter,createWebHashHistory } from "vue-router";
/* 添加 */
import CreateClassmate from '../views/CreateClassmate.vue';
import CreateInterestingEvent from "../views/CreateInterestingEvent.vue";
import CreateTravel from "../views/CreateTravel.vue";
/* 编辑 */
import UpdateClassmate from '../views/UpdateClassmate.vue';
// import UpdateInterestingEvent from "../views/UpdateInterestingEvent.vue";

/* 404页面 */
import NotFound from '../views/404.vue';
/* 测试 */
import Test from '../views/Test.vue'
import m3u8 from "../views/m3u8.vue";
/* 主要展示页面 */
import MainLayout from '../views/MainLayout.vue'
import Album from '../views/Album.vue';
import About from '../views/About.vue'
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
        redirect: "/about",
        component: MainLayout,
        children: [
            {
                path: "/about",
                name: "About",
                component: About,
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
            // {
            //     path:'/同学录/informshow',
            //     component:InformShowC,
            //     props:(router)=>({stage:router.query.stage}),
            // },
            // {
            //     path:"/同学录/createclassmate",
            //     component:CreateClassmate,
            //     props:(router)=>({type:router.query.type}),
            // },
            {
                path: "/test",
                name: "Test",
                component: FileList,
            },
            {
                path: "/同学录",
                children:[
                    {
                        path:"informshow",
                        name:"InformShowC",
                        component:InformShowC,
                        // props:(router)=>({stage:router.query.stage}),
                    },
                    {
                        path:"createclassmate",
                        name:"CreateClassmate",
                        component:CreateClassmate,
                        // props:(router)=>({type:router.query.type}),
                    },
                    {
                        path:"updateclassmate",
                        name:"UpdateClassmate",
                        component:UpdateClassmate,
                        // props:()=>({type:router.query.type}),
                    },
                ],
            },
            
            // {
            //     path:'/同学录/informshow',
            //     name:"InformShowC",
            //     component:InformShowC,
            // },
            // {
            //     path:"/同学录/createclassmate",
            //     name:"CreateClassmate",
            //     component:CreateClassmate,
            // },
            // {
            //     path:"/同学录/updateclassmate",
            //     name:"UpdateClassmate",
            //     component:UpdateClassmate,
            // },
            // {
            //     path:"/趣事录/informshow",
            //     name:"InformShowI",
            //     component:InformShowI,
            // },
            // {
            //     path:"/趣事录/createinterestingevent",
            //     name:"CreateInterestingEvent",
            //     component:CreateInterestingEvent,
            // },
            // {
            //     path:"/旅游志/informshow",
            //     name:"InformShowT",
            //     component:InformShowT,
            // },
            // {
            //     path:"/旅游志/createtravel",
            //     name:"CreateTravel",
            //     component:CreateTravel,
            // },
            
            {
                path:"/趣事录",
                children:[
                    {
                        path:"informshow",
                        name:"InformShowI",
                        component:InformShowI
                    },
                    {
                        path:"createinterestingevent",
                        name:"CreateInterestingEvent",
                        component:CreateInterestingEvent,
                    },
                    {
                        path:"updateinterestingevent",
                        name:"UpdateInterestingEvent",
                        component:()=>import("../views/UpdateEvent.vue")
                    },
                ],
            },
            {
                path:"/旅游志",
                children:[
                    {
                        path:"informshow",
                        component:()=>import("../views/InformShowT.vue")
                    },
                    {
                        path:"createtravel",
                        name:"CreateTravel",
                        component:CreateTravel,
                    },
                    {
                        path:"updatetravel",
                        name:"UpdateTravel",
                        component:()=>import("../views/UpdateTravel.vue")
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