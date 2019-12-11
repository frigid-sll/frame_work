<template>
    <div id="AddShop">
        请输入你要添加的商店:
        <input type="text" v-model="shop_name">
        <button @click="add">点击添加</button>
    </div>
</template>
<script>
import Qs from 'qs'
export default {
    name:"#AddShop",
    data(){
        return{
            shop_name:'',
        }
    },
    methods:{
        add:function(){
            if(this.shop_name!=''){
                this.axios.post('/api/shop/add/',
					Qs.stringify({  
               			shop_name: this.shop_name,
            		}),
					).then((res)=>{
						if(res.data.code==200){
                            alert('添加成功')
                        }else{
                            alert('添加失败')
                        }
					})
            }else{
                alert('请输入你要添加的商店')
            }
        }
    }
}
</script>

