<template>
	<full-calendar :events="[]"  />
</template>

<script type="text/javascript">
export default {
  name: "calendar",
  components: {
    "full-calendar": require("vue-fullcalendar")
  }
};
</script>