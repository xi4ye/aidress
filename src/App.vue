<template>
  <HistoryDocument/>
  <ModelShow :isShirnk="isshrink" :model_existed="model_existed" :model_image_Url="model_image_Url" :makesure="make_sure"/>
  <MoDel @send-message="receive_shrink" @send-message-model-existed="receive_model_existed" @send-message-makesure="receive_make_sure"/>
</template>

<script>
import MoDel from './components/MoDel.vue';
import ModelShow from './components/ModelShow.vue';
import HistoryDocument from './components/HistoryDocument.vue';


export default {
  name: 'App',
  components: {
    HistoryDocument,
    ModelShow,
    MoDel
  },
  data(){
    return {
      isshrink:false,
      model_existed:false,
      model_image_Url:null,
      make_sure:false
    }
  },
  methods:{
    receive_shrink(isCollasped){
      this.isshrink = isCollasped;
    },

    receive_model_existed(model_existed, model_image_Url){
      this.model_existed = model_existed;
      this.model_image_Url = model_image_Url;
    },
    receive_make_sure(make_sure){
      this.make_sure = make_sure;
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
