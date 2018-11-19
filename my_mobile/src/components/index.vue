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
export default {
  name: "home_index",
  data() {
    return {
      active: 0
    };
  },
  methods: {
    change_item(active) {
      console.log(active);
    }
  },
  computed: {
    currentTabComponent: () => {
      return hello;
    }
  }
};
</script>

