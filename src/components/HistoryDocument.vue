<template>
    <div class="history_background">
        <div class="add_document_button" @click="addHistorydocument">
            <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg">
                <!-- 垂直线 -->
                <rect x="23" y="5" width="5" height="40" fill="white" rx="2" ry="2"/>
                <!-- 水平线 -->
                <rect x="5" y="22" width="40" height="5" fill="white" rx="2" ry="2"/>
            </svg>
        </div>
        
        <div 
        v-for="(item, index) in divs" 
        :key="index" 
        class="history" 
        @click="selectHistory(index)"
        :class="{ focuse: selectedIndex === index }"
        >
        第 {{ index + 1 }} 条记录
        </div> 
    
    
    </div>
</template>

<script>
export default {
    data (){
        return {
            divs:[{}],
            selectedIndex : 0,
        }
    },
    methods: {
        selectHistory(index) {
            this.selectedIndex = index;
        },
        addHistorydocument(){
            if (this.selectedIndex == null){
                this.selectedIndex = 0;
            } else {
                this.selectedIndex ++;
            }
            this.divs.push({});

        }
    },
    computed:{

    }
}

</script>


<style scoped>
.history_background {
    position:absolute;
    background-color: rgba(139, 139, 139, 0.589);
    height: 100%;
    overflow-y: scroll;
    width: calc(100vw - 1100px);
    border-radius: 10px;
    top: 0;
    left: 0;
    z-index: 0;

}

.history.focuse{
    background-color: rgb(230, 232, 238); 
    box-shadow: 10px 10px 15px rgba(0, 0, 0, 0.3);
    border:none;
    border-top: 5px solid rgb(202, 202, 202);
    border-bottom: 5px solid rgb(202, 202, 202);
    width: calc(100vw - 1100px);
    box-shadow: 10px 10px 15px rgba(0, 0, 0, 0.3);

}

.add_document_button {
    height: 50px;
    width: 50px;
    left: 25px;
    top: 25px;
    position: fixed;
    border-radius: 25px; 
    background-color: rgba(176, 221, 221, 0.822); 
    box-shadow: 10px 10px 15px rgba(0, 0, 0, 0.3);
    cursor: pointer;
    z-index: 10;

}
.history {
    position: relative;
    left: 0;
    top: 100px;
    height:100px;
    width: calc(100vw - 1110px);
    background-color: rgb(227, 238, 241);
    border: 5px solid rgb(202, 202, 202);
    margin-top: 20px;
    cursor: pointer;
    z-index: 9;

}
/* 隐藏滚动条 */
.history_background::-webkit-scrollbar {
  display: none;  /* 完全隐藏滚动条 */
}


</style>