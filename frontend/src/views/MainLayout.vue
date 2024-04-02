<template>
    <div>
      <!-- 导航栏 -->
      <Navigation />
      <!-- 子路由将在这里渲染 -->
      <router-view />
    </div>
  </template>
  
  <script>
  import Navigation from '../components/Navigation.vue'
  
  export default {
    components: {
      Navigation
    }
  }
  </script>