<template>
    <div class="video">
    <el-carousel :interval="5000" arrow="always">
        <el-carousel-item v-for="item in 4" :key="item">
            <h3 text="2xl" justify="center">{{ item }}</h3>
        </el-carousel-item>
    </el-carousel>
    </div>
</template>
<style>
.video {
    margin-top: 20px;
    width: 60%;
    padding: 10px;
    margin-bottom: 50px;
    align-items: center;
    justify-content: center;
}
/* 视频轮播图样式 */
.el-carousel__item h3 {
    color: #475669;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
    text-align: center;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
}
</style>