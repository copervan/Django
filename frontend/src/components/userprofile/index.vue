
<script type="text/javascript">
	import $ from 'jquery'
	// import showuser from './showuser'
	import {mapState} from 'vuex'
	import login from '../login'
	export default {
		name: 'home',
		data() {
			return  {
				users1 : [],
				columns1: [
					{
						title: "id",
						key : "id"
					},
					{
						title: "user_name",
						key : "user_name"
					},
					{
						title: "device_no",
						key : "device_no"
					}]
			}
		},
		methods: {
			get_device(callback) {
				var mytoken = this.$store.state.token
				var myusers = $.ajax({
					url:"/rocky/device/",
					type:"GET",
					contentType: 'application/json'	,
					beforeSend: function(xhr){
						xhr.setRequestHeader("Authorization", mytoken);
					},
					success: function(data){
						console.log(data)
						// callback =  data
					},
					error: function(err){
						console.log(err)
						alert(err)
					}
				}).done(callback)
			},
			setusers(data) {
				console.log(data)
				this.users1 = data
			}
		},
		created: function(){
			this.get_device(this.setusers)
		},
		computed:{
			data1: function() {
				return this.users1
			}
		},
		watch: {
			users1: function() {
				console.log(this.users1)
			}
		}			

	}
</script>


<template>
	<div>
		<h1>Hello Rocky</h1>
		<P>这是主页</P>
		<button v-on:click="get_device()">Submmit!</button>
		<div v-if="users1">
			{{users1}}
		<Table :columns="columns1" :data="data1"></Table>
		<!-- <showuser  ></showuser> -->
		</div>
	</div>
</template>