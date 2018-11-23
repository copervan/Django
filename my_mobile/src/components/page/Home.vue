<template>
    <div id="home">
        <van-nav-bar title="首页"  fixed />
        <div id="my-home-page"></div>
        <van-pull-refresh v-model="isLoading" @refresh="onRefresh" >
            <div id="notice_list">
                <div v-if="my_list.length == 0">
                    <p>暂无任务</p>
                </div>
                <template v-else>
                    <van-swipe :autoplay="3000" :show-indicators="fal">
                        <van-swipe-item v-for="notice in my_list" :key="notice.id">
                            <van-panel class="my-panel" icon="clock" :title="notice.notice_item" :status="notice_code(notice.status)">
                                <div slot="footer">
                                    内容
                                </div>
                            </van-panel>
                        </van-swipe-item>
                    </van-swipe>
                </template>
            </div>
            <div id="diary_list" class="notice-list">
                <div v-if="diary_list.length == 0">
                    <p>你已经好几天没写日志了，赶紧填写日志吧！</p>
                </div>
                <template else>
                    <van-list>
                        <van-cell v-for="item in diary_list" :key="item.id" :title="item.title" is-link :value="formatDate(item.date)"/>
                    </van-list>
                </template>
            </div>
        </van-pull-refresh>
    </div>
</template>

<script>
import { Notice, Diarys } from "@/utils/ajaxFunctions";
export default {
  name: "home",
  data() {
    return {
      my_list: [],
      diary_list: [],
      diary_count: 0,
      currentPage: 1,
      isLoading: false,
      finished: false,
      token: this.$store.state.token
    };
  },
  methods: {
    onRefresh() {
      setTimeout(() => {
        this.isLoading = false;
        Notice.get_notice(this.currentPage, this.token, this.set_notice_list);
        this.$toast("刷新成功");
      }, 2000);
    },
    set_notice_list(data) {
      this.my_list = data;
      console.log(data);
    },
    set_diary_list(data) {
      this.diary_list = data.results;
      this.diary_count = data.count;
      console.log(this.diary_list);
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
        (min < 10 ? "0" + min : min)

      return newTime;
    },
    notice_code(code) {
      if (code === 0) {
        return "未开始";
      } else if (code === 1) {
        return "已完成";
      } else if (code === 2) {
        return "进行中";
      } else if (code === 3) {
        return "拒  绝";
      } else {
        return "未知状态：" + code;
      }
    }
  },
  created() {
    Notice.get_notice(this.currentPage, this.token, this.set_notice_list);
    Diarys.get_diary(this.currentPage, this.token, this.set_diary_list);
  }
};
</script>

<style>
.my-panel {
  border: solid white 1px;
  text-align: left;
  min-height: 30px;
}
.notice-list {
  text-align: left;
}
#my-home-page {
    margin-top: 50px;
    margin-bottom: 50px;
}
</style>
