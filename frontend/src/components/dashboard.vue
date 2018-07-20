<style scoped>
.layout{
    border: 1px solid #d7dde4;
    background: #f5f7f9;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
}
.layout-logo{
    width: 100px;
    height: 30px;
    background: #5b6270;
    border-radius: 3px;
    float: left;
    position: relative;
    top: 15px;
    left: 20px;
}
.layout-nav{
    width: 420px;
    margin: 0 auto;
    margin-right: 20px;
}
.layout-footer-center{
    text-align: center;
}
</style>
<template>
    <div class="layout">
        <Layout>
            <Header>
                <Menu mode="horizontal" theme="dark" active-name="1" @on-select="bind_template">
                    <div class="layout-logo">
                    	<!-- <img src="https://file.iviewui.com/dist/03635a3c88122ad605117128f3fda0ca.png"/> -->
                    	<Icon type="ios-world-outline"></Icon>
                    </div>
                    <div class="layout-nav">
                        <MenuItem name="1" >
                            <Icon type="ios-navigate"></Icon>
                            {{type_0}}
                        </MenuItem>
                        <MenuItem name="2" >
                            <Icon type="ios-keypad"></Icon>
                            {{type_1}}
                        </MenuItem>
                        <MenuItem name="3" >
                            <Icon type="ios-analytics"></Icon>
                            {{type_2}}
                        </MenuItem>
                        <MenuItem name="4">
                            <Icon type="ios-paper"></Icon>
                            {{type_3}}
                        </MenuItem>
                        <!-- <input type="button" name="tijiao" v-on:click="currentTab = 'type_1'" />	 -->
                    </div>
                </Menu>
            </Header>
            <Content :style="{padding: '0 50px'}">
                <!-- <Breadcrumb :style="{margin: '20px 0'}">
                    <BreadcrumbItem v-on:click="currentTabComponent = login">主页</BreadcrumbItem>
                    <BreadcrumbItem v-on:click="currentTabComponent = HelloWorld">日历</BreadcrumbItem>
                    <BreadcrumbItem>日志</BreadcrumbItem>
                    <BreadcrumbItem>备忘录</BreadcrumbItem>
                </Breadcrumb> -->
                <Card>
                    <div style="min-height: 800px;">
                        <keep-alive>
						  <component v-bind:is="currentTabComponent"></component>
						</keep-alive>
                    </div>
                </Card>
            </Content>
            <Footer class="layout-footer-center">2011-2018 &copy; TalkingData</Footer>
        </Layout>
    </div>
</template>
<script>
	import login from './login'
	import HelloWorld from './HelloWorld'
	import home from './userprofile/'
	import notice from './notice/'
	import calendar from './calendar'
    import {mapState} from 'vuex'
    export default {
        name: "dashboard",
        props: ['token'],
        data() {
        	return {
        		type_0 : "主页",
        		type_1 : "日志",
        		type_2 : "备忘录",
        		type_3 : "日历",
        		currentTab: 'type_0'
        	}
        },
        created: function() {
            if(!this.token || typeof this.token === 'undefined' ){
                this.$router.replace({path:"/"})
            }
            else {
                console.log("the Token: "+ this.token)
            }
        },
        computed: {
            currentTabComponent: function () {
        		if (this.currentTab === 'type_0') {
        			return home
        		}
        		else if (this.currentTab === 'type_1'){
        			return login 
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
        	}        
        },
    }

</script>
