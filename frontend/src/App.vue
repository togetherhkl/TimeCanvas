<template>
  <!-- //渲染路由 -->
  <router-view :key="$route.fullPath" />
</template>

<script>
export default{
  name: 'App'
};
</script>
