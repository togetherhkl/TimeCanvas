<template>
  <div class="header">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false">
      <el-menu-item>
        <img class="logo" src="../assets/logo.png" alt="project logo" />
      </el-menu-item>
      <el-menu-item index="/home" @click="$router.push('/home')">首页</el-menu-item>
      <el-menu-item index="/albumtype" @click="$router.push('/albumtype')">相册</el-menu-item>
      <div class="flex-grow" />
      <el-menu-item index="/albummanage" @click="$router.push('/albummanage')">相册管理</el-menu-item>
      <el-menu-item index="/picturesmanage" @click="$router.push('/picturesmanage')">照片管理</el-menu-item>
      <el-menu-item index="/videomanage" @click="$router.push('/videomanage')">视频管理</el-menu-item>
      <el-sub-menu index="5">
        <template #title >创建</template>
        <el-menu-item index="5-1" @click="openDrawer('同学录')">同学录</el-menu-item>
        <el-menu-item index="5-2" @click="openDrawer('趣事录')">趣事录</el-menu-item>
        <el-menu-item index="5-3" @click="openDrawer('旅游志')">旅游志</el-menu-item>
      </el-sub-menu>
      <!-- <el-menu-item index="6">
        <el-icon>
          <Moon />
        </el-icon>
      </el-menu-item> -->
      <el-sub-menu index="7" @click="getTaken">
        <template #title>
          <el-avatar :src="avatar_url" :size="40" />
          {{ baidu_name }}
        </template>
        <el-menu-item index="7-1">个人中心</el-menu-item>
        <el-menu-item index="7-2" @click="exit">退出</el-menu-item>
      </el-sub-menu>
    </el-menu>
  </div>
  <el-drawer v-model="drawer" :title=drawerTitle :with-header="false">
    <CreateEvent :title="drawerTitle" />
  </el-drawer>
</template>

<script>
import axios from 'axios';
import avatar_url from '../assets/user.png';//引入默认头像
import CreateEvent from './CreateEvent.vue';
//从common中引入公共方法
import { GetCookie } from '../assets/common/utils.js';
import { ElMessage } from 'element-plus';
export default {
  // 状态
  data() {
    return {
      count: 0,
      activeIndex: '1',
      baidu_name: '请登录',
      avatar_url: avatar_url,
      access_token: '',
      drawer: false,
      drawerTitle: '',
    }
  },
  //引入组件
  components: {
    CreateEvent,
  },
  // 动作
  methods: {
    increment() {
      this.count++
    },
    getTaken() {
      if (localStorage.getItem('timecanvas_token') == null || GetCookie("timecanvas_token") == null) {
        axios.get("/auth").then(
          response => {
            if (response.status == 200) {
              //加载后端传送过来的授权url地址
              window.location.href = response.data.auth_url;
            }
          },
        )
      }
    },
    exit() {
      //退出登录，清除cookie和localStorage中的token
      console.log("退出登录")
      localStorage.removeItem('timecanvas_token');
      document.cookie = "timecanvas_token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
      this.baidu_name = '请登录',
        this.avatar_url = avatar_url,
        sessionStorage.clear();/* 清除缓存与会话记录，但失败 */
      this.$router.push('/');
    },
    //创建相册
    openDrawer(title) {
      if (this.baidu_name === '请登录') {
        ElMessage.error("你还没有登录，授权登录后才可以使用完整功能");
      } else {
        if(this.$router.currentRoute.value.path === '/album' && this.$router.currentRoute.value.query.id === '1'&&title === '同学录'){
          this.drawerTitle = title;
          this.drawer = true;
        }else if(this.$router.currentRoute.value.path === '/album' && this.$router.currentRoute.value.query.id === '2'&&title === '趣事录'){ 
          this.drawerTitle = title;
          this.drawer = true;
        }else if(this.$router.currentRoute.value.path === '/album' && this.$router.currentRoute.value.query.id === '3'&&title === '旅游志'){
          this.drawerTitle = title;
          this.drawer = true;
        }else{
          ElMessage.error("请在对应相册页面创建");
        }
      }
    },
  },
  mounted() {
    //从cookie中获取token
    let path=location.href.split('#')[1];
    this.activeIndex = path.split('?')[0];
    let validValues=['/','/home','/albumtype','/albummanage','/picturesmanage','/videomanage'];
    if(!validValues.includes(this.activeIndex)){
      this.activeIndex='/albumtype';
    }
    const timecanvas_token = GetCookie("timecanvas_token")
    const token = window.localStorage.getItem('timecanvas_token')
    if (timecanvas_token == null && token == null) {
      //使用ElMessage警告
      ElMessage.error("你还没有登录，授权登录后才可以使用完整功能");
    }
    else {
      if (timecanvas_token != null) {
        localStorage.setItem('timecanvas_token', timecanvas_token)
        axios.get("/userinfo").then(
          response => {
            if (response.status == 200) {
              this.baidu_name = response.data.baidu_name;
              this.avatar_url = response.data.avatar_url;
            }
          },
        )
      }
    }
  },
}
</script>

<style>
.header {
  flex: 0 0 auto;
}

.flex-grow {
  flex-grow: 1;
}

.logo {
  width: auto;
  height:60px;
  padding: 0;
}
</style>
