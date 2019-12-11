<template>
    <div id="AddGoods">
        {{get_all_shop}}
        <input type="text" v-model="goods_name" placeholder="请输入商品名称">
        <br>商品所属店铺有：<br>
        <select id="shop" multiple="multiple">
            <option v-for="x in all_shop">{{x.shop_name}}</option>
        </select>
        <br>
        <button @click="add">点击添加</button>
    </div>
</template>
<script>
import Qs from 'qs'
export default {
    name:'#AddGoods',
    data(){
        return{
            all_shop:'',
            shop:[],
            goods_name:'',
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
        add:function(){
            if(this.goods_name==''){
                alert('请输入你要添加的商品')
            }else{
                const options=document.getElementById('shop').options
                for(var i=0;i<options.length;i++){
                    if(options[i].selected){
                        this.shop.push(options[i].value)
                    }
                }
                console.log(this.shop)
                if(this.shop.length!=0){
                    this.axios.post('/api/goods/add/',
                        Qs.stringify({  
                            goods_name: this.goods_name,
                            shop_list:this.shop.join(',')
                        }),
                        ).then((res)=>{
                            if(res.data.code==200){
                                alert('添加成功')
                            }else{
                                alert('添加失败')
                            }	
                        })
                }else{
                    alert('请选择你要添加商品所属店铺')
                }
            }
        }
    }
}
</script>
