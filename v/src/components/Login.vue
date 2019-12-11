<template>
    <div id="Login">
        请输入账号:<input type="text" v-model="account">
        <button @click="login">点击登录</button>
    </div>
</template>
<script>
import Qs from 'qs'
export default {
    name:'#Login',
    data(){
        return{
            account:'',
        }
    },
    methods:{
        login:function(){
            this.axios.post('/api/user/login/',
                            Qs.stringify({  
                                account:this.account
                            }),
                            ).then((res)=>{
                                if(res.data.code==200){
                                    localStorage.setItem('account',this.account)
                                    alert('登录成功')
                                }else{
                                    alert('登陆失败')
                                }
                            })
        }
    }
}
</script>

