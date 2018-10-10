<template>
    <div class="layout">
        <el-tabs v-model="activeName"  type="card" >
            <el-tab-pane name="first" v-if="username == 'admin' || username == 'copervan' ">
                <span slot="label"><i class="el-icon-lx-addressbook"></i>用户管理</span>
                <home></home>
            </el-tab-pane>
            <el-tab-pane  name="second">
                <span slot="label"><i class="el-icon-lx-notice"></i>备忘录</span>
                <notice></notice>
            </el-tab-pane>
            <el-tab-pane name="fourth">
                <span slot="label"><i class="el-icon-lx-edit"></i>日志</span>
                <diary></diary>
            </el-tab-pane>
            <el-tab-pane label="" name="third">
                <span slot="label"><i class="el-icon-lx-calendar"></i>日历</span>
                <calendar ></calendar>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>

<script>
import home from "./userprofile";
import notice from "./notice";
import calendar from "./calendar";
import diary from "./diary";
import login from "@/components/page/Login";
import { mapState } from "vuex";
export default {
  name: "dashboard",
  data() {
    return {
      activeName: "second",
      username: localStorage.getItem('ms_username'),
    };
  },
  created: function() {
    if (!this.token || typeof this.token === "undefined") {
      this.$router.replace({ path: "/login" });
    } else {
      // console.log("the Token: "+ this.token)
    }
  },
  computed: {
    ...mapState(["token"])
  },
  methods: {
    bind_template(name) {
      this.currentTab = "type_" + String(Number(name) - 1);
    },
    handleClick(tab, event) {
      console.log(tab, event);
    }
  },
  components: {
    home,
    diary,
    notice,
    calendar,
    login
  }
};
</script>

<style>
.layout {
  min-height: 600px ;
  /* border: solid 2px */
}
</style>

