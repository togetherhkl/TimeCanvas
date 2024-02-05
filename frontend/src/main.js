import { createApp } from 'vue'
import App from './App.vue'
// 引入element-plus
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
//注册element-plus的图标
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
//引入axios
import axios from 'axios'
//引入router
import router from './router';
//引入图标
import './assets/iconfont/iconfont.css'

const app=createApp(App)

for(const[key,component] of Object.entries(ElementPlusIconsVue)){
    app.component(key,component)//注册element-plus的图标
}
app.use(ElementPlus)//注册element-plus
app.use(router)//注册router
app.mount('#app')
//修改axios的默认配置http://192.168.43.162:5173/
axios.defaults.baseURL="http://192.168.43.162:8000"
//配置请求拦截器
// axios.interceptors.request.use(
//     config=>{
//         //获取token
//         const token=window.localStorage.getItem('token')
//         //如果token存在
//         if(token){
//             //在请求头中添加token
//             config.headers.Authorization=token
//         }else if(!config.url.includes('login')){
//             axios.get('/auth').then(
//                 response=>{
//                     window.localStorage.setItem('token',response.data.token)
//                 }
//             )            
//         }
//         return config
//     },
//     error=>{
//         return Promise.reject(error)
//     }
// )
//配置响应拦截器
// axios.interceptors.response.use(
//     response=>{
//         return response
//     },
//     error=>{
//         if(error.response.status===401){
//             axios.get('/auth').then(
//                 response=>{
//                     window.localStorage.setItem('token',response.data.token)
//                 }
//             )
            
//         }
//         return Promise.reject(error)
//     }
// )

