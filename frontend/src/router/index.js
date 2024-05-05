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
import VideoManage from "../views/VideoManage.vue";
import AlbumManage from "../views/AlbumManage.vue";
import PicturesManage from "../views/PicturesManage.vue";

import axios from 'axios'
import { isProxy } from "vue";
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
                meta:{title:"时光画廊"}
            },
            {
                path: "/album",
                name: "Album",
                component: Album,
                props:(router)=>({id:router.query.id}),
                meta:{title:"相册"}
            },
            {
                path:"/albumtype",
                name:"AlbumType",
                component:AlbumType,
                meta:{title:"相册类型"}
            },
            {
                path: "/test",
                name: "Test",
                component: PicturesManage,
            },
            {
                path:"/videomanage",
                name:"VideoManage",
                component:VideoManage,
                meta:{title:'视频管理'}
            },
            {
                path:"/AlbumManage",
                name:"AlbumManage",
                component:AlbumManage,
                meta:{title:'相册管理'}
            },
            {
                path:"/picturesmanage",
                name:"PicturesManage",
                component:PicturesManage,
                meta:{title:'照片管理'}
            },
            {
                path:"/m3u8",
                name:"m3u8",
                component:m3u8,
            },
            {
                path:"/m3",
                name:"m3",
                component:m3,
            },
            {
                path: "/classmates",
                children:[
                    {
                        path:"informshow",
                        name:"InformShowC",
                        component:InformShowC,
                        meta:{title:"同学录"}
                    },
                    {
                        path:"createclassmate",
                        name:"CreateClassmate",
                        component:CreateClassmate,
                        meta:{title:"添加同学"}
                    },
                    {
                        path:"updateclassmate",
                        name:"UpdateClassmate",
                        component:UpdateClassmate,
                        meta:{title:"编辑同学"}
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
                        meta:{title:"趣事录"}
                    },
                    {
                        path:"createinterestingevent",
                        name:"CreateInterestingEvent",
                        component:CreateInterestingEvent,
                        meta:{title:"添加趣事"}
                    },
                    {
                        path:"updateinterestingevent",
                        name:"UpdateInterestingEvent",
                        component:UpdateEvent,
                        meta:{title:"编辑趣事"}
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
                        meta:{title:"旅游志"}
                    },
                    {
                        path:"createtravel",
                        name:"CreateTravel",
                        component:CreateTravel,
                        meta:{title:"添加旅游"}
                    },
                    {
                        path:"updatetravel",
                        name:"UpdateTravel",
                        component:UpdateTravel,
                        meta:{title:"编辑旅游"}
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
router.afterEach((to,from,next)=>{
    if(to.meta&&to.meta.title){
        document.title = to.meta.title
    }
})
export default router;