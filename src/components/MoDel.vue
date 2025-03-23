<template>
    <div class="arrow" :style="moveStyle" @click="shrinkbtn">
        <svg v-if="isCollasped" width="20" height="50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50 50">
            <path d="M35 10 L15 25 L35 40" stroke="white" stroke-width="2" fill="none"/>
        </svg>
        <svg v-else width="20" height="50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50 50">
            <path d="M15 10 L35 25 L15 40" stroke="white" stroke-width="2" fill="none"/>
        </svg>
    </div>      
    <div class="background" :style="shrinkStyle">
        <div class="gender_M" :style="gender_man_button" @click="gender = true">
                Man
        </div> 
        <div class="gender_W" :style="gender_woman_button" @click="gender = false">
                Woman
        </div>
        <div class="title">
            选择模特身形
        </div>
        <div class="options">
            <div class="area1">
                <!-- <div v-if="gender" class="man_area1" >
                    暂无选项
                </div> -->
                <div class="woman_area1" :style="gender_man_area1">
                
                    <img class="user" src="./img/user.png" alt="user">                           
                    <div class="form">
                        <form id="usercmandkgForm">
                            <div class="form1">
                                <label for="cm">身高</label>
                                <input v-model="formData.cm" type="number" id="cm" name="cm" >
                                <span>
                                    cm
                                </span>
                            </div>
                            <div class="form2">
                                <label for="kg">体重</label>
                                <input v-model="formData.kg" type="number" id="kg" name="kg" >
                                <span>
                                    kg
                                </span>
                            </div>
                        </form>
                    </div>
                    <button @click="Save(),fetch_model_image()" class="cmkgbtn" :style="gender_cmkgbtn">
                        保存并生成模特
                    </button>
                    <button @click="makesure" class="cmkgbtn" style='top:15vh;' :style="makesure_unable_style">
                        确定应用
                    </button>                    
                </div>    
            </div>
            <div class="skin_title">
                选择你的肤色
            </div>

            <div class="area2" :style="gender_man_area2">

                <div class="woman_area2" :style="gender_man_area2">
                    <div class="clrcle-container">                   
                        <div class="circle" style="background-color: #6d4528;"></div>
                        <div class="circle" style="background-color: #ffe5cb;"></div>
                        <div class="circle" style="background-color: #fffaed;"></div>
                    </div>
                    
                    <div class="clrcle-container2">
                        <div class="circle_write" :class="{ selected: selectedIndex === 0}" v-on:click="selectCircle(0)"></div>
                        <div class="circle_write" :class="{ selected: selectedIndex === 1}" @click="selectCircle(1)"></div>
                        <div class="circle_write" :class="{ selected: selectedIndex === 2}" @click="selectCircle(2)"></div>
                    </div>
                    <div class="clrcle-container3">
                        <span>黑皮肤</span>
                        <span>黄皮肤</span>
                        <span>白皮肤</span>
                    </div>
                </div>
                

            </div>
            <div class="shape_title">
                选择你的身型
            </div>
            <div class ="area3" :style=gender_man_area3>
                <div class="woman_area3">
                    <img v-if='gender' src="./img/shape_man.png" alt="身型图片">
                    <img v-else src="./img/shape_woman.jpg" alt="身型图片">
                    <div class="clrcle-container2" style="top : 32vh;justify-content:space-evenly;">
                        <div class="circle_write" :class="{ selected: selectedIndex2 === 0}" @click="selectCircle2(0)"></div>
                        <div class="circle_write" :class="{ selected: selectedIndex2 === 1}" @click="selectCircle2(1)"></div>
                        <div class="circle_write" :class="{ selected: selectedIndex2 === 2}" @click="selectCircle2(2)"></div>
                        <div class="circle_write" :class="{ selected: selectedIndex2 === 3}" @click="selectCircle2(3)"></div>
                        <div class="circle_write" :class="{ selected: selectedIndex2 === 4}" @click="selectCircle2(4)"></div>
                    </div>
                </div>
                
            </div>
            
        </div>
    </div>
    

</template>
<script>
import Swal from 'sweetalert2';
import axios from 'axios';

