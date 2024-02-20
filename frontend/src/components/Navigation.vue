<template>
  <div class="header">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false"
      @select="handleSelect">
      <el-menu-item index="0">
        <img class="logo" src="../assets/vue.svg" alt="Element logo" />
      </el-menu-item>
      <el-menu-item index="1">首页</el-menu-item>
      <el-menu-item index="2">关于</el-menu-item>
      <div class="flex-grow" />
      <el-sub-menu index="2">
        <template #title>创建</template>
        <el-menu-item index="2-1">同学录</el-menu-item>
        <el-menu-item index="2-2">趣事录</el-menu-item>
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
  </div>
</template>

<script>
import axios from 'axios';
import avatar_url from '../assets/user.png';//引入默认头像
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
          if (response.status == 200) {
            //加载后端传送过来的授权url地址
            window.location.href = response.data.auth_url;
          }
        },
      )
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
  width: 50px;
  height: 50px;
}
</style>
