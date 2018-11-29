<template>
    <div id="poetry">
        <van-nav-bar title="我的诗歌" fixed left-arrow @click-left="onClickLeft"> </van-nav-bar>
        <div id="my-poetry">
            <van-list v-model="loading" :finished="finished" @load="onLoad">
                <van-collapse v-model="activeName" accordion>
                    <van-collapse-item v-for="(item,index) in PoetryList" :key="index" :name="index">
                        <div slot="title">
                            <span>{{item.title}}</span>
                        </div>
                        <div slot="value"> {{item.author}} </div>
                        <div id="poetry-content" v-html="item.content"></div>
                    </van-collapse-item>
                </van-collapse>
            </van-list>

        </div>
    </div>
</template>

<script>
import { Poetry } from "@/utils/ajaxFunctions";
export default {
  name: "home",
  data() {
    return {
      PoetryList: [],
      count: 0,
      currentPage: 0,
      token: this.$store.state.token,
      loading: false,
      finished: false,
      activeName: 0
    };
  },
  methods: {
    set_list(data) {
      this.PoetryList = [...this.PoetryList, ...data.results];
      this.count = data.count;
      this.loading = false;
      let next = data.next;
      if (!next) {
        this.finished = true;
        console.log(next + "true");
      } else {
        this.finished = false;
        console.log(next + "false");
      }
      console.log(this.PoetryList);
    },
    onLoad() {
      this.currentPage += 1;
      Poetry.get_poetry(this.currentPage, this.token, this.set_list);
    },
    onClickLeft() {
      this.$router.back(-1);
    }
  }
};
</script>

<style>
#my-poetry {
  margin-top: 50px;
  margin-bottom: 50px;
  text-align: left;
}
#poetry-content {
  font-size: 16px;
}
</style>