export default {
    
    name : 'MoDel',
    CanEdit : false,
    formData:{
                cm: "",
                kg: "",
            },
    data (){
        return {
            formData:{
                cm: null,
                kg: null,
            },
            gender: false,
            selectedIndex: null,
            selectedIndex2: null,
            isCollasped : false,
            model_existed :  false,
            model_image_Url : null,
            makesure_model : false,
        }    
    },
    computed :{
        shrinkStyle(){
            if(this.isCollasped){
                return {
                    width : '0',
                };
            }
            return {};
        },
        moveStyle(){
            if(this.isCollasped){
                return {
                    right : '1px',
                };
            }
            return {};
        },
        gender_man_button(){
            if (this.gender){
                return {
                    // top : '0',
                    'box-shadow' : '5px 5px 5px 0px #534f4f',
                };
            }
            return {};
            
        },
        gender_woman_button(){
            if (!this.gender){
                return {
                    // top : '0',
                    'box-shadow' : '5px 5px 5px 0px #534f4f',
                };
            } 
            return {};
        },
        gender_man_area1(){
            if (this.gender){
                return {
                    'background-color': 'rgb(214, 230, 235)',
                    'border-radius': '10px',   
                    'font-family' : 'Arial, sans-serif', /* 设置字体样式 */
                    'font-size': '16px',/* 设置字体大小 */
                    'transition': 'background-color 0.3s ease', /* 背景色过渡 */
                }
            }
            return {};
        },
        gender_cmkgbtn(){
            if(this.makesure_model){
                return {
                    'background-color': '#a3a3a3',  /* 灰色背景 */
                    'pointer-events': 'none',           /* 禁用鼠标事件 */
                    'cursor': 'default',           /* 鼠标悬停时变为手形光标 */
                    'border': '2px solid #a3a3a3',  /* 边框颜色与按钮背景一致 */
                }
            } else if (this.gender){
                return {
                    'background-color': '#00b8b8',  /* 青色背景 */
                    'color': 'white',               /* 白色文本 */
                    'padding': '10px 20px',         /* 内边距 */
                    'border': '2px solid #00b8b8',  /* 边框颜色与按钮背景一致 */
                    'border-radius': '10px',        /* 10px 圆角 */
                    'font-size': '16px',            /* 字体大小 */
                    'font-weight': 'bold',          /* 字体加粗 */            /* 字体大小 */
                    'cursor': 'pointer',           /* 鼠标悬停时变为手形光标 */
                    'transition': 'background-color 0.3s ease', /* 背景色过渡 */
                }
            }
            return {};
        },
        gender_man_area2(){
            if (this.gender){
                return {
                    'background-color': 'rgb(187, 187, 187)',
                    'border-radius': '10px',   
                    'font-family' : 'Arial, sans-serif', /* 设置字体样式 */
                    'font-size': '16px',/* 设置字体大小 */
                    'color': 'rgb(255,255,255)', /* 设置字体颜色 */
                    'transition': 'background-color 0.3s ease', /* 背景色过渡 */
                }
            }
            return {};
        },
        gender_man_area3(){
            if(this.gender){
                return {
                    'background-color': 'rgb(183, 193, 209)',
                    'border-radius': '10px',   
                    'font-family' : 'Arial, sans-serif', /* 设置字体样式 */
                    'font-size': '16px',/* 设置字体大小 */
                    'color': 'rgb(255,255,255)', /* 设置字体颜色 */
                    'transition': 'background-color 0.3s ease', /* 背景色过渡 */
                }
            }
            
            return {};
        },

        makesure_unable_style(){
        if (!this.model_existed){ 
                return {
                    display: 'none',
                }
            }
        if (this.makesure_model){    
            return {
                    'background-color': '#a3a3a3',  /* 灰色背景 */
                    'pointer-events': 'none',           /* 禁用鼠标事件 */
                    'cursor': 'default',           /* 鼠标悬停时变为手形光标 */
                    'border': '2px solid #a3a3a3',  /* 边框颜色与按钮背景一致 */
                }
            }
        return {};    
        }
        
        
    },    
    methods :{
        shrinkbtn(){
            this.isCollasped = !this.isCollasped;
            this.$emit('send-message',this.isCollasped);
        },

        showAlert() {
            Swal.fire({
            text: '操作完成！',
            icon:'success',
            customClass: {
                icon:'custom-icon-size'
            },
            confirmButtonText: '确定',
            showConfirmButton: false,
            position:'top',
            timer:1800,
            width:"200px",
            
        })},
        Save(){
            // 输入
            if([this.formData.kg,this.formData.cm,this.selectedIndex,this.selectedIndex2].includes(null)){
                Swal.fire({
                    text: '请先输入信息！',
                    icon:'error',
                    customClass: {
                        icon:'custom-icon-size'
                    },
                    showConfirmButton: false,
                    position:'top',
                    timer:1800,
                    width:"200px",
                    })
            }
            else if (this.formData.kg < 0 || this.formData.cm < 0) {
                Swal.fire({
                    text: '身高体重输入有误！',
                    icon:'error',
                    customClass: {
                        icon:'custom-icon-size'
                    },
                    showConfirmButton: false,
                    position:'top',
                    timer:1800,
                    width:"200px",
                    })
            } else {
                Swal.fire({
                    text: '保存成功',
                    icon:'success',
                    customClass: {
                        icon:'custom-icon-size'
                    },
                    showConfirmButton: false,
                    position:'top',
                    timer:1800,
                    width:"200px",
                    })

                    // 这里要把数据发给后端
                    axios.post('http://localhost:5000/api/receive_shape_data', [this.formData.kg,this.formData.cm,this.selectedIndex,this.selectedIndex2,this.gender])
                    .then(response => {
                        console.log('Response from Flask:', response.data);
                    })
                    .catch(error => {
                        console.error('There was an error!', error);
                    });
            }

        
        },
        fetch_model_image() {
        // 向后端发送 GET 请求，获取图像数据
        if (!([this.formData.kg,this.formData.cm,this.selectedIndex,this.selectedIndex2].includes(null))) {
            const swalInstance = this.loading();
            axios.post('http://localhost:5000/api/send_model_img', {},{ responseType: 'blob' ,timeout: 1400000})
            .then(response => {
                // 将返回的 Blob 数据转换为图像 URL
                this.model_image_Url = URL.createObjectURL(response.data);
                swalInstance.close()
                console.log('Image fetched:', this.model_image_Url);
                this.model_existed = true;
                this.$emit('send-message-model-existed',this.model_existed,this.model_image_Url);
            })
            .catch(error => {
                console.error('Error fetching image:', error);
            });
        } else {
            return;
        }
        },
        makesure(){
            if(this.model_existed){
                this.makesure_model = true;
            }
            axios.get('http://localhost:5000/api/close_SD')
            this.$emit('send-message-makesure',this.makesure_model);

        },
        selectCircle(index) {
            
            if (this.selectedIndex === index) {
                this.selectedIndex = null;
            } else {
                this.selectedIndex = index;
            }
        },
        selectCircle2(index) {

            if (this.selectedIndex2 === index) {
                this.selectedIndex2 = null;
            } else {
                this.selectedIndex2 = index;
            }
        },
        loading(){
        const swalInstance = Swal.fire({
            title: '正在生成模特...',
            html: '请稍等...',
            timer: 80000,
            timerProgressBar: true,
            didOpen: () => {
            Swal.showLoading()
            }
        })
        return swalInstance;
        },
    }
}
</script>

