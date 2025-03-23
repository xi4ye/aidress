<template>
  <div class="background_show_area" :style="shirinkStyle_outside">
    <div class="clothe_area" :style="shirinkStyel_inside2">
      <div v-if="elementPosition" 
      :style="elementPositionStyle" 
      class="remind" >
        <p>单击以添加或修改图片</p>
      </div>
      <div 
      @mouseenter="getDesignPosition"  
      @mouseleave="removeDesignPosition"
      class="design" id="head">
        <!-- <img src="./img/clothe_icon_img/cap1.png" alt="头饰"> -->
        <img 
        v-if="!imageUrl1" 
        src="./img/clothe_icon_img/cap1.png" 
        alt="帽子图标"  
        @click="triggerFileInput(1)"
        />
        
        <!-- 上传的图片 -->
        <img 
          v-if="imageUrl1" 
          :src="imageUrl1" 
          alt="更新帽子" 
          ref="embeddedImg1"
          @click="triggerFileInput(1)" 
        />

      </div>
      <div
      @mouseenter="dress_move=true"
      @mouseleave="dress_move=false"
      @click="dress_behind=false"
      :class="{dress_front_style: !dress_behind,adesign: dress_move && dress_behind}" 
      class="dress_behind_style">
        <img v-if="!imageUrl5" src="./img/clothe_icon_img/dress.png" alt="连衣裙图标"
        @click="showClothesDiv5=true">
        <img 
          v-if="imageUrl5" 
          :src="imageUrl5" 
          alt="更新连衣裙" 
          ref="embeddedImg5"
          @click="showClothesDiv5=true" 
          @load="handleImageLoad"
        />

        <div class="image-container">
          <button v-if='imageUrl5' class="delete-button" @click="deleteImage(5)">×</button>
        </div>
      <!-- 选择衣服的div -->
      <div v-show="showClothesDiv5" class="clothes-selection" @mouseleave="hideClothesSelection">
        <div v-for="(dynasty, index) in dynasties" :key="index" class="dynasty-section">
          <div class="dynasty-name">{{ dynasty.name }}</div>
          <hr /> 
          <div class="clothes-row">
            <img v-for="(clothes, idx) in dynasty.clothes" :key="idx" :src="clothes.img" @click="selectClothes(clothes.img,5)" class="clothes-item" />
          </div>
        </div>
      </div>
      </div>


      <div v-if="elementPosition" 
      :style="elementPositionStyle" 
      class="remind" >
        <p>单击以添加或修改图片</p>
      </div>
      <div
      @click="clothe_front" 
      @mouseenter="getDesignPosition,dress_move=true"  
      @mouseleave="removeDesignPosition,dress_move=false"
      :class="{clothe_behind_style: !dress_behind,adesign: dress_move && !dress_behind}"
      class="design" id="clothes">
        <img 
        v-if="!imageUrl2" 
        src="./img/clothe_icon_img/clothes.png" 
        alt="衣服图标"  
        @click="showClothesDiv=true"
        />        
        <!-- 上传的图片 -->        
        <img 
          v-if="imageUrl2"
          :src="imageUrl2" 
          alt="更新衣服" 
          ref="embeddedImg2"
          @click="showClothesDiv=true" 
        />


        <div class="image-container">
          <button v-if='imageUrl2' class="delete-button" @click="deleteImage(2)">×</button>
        </div>
      </div>

      <!-- 选择衣服的div -->        
      <div v-show="showClothesDiv" class="clothes-selection" @mouseleave="hideClothesSelection">
        <div v-for="(dynasty, index) in dynasties" :key="index" class="dynasty-section">
          <div class="dynasty-name">{{ dynasty.name }}</div>
          <hr />
          <div class="clothes-row">
            <img 
            v-for="(clothes, idx) in dynasty.clothes" :key="idx" :src="clothes.img" @click="selectClothes(clothes.img,2)" class="clothes-item" />
          </div>
        </div>
      </div>

      <div v-if="elementPosition" 
      :style="elementPositionStyle" 
      class="remind" >
        <p>单击以添加或修改图片</p>
      </div>
      <div 
      v-show="dress_behind"
      @mouseenter="getDesignPosition"  
      @mouseleave="removeDesignPosition"
      class="design" id="trousers">
        <img 
        v-if="!imageUrl3" 
        src="./img/clothe_icon_img/trousers.png" 
        alt="裤子图标"  
        @click="triggerFileInput(3)"
        />
        
        <!-- 上传的图片 -->
        
        <img 
          v-if="imageUrl3"
          :src="imageUrl3" 
          alt="更新裤子" 
          ref="embeddedImg3"
          @click="triggerFileInput(3)" 
        />

        <div class="image-container">
          <button v-if='imageUrl3' class="delete-button" @click="deleteImage(3)">×</button>
        </div>
        
      </div>
      <div v-if="elementPosition" 
      :style="elementPositionStyle" 
      class="remind" >
        <p>单击以添加或修改图片</p>
      </div>
      <div 
      @mouseenter="getDesignPosition"  
      @mouseleave="removeDesignPosition"
      class="design" id="shoes">
        <img 
        v-if="!imageUrl4" 
        src="./img/clothe_icon_img/shoes.png" 
        alt="鞋子图标" 
        @click="triggerFileInput(4)"
        />
        
        <!-- 上传的图片 -->
        <img 
          v-if="imageUrl4" 
          :src="imageUrl4" 
          alt="更新鞋子" 
          ref="embeddedImg4"
          @click="triggerFileInput(4)" 
        />

        
      </div>
      <button class="commit_clothes_button" @click="send_clothes_imgs_data(),fetch_clothed_model_image()">
        保存并生成图片
      </button>

    </div>
    <div class="model_area" :style="shirinkStyel_inside1">
      <div v-if="!model_exist" class="remind_create">
        请先生成模特！
      </div>
      <img v-if="!model_existed" src="./img/model_example.png" alt="默认模特图片">
      <img v-else-if="model_existed && !model_state" :src=model_image_Url alt="模特图片">
      <img v-else-if="clothed_model_image_Url && model_state" :src="clothed_model_image_Url" alt="更新模特图片">
      <img v-else :src="getImageSrc(model_existed)" ref="model_image" alt="模特图片">
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Swal from 'sweetalert2';

