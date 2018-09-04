<template>
	<div id="wangeditor">
        <div ref="editorElem" style="text-align:left"></div>
    </div> 
</template>

<script type="text/javascript" >
import E from 'wangeditor'
export default {
  name: "myeditor",
  data () {
    return {
    }
  },
  props:['catchData','data'],
  mounted() {
    let editor = new E(this.$refs.editorElem)
    editor.customConfig.onchange = (html) => {
      this.data.content = html
      this.catchData(html)
    }
    editor.customConfig.menus = [ //菜单配置
    'head', 
    'list', // 列表 
    'justify', // 对齐方式 
    'bold', 
    'fontSize', // 字号 
    'italic', 
    'underline', 
    // 'image', // 插入图片 
    'foreColor', // 文字颜色 
    'undo', // 撤销 
    'redo', // 重复 
    ]

    editor.create()
  }
}
</script>


