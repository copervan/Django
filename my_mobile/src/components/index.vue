<template>
    <div id="app_index">
        <keep-alive>
            <component v-bind:is="currentTabComponent"></component>
        </keep-alive>
        <van-tabbar v-model="active" :change="change_item(active)">
            <van-tabbar-item icon="shop">首页</van-tabbar-item>
            <van-tabbar-item icon="chat">日志</van-tabbar-item>
            <van-tabbar-item icon="records">备忘录</van-tabbar-item>
            <van-tabbar-item icon="gold-coin">我的</van-tabbar-item>
        </van-tabbar>
    </div>
</template>

<script>
import hello from "@/components/HelloWorld.vue";
import Home from "@/components/page/Home.vue";
import Diary from "@/components/page/Diary.vue";
import Notice from "@/components/page/Notice.vue";
import Profile from "@/components/page/Profile.vue";

export default {
  name: "home_index",
  data() {
    return {
      active: 0,
      token: 123,
      currentPage: Home
    };
  },
  methods: {
    change_item(active) {
    //   console.log(active);
      if (active == 0) {
        this.currentPage = Home;
      } else if (active == 1) {
        this.currentPage = Diary;
      } else if (active == 2) {
        this.currentPage = Notice;
      } else if (active == 3) {
        this.currentPage = Profile;
      } else {
        this.currentPage = Home;
      }
    }
  },
  created: function() {
    if (!this.token || typeof this.token === "undefined") {
      this.$router.replace({ path: "/" });
    } else {
      // console.log("the Token: "+ this.token)
    }
  },
  computed: {
    currentTabComponent: function() {
    //   console.log("currentTabComponent index:" + this.active);
      return this.currentPage;
    }
  }
};
</script>

