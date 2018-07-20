<template>
	<div>
		<h1>Hello Rocky</h1>
		<P>这是主页</P>
		<button>Submmit!</button>
		<showuser  v-bind:users="users"></showuser>
	</div>
</template>

<script type="text/javascript">
	import $ from 'jquery'
	import showuser from './showuser'
	import {mapState} from 'vuex'
	import login from '../login'
	export default {
		name: 'home',
		methods: {
			get_device() {
				var mytoken = this.$store.state.token
				$.ajax({
					url:"/rocky/device/",
					type:"GET",
					contentType: 'application/json'	,
					beforeSend: function(xhr){
						xhr.setRequestHeader("Authorization", mytoken);
					},
					success: function(data){
						console.log(data)
						return data
					},
					error: function(err){
						console.log(err)
						alert(err)
					}
				})
			}
		},
		computed : {
			users: function() {
				var users = this.get_device()
				return users
			}
		}
	}
</script>
