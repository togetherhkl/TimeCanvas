<template>
  <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false" @select="handleSelect">
    <el-menu-item index="0">
      <img class="logo" src="../assets/vue.svg" alt="Element logo" />
    </el-menu-item>
    <el-menu-item index="1">首页</el-menu-item>
    <el-menu-item index="2">关于</el-menu-item>
    <div class="flex-grow" />
    <el-sub-menu index="2">
      <template #title>创建</template>
      <el-menu-item index="2-1">item one</el-menu-item>
      <el-menu-item index="2-2">item two</el-menu-item>
      <el-menu-item index="2-3">item three</el-menu-item>
    </el-sub-menu>
    <el-menu-item index="3">
      <el-icon>
        <Moon />
      </el-icon>
    </el-menu-item>
    <el-sub-menu index="4" @click="getTaken">
      <template #title>
        <el-avatar :src="avatar_url" :size="40" />
        {{ baidu_name }}
      </template>
      <el-menu-item index="3-1">个人中心</el-menu-item>
      <el-menu-item index="3-2">退出</el-menu-item>
    </el-sub-menu>
  </el-menu>
</template>

<script>
import axios from 'axios'
import avatar_url from '../assets/user.png'
export default {
  // 状态
  data() {
    return {
      count: 0,
      activeIndex: '1',
      baidu_name: '请登录',
      avatar_url: avatar_url,
      access_token: '',
    }
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
          // console.log(response)
          if(response.status==200){
            //加载后端传送过来的授权url地址
            // console.log(response.data.auth_url)
            window.location.href=response.data.auth_url;
          }
        },
      )
    }, 
  },
  created() {
    if(this.$route.query.baidu_name!=undefined){
      this.baidu_name = this.$route.query.baidu_name
    }
    if(this.$route.query.avatar_url!=undefined){
      this.avatar_url = this.$route.query.avatar_url
    }
    this.access_token = this.$route.query.access_token
  },
}
</script>

<style>
.flex-grow {
  flex-grow: 1;
}

.logo {
  width: 50px;
  height: 50px;
}
</style>
