<template>
  <div class="main">
    <div class="main-on">
      <div class="on-space">
        <el-row :gutter="20">
          <el-col :span="4">
            <div class="grid-content ep-bg-purple" style="text-align: center;">
              <img src="../assets/1.png" style="width: 180px;height: 250px;" alt="同学录">
              <p style="font-size: larger; align-items: center;">同学录</p>
            </div>
          </el-col>
          <el-col :span="20">
            <ul class="card-list">

              <li class="card">
                <a class="card-image" target="_blank" @click="$router.push('/home/primary')">
                  <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/310408/psychopomp-500.jpg"
                    @click="$router.push('/home/primary')" alt="primary" />
                </a>
                <a class="card-description"  @click="$router.push('/home/primary')">
                  <h2>小学</h2>
                </a>
              </li>

              <li class="card">
                <a class="card-image" @click="$router.push('/home/junior')">
                  <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/310408/lets-go-500.jpg" alt="junior" />
                </a>
                <a class="card-description" @click="$router.push('/home/junior')">
                  <h2>初中</h2>
                </a>
              </li>

              <li class="card">
                <a class="card-image" target="_blank" @click="$router.push('/home/senior')">
                  <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/310408/beautiful-game-500.jpg" alt="senior" />
                </a>
                <a class="card-description"  @click="$router.push('/home/senior')">
                  <h2>高中</h2>
                </a>
              </li>

              <li class="card">
                <a class="card-image" target="_blank" @click="$router.push('/home/university')">
                  <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/310408/jane-doe-500.jpg" alt="university" />
                </a>
                <a class="card-description"  @click="$router.push('/home/university')">
                  <h2>大学</h2>
                </a>
              </li>

            </ul>
          </el-col>
        </el-row>

      </div>
    </div>
    <div class="main-off">
      <div class="on-space">
        <el-row :gutter="20">
          <el-col :span="4">
            <div class="grid-content ep-bg-purple" style="text-align: center;">
              <img src="../assets/1.png" style="width: 180px;height: 250px;" alt="趣事录">
              <p style="font-size: larger; align-items: center;">趣事录</p>
            </div>
          </el-col>
          <el-col :span="20">
            <ul class="card-list">


              <li class="card">
                <a class="card-image" @click="$router.push('/home/junior')">
                  <img src="../assets/vue.svg" alt="junior" />
                </a>
                <a class="card-description" @click="$router.push('/home/junior')">
                  <h2>篮球</h2>
                </a>
              </li>

              <li class="card">
                <a class="card-image" @click="$router.push('/home/junior')">
                  <img src="../assets/vue.svg" alt="junior" />
                </a>
                <a class="card-description" @click="$router.push('/home/junior')">
                  <h2>足球</h2>
                </a>
              </li>

              <li class="card">
                <a class="card-image" @click="$router.push('/home/junior')">
                  <img src="../assets/vue.svg" alt="junior" />
                </a>
                <a class="card-description" @click="$router.push('/home/junior')">
                  <h2>羽毛球</h2>
                </a>
              </li>

              <li class="card">
                <a class="card-image" @click="$router.push('/home/junior')">
                  <img src="../assets/vue.svg" alt="junior" />
                </a>
                <a class="card-description" @click="$router.push('/home/junior')">
                  <h2>拔河</h2>
                </a>
              </li>

            </ul>
          </el-col>
        </el-row>

      </div>
    </div>
  </div>
</template>
    
<script setup>
/* 图片js */
const src = 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'
//图片懒加载实现
// 等待整个页面加载完成
/* window.addEventListener('load', function () {
  // 使用setTimeout来模拟真实页面加载的延迟
  setTimeout(lazyLoad, 1000);
});

function lazyLoad() {
  var card_images = document.querySelectorAll('.card-image');
  // 遍历每个card image
  card_images.forEach(function (card_image) {
    var image_url = card_image.getAttribute('data-image-full');
    var content_image = card_image.querySelector('img');
    // 更改内容图片的src以加载新的高清图片
    content_image.src = image_url;
    // 当新图片加载完成时监听load事件
    content_image.addEventListener('load', function () {
      // 使用新下载的图片替换可见背景图片
      card_image.style.backgroundImage = 'url(' + image_url + ')';
      // 添加一个类以移除模糊滤镜，实现平滑过渡图片更改效果
      card_image.className = card_image.className + ' is-loaded';
    });
  });
} */

</script>
    
<style scoped>
.main {
  width: 100vw;
  height: 100vh;
  flex: 1;
  display: flex;
  flex-direction: column;/* 设置主轴方向为垂直方向 */
  .main-on {
    flex: 1;/* 让子项填充剩余空间 */
    width: 100%;
    margin: 0 auto;/* 控制边缘边距 */
  }
  .main-off {
    flex: 1;/* 让子项填充剩余空间 */
    width: 100%;
    margin: 0 auto;/* 控制边缘边距 */
  }
}

.on-space {
  height: 300px;
  width: auto;
  margin: 40px 50px auto;
}

/* 同学录相册样式 */
/* 懒加载样式 */
.card-image {
  display: block;
  min-height: 230px;
  background: #fff center center no-repeat;
  background-size: cover;
}

.card-image>img {
  display: block;
  width: 100%;
  opacity: 1;
}
.card-list {
  display: block;
  margin: 0 auto;
  padding: 0;
  font-size: 0;
  text-align: center;
  list-style: none;
}

.card {
  display: inline-block;
  width: 200px;
  max-width: 20rem;
  margin: 0 1rem auto;
  font-size: 1rem;
  text-decoration: none;
  overflow: hidden;
  box-shadow: 0 0 3rem -1rem rgba(0, 0, 0, 0.5);
  transition: transform 0.1s ease-in-out, box-shadow 0.1s;
}

.card:hover {
  transform: translateY(-0.5rem) scale(1.0125);
  box-shadow: 0 0.5em 3rem -1rem rgba(0, 0, 0, 0.5);
}

.card-description {
  display: block;
  padding: 1em 0.5em;
  color: #515151;
  text-decoration: none;
}

.card-description>h2 {
  margin: 0 0 0.5em;
}
</style>
    