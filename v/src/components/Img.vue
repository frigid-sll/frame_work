<template>
    <div id="Img">
        商品图片：<input type="file" id="saveimage"><br>
        <button @click="addgoods()">添加</button>
        <img src="" id="img">
    </div>
</template>
<script>
import Qs from 'qs'
export default {
    name:'#Img',
    data(){
        return{

        }
    },
    methods:{
        addgoods:function () {
            //定义data值，方便于传送数据
            var data = new FormData();
            //1.从input框里获取图片
            var img = document.getElementById('saveimage').files[0];
            //2.将图片添加到Formdata中
            data.append('file',img,img.name);
            this.axios({
                    url:'/api/user/img/',
                    method:'post',
                    data:data,
                    headers:{'Content-Type':'multipart/form-data'}
                }).then((res)=>{
                    document.getElementById('img').src=res.data.img_url
            })
        }
    }
}
</script>