export default {
  name : 'ModelShow',
  data() {
    return {
      model_state: false,
      model_file:null,
      showDiv : false,
      imageUrl1: null,
      imageUrl2: null,
      dress_behind: true,
      dress_move: false,
      imageUrl5: null,
      imageUrl3: null, 
      imageUrl4: null, 
      elementPosition: null,
      isImageLoaded: false,
      clothed_model_image_Url: null,
      isgenerated: false,
      make_sure: false,
      showClothesDiv: false,
      showClothesDiv5: false,
      currentClothesIcon: './img/clothe_icon_img/clothes.png',
      selectedClothes: null,
      model_exist: false,
      dynasties: [
        {
          name: '唐',
          clothes: [
            { img: require('./img/clothes/tang1.jpg') },
            { img: require('./img/clothes/tang2.jpg') },
            { img: require('./img/clothes/tang3.jpg') },
          ],
        },
        {
          name: '宋',
          clothes: [
          { img: require('./img/clothes/song1.jpg') },
          { img: require('./img/clothes/song2.jpg') },
          { img: require('./img/clothes/song3.jpg') },
          { img: require('./img/clothes/song4.jpg') },
          ],
        },
        // 其他朝代省略
      ], 
      clothes_data:
      {
        clothe1:null,
        clothe2:null,
        clothe3:null,
        clothe4:null,
        clothe5:null,
      }     
    };
  },
  watch: {
    makesure(){
      if (this.makesure){
        this.make_sure = true;
      }
    },
    clothed_model_image_Url(){
      this.model_state = true;
    },
    model_existed(){
      this.model_exist = this.model_existed;
    }
  
  },
  // 如果postion发生改变，就修改样式
  computed: {
    elementPositionStyle(){
      if (this.elementPosition){
        return {
          top: `${this.elementPosition.top + 30}px`,
          left: `-70px`,          
        };
      }
      return {};
    },
    shirinkStyle_outside(){
      if(this.isShirnk){
        return {
          right :'0',
          width : '1100px',
        };
      }
      return {};
    },
    shirinkStyel_inside1(){
      if(this.isShirnk){
        return {
          right : '300px',
        };
      }
      return {};
    },
    shirinkStyel_inside2(){
      if(this.isShirnk){
        return {
          left : '200px',
        };
      }
      return {};
    }
  },
  props:{
    isShirnk:{
      type:Boolean,
    },
    model_existed:{
      type:Boolean,
    },
    model_image_Url:{
      type:String,
    },
    makesure:{
      type:Boolean,
    }

  },
  methods: {
    // 触发文件上传输入框
    triggerFileInput(index) {
      const inputElement = this.$refs[`fileInput${index}`];
      // 在点击事件上传递index
      inputElement.click();
    },

    send_clothes_imgs_data(){

      let count = 0;
      for (let key in this.clothes_data) {
        if (this.clothes_data[key]) {
          count++;
        }
      }
      if (!this.model_exist) {
        Swal.fire({
          text: '请先生成模特！',
          icon:'error',
          customClass: {
              icon:'custom-icon-size'
          },
          showConfirmButton: false,
          position:'top',
          timer:1800,
          width:"200px",
          })
        return
      }
      // 使用 axios 发送请求到后端
      if (count > 0) {
        axios.post('http://localhost:5000/api/receive_clothes_img',this.clothes_data, {headers: {'Content-Type': 'application/json',timeout: 700000},}
        )
        .then(response => {
          console.log('上传成功:', response.data);
        })
        .catch(error => {
          console.error('上传失败:', error);
        });
      } else {
          
        Swal.fire({
                    text: '请先选取服装！',
                    icon:'error',
                    customClass: {
                        icon:'custom-icon-size'
                    },
                    showConfirmButton: false,
                    position:'top',
                    timer:1800,
                    width:"200px",
                    })
        return
      
      }
    },
    clothe_front(){
      this.dress_behind = true;
    },
    deleteImage(index) {
      this[`imageUrl${index}`] = null;
      this.clothes_data[`clothe${index}`] = null;
    },

    hideClothesSelection() {
      this.showClothesDiv = false;
      this.showClothesDiv5 = false;
    },
    selectClothes(img,index) {
      this[`imageUrl${index}`]= img;
      this.selectedClothes = img;
      this.hideClothesSelection();
      this.clothes_data[`clothe${index}`] = img.slice(0,10);
    },    
    loading(){
      const swalInstance = Swal.fire({
        title: '正在生成图片',
        html: '请稍等...',
        timer: 20000,
        timerProgressBar: true,
        didOpen: () => {
          Swal.showLoading()
        }
      })
      return swalInstance;
    },

    //获取clothesdesign元素的位置及其显示
    getDesignPosition(event){
      const parentElement = event.target;
      const rect = parentElement.getBoundingClientRect();


      // 获取四个位置
      const position = {
        top: rect.top + window.scrollY,
        left: rect.left + window.scrollX,
        bottom: rect.bottom + window.scrollY,
        right: rect.right + window.scrollX,     
      };
      this.elementPosition = position;
    },
    removeDesignPosition() {
      this.elementPosition = null;
    },
    fetch_clothed_model_image() {
      // if(!this.make_sure){
      //   return;
      // }
      // 向后端发送 GET 请求，获取图像数据
      if ((this.imageUrl1 || this.imageUrl2 || this.imageUrl3|| this.imageUrl4 || this.imageUrl5) && this.model_existed) {
        const swalInstance = this.loading();
        axios.post('http://localhost:5000/api/send_clothed_img', {},{ responseType: 'blob' ,timeout: 700000})
        .then(response => {
          // 将返回的 Blob 数据转换为图像 URL
          
          this.clothed_model_image_Url = URL.createObjectURL(response.data);
          swalInstance.close();
          console.log('Image fetched:', this.clothed_model_image_Url);
        })
        .catch(error => {
          console.error('Error fetching image:', error);
        });
      } else {
        return;
      }
    },

  }
}

