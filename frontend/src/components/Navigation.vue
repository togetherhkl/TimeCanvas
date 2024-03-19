<template>
  <div class="header">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false"
      @select="handleSelect">
      <el-menu-item index="0">
        <img class="logo" src="../assets/vue.svg" alt="project logo" />
      </el-menu-item>
      <el-menu-item index="1" @click="$router.push('/about')">首页</el-menu-item>
      <el-menu-item index="3" @click="$router.push('/albumtype')">相册</el-menu-item>
      <div class="flex-grow" />
      <el-sub-menu index="2">
        <template #title>创建</template>
        <el-menu-item index="2-1" @click="drawer = true">趣事录</el-menu-item>
        <el-menu-item index="2-2">旅游志</el-menu-item>
      </el-sub-menu>
      <el-sub-menu index="3">

        <template #title>管理</template>
        <el-sub-menu index="2-1">

          <template #title>同学录</template>
          <el-menu-item index="2-1-1" @click="AddCPage">添加</el-menu-item>
          <el-menu-item index="2-1-2">修改</el-menu-item>
          <el-menu-item index="2-1-3">删除</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="2-2">

          <template #title>趣事录</template>
          <el-menu-item index="2-2-1" @click="AddIPage">添加</el-menu-item>
          <el-menu-item index="2-2-2">修改</el-menu-item>
          <el-menu-item index="2-2-3">删除</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="2-3">

          <template #title>旅游志</template>
          <el-menu-item index="2-3-1" @click="AddTPage">添加</el-menu-item>
          <el-menu-item index="2-3-2">修改</el-menu-item>
          <el-menu-item index="2-3-3">删除</el-menu-item>
        </el-sub-menu>
      </el-sub-menu>
      <el-menu-item index="4">
        <el-icon>
          <Moon />
        </el-icon>
      </el-menu-item>
      <el-sub-menu index="5" @click="getTaken">

        <template #title>
          <el-avatar :src="avatar_url" :size="40" />
          {{ baidu_name }}
        </template>
        <el-menu-item index="5-1">个人中心</el-menu-item>
        <el-menu-item index="5-2" @click="exit">退出</el-menu-item>
      </el-sub-menu>
    </el-menu>
  </div>
  <el-drawer v-model="drawer" title="创建趣事录" :with-header="true" >
    <CreateInterestingEvent />
  </el-drawer>
</template>

<script>
import axios from 'axios';
import avatar_url from '../assets/user.png';//引入默认头像
import { routerKey } from 'vue-router';
import CreateInterestingEvent from './CreateIntersetingEvent.vue';
//从common中引入公共方法
import { GetCookie } from '../assets/common/utils.js'
import { ElMessage } from 'element-plus'
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
    }
  },
  //引入组件
  components: {
    CreateInterestingEvent,
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
    //跳转到添加同学录页面
    AddCPage() {
      this.$router.push('/classmates/addinformation');
    },
    //跳转到添加趣事录页面
    AddIPage() {
      this.$router.push('/classmates/addinterestingevent');
    },
    //跳转到添加旅游志页面
    AddTPage() {
      this.$router.push('/classmates/addtravel');
    },
    //退出功能，删除cookie和localStorage中的token
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
      }
      const toten = localStorage.getItem('timecanvas_token')
      axios.get("/userinfo").then(
        response => {
          if (response.status == 200) {
            this.baidu_name = response.data.baidu_name;
            this.avatar_url = response.data.avatar_url;
          }
        },
      )
    }
  },
}
</script>

<style>
.header {
  flex: 0 0 auto;
  /* 设置头部不随着主体内容而伸缩 */
}

.flex-grow {
  flex-grow: 1;
}

.logo {
  width: 60px;
  height: 60px;
}
</style>
