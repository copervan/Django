<template>
	<div id = "booklist">
		<books></books>
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