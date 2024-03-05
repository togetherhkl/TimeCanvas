<template>
  <!-- //渲染路由 -->
  <router-view :key="$route.fullPath" />
</template>

<script>
export default{
  name: 'App'
};
</script>
<style>
/* 隐藏所有滚动条 */
::-webkit-scrollbar {
  width: 0 !important;
}
::-webkit-scrollbar {
  width: 0 !important;
  height: 0;
}
</style>