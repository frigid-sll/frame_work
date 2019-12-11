import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ShowStu from '@/components/ShowStu'
import AddGoods from '@/components/AddGoods'
import AddShop from '@/components/AddShop'
import DelShop from '@/components/DelShop'
import DelGoods from '@/components/DelGoods'
import AmendShop from '@/components/AmendShop'
import AmendGoods from '@/components/AmendGoods'
import SearchGoods from '@/components/SearchGoods'
import SearchShop from '@/components/SearchShop'
import Login from '@/components/Login'
import Img from '@/components/Img'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/ShowStu',
      name: 'ShowStu',
      component: ShowStu
    },
    {
      path: '/AddGoods',
      name: 'AddGoods',
      component: AddGoods
    },
    {
      path: '/AddShop',
      name: 'AddShop',
      component: AddShop
    },
    {
      path: '/DelShop',
      name: 'DelShop',
      component: DelShop
    },
    {
      path: '/DelGoods',
      name: 'DelGoods',
      component: DelGoods
    },
    {
      path: '/AmendShop',
      name: 'AmendShop',
      component: AmendShop
    },
    {
      path: '/AmendGoods',
      name: 'AmendGoods',
      component: AmendGoods
    },
    {
      path: '/SearchGoods',
      name: 'SearchGoods',
      component: SearchGoods
    },
    {
      path: '/SearchShop',
      name: 'SearchShop',
      component: SearchShop
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login
    },
    {
      path: '/Img',
      name: 'Img',
      component: Img
    }
  ]
})
