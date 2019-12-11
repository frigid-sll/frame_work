<template>
    <div id="DelShop">
        {{get_all_shop}}
        请选择你要删除的店铺名:<br>
        <select id="shop" multiple="multiple">
            <option v-for="x in all_shop">{{x.shop_name}}</option>
        </select>
        <br>
        <button @click="del">点击删除</button>
    </div>
</template>
<script>
import Qs from 'qs'
export default {
    name:'#DelShop',
    data(){
        return{
            all_shop:'',
            shop_list:[]
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
        del:function(){
            const options=document.getElementById('shop').options
            for(var i=0;i<options.length;i++){
                if(options[i].selected){
                    this.shop_list.push(options[i].value)
                }
            }
            if(this.shop_list.length!=0){
                this.axios.post('/api/shop/delete/',
					Qs.stringify({  
               			shop_name: this.shop_list.join(','),
            		}),
					).then((res)=>{
						if(res.data.code==200){
                            alert('删除成功')
                            location.reload()
                        }else{
                            alert('删除失败')
                        }
					})
            }else{
                alert('请选择你要删除的商店')
            }
        }
    }
}
</script>

