<template>
    <div class="parent-container">

        <div class="junior-layout">
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
.parent-container {
    height: 100vh;
    display: flex;
    flex-direction: column;
    background-image: linear-gradient(to right bottom, #fdf5e6, #ffe7d8, #ffd8d6, #fccbdf, #e4c4ee, #d5bff3, #c0bbf8, #a6b8fc, #abaffc, #b3a5fa, #bd99f5, #c88dee);
    .junior-layout {
        flex: 1;
        display: grid;
        grid-template-columns: 1.2fr 1fr;
        .left {
            display: grid;
            grid-template-rows: repeat(2, 1fr);
        }
        .right {
            display: grid;
            grid-template-rows: repeat(2, 1fr);
            .right-on {
                padding: 30px 60px 15px;
            }
            .right-off {
                padding: 20px 60px 44px;
            }
        }
    }
}
</style>