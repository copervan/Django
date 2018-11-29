<template>
  <div id="notice">
    <van-nav-bar title="备忘录" fixed @click-right="onRefresh">
      <i slot="right" style="font-size: 18px;color: #ff5900" class="el-icon-lx-refresh"></i>
    </van-nav-bar>
    <div id="notice-content" />
    <div id="notice_list">
      <van-list v-model="loading" :finished="finished" @load="onLoad">
        <van-collapse v-model="activeNames" accordion>
          <van-collapse-item v-for="(notice,index) in all_notice " :key="notice.id*(new Date().getTime())" :name="index">
            <div slot="title" style="-webkit-box-flex:2">
              <van-icon name="question" /><span>{{notice.notice_item}}</span>
            </div>
            <div slot="value" @click="update_notice(notice)">
              <van-tag :type="notice_type(notice.status)">{{notice_code(notice.status)}}</van-tag>
            </div>
            <div>
              <!-- <van-cell class="custom-icon" title="StartTime:" :value="formatDate(notice.datetime)"> </van-cell>
              <van-cell class="custom-icon" title="EndTime:" :value="formatDate(notice.end_time)"> </van-cell> -->
              <ol>
                <li>StartTime: <span> {{formatDate(notice.datetime)}} </span></li>
                <li>EndTime: <span>{{formatDate(notice.end_time)}} </span></li>
              </ol>
            </div>
          </van-collapse-item>
        </van-collapse>
      </van-list>

    </div>
    <van-dialog v-model="show" show-cancel-button @confirm="submmit_notice()" @cancle="show = false">
      <van-picker :defaultIndex="current_notice.status" :columns="columns" @change="onChange" />
    </van-dialog>
  </div>
</template>

<script>
import { Notice, Functions } from "@/utils/ajaxFunctions";
export default {
  name: "home",
  data() {
    return {
      show: false,
      notice_list: [],
      all_notice: [],
      currentPage: 0,
      token: this.$store.state.token,
      notice_count: 0,
      loading: false,
      finished: false,
      isLoading: false,
      activeNames: 0,
      current_notice: { status: 3 },
      columns: ["未开始", "已完成", "进行中", "已拒绝"]
    };
  },
  methods: {
    set_notice_list(data) {
      this.notice_list = data;
    },
    set_all_notice(data) {
      this.notice_count = data.count;
      let next = data.next;
      this.all_notice = [...this.all_notice, ...data.results];
      console.log(this.all_notice);
      this.loading = false;
      if (!next) {
        this.finished = true;
        console.log(next + "true");
      } else {
        this.finished = false;
        console.log(next + "false");
      }
    },
    notice_code(code) {
      if (code === 0) {
        return "未开始";
      } else if (code === 1) {
        return "已完成";
      } else if (code === 2) {
        return "进行中";
      } else if (code === 3) {
        return "被拒绝";
      } else {
        return "未知状态：" + code;
      }
    },
    // 控制el-tag 标签的类型
    notice_type(code) {
      if (code === 0) {
        return "";
      } else if (code === 1) {
        return "success";
      } else if (code === 2) {
        return "primary";
      } else if (code === 3) {
        return "danger";
      } else {
        return "";
      }
    },
    onChange(picker, value, index) {
      console.log(index);
      this.current_notice.status = index;
    },
    update_notice(notice) {
      console.log(this.show);
      this.current_notice = JSON.parse(JSON.stringify(notice));
      this.show = true;
      console.log(this.current_notice + " : " + this.show);
    },
    submmit_notice() {
      Notice.edit_notice(this.current_notice, this.token, data => {
        this.$toast.success("更新成功");
        this.show = false;
        this.onRefresh();
      });
    },
    onLoad() {
      this.currentPage += 1;
      Notice.all_notice(this.currentPage, this.token, this.set_all_notice);
    },
    formatDate(data) {
      return Functions.formatDate(data);
    },
    onRefresh() {
      this.currentPage = 0;
      this.notice_list = [];
      this.all_notice = [];
      Notice.get_notice(this.currentPage, this.token, this.set_notice_list);
      this.onLoad();
    }
  },
  created() {
    Notice.get_notice(this.currentPage, this.token, this.set_notice_list);
  }
};
</script>

<style>
#notice-content {
  margin-top: 50px;
  margin-bottom: 50px;
}
</style>

