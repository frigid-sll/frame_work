<template>
    <div id="DelGoods">
        {{get_all_goods}}
        请选择你要删除的商品名:<br>
        <select id="goods" multiple="multiple">
            <option v-for="x in all_goods">{{x.goods_name}}</option>
        </select>
        <br>
        <button @click="del">点击删除</button>
    </div>
</template>
<script>
import Qs from 'qs'
export default {
    name:'#DelGoods',
    data(){
        return{
            all_goods:'',
            goods_list:[]
        }
    },
    computed:{
         get_all_goods:function(){
            this.axios.get('/api/goods/get_all_goods/').then((res)=>{
                    this.all_goods=res.data
					})
        }
    },
    methods:{
        del:function(){
            const options=document.getElementById('goods').options
            for(var i=0;i<options.length;i++){
                if(options[i].selected){
                    this.goods_list.push(options[i].value)
                }
            }
            if(this.goods_list.length!=0){
                this.axios.post('/api/goods/delete/',
					Qs.stringify({  
               			goods_name: this.goods_list.join(','),
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
                alert('请选择你要删除的商品')
            }
        }
    }
}
</script>

