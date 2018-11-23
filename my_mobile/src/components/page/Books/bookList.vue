<template>
    <div id="mybook">
        <van-nav-bar title="书籍列表" fixed left-arrow @click-left="onClickLeft">
        </van-nav-bar>
        <div id="book-content">
            <van-list v-model="loading" :finished="finished" @load="onLoad">
                <van-collapse v-model="activeName" accordion>
                    <van-collapse-item v-for="(book,index) in BookList" :key="index" :title="book.name" :name="index">
                        <div slot="title">
                            <span>{{book.name}}</span>
                        </div>
                        <div slot="value"> {{book.author}} </div>
                        <div class="book-introduction" v-html="book.introduction"> </div>
                        <van-cell-group>
                            <van-cell v-for="chapter in book.book_content" :key="chapter.id" :title="chapter.chapter" is-link :to="{name: 'chapterdetail',params: { 'chapter_id': chapter.id }}">
                            </van-cell>
                        </van-cell-group>
                    </van-collapse-item>
                </van-collapse>
            </van-list>
        </div>
    </div>
</template>

<script>
import { Books } from "@/utils/ajaxFunctions";
export default {
  name: "booklist",
  data() {
    return {
      BookList: [],
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
      this.BookList = [...this.BookList, ...data.results];
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
      console.log(this.BookList);
    },
    onLoad() {
      this.currentPage += 1;
      Books.get_book_list_detail(this.currentPage, this.token, this.set_list);
    },
    onClickLeft() {
      this.$router.back(-1);
    }
  }
};
</script>

<style>
#book-content {
  margin-top: 50px;
  text-align: left;
}
.book-introduction {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 4;
  overflow: hidden;
}
</style>
