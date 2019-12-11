<template>
    <div id="SearchGoods">
        {{get_all_shop}}
        请输入你要查询的店铺：
        <input type="text" v-model="shop_name">
        <button @click="search">点击查询</button>
        <p v-show="is_click_search && goods!='' && shop_name!=''">店铺含有的商品有:</p>
        <table v-show="is_click_search && goods!='' && shop_name!=''">
            <tr>
                <td v-for="x in goods">{{x}}</td>
            </tr>
        </table>
        <p v-show="goods=='' && is_click_search">无该店铺数据</p>
    </div>
</template>
<script>
import Qs from 'qs'
export default {
    name:'#SearchGoods',
    data(){
        return{
            shop_name:'',
            goods:'',
            all_shop:[],
            is_click_search:false
        }
    },
    computed:{
        get_all_shop:function(){
            this.axios.get('/api/shop/get_all_shop/').then((res)=>{
                    for(var i=0;i<res.data.length;i++){
                        this.all_shop.push(res.data[i].shop_name)
                    }
                    })
        },
    },
    methods:{
        search:function(){
            this.goods=''
            this.is_click_search=true
            if(this.all_shop.indexOf(this.shop_name)!=-1){
                this.axios.post('/api/shop/search/',
                            Qs.stringify({  
                                shop_name:this.shop_name
                            }),
                            ).then((res)=>{
                                this.goods=res.data.goods_name
                            })
            }
        }
    }
}
</script>