<style scoped>
.background {
    position: absolute;
    top: 0;
    right:0;
    width: 450px;
    height: 100vh;
    overflow: hidden;
    background-color: rgb(208, 241, 230);
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    transition: width 0.3s ease;
}
.arrow {
    position: absolute;
    top: 45%;
    right: 440px;
    z-index:10;
    background-color: #b1bec0;
    box-shadow: #000000;
    border-radius: 3px;
    transition: right 0.3s ease;
    cursor: pointer;
    
}
.gender_M {
    position: absolute;
    top : 0;
    right : 117px;
    width: 40px;
    height: 30px;
    font-weight: bold;
    font-size: 16px;
    z-index: 100;
    background-color: rgb(67, 67, 67);
    color: #f8f8f7;
    display: flex;
    align-items: center; /* 垂直居中 */
    justify-content: center; /* 水平居中 */
    cursor: pointer;
}
.gender_W {
    position: absolute;
    top : 0;
    right : 60px;
    height: 30px;
    font-weight: bold;
    font-size: 16px;
    z-index: 10;
    background-color: #efecec;
    display: flex;
    align-items: center; /* 垂直居中 */
    justify-content: center; /* 水平居中 */
    cursor: pointer;

}
.title {
    position: absolute;
    top : 5px;
    left : 10px;
    font-weight: bold;
    font-size: 16px;
    z-index: 2000;
}
.area1 {
    position: absolute;
    top : 30px;
    left: 0;
    right : 0;
    height: 24vh;
    background-color: #efecec;
    border-radius: 10px;
    z-index: 1000;
    transition: background-color 0.3s ease;
}
.woman_area1 {
    position: relative;
    height: 24vh;
    z-index: 2000;
    transition: background-color 0.3s ease;
}
.user {
    position: absolute;
    display: block;
    height: 40px;
    width: auto;
    left: 60px;  
    top:80px;
    z-index: 200;
}

