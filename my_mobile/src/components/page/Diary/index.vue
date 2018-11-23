<template>
  <div id="diary">
    <van-nav-bar title="日志" fixed @click-right="onRefresh" >
      <van-icon name="more-o" slot="right" />
    </van-nav-bar>
    <!-- <van-pull-refresh v-model="isLoading" @refresh="onRefresh"> -->
    <van-list v-model="loading" :finished="finished" @load="onLoad" class="my-dairy-list">
      <van-cell class="my-diary" v-for="item in diary_list" :key="item.id * (new Date().getTime() )" :title="item.title" is-link :value="formatDate(item.date)" :to="{name: 'diaryView',params: { 'diary_id': item.id }}" />
    </van-list>
    <!-- </van-pull-refresh> -->
  </div>
</template>

<script>
import { Diarys } from "@/utils/ajaxFunctions";
export default {
  name: "diary",
  data() {
    return {
      diary_list: [],
      token: this.$store.state.token,
      currentPage: 0,
      diary_count: 0,
      loading: false,
      finished: false,
      isLoading: false
    };
  },
  methods: {
    set_diary_list(data) {
      let next = data.next;
      this.diary_list = [...this.diary_list, ...data.results];
      this.diary_count = data.count;
      console.log(this.diary_list);
      console.log(new Date());
      this.loading = false;
      if (!next) {
        this.finished = true;
        console.log(next + "true");
      } else {
        this.finished = false;
        console.log(next + "false");
      }
    },
    onLoad() {
      console.log("onload ---");
      this.currentPage += 1;
      Diarys.get_diary(this.currentPage, this.token, this.set_diary_list);
    },
    onRefresh() {
      this.currentPage = 0;
      this.diary_list = [];
      this.onLoad();
    },
    // 格式化时间输出，可以写成功能函数， 有时间再弄
    formatDate(time) {
      var date = new Date(time);
      var year = date.getFullYear(),
        month = date.getMonth() + 1, //月份是从0开始的
        day = date.getDate(),
        hour = date.getHours(),
        min = date.getMinutes(),
        sec = date.getSeconds();
      var newTime =
        year +
        "-" +
        (month < 10 ? "0" + month : month) +
        "-" +
        (day < 10 ? "0" + day : day) +
        " " +
        (hour < 10 ? "0" + hour : hour) +
        ":" +
        (min < 10 ? "0" + min : min);

      return newTime;
    }
  }
  // created() {
  //   Diarys.get_diary(this.currentPage+1, this.token, this.set_diary_list);
  // }
};
</script>

<style>
.my-diary {
  text-align: left;
}
.my-dairy-list {
  margin-top: 50px;
  margin-bottom: 50px;
}
</style>
