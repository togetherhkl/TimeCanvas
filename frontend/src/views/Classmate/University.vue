<template>
    <div class="container">
        <Header></Header>
        <div class="primary-layout">
            <div class="left">
                <div class="left-on">
                    <!-- 同学录信息展示 -->
                    <Information></Information>
                </div>
                <div class="left-off">
                    <!-- 毕业寄语 -->
                    <GraduationMessage></GraduationMessage>
                </div>
            </div>
            <div class="right">
                <div class="right-on">
                    <!-- 图片轮播图 -->
                    <Picture></Picture>
                </div>
                <div class="right-off">
                    <!-- 视频轮播图 -->
                    <Video></Video>
                </div>
            </div>
        </div>
    </div>
</template>
<script >
import Header from '@/components/Navigation.vue';
import Information from '@/components/Information.vue';
import GraduationMessage from '@/components/GraduationMessage.vue';
import Picture from '@/components/Carousel/Picture.vue';
import Video from '@/components/Carousel/Video.vue';
export default {
    // 状态
    data() {
        return {

        }
    },
    components: {
        Header,
        Information,
        GraduationMessage,
        Picture,
        Video,
    },
    // 动作
}
</script>
<style scoped>
* {
    padding: 0;
    margin: 0;
}

.container {
    height: 100%;
    width: 100%;
    background-image: linear-gradient(to right bottom, #fdf5e6, #ffe7d8, #ffd8d6, #fccbdf, #e4c4ee, #d5bff3, #c0bbf8, #a6b8fc, #abaffc, #b3a5fa, #bd99f5, #c88dee);
/*     background-image: linear-gradient(to right bottom, #d1806b, #d89164, #d9a360, #d4b761, #c8cc6a, #a1d476, #70d98e, #00dcae, #00cdd8, #00b9ff, #009dff, #5f76fb); */
/* background-image: linear-gradient(to right bottom, #d1806b, #d89164, #d9a360, #d4b761, #c8cc6a, #c8cc6a, #c8cc6a, #c8cc6a, #d4b761, #d9a360, #d89164, #d1806b); */
    .primary-layout {
        height: calc(100vh-50px);
        display: grid;
        grid-template-columns: 1.2fr 1fr;

        /* gap:20px; */
        .left {
            display: grid;
            grid-template-rows: repeat(2, 1fr);
        }
        .right {
            display: grid;
            grid-template-rows: repeat(2, 1fr);
            .right-on {
                padding: 30px 70px 15px;
            }
            .right-off {
                padding: 20px 70px 44px;
            }
        }
    }
}
</style>