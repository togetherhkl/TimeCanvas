<template>
    <div class="classmate_container">
        <!-- ... 其他内容 ... -->
        <div class="header">
            <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false"
                @select="handleSelect">
                <el-menu-item index="0">
                    <img class="logo" src="../assets/vue.svg" alt="Element logo" />
                </el-menu-item>
                <el-menu-item index="1" @click="$router.push('/home')">首页</el-menu-item>
                <el-menu-item index="2" @click="$router.push('/about')">关于</el-menu-item>
                <div class="flex-grow">
                    <div class="title">同学录</div>
                </div>
                <el-menu-item index="3">
                    <el-button type="text" @click="drawer = true">创建同学录</el-button>
                </el-menu-item>
                <el-sub-menu index="4">
                    <template #title>管理同学录</template>
                    <el-menu-item index="4-1" @click="$router.push('/home/classmate/addinformation')">增加</el-menu-item>
                    <el-menu-item index="4-2">编辑</el-menu-item>
                    <el-menu-item ibndex="4-3">删除</el-menu-item>
                </el-sub-menu>
                <el-menu-item index="5">
                    <el-icon>
                        <Moon />
                    </el-icon>
                </el-menu-item>
                <el-sub-menu index="6" @click="getTaken">
                    <template #title>
                        <el-avatar :src="avatar_url" :size="40" />
                        {{ baidu_name }}
                    </template>
                    <el-menu-item index="3-1">个人中心</el-menu-item>
                    <el-menu-item index="3-2">退出</el-menu-item>
                </el-sub-menu>
            </el-menu>
        </div>

        <div class="cards">
            <el-row :gutter="24">
                <el-col :span="4" v-for="card in cards" :key="card.id" @click="handleCardClick(card.id)">
                    <div class="card" style="text-align: center;">
                        <img :src="card.imageUrl" style="width: 200px; height: 250px;background-size: cover;"
                            :alt="card.alt" />
                        <p style="font-size: larger; align-items: center;">{{ card.title }}</p>
                    </div>
                </el-col>
            </el-row>
        </div>

        <el-drawer v-model="drawer" title="创建同学录" :with-header="ture">
            <el-form :model="classmateForm" label-width="100px">
                <el-form-item label="同学录名称" prop="name">
                    <el-input v-model="classmateForm.name"></el-input>
                </el-form-item>
                <el-form-item label="上传封面图" prop="imgurl">
                    <el-input v-model="classmateForm.imgurl"></el-input>
                    <!-- <el-upload
              class="avatar-uploader"
              action="https://"
              :on-success="handleAvatarSuccess"
              :before-upload="beforeAvatarUpload"
            >
              <img v-if="classmateForm.imgurl" :src="classmateForm.imgurl" class="avatar">
              <el-icon v-else class="avatar-uploader-icon"><Plus /></el-icon>
            </el-upload> -->
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="confirmClassmate">确认</el-button>
                    <el-button @click="closeDrawer">取消</el-button>
                </el-form-item>
            </el-form>
        </el-drawer>

    </div>
</template>

<script>

export default {
    data() {
        return {
            drawer: false,
            classmateForm: {       // 表单数据
                name: '',
                imgurl: ''
            },
            cards: [
                { id: 1, imageUrl: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/310408/psychopomp-500.jpg', alt: 'primary', title: '小学' },
                { id: 2, imageUrl: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/310408/lets-go-500.jpg', alt: 'junior', title: '初中' },
                { id: 3, imageUrl: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/310408/beautiful-game-500.jpg', alt: 'senior', title: '高中' },
                { id: 4, imageUrl: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/310408/jane-doe-500.jpg', alt: 'university', title: '大学' }
            ]
        };
    },
    methods: {
        openDrawer() {
            this.drawer = true;
        },
        closeDrawer() {
            this.drawer = false;
            this.resetForm();
        },
        /* 图片 */
        handleAvatarSuccess(res, file) {
            this.classmateForm.imgurl = URL.createObjectURL(file.raw);// 上传成功后的图片地址
        },
        beforeAvatarUpload(file) {
            // ... 校验规则 ...
        },
        confirmClassmate() {
            /* 先将数据传到后端 */

            this.cards.push({
                id: this.cards.length + 1,
                imageUrl: this.classmateForm.imgurl,// 上传成功后的图片地址
                alt: 'custom',
                title: this.classmateForm.name
            });
            this.closeDrawer();
        },
        resetForm() {
            this.classmateForm.name = '';
            this.classmateForm.imgurl = '';
        },
        /* 跳转路由 */
        handleCardClick(id) {
            let card = this.cards.find(card => card.id === id);//
            let url = `/home/classmate/${card.alt}`;
            this.$router.push(url);
        }
    }
};
</script>

<style scoped>
.on-space {
    height: 300px;
    width: auto;
    margin: 40px 50px auto;
}

.header {
    flex: 0 0 auto;
    /* 设置头部不随着主体内容而伸缩 */
}

.flex-grow {
    flex-grow: 1;
    font-size: 30px;
    text-align: center;
    /* 文字水平、垂直居中 */
    line-height: 50px;
}

.logo {
    width: 50px;
    height: 50px;
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
    margin: 1rem 1rem auto;
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

/* 上传图片 */
.avatar-uploader .avatar {
    width: 178px;
    height: 178px;
    display: block;
}

.avatar-uploader .el-upload {
    border: 1px dashed var(--el-border-color);
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
    border-color: var(--el-color-primary);
}

.el-icon.avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    text-align: center;
}
</style>