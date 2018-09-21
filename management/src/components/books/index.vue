<template>
	<div id = "booklist">
		<!-- <h2>User {{ $route.params.id }}</h2> -->
		<router-view></router-view>
	</div>
</template>

<script type="text/javascript">
// import {Books} from '@/utils/ajaxFunctions'
import books from "./booklist"
export default {
	name:"bookindex",
	components: {
		books
	}
}
</script>