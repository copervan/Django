<style scoped>
.layout{
    border: 1px solid #d7dde4;
    /*background: #f5f7f9;*/
    background: #C7EDCC;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
}
.layout-logo{
    width: 100px;
    height: 30px;
    float: left;
    position: relative;
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
                    	<img style="max-width:117px;max-height:50px;vertical-align:middle;"  
                            src="https://file.iviewui.com/dist/03635a3c88122ad605117128f3fda0ca.png"/>
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
                    </div>
                </Menu>
            </Header>
            <Content :style="{padding: '0 50px'}">
                <div style="min-height: 800px;">
                    <keep-alive>
					  <component v-bind:is="currentTabComponent"></component>
					</keep-alive>
                </div>
                <a href="/#/mobile">to the image</a>
            </Content>
            <Footer class="layout-footer-center">2011-2018 &copy; Rocky</Footer>
        </Layout>
    </div>
</template>
<script>
	import login from './login'
	import HelloWorld from './HelloWorld'
	import home from './userprofile/'
	import notice from './notice/'
	import calendar from './calendar'
    import diary from './diary'
    import {mapState} from 'vuex'
    export default {
        name: "dashboard",
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
        	}
        },
    }

</script>
