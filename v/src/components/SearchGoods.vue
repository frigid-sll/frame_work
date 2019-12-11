<template>
    <div id="SearchGoods">
        {{get_all_goods}}
        请输入你要查询的商品：
        <input type="text" v-model="goods_name">
        <button @click="search">点击查询</button>
        <p v-show="is_click_search && shop!='' && goods_name!=''">商品所属店铺有:</p>
        <table v-show="is_click_search && shop!='' && goods_name!=''">
            <tr>
                <td v-for="x in shop">{{x}}</td>
            </tr>
        </table>
        <p v-show="shop=='' && is_click_search">无该商品数据</p>
    </div>
</template>
<script>
import Qs from 'qs'
export default {
    name:'#SearchGoods',
    data(){
        return{
            goods_name:'',
            shop:'',
            all_goods:[],
            is_click_search:false
        }
    },
    computed:{
        get_all_goods:function(){
            this.axios.get('/api/goods/get_all_goods/').then((res)=>{
                    for(var i=0;i<res.data.length;i++){
                        this.all_goods.push(res.data[i].goods_name)
                    }
                    })
        },
    },
    methods:{
        search:function(){
            this.shop=''
            this.is_click_search=true
            if(this.all_goods.indexOf(this.goods_name)!=-1){
                this.axios.post('/api/goods/search/',
                            Qs.stringify({  
                                goods_name:this.goods_name
                            }),
                            ).then((res)=>{
                                this.shop=res.data.shop_name
                            })
            }
        }
    }
}
</script>