</script>

<style scoped>
.background_show_area {
  position: absolute;
  top: 0;       
  right:  450px;   
  width: 650px;   
  height: 100vh; 
  background-color: rgba(230, 232, 238); 
  border-radius: 10px;
  transition: all ease 0.3s

}

.model_area {
  position: absolute;
  right: 20px;
  width: 400px;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #d8d8d8;
  transition: right ease 0.3s;
  border-radius: 20px;
  box-shadow: 10pc;
  z-index: 10;

}
.model_area img {
  position: relative;
  margin: 20px;
  width: 300px;
  height: auto;

}

/* 设置父容器 cloth_area */
.clothe_area {
  position: absolute; 
  left: 15px;
  top: 50%; /* 垂直居中 */
  width: 200px;
  height: 100vh;
  transform: translateY(-50%); /* 使其垂直居中 */
  display: flex;
  justify-content: center;
  flex-direction: column; /* 垂直排列子类 */
  align-items: center; /* 水平居中对齐子类 */
  gap: 25px; /* 子类之间的间距 */
  background-color: #f0f0f0;
  border-radius: 20px;
  transition: left ease 0.3s;
  z-index: 100;
}
.image-container {
  position: relative;
}
.delete-button {
  position: absolute;
  right: -10px;
  top: -55px;

  background: rgb(13, 13, 13);
  color: white;
  border: none;
  border-radius: 50%;
  cursor: pointer;
}

