<template>
    <div id="chapter">
        <van-nav-bar :title="currentChapter.chapter" fixed left-arrow @click-left="onClickLeft">
        </van-nav-bar>
        <div id="chapter-content" v-html="currentChapter.content">
        </div>
    </div>
</template>

<script>
import { Books } from "@/utils/ajaxFunctions";
export default {
  name: "booklist",
  data() {
    return {
      chapterId: this.$route.params.chapter_id,
      currentChapter: {},
      token: this.$store.state.token
    };
  },
  methods: {
    set_chapter_data(data) {
      this.currentChapter = data;
    },
    onClickLeft() {
      this.$router.back(-1);
    }
  },
  created: function() {
    Books.get_chapter_detail(this.chapterId, this.token, this.set_chapter_data);
  }
};
</script>

<style>
#chapter-content {
  margin-top: 50px;
  text-align: left;
  padding: 10px
}
.book-introduction {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 4;
  overflow: hidden;
}
</style>
