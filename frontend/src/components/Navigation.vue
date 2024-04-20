<template>
  <div class="header">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false"
      @select="handleSelect">
      <el-menu-item>
        <img class="logo" src="../assets/vue.svg" alt="project logo" />
      </el-menu-item>
      <el-menu-item index="0" @click="$router.push('/home')">首页</el-menu-item>
      <el-menu-item index="1" @click="$router.push('/albumtype')">相册</el-menu-item>
      <div class="flex-grow" />
      <el-menu-item index="2" @click="$router.push('/picturesmanage')">照片管理</el-menu-item>
      <el-menu-item index="3" @click="$router.push('/videomanage')">视频管理</el-menu-item>
      <el-sub-menu index="4">
        <template #title >创建</template>
        <el-menu-item index="4-1" @click="openDrawer('趣事录')">趣事录</el-menu-item>
        <el-menu-item index="4-2" @click="openDrawer('旅游志')">旅游志</el-menu-item>
      </el-sub-menu>
      <el-menu-item index="5">
        <el-icon>
          <Moon />
        </el-icon>
      </el-menu-item>
      <el-sub-menu index="6" @click="getTaken">
        <template #title>
          <el-avatar :src="avatar_url" :size="40" />
          {{ baidu_name }}
        </template>
        <el-menu-item index="6-1">个人中心</el-menu-item>
        <el-menu-item index="6-2" @click="exit">退出</el-menu-item>
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
import { routerKey } from 'vue-router';
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
    handleSelect(key, keyPath) {
      console.log(key, keyPath)
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
      //退出登录，清楚cookie和localStorage中的token
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
        if(this.$router.currentRoute.value.path === '/album' && this.$router.currentRoute.value.query.id === '2'&&title === '趣事录'){ 
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
  width: 60px;
  height: 60px;
}
</style>
