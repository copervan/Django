<template>
    <div id="diary-detail">
        <van-nav-bar title="日志详情" fixed left-arrow @click-left="onClickLeft" />
        <div style="margin-top:50px;margin-buttom:50px">
            <van-panel :title="diary.title"  :status="formatDate(diary.date)">
                <div v-html="diary.content"></div>
            </van-panel>
        </div>
    </div>
</template>

<script>
import { Diarys,Functions } from "@/utils/ajaxFunctions";
export default {
  name: "diary_detail",
  data() {
    return {
      diary_id: this.$route.params.diary_id,
      diary: {},
      token: this.$store.state.token
    };
  },
  methods: {
    set_diary(data) {
      this.diary = data;
    },
    onClickLeft() {
      this.$router.back(-1);
    }, 
    formatDate(data) {
        return Functions.formatDate(data)
    }
  },
  created() {
    Diarys.get_diary_by_id(this.diary_id, this.token, this.set_diary);
  }
};
</script>

<style>
#diary-detail {
    text-align: left;
    padding: 5px
}
</style>
