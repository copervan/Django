<template>
  <div id="profile">
    <van-nav-bar title="我的" fixed> </van-nav-bar>
    <div id="my-profile">
      <van-cell title="我的诗歌"  size="large" is-link   :to="{name: 'poetry'}"/>
      <van-cell title="我的书籍"  size="large" is-link  :to="{name: 'booklist'}"/>
    </div>
  </div>
</template>

<script>
export default {
  name: "home",
  data() {
    return {};
  }
};
</script>

<style>
#my-profile {
  margin-top: 50px;
  margin-bottom: 50px;
  text-align: left;
}
</style>
