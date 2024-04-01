<template>
    <div class="container">
        <div class="layout-on">
            <div class="label">旅游志名称</div>
            <div class="box">{{ travel_theme }}</div>
            <div/>
            <div class="label">旅游日期</div>
            <div class="box">{{ travel_date }}</div>
            <div />
            <div class="label">旅游地点</div>
            <div class="box">{{ travel_place }}</div>
        </div>
        <!-- <div class="empty"></div> -->
        <div class="layout-off">
            <div class="label">旅游参与者</div>
            <div class="box">{{ travel_participant }}</div>
            <div class="label">旅游描述</div>
            <div class="box">{{ travel_description }}</div>
        </div>
    </div>
</template>
<script lang="ts">
import { PropType, watch, ref } from 'vue';
export default {
    props: {
        selectedTravel: {
            type: Object as PropType<any>,
            default: null
        },
    },
    setup(props) {
        const travel_theme = ref('');
        const travel_date = ref('');
        const travel_place = ref('');
        const travel_participant = ref('');
        const travel_description = ref('');
        watch(() => props.selectedTravel, (newVal) => {
            if (newVal) {
                travel_theme.value = newVal.travel_theme;
                travel_date.value = newVal.travel_date;
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
        };
    },
}
</script>
<style scoped>
.container {
    height: 100%;
    width: 100%;
    display: grid;
    /* grid-template-columns: 1fr 1fr; */
}
.layout-on {
    display: grid;
    grid-template-columns: 1fr 3fr 20px 1fr 2fr 20px 1fr 3fr;
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