<template>
    <div class="information-container">
        <div class="classmate-image">
            <img src="../assets/1.png" style="width: 170px; height: 200px; margin: 20px;border-radius: 50%;" alt="同学录头像">
        </div>
        <div class="information">
            <div class="label">
                <i class="iconfont icon-xingming"></i>
                姓名
            </div>
            <div class="box">姓名</div>
            <div class="label">
                <i class="iconfont icon-nicheng"></i>
                昵称
            </div>
            <div class="box">昵称</div>
            <div class="label">
                <i class="iconfont icon-shengrix"></i>
                生日
            </div>
            <div class="box">生日</div>
            <div class="label">
                <i class="iconfont icon-jiaxiang"></i>
                家乡
            </div>
            <div class="box">家乡</div>
            <div class="label">
                <i class="iconfont icon-ziyuan25"></i>
                爱好
            </div>
            <div class="box">爱好</div>
            <div class="label">
                <i class="iconfont icon-QQ"></i>
                QQ
            </div>
            <div class="box">QQ</div>
            <div class="label">
                <i class="iconfont icon-weixin"></i>
                微信
            </div>
            <div class="box">微信</div>
            <div class="label">
                <i class="iconfont icon-shouji"></i>
                手机
            </div>
            <div class="box">手机号</div>
            <div class="label">
                <i class="iconfont icon-youxiang"></i>
                邮箱
            </div>
            <div class="box">邮箱</div>
            <div class="label">
                <i class="iconfont icon-xingzuo"></i>
                星座
            </div>
            <div class="box">星座</div>
        </div>
        <div class="left-off">
            <div class="mengxiang-label">
                <i class="iconfont icon-mengxiang"></i>
                <span style="writing-mode: vertical-rl;">梦</span>
                <span style="writing-mode: vertical-rl;">想</span>
            </div>
            <div class="mengxiang-box">梦想</div>
        </div>
        <div class="right-off"></div>
    </div>
</template>
<script setup>

</script>

<style scoped>
.information-container {
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-columns: 1fr 2fr;

    .left-off {
        grid-column: 1/3;
        display: grid;
        grid-template-columns: 1fr 17fr;
    }

    .right-off {
        display: none;
    }
}
.information {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr 2fr;

}

.label {
    height: 20px;
    background-color: #fdf5e6;
    border-radius: 8px;
    padding: 10px;
    margin: 0;
    display: flex;
}
.box {
    height: 20px;
    padding: 10px;
    margin: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.2);
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    box-shadow:inset 0 0 6px rgba(255, 255, 255, 0.2);
}
.mengxiang-label {
    height: auto;
    background-color: #fdf5e6;
    border-radius: 8px;
    padding: 10px;
    margin: 0;
    display: flex;
    writing-mode: vertical-rl;
}
.mengxiang-box {
    padding: 10px;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.2);
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    box-shadow:inset 0 0 6px rgba(255, 255, 255, 0.2);
}
</style>