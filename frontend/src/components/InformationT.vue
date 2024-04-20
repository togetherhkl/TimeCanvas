<template>
    <div class="container">
        <div class="layout-on">
            <div class="label">旅游志名称</div>
            <div class="box">{{ travel_theme }}</div>
            <div />
            <div class="label">旅游日期</div>
            <div class="box">{{ travel_date }}</div>
            <div />
            <div class="label">旅游地点</div>
            <div class="box">{{ travel_province + travel_place }}</div>
        </div>
        <div class="layout-off">
            <div class="label">旅游参与者</div>
            <div class="box">{{ travel_participant }}</div>
            <div class="label">旅游描述</div>
            <div class="box" v-html="markdownToHtml"></div>
        </div>
    </div>
</template>
<script lang="ts">
import { PropType, watch, ref } from 'vue';
import { marked, options } from 'marked';//markdown解析器
export default {
    props: {
        selectedTravel: {
            type: Object as PropType<any>,
            default: null
        },
    },
    computed: {
        markdownToHtml() {
            return marked(this.travel_description);
        }
    },
    setup(props) {
        const travel_theme = ref('');
        const travel_date = ref('');
        const travel_place = ref('');
        const travel_participant = ref('');
        const travel_description = ref('');
        const travel_province = ref('');
        watch(() => props.selectedTravel, (newVal) => {
            if (newVal) {
                console.log('new:', newVal);
                travel_theme.value = newVal.travel_theme;
                const TravelDate = new Date(newVal.travel_date);
                const year = TravelDate.getFullYear();//获取年份
                const month = TravelDate.getMonth() + 1;
                const day = TravelDate.getDate();
                travel_date.value = '' + year + '年' + month + '月' + day + '日';
                travel_province.value = newVal.travel_province;
                travel_place.value = newVal.travel_place;
                travel_participant.value = newVal.travel_participant;
                travel_description.value = newVal.travel_description;
            }
        });
        return {
            travel_theme,
            travel_date,
            travel_place,
            travel_participant,
            travel_description,
            travel_province,
        };
    },
}
</script>
<style scoped>
.container {
    height: 100%;
    width: 100%;
    display: grid;
}

.layout-on {
    display: grid;
    grid-template-columns: 1fr 2fr 20px 1fr 1fr 20px 1fr 3fr;
}

.layout-off {
    grid-column: 1/3;
    display: grid;
    grid-template-columns: 1fr 9fr;
}

.label {
    height: 20px;
    background-color: #fdf5e6;
    border-radius: 8px;
    padding: 10px;
    margin: 0 0 20px 0;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.layout-on .box {
    width: 100%;
    height: 20px;
    padding: 10px;
    margin-bottom: 20px;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.2);
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    box-shadow: inset 0 0 6px rgba(255, 255, 255, 0.2);
}

.layout-off .box {
    width: 100%;
    height: 100px;
    padding: 10px;
    margin-bottom: 20px;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.2);
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    box-shadow: inset 0 0 6px rgba(255, 255, 255, 0.2);
}
</style>