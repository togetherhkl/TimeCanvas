<template>
  <div class="header">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false"
      @select="handleSelect">
      <el-menu-item index="0">
        <img class="logo" src="../assets/vue.svg" alt="project logo" />
      </el-menu-item>
      <el-menu-item index="1">首页</el-menu-item>
      <el-menu-item index="2">关于</el-menu-item>
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
  <el-drawer v-model="drawer" title="创建趣事录" :with-header="true" :before-close="handleClose">
    <CreateInterestingEvent />
  </el-drawer>
</template>

<script>
import axios from 'axios';
import avatar_url from '../assets/user.png';//引入默认头像
import { routerKey } from 'vue-router';
import CreateInterestingEvent from './CreateIntersetingEvent.vue';
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
      axios.get("/auth").then(
        response => {
          if (response.status == 200) {
            //加载后端传送过来的授权url地址
            window.location.href = response.data.auth_url;
          }
        },
      )
    },
    exit(){
      console.log('ok');
      sessionStorage.clear();/* 清除缓存与会话记录，但失败 */
      this.$router.push('/home');
    },
    //跳转到添加同学录页面
    AddCPage(){
      this.$router.push('/home/addinformation');
    },
    //跳转到添加趣事录页面
    AddIPage(){
      this.$router.push('/home/addinterestingevent');
    },
    //跳转到添加旅游志页面
    AddTPage(){
      this.$router.push('/home/addtravel');
    },
  },
  //重新加载页面时，获取url中的参数
  created() {
    //使用js代码获取url中的参数
    var urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('baidu_name') != null) {
      this.baidu_name = urlParams.get('baidu_name')
    }
    if (urlParams.get('avatar_url') != null) {
      this.avatar_url = urlParams.get('avatar_url')
    }
    if (urlParams.get('access_token') != null) {
      localStorage.setItem('timecanvas_token', urlParams.get('access_token'))
    }
    // if (this.$route.query.baidu_name != undefined) {
    //   this.baidu_name = this.$route.query.baidu_name
    // }
    // if (this.$route.query.avatar_url != undefined) {
    //   this.avatar_url = this.$route.query.avatar_url
    // }
    // if (this.$route.query.access_token != undefined) {
    //   localStorage.setItem('timecanvas_taken', this.$route.query.access_token)
    // }
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
