<template>
    <div class="container">
        <div class="layout-on">
            <div class="label">事件名称</div>
            <div class="box">{{ event_name }}</div>
            <div/>
            <div class="label">事件日期</div>
            <div class="box">{{ event_date }}</div>
        </div>
        <div class="empty"></div>
        <div class="layout-off">
            <div class="label">事件参与者</div>
            <div class="box">{{ event_participant }}</div>
            <div class="label">事件描述</div>
            <div class="box" v-html="markdownToHtml"></div>
            <!-- <div class="box">{{ event_description }}</div> -->
        </div>
    </div>
</template>
<script lang="ts">
import { PropType, watch, ref } from 'vue';
import { marked, options } from 'marked';//markdown解析器
export default {
    props: {
        selectedEvent: {
            type: Object as PropType<any>,
            default: null
        },
    },
    computed: {
        markdownToHtml() {
            return marked(this.event_description);
        }
    },
    setup(props) {
        const event_name = ref('');
        const event_date = ref('');
        const event_participant = ref('');
        const event_description = ref('');
        watch(() => props.selectedEvent, (newVal) => {
            if (newVal) {
                event_name.value = newVal.event_name;
                const EventDate=new Date(newVal.event_date);//获取事件日期
                const year= EventDate.getFullYear();//获取年份
                const month= EventDate.getMonth()+1;
                const day= EventDate.getDate();
                event_date.value = ''+year+'年'+month+'月'+day+'日';
                event_participant.value = newVal.event_participant;
                event_description.value = newVal.event_description;
            }
        });
        return {
            event_name,
            event_date,
            event_participant,
            event_description,
        };
    },
}
</script>
<style scoped>
.container {
    height: 100%;
    width: 100%;
    display: grid;
    grid-template-columns: 2fr 1fr;
}
.layout-on {
    display: grid;
    grid-template-columns: 1fr 3fr 20px 1fr 2fr;
}
.layout-off {
    grid-column: 1/3;
    display: grid;
    grid-template-columns: 1fr 10fr;
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