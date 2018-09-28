<template>
	<div id = "booklist" class = 'bookcontent'>
		<!-- <h2>User {{ $route.params.id }}</h2> -->
		<router-view></router-view>
	</div>
</template>

<script type="text/javascript">
// import {Books} from '@/utils/ajaxFunctions'
import books from "./booklist";
export default {
  name: "bookindex",
  components: {
    books
  }
};
</script>
<style>
.bookcontent {
  min-height: 100%;
  max-width: 100%;
}
</style>
