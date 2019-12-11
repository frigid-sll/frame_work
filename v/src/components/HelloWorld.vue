<template>
    <div id="HelloWorld">
        {{start}}
        {{HelloWorld}}<br>
        <input type="text" v-model="username"><br>
        <input type="text" v-model="password"><br>
        <button @click="login">点击登录</button>
    </div>
</template>
<script>
import Qs from 'qs'
export default {
    name:'#HelloWorld',
    data(){
        return{
            HelloWorld:'HelloWorld',
            username:'',
            password:'',
        }
    },
    computed:{
        start:function(){
            this.axios.get('/api/hello/bye/',).then((res)=>{
                if(res.data.code==200){
                    alert('已登录')
                }else{
                    alert('未登录')
                }
                })
        }
    },
    methods:{
        login:function(){
            this.axios.post('/api/hello/world/',
					Qs.stringify({  
               			username: this.username,
               			password:this.password
            		}),
					).then((res)=>{
						if(res.data.code==200){
                            alert('登录成功')
                            this.$router.replace('/stu')
						}else{
							alert('登录失败')
						}		
					})
        }
    }
}
</script>
