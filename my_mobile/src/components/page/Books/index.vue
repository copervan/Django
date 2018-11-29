<template>
    <div id="mybook">
        <van-nav-bar title="书籍列表" fixed left-arrow @click-left="onClickLeft">
        </van-nav-bar>
        <div class="main-book">
            <keep-alive>
                <router-view v-if="$route.meta.keepAlive"></router-view>
            </keep-alive>
            <router-view v-if="!$route.meta.keepAlive"></router-view>
        </div>
    </div>
</template>

<script>
export default {
  name: "mybook",
  data() {
    return {
      keepAlive: this.$route.meta.keepAlive,
      path: this.$route.path
    };
  },
  created() {
    console.log(this.keepAlive, "   ", this.path);
  },
  methods: {
    onClickLeft() {
      this.$router.back(-1);
    }
  }
};
</script>

<style>
.main-book {
  margin-top: 50px;
  text-align: left;
}
</style>
