<template>
  <div class="container">
    <Navigation />
    <Main></Main>
  </div>
</template>

<script>
//从components中导入Navigation组件
import Navigation from '../components/Navigation.vue'
import Main from '../components/Main.vue'
export default {
  // 状态
  data() {
    return {

    }
  },
  components: {
    Navigation,
    Main,
  },
  // 动作
}
</script>
<style scoped>
.container{
  display: flex;
  flex-direction: column;
  height: 100vh; /* 使用视口高度作为整个布局的高度 */
}
</style>