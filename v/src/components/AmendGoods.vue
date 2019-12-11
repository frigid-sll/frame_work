<template>
    <div id="AmendShop">
        {{get_all_goods}}{{get_all_shop}}{{get_first_goods_shop}}
        请选择你要修改的商品名:<br>
        <select id="goods" @change="get_goods_shop">
            <option v-for="x in all_goods">{{x.goods_name}}</option>
        </select>
        <br>请输入修改后的商品名：
        <input type="text" v-model="new_name">
        <br>请选择该商品修改后的所属店铺<br>
        <select id="shop" multiple="multiple">
            <option v-for="x in all_shop">{{x.shop_name}}</option>
        </select>
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
            all_goods:'',
            new_name:'',
            old_name:'',
            shop_list:[],
            goods_shop:[],
        }
    },
    computed:{
         get_all_goods:function(){
            this.axios.get('/api/goods/get_all_goods/').then((res)=>{
                    this.all_goods=res.data
                    })
        },
        get_all_shop:function(){
            this.axios.get('/api/shop/get_all_shop/').then((res)=>{
                    this.all_shop=res.data
					})
        },
        get_first_goods_shop:function(){
            this.axios.get('/api/goods/get_first_goods_shop/').then((res)=>{
                        this.goods_shop=res.data.shop_name
                        const options=document.getElementById('shop').options
                        for(var i=0;i<options.length;i++){
                            if(this.goods_shop.indexOf(options[i].value)!=-1){
                                options[i].selected=true
                            }
                        }
					})
        },
       
    },
    methods:{
        get_goods_shop:function(){
            this.axios.post('/api/goods/get_goods_shop/',
                            Qs.stringify({  
                                goods_name:document.getElementById('goods').value
                            }),
                            ).then((res)=>{
                                this.goods_shop=res.data.shop_name
                                const options=document.getElementById('shop').options
                                for(var i=0;i<options.length;i++){
                                    if(this.goods_shop.indexOf(options[i].value)!=-1){
                                        options[i].selected=true
                                    }else{
                                        options[i].selected=false
                                    }
                                }
                            })
        },
        update:function(){
            this.old_name=document.getElementById('goods').value
            const options=document.getElementById('shop').options
            for(var i=0;i<options.length;i++){
                if(options[i].selected){
                    this.shop_list.push(options[i].value)
                }
            }
            if(this.old_name.length!=0){
                if(this.new_name.length!=0){
                    if(this.shop_list.length!=0){
                        this.axios.post('/api/goods/amend/',
                            Qs.stringify({  
                                old_name: this.old_name,
                                new_name:this.new_name,
                                shop_list:this.shop_list.join(',')
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
                        alert('请选择该商品所属店铺')
                    }
                }else{
                    alert('请输入修改后的商品名')
                }
            }else{
                alert('请选择你要修改的商品')
            }
        }
    }
}
</script>

