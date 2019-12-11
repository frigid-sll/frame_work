<template>
    <div id="stu">
        {{first_page_res}}{{get_total_page_num}}
        <table>
            <tr v-for="x in stu_data">
               <td>{{x.name}}</td> 
            </tr>
        </table>
        <button v-if='page!=1' @click="page_res(page-1)">上一页</button>
        <button v-if='page<total_page_num' @click="page_res(page+1)">下一页</button>
    </div>
</template>
<script>
import Qs from 'qs'
export default {
    name:'#stu',
    data(){
        return{
            stu_data:'',
            page:1,
            url:'',
            total_page_num:'',
        }
    },
    computed:{
        first_page_res:function(){
            this.axios.get('/api/user/get_page_res/').then((res)=>{
                    this.stu_data=res.data
					})
        },
        get_total_page_num:function(){
            this.axios.get('/api/user/get_total_page_num/').then((res)=>{
                    this.total_page_num=res.data.total_page
                    // alert(this.total_page_num)
					})
        }
    },
    methods:{
        page_res:function(num){
            this.page=num
            this.url='/api/user/get_page_res/?p='+num
            this.axios.get(this.url).then((res)=>{
                    this.stu_data=res.data
					})
        }
    }
}
</script>

