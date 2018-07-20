<template>
	<div id = "user-list">
		<table>
			<tr>
				<th>id</th><th>device_no</th><th>user_name</th>
			</tr>
			<tr v-for="user in users">
				<td>{{user.id}}</td><td>{{user.device_no}}</td><td>user.user_name</td>
			</tr>
		</table>>
		<li>{{user}}</li>
	</div>
</template>

<script type="text/javascript">
	export default {
		name : 'showuser',
		props: ['users']
	}
</script>