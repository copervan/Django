<template>
    <div class="layout">
        <el-tabs v-model="activeName"  type="card" >
            <el-tab-pane name="first">
                <span slot="label"><i class="el-icon-lx-addressbook"></i>用户管理</span>
                <home></home>
            </el-tab-pane>
            <el-tab-pane  name="second">
                <span slot="label"><i class="el-icon-lx-notice"></i>备忘录</span>
                <notice></notice>
            </el-tab-pane>
            <el-tab-pane label="" name="third">
                <span slot="label"><i class="el-icon-lx-calendar"></i>日历</span>
                <calendar ></calendar>
            </el-tab-pane>
            <el-tab-pane name="fourth">
                <span slot="label"><i class="el-icon-lx-edit"></i>日志</span>
                <diary></diary>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>

<script>
	// import login from './login'
	// import HelloWorld from './HelloWorld'
	import home from './userprofile'
	import notice from './notice'
	import calendar from './calendar'
    import diary from './diary'
    import login from '@/components/page/Login'
    import {mapState} from 'vuex'
    export default {
        name: "dashboard",
        data() {
        	return {
        		type_0 : "主页",
        		type_1 : "日志",
        		type_2 : "备忘录",
        		type_3 : "日历",
        		currentTab: 'type_0',
                activeName : "first"
        	}
        },
        created: function() {
            if(!this.token || typeof this.token === 'undefined' ){
                this.$router.replace({path:"/login"})
            }
            else {
                // console.log("the Token: "+ this.token)
            }
        },
        computed: {
            currentTabComponent: function () {
        		if (this.currentTab === 'type_0') {
        			return home
        		}
        		else if (this.currentTab === 'type_1'){
        			return diary 
        		}
        		else if (this.currentTab === 'type_2'){
        			return notice
        		}
        		else if (this.currentTab === 'type_3'){
        			return calendar
        		}
        		else {
        			return login
        		}
            },
            ...mapState(
                ['token']
            )
        },
        methods: {
        	bind_template(name){
        		this.currentTab = 'type_'+ String(Number(name) - 1)
        	},
            handleClick(tab, event) {
                console.log(tab, event);
            }
        },
        components: {
            home, diary, notice, calendar, login
        }
    }

</script>
