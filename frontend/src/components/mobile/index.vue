<template>
	<div id="mobile_main">
		<div>
			<component v-bind:is="currentComponent"></component>
		</div>
		<mt-tabbar fixed v-model="selected_value" >
		  <mt-tab-item id="0">
		    <img slot="icon" src="@/assets/logo.png">
		    主页
		  </mt-tab-item>
		  <mt-tab-item id="1">
		    <img slot="icon" src="@/assets/logo.png">
		    日志 
		  </mt-tab-item>
		  <mt-tab-item id="2">
		    <img slot="icon" src="@/assets/logo.png">
		    备忘录
		  </mt-tab-item>
		  <mt-tab-item id="3">
		    <img slot="icon" src="@/assets/logo.png">
		    日历
		  </mt-tab-item>
		</mt-tabbar>
	</div>
</template>

<script type="text/javascript">
	import home from './home/'
	import notice from './notice/'
	import calendar from './calendar/'
    import diary from './diary/'
    import {mapState} from 'vuex'
    import image from '@/components/image'
	export default {
		name : "mobile",
		data() {
			return {
				selected_value : 0,
				currentTab : 0
				//currentComponent: home
			}
		},
		methods: {
        	bind_template(name){
        		this.currentTab = 'type_'+ String(Number(name))
        	}
        },
		computed: {
            currentComponent: function () {
            	console.log("this.currentTab",this.currentTab)
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
        			return image
        		}
        		else {
        			return home
        		}
            },
            ...mapState(
                ['token']
            )
        },
        created: function() {
            if(!this.token || typeof this.token === 'undefined' ){
                this.$router.replace({path:"/"})
            }
            else {
                // console.log("the Token: "+ this.token)
            }
        },
        watch: {
		    selected_value: function (val, oldVal) {
		        // 这里就可以通过 val 的值变更来确定
		        console.log(val)
		        this.bind_template(val)
		    }
		}
	}
</script>

<style type="text/css">
	#mobile_main { padding: 5px }
</style>