<template>
    <div id="AmendShop">
        {{get_all_shop}}
        请选择你要修改的店铺名:<br>
        <select id="shop">
            <option v-for="x in all_shop">{{x.shop_name}}</option>
        </select>
        <br>请输入修改后的店铺名：
        <input type="text" v-model="new_name">
        <button @click="update">点击修改</button>
    </div>
</template>
<script>
import Qs from 'qs'
export default {
    name:'#AmendShop',
    data(){
        return{
            all_shop:'',
            new_name:'',
            old_name:'',
        }
    },
    computed:{
         get_all_shop:function(){
            this.axios.get('/api/shop/get_all_shop/').then((res)=>{
                    this.all_shop=res.data
					})
        }
    },
    methods:{
        update:function(){
            this.old_name=document.getElementById('shop').value
            if(this.old_name.length!=0){
                this.axios.post('/api/shop/amend/',
					Qs.stringify({  
                        old_name: this.old_name,
                        new_name:this.new_name
            		}),
					).then((res)=>{
						if(res.data.code==200){
                            alert('修改成功')
                            location.reload()
                        }else{
                            alert('修改失败')
                        }
					})
            }else{
                alert('请选择你要修改的店铺')
            }
        }
    }
}
</script>

