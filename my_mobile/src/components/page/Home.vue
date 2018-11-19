<template>
    <div id="home">
        <van-pull-refresh v-model="isLoading" @refresh="onRefresh">
            <div id="notice_list">
                <div v-if="my_list.length == 0">
                    <p>暂无任务</p>
                </div>
                <template v-else>
                    <van-swipe :autoplay="3000">
                        <van-swipe-item v-for="notice in my_list" :key="notice.id">1</van-swipe-item>
                        <van-swipe-item>2</van-swipe-item>
                        <van-swipe-item>3</van-swipe-item>
                        <van-swipe-item>4</van-swipe-item>
                    </van-swipe>
                </template>
            </div>
        </van-pull-refresh>
    </div>
</template>

<script>
import { Notice } from "@/utils/ajaxFunctions";
export default {
  name: "home",
  data() {
    return {
      my_list: [],
      currentPage: 1,
      isLoading: false,
      token: this.$store.state.token
    };
  },
  methods: {
    onRefresh() {
      Notice.get_notice(this.currentPage, this.token, this.set_notice_list);
    },
    set_notice_list(data) {
        this.my_list = data;
    }
  },
  created() {
    Notice.get_notice(this.currentPage, this.token, this.set_notice_list);
  }
};
</script>

