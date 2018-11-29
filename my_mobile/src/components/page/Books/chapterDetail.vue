<template>
  <div id="chapter-content" v-html="currentChapter.content">
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
      this.$router.go("booklist");
    }
  },
  created: function() {
    Books.get_chapter_detail(this.chapterId, this.token, this.set_chapter_data);
  }
};
</script>

<style>
#chapter-content {
  padding: 10px;
}
</style>
