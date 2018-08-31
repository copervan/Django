<template>
	<div> <mt-header title="Calendar"></mt-header> 
		<full-calendar/>
	</div>
</template>

<script type="text/javascript">
	export default {
		name: "calendar",
		components: {
			'full-calendar': require('vue-fullcalendar')
		}
	}
</script>