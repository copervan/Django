<template>
  <div> 
    <calendar-view
            :show-date="showDate"
            class="theme-default">
            <calendar-view-header
                slot="header"
                slot-scope="t"
                :header-props="t.headerProps"
                @input="setShowDate" />
        </calendar-view>
  </div>
</template>

<script type="text/javascript">
import Calendar from "vue-calendar-component";
import { CalendarView, CalendarViewHeader } from "vue-simple-calendar";
require("vue-simple-calendar/static/css/default.css");
// require("vue-simple-calendar/static/css/holidays-us.css");
export default {
  name: "calendar",
  data() {
    return {
      arr: ["2018/10/1", "2018/10/3"],
      showDate: new Date()
    };
  },
  methods: {
    setShowDate(d) {
      this.showDate = d;
    }
  },
  components: {
    CalendarView,
    CalendarViewHeader
  }
};
</script>