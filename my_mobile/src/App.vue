<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App"
};
</script>

<style>
#app {
  /* font-family: Helvetica Neue, Helvetica, PingFang SC, Hiragino Sans GB,
    Microsoft YaHei, \5fae软雅黑, Arial, sans-serif; */
  font-family: "Courier New", Courier, monospace;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  font-size: 18px;
  color: #2c3e50;
  height: 100%;
  width: 100%;
  background-color: #c7edcc !important;
  /* margin-top: 60px; */
}
.van-cell__title {
  -webkit-box-flex: 2 !important;
  -ms-flex: 2 !important;
  flex: 2 !important;
}
.van-cell__value {
  -webkit-box-flex: 1 !important;
  -ms-flex: 1 !important;
  flex: 1 !important;
}
</style>
