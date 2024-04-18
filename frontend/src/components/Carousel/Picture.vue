<template>
    <div class="picture">
        <el-carousel :interval="5000" type="card" arrow="hover">
            <el-carousel-item height="auto"  v-for="item in pictures" :key="item">
                <el-image style="width: 100%; height: 100%;" :src=item fit="fill" :crossorigin="null"/>
            </el-carousel-item>
        </el-carousel>
    </div>
</template>
<script>
import { ref, onMounted ,watch} from 'vue';
import axios from 'axios';
export default {
    props: {
        selectedClassmate: {
            type: Object,
            default: null
        },
        selectedEvent: {
            type: Object,
            default: null
        },
        selectedTravel: {
            type: Object,
            default: null
        },
    },
    setup(props) {
        const pictures = ref([]);//图片列表
        const backdata=ref([]);//储存后端传过来的数据：id和name
        watch(()=>props.selectedClassmate,(newVal)=>{
            if(newVal){
                backdata.value={id:newVal.id,name:newVal.name};
                axios.get('/albumfiles',{params:{folder_name:newVal.classmates_album_path+'/'+newVal.name+'/pictures'}})
                .then(response=>{
                    pictures.value=response.data;
                }).catch(error=>{
                    console.error('响应失败！',error);
                });
            }else{
                console.log('没有匹配到同学的照片信息！');
            };
        });
        watch(()=>props.selectedEvent,(newVal)=>{
            if(newVal){
                backdata.value={id:newVal.id,name:newVal.event_name};
                axios.get('/albumfiles',{params:{folder_name:newVal.event_album_path+'/'+newVal.event_name+'/pictures'}})
                .then(response=>{
                    pictures.value=response.data;
                }).catch(error=>{
                    console.error('响应失败！',error);
                });
            }else{
                console.log('没有匹配到活动的照片信息！');
            };
        });
        watch(()=>props.selectedTravel,(newVal)=>{
            if(newVal){
                backdata.value={id:newVal.id,name:newVal.travel_theme};
                axios.get('/albumfiles',{params:{folder_name:newVal.travel_album_path+'/'+newVal.travel_theme+'/pictures'}})
                .then(response=>{
                    pictures.value=response.data;
                }).catch(error=>{
                    console.error('响应失败！',error);
                });
            }else{
                console.log('没有匹配到旅游的照片信息！');
            };
        });
        onMounted(async () => {
            try {
                // const response = await axios.get('/api/pictures');
                // pictures.value = response.data;
                // pictures.value=[
                //     {id:1,src:"https://images.unsplash.com/photo-1479660656269-197ebb83b540?dpr=2&auto=compress,format&fit=crop&w=1199&h=798&q=80&cs=tinysrgb&crop="},
                //     {id:2,src:"https://images.unsplash.com/photo-1550191778-d58f82c7ce5f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80"},
                //     {id:3,src:"https://images.unsplash.com/photo-1557684466-0e6563559d70?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80"},
                //     {id:4,src:"https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80"},
                //     {id:5,src:"https://images.unsplash.com/photo-1517212160285-e9fbf358c905?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=667&q=80"}
                // ]
            } catch (error) {
                console.error(error);
            }
        });

        return {
            pictures,
        };
    },
};

</script>
<style>
.picture {
    margin-top: 40px;
    width: 90%;
    height: auto;
    padding: 10px;
    align-items: center;
    justify-content: center;
}

/* 相册轮播图样式 */

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
}

</style>