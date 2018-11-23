<template>
  <div id="app_index">
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
    <van-tabbar v-model="activecode">
      <van-tabbar-item icon="shop" :to="{name:'home',params:{'active':0}}">首页</van-tabbar-item>
      <van-tabbar-item icon="chat" :to="{name:'diary',params:{'active':1}}">日志</van-tabbar-item>
      <van-tabbar-item icon="records" :to="{name:'notice',params:{'active':2}}">备忘录</van-tabbar-item>
      <van-tabbar-item icon="gold-coin" :to="{name:'profile',params:{'active':3}}">我的</van-tabbar-item>
    </van-tabbar>
  </div>
</template>

<script>
export default {
  name: "home_index",
  data() {
    return {
      activecode: 0,
      token: 123
    };
  },
  created: function() {
    if (!this.token || typeof this.token === "undefined") {
      this.$router.replace({ path: "/login" });
    } else {
      console.log("Print the url:" + this.$route.name);
      if (this.$route.name == "home") {
        this.activecode = 0;
      } else if (this.$route.name == "diary") {
        this.activecode = 1;
      } else if (this.$route.name == "notice") {
        this.activecode = 2;
      } else if (this.$route.name == "profile") {
        this.activecode = 3;
      } else {
        this.activecode = 0;
      }
      console.log(this.activecode);
    }
  }
};
</script>

