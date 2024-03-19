<template>
    <div class="home">
      <div class="bookshelf">
        <div class="book">
          <h1>同学录</h1>
          <p>记录美好校园时光</p>
         <!--  <img src="../assets/1.png" alt="同学录封面"> -->
          <button @click="readBook('同学录')">阅读</button>
        </div>
        <div class="book">
          <h1>趣事录</h1>
          <p>留下生活中的点点滴滴</p>
         <!--  <img src="../assets/1.png" alt="趣事录封面"> -->
          <button @click="readBook('趣事录')">阅读</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import Navigation from '../components/Navigation.vue';
  import Classmate from './Classmate1.vue';

  export default {
    components: {
      Navigation
    },
    methods: {
      readBook(title) {
        /*
        data: {
          album_type: [
            { id:'1' ,albumtype_name: '同学录', albumtype_description: '1.png' },
            { id:'2' ,albumtype_name: '趣事录', albumtype_description: '2.png' }
          ]
        }


        */
        alert('打开' + title);
        // 这里可以添加跳转逻辑，打开书籍详情页面等
        //跳转到addinformation页面
        if(title == '同学录')
          this.$router.push({path:'/album',query:{id:1}});
        if(title == '趣事录')
          this.$router.push('/home/interestingevent');
      }
    }
  }
  </script>
  
  <style scoped>
  .bookshelf {
    display: flex;
    justify-content: center;
    height: 100vh;
    padding-top: 100px ;
  }
  
  .book {
    width: 400px;
    height: 500px;
    background-color: #f2f2f2;
    background-image: url('../assets/1.png');
    background-size: cover;
    background-position: center;
    backdrop-filter: blur(10px);
    text-align: center;
    margin: 0 50px;
    padding: 40px;
    border-radius: 5px;
    box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  }
  
  .book h1 {
    font-size: 30px;
    margin: 20px 0;
  }
  .book p {
    font-size: 20px;
    margin: 20px 0;
  }
  .book button {
    width: 100px;
    height: 40px;
    position: relative;
    top: 320px;
    font-size: larger;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.3s;
  }
  </style>