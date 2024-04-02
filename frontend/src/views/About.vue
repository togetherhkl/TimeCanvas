<template>
    <div id="app">
      <!--  <header>头部内容</header> -->
      <main ref="scrollContainer" @wheel="handleScroll" style="overflow: hidden;">
        <div class="page" v-for="(page, index) in pages" :key="index">
          <div v-if="index === 0">
            <div class="page1">
              <div class="background"></div>
              <div class="title">时光画廊</div>
              <div class="welcome">
                ————你心灵栖息的地方
              </div>
            </div>
          </div>
          <div v-else-if="index === 1">
            <div class="page2">
              <h1 class="gongneng">时光画廊功能</h1>
              <div class="card">
                <el-row :gutter="24">
                  <el-col :span="8">
                    <el-card shadow="hover">
                      <img src="../assets/2.jpg" style="max-width: 100%;height: auto;" alt="同学录展示图片">
                      <h3>同学录</h3>
                      <p>这是同学录的介绍文字······</p>
                    </el-card>
                  </el-col>
                  <el-col :span="8">
                    <el-card shadow="hover">
                      <img src="../assets/2.jpg" style="max-width:100%;height: auto;" alt="相册展示图片">
                      <h3>相册</h3>
                      <p>这是相册的介绍文字······</p>
                      <p>这是相册的介绍文字······</p>
                      <p>这是相册的介绍文字······</p>
                      <p>这是相册的介绍文字······</p>
                    </el-card>
                  </el-col>
                  <el-col :span="8">
                    <el-card shadow="hover">
                      <img src="../assets/2.jpg" style="max-width: 100%;height: auto;" alt="视频展示图片">
                      <h3>视频</h3>
                      <p>这是同学录的介绍文字······</p>
                    </el-card>
                  </el-col>
                </el-row>
              </div>
            </div>
          </div>
          <div v-else-if="index === 2">
            <div class="page3">
              <h1 class="xijie">细节</h1>
              <div class="xijie-card-container">
                <div class="xijie-card">
                  <h>大语言模型</h>
                  <p>引入先进的大语言模型技术，让您的文字更加生动优美</p>
                </div>
                <div class="xijie-card">
                  <h>AES加密</h>
                  <p>采用AES加密技术，保障您的数据安全</p>
                </div>
                <div class="xijie-card">
                  <h>百度网盘授权</h>
                  <p>通过百度网盘授权，轻松实现数据的便捷存储与登录</p>
                </div>
                <div class="xijie-card">
                  <h>数据可视化</h>
                  <p>通过数据可视化技术，让您的数据更加直观</p>
                </div>
                <div class="xijie-card">
                  <h>AI分析</h>
                  <p>通过AI分析技术，让您的数据更加深入</p>
                </div>
              </div>
            </div>
          </div>
          <div v-else>
            <div class="last">
              <div class="page4">
                <div class="page4_img">
                  <img src="../assets/2.jpg" alt="look">
                </div>
                <div class="page4_text">
                  <h3>时光画廊</h3>
                  <p>
                    <br>在时光的镜里倒影，
                    <br>过去的影子如梦般飘忽。
                    <br>回忆如潮水般汹涌，
                    <br>泛起涟漪，激荡心灵深处。
                    <br>
                    <br>曾经的欢声笑语，
                    <br>在记忆中轻轻回响。
                    <br>那段岁月如流水匆匆，
                    <br>承载着无数珍贵瞬间。
                    <br>
                    <br>思念是一种甜蜜的负担，
                    <br>沉甸甸地压在胸口。
                    <br>我用文字编织着往昔的画卷，
                    <br>诉说那些被时间镌刻的情愫。
                    <br>
                    <br>时光在指尖流转，
                    <br>回忆在心头翩跹起舞。
                    <br>过去的思绪如实践，
                    <br>在现代的世界里闪烁。
                  </p>
                </div>
              </div>
              <div class="version">
                <ul>
                  <li>版权归属 © 2024 HKL,LJL. All Rights Reserved.</li>
                  <li>Powered By HKL,LJL.</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        currentPage: 0,
        pages: [0, 1, 2, 3],
      };
    },
    components: {
      Navigation,
    },
    mounted(){
      window.addEventListener('scroll', this.checkSlide);
    },
    methods: {
      handleScroll(event) {
        if (event.deltaY > 0 && this.currentPage < this.pages.length - 1) {
          this.currentPage++;
        } else if (event.deltaY < 0 && this.currentPage > 0) {
          this.currentPage--;
        }
        this.scrollToPage(this.currentPage);
        /* this.checkSlide(); */
      },
      scrollToPage(page) {
        const container = this.$refs.scrollContainer;
        container.scrollTop = page * window.innerHeight;
      },
      /* checkSlide() {
        const cards = document.querySelectorAll('.xijie-card');
        cards.forEach((cards)=>{
          const slideInAt = (window.scrollY + window.innerHeight) - cards.height / 2;
          const isHalfShown = slideInAt > cards.offsetTop;
          if (isHalfShown) {
            cards.classList.add('slide-up');
          } else {
            cards.classList.remove('slide-up');
          }
        });
      }, */
    },
  };
  </script>
  
  <style scoped>
  body {
    margin: 0;
    padding: 0;
    height: 100%;
    overflow: hidden;
  }
  
  #app {
    height: 100%;
  }
  
  .footer {
    height: 10vh;
    background-color: lightgray;
  }
  
  main {
    height: 100vh;
    overflow-y: hidden;
  }
  
  .page {
    height: 100%;
  }
  
  /* page1样式 */
  .page .page1 {
    position: relative;
  }
  
  .page .page1 .title {
    position: absolute;
    top: 35%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-family:'华文行楷', cursive;
    font-size: 15rem;
    font-weight: normal;
    color: black;
    white-space: nowrap;
  }
  .page .page1 .welcome {
    position: absolute;
    top: 65%;
    left: 70%;
    transform: translate(-50%, -50%);
    font-family:'华文行楷', cursive;
    font-size: 3rem;
    font-weight: normal;
    color: black;
    white-space: nowrap;
  }
  .page .page1 .background {
    height: 100vh;
    width: 100vw;
    opacity: 0.3;
    background-image: url('../assets/page1.png');
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
  }
  
  /* page2样式 */
  .gongneng {
    margin: 30px 0 60px 0;
    font-size: 40px;
    text-align: center;
  }
  
  .card {
    padding: 0 80px;
    animation: slide-up 1s ease-out both;
  }
  @keyframes slide-up {
    0% {
      transform: translateY(100px);
      opacity: 0;
    }
    100% {
      transform: translateY(0);
      opacity: 1;
    }
  }
  .card-container {
    width: 80%;
    max-width: 900px;
    margin: 0 auto;
  }
  
  /* page3样式 */
  .xijie {
    font-size: 40px;
    text-align: center;
  }
  .xijie-card-container {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    justify-content: space-around;
    align-items: center;
    flex-wrap: wrap;
    width: 100%;
    max-width: 900px;
    margin: 0 auto;
  }
  .xijie-card {
    width: 200px;
    height: 400px;
    margin: 20px 20px;
    justify-content: center;
    align-items: center;
    background-color: #f5f5f5;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    font-size: 20px;
    text-align: center;
    font-weight: bold;
    animation: slide-up 1s ease-out both;
  }
  /* page4样式 */
  .last {
    height: 90vh;
    display: grid;
    grid-template-rows: 1fr 100px;
    justify-content: center;
    align-items: center;
  }
  .page4 {
    width: 100%;
    height: 100%;
    padding: 20px 20px 50px 20px;
    display: flex;
    justify-content: center;
  }
  .page4_img {
    width: 50%;
    img {
      width: 100%;
      height: 80%;
      background-size: cover;
      background-repeat: no-repeat;
      background-position: center;
    }
  }
  .page4_text {
    width: 30%;
    padding: 0 90px;
  }
  .version {
    width: 100%;
    position: relative;
    bottom: 10px;
    text-align: center;
    background-color: black;
    li{
      color: white;
      list-style-type: none;
    }
  }
  </style>