.remind {
  width: 100px; 
  height: 80px; 
  background-color: rgba(78, 78, 78, 0.445); 
  position:absolute; 
  font-style: normal;
  color:#ffffff;
  z-index : 100;
  font-size: large;
}
/* 设置每个子类的样式 */
.design {
  width: 100px; /* 设置宽度 */
  height: 100px; /* 设置高度，使长宽相等 */
  background-color: #d8d8d8; /* 背景色 */
  color: white;
  display: flex;
  justify-content: center;
  align-items: center; /* 文字居中 */
  border-radius: 5px; /* 圆角 */
  text-align: center;
  padding : 5px;
  border: 1px dashed rgb(161, 161, 161);
  z-index: 5;
}

.dress_behind_style {
  position: fixed;
  top: 25%;
  left: 30%;
  width: 100px; /* 设置宽度 */
  height: 100px; /* 设置高度，使长宽相等 */
  background-color: #d8d8d8; /* 背景色 */
  color: white;
  display: flex;
  justify-content: center;
  align-items: center; /* 文字居中 */
  border-radius: 5px; /* 圆角 */
  text-align: center;
  padding : 5px;
  border: 1px dashed rgb(161, 161, 161);
  z-index: 5;
  transition: left 1.5s ease, top 1.5s ease;
}

.dress_behind_style img{
  pointer-events: none;
  cursor: pointer;
}

.dress_front_style {
  position: static;
  z-index: 6;
  transition: left 1.5s ease, top 1.5s ease;
}

.dress_front_style img{
  pointer-events: all;
  cursor: pointer;
}

.clothe_behind_style{
  position: absolute;
  top: 35%;
  left: 28%;
  width: 100px; /* 设置宽度 */
  height: 100px; /* 设置高度，使长宽相等 */
  z-index: 5;
  transition: left 1.5s ease, top 1.5s ease;
}

.clothe_behind_style img{
  pointer-events: none;
  cursor: pointer;
}

.adesign{
  position: absolute;
  top: 22%;
  left: 35%;
  z-index:5;
  
}
.dress_behind_style img{
  height: 100px;
  width: auto;
  cursor: pointer;
}
.clothes-selection {
  position: fixed;
  top: 0;
  left: 200px;
  width: 400px;
  height: 600px;
  background-color: white;
  border: 1px solid #ccc;
  overflow-y: scroll;
  z-index: 9999;
}
.dynasty-section {
  padding: 10px;
}
.dynasty-name {
  font-size: 18px;
  font-weight: bold;
}
.clothes-row {
  display: flex;
  justify-content: space-between;
}

.clothes-item {
  width: 70px;
  cursor: pointer;
}
#head img {
  height: 100px;
  width: auto;
  cursor: pointer;
}
#clothes img {
  height: 100px;
  width: auto;
  cursor: pointer;
}
#trousers img {
  height: 100px;
  width: auto;
  cursor: pointer;
}
#shoes img {
  height: 100px;
  width: auto;
  cursor: pointer;
}

.remind_create{
  font-size: 20px;
  color: #000000;
  font-weight: bold;  
  z-index: inherit;
}
.commit_clothes_button {
  background-color: #00b8b8;  
  color: white;             
  padding: 10px 20px;       
  border: 2px solid #00b8b8; 
  border-radius: 10px;        
  font-size: 16px;            
  font-weight: bold;        
  cursor: pointer;          
  transition: background-color 0.3s ease; 
}
.commit_clothes_button:hover {
    background-color: #009999;  /* 鼠标悬停时，背景色稍微变暗 */
}
</style>