.form {
    position:absolute;
    left: 50px;
    top : 30px;
}
.form1 {
    margin: 12px;
    font-size: 16px;            
    font-weight: bold;
}
.form2 {
    margin: 12px;
    font-size: 16px;            
    font-weight: bold;
}
form input {
    top: 80px;
    width: 20%;
    left: 50px; 
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
}
.cmkgbtn {
    position: absolute;
    right:20px;
    top:6vh;
    background-color: #00b8b8;  /* 青色背景 */
    color: white;               /* 白色文本 */
    padding: 10px 20px;         /* 内边距 */
    border: 2px solid #00b8b8;  /* 边框颜色与按钮背景一致 */
    border-radius: 10px;        /* 10px 圆角 */
    font-size: 16px;            /* 字体大小 */
    font-weight: bold;          /* 字体加粗 */            /* 字体大小 */
    cursor: pointer;           /* 鼠标悬停时变为手形光标 */
    transition: background-color 0.3s ease; /* 背景色过渡 */
}
.cmkgbtn:hover {
    background-color: #009999;  /* 鼠标悬停时，背景色稍微变暗 */
}
.skin_title{
    left: 10px;
    position: absolute;
    top: 30vh;
    font-size: 12px;
    z-index: 2;
}
/* .man_choice1 {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 25vh;
    background-color: #f2f8f9;
} */
.clrcle-container {
    position: absolute;
    top : 0;
    width: auto;
    height: 16vh;
    display: flex;
    justify-content: space-evenly; /* 或者使用 space-between，视需求而定 */
    align-items: center; /* 垂直居中对齐 */
    width: 100%; /* 确保容器宽度占满整个可用宽度 */
    z-index: 2;
}
.clrcle-container2 {
    position: absolute;
    top : 20vh;
    width: auto;
    height: auto;
    display: flex;
    justify-content: space-evenly; /* 或者使用 space-between，视需求而定 */
    align-items: center; /* 垂直居中对齐 */
    width: 450px; /* 确保容器宽度占满整个可用宽度 */
}
.circle {
    top: 30px;
    margin-top: 50px;
    width: 50px; /* 圆的宽度 */
    height: 50px; /* 圆的高度 */
    background-color: #f8e7d7; /* 圆的颜色 */
    border-radius: 50%; 
    border: 2px solid #ffffff; 
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    font-size: 18px;
    z-index : 2;
}

.circle_write {
    top: 0;
    margin: 21px;
    width: 15px; /* 圆的宽度 */
    height: 15px; /* 圆的高度 */
    background-color: #f8f8f7; /* 圆的颜色 */
    border-radius: 50%; 
    border: 1px solid #a7a0a0; 
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    font-size: 18px;
    z-index : 4;
    cursor: pointer;
}
.area2 {
    position: absolute;
    top : 28vh;
    left: 0;
    right : 0;
    height: 28vh;
    background-color: rgb(199, 222, 222);
    z-index: 1;
}
.circle_write.selected {
  background-color: rgb(158, 156, 156);
  border-color: rgb(255, 255, 255);    
  z-index : 3;
}
.clrcle-container3 {
    position: absolute;
    top : 0;
    width: auto;
    height: 40vh;
    display: flex;
    justify-content: space-evenly; /* 或者使用 space-between，视需求而定 */
    align-items: center; 
    width: 100%; 
    z-index : 2;
}
.shape_title{
    left : 10px;
    position: absolute;
    top: 58vh;
    font-size: 12px;
    z-index:2
}
.area3{
    position: absolute;
    top: 56vh;
    width: 500px;
    height: 44vh;
    background-color: #f2f8f9;
    justify-content: center;
    align-items: center;
}
.area3 img{
    display: block;
    left: 14px;
    max-width: 425px;
    position: absolute;
    top: 8vh;
    height: auto;
    z-index: 3;
}
.custom-ico-size {
    font-size: 30px;
}
</style>