import { createRouter,createWebHashHistory } from "vue-router";
import Home from "../views/Home.vue";
import Primary from '../views/Classmate/Primary.vue';
import Junior from '../views/Classmate/Junior.vue';
import Senior from '../views/Classmate/Senior.vue';
import University from '../views/Classmate/University.vue';
import AddInformation from '../views/AddInformation.vue';
import AddInterestingEvent from "../views/AddInterestingEvent.vue";
import AddTravel from "../views/AddTravel.vue";
import NotFound from '../views/404.vue'
import Test from '../views/Test.vue'
import About from '../views/About.vue'
import MainLayout from '../views/MainLayout.vue'
import Album from '../views/Album.vue'
import AlbumType from '../views/AlbumType.vue'
import InformShow from "../views/InformShow.vue";
import AddInformation1 from "../views/AddInformation1.vue";
import axios from 'axios'
import { isProxy } from "vue";

//创建路由
const routes = [
    {
        path: "/",
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
            },
            {
                path:"albumtype",
                name:"AlbumType",
                component:AlbumType,
            },
            {
                path: "/test",
                name: "Test",
                component: Test,
            },
            {
                path: "/classmates",
                children:[
                    {
                        path:"informshow",
                        name:"InformShow",
                        component:InformShow
                    },
                    {
                        path:"小学",
                        name:"Primary",
                        component:Primary
                    },
                    {
                        path:"初中",
                        name:"Junior",
                        component:Junior
                    },
                    {
                        path:"高中",
                        name:"Senior",
                        component:Senior
                    },
                    {
                        path:"大学",
                        name:"Universtiy",
                        component:University
                    },
                    {
                        path:"addinformation",
                        name:"AddInformation1",
                        component:AddInformation1
                    },
                    {
                        path:"addinterestingevent",
                        name:"AddInterestingEvent",
                        component:AddInterestingEvent
                    },
                    {
                        path:"addtravel",
                        name:"AddTravel",
                        component:AddTravel
                    },
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