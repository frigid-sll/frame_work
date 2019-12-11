from django.shortcuts import render,HttpResponse,redirect,reverse
from django.db.models import Q,F
from myapp.serializers import *
from myapp import models
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import pagination                #分页
import datetime
import os
from dja import settings
# from django.core import serializers
# import json
# from django.views import View

class Mypagination(pagination.PageNumberPagination):  # 分页类定义
    """自定义分页"""
    page_size=2  #默认每页显示个数配置
    page_query_param = 'p' # 页面传参的key,默认是page
    page_size_query_param='size'  # 指定每页显示个数参数
    max_page_size=4 # 每页最多显示个数配置，使用以上配置，可以支持每页可显示2~4条数据

class Manage_User(GenericViewSet):
    """管理用户数据"""

    @action(methods=["POST"],detail=False)
    def login(self,request):
        account=request.data.get('account')
        res={'code':200} if account == '123' else {'code':0}
        return Response(res)

    @action(methods=["POST"],detail=False)
    def img(self,request):
        image = request.FILES.get('file')
        #以防上传图片会覆盖以前的所以我们拼接一个时间戳解决
        image_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')+image.name
        f = open(os.path.join(settings.UPLOAD_FILE,image_name),'wb')
        #image.chunks() 以二进制流写入文件
        for i in image.chunks():
            f.write(i)
        f.close()
        mes={'code':200,'img_url':'http://127.0.0.1:8000/upload/'+image_name}
        return Response(mes)

class Manage_Goods(GenericViewSet):
    """管理商品数据"""
    queryset=''

    @action(detail=False)
    def get_first_goods_shop(self,request):
        first_goods_name=models.Goods.objects.all()[0].goods_name
        self.queryset=models.Goods.objects.filter(goods_name='{}'.format(first_goods_name)).first().shop.all()
        res= [x.shop_name for x in self.queryset]
        return Response({'shop_name':res})

    @action(detail=False)
    def get_all_goods(self,request):
        self.queryset=models.Goods.objects.all()
        res=GoodsSerializer(self.queryset,many=True)
        return Response(res.data)

    @action(methods=["POST"],detail=False)
    def get_goods_shop(self,request):
        goods_name=request.data.get('goods_name')
        self.queryset=models.Goods.objects.filter(goods_name='{}'.format(goods_name)).first().shop.all()
        res= [x.shop_name for x in self.queryset]
        return Response({'shop_name':res})

    @action(methods=["POST"],detail=False)
    def add(self,request):
        goods_name=request.data.get('goods_name')
        shop_list=[models.Shop.objects.filter(shop_name=x).first() for x in request.data.get('shop_list').split(',')]
        #商品表添加商品
        add_goods=models.Goods.objects.create(goods_name=goods_name)
        add_goods.shop.add(*shop_list)  
        add_goods.save()
        #店铺表添加商品
        for x in shop_list:
            models.Shop.objects.filter(shop_name=x).first().goods.add(add_goods)
        return Response({'code':200})

    @action(methods=["POST"],detail=False)
    def delete(self,request):
        for x in request.data.get('goods_name').split(','):
            models.Goods.objects.filter(goods_name=x).delete()
        return Response({'code':200})

    @action(methods=["POST"],detail=False)
    def amend(self,request):
        old_name=request.data.get('old_name')
        new_name=request.data.get('new_name')
        shop_list=request.data.get('shop_list').split(',')
        models.Goods.objects.filter(goods_name=old_name).update(goods_name=new_name)
        id_list=[models.Shop.objects.filter(shop_name=x).first().id for x in shop_list]
        models.Goods.objects.filter(goods_name=new_name).first().shop.set(id_list)
        return Response({'code':200})
    
    @action(methods=["POST"],detail=False)
    def search(self,request):
        goods_name=request.data.get('goods_name')
        self.queryset=models.Goods.objects.filter(goods_name='{}'.format(goods_name)).first().shop.all()
        shop= [x.shop_name for x in self.queryset]
        res={'goods_name':goods_name,'shop_name':shop} 
        return Response(res)

class Manage_Shop(GenericViewSet):
    """管理商店数据"""
    queryset = ''  #数据的queryset

    @action(detail=False)
    def get_all_shop(self,request):
        self.queryset=models.Shop.objects.all()
        res=ShopSerializer(self.queryset,many=True)
        return Response(res.data)

    @action(methods=["POST"],detail=False)
    def add(self,request):
        shop_name=request.data.get('shop_name')
        models.Shop.objects.create(shop_name=shop_name)
        return Response({'code':200})
    
    @action(methods=["POST"],detail=False)
    def delete(self,request):
        for x in request.data.get('shop_name').split(','):
            models.Shop.objects.filter(shop_name=x).delete()
        return Response({'code':200})
    
    @action(methods=["POST"],detail=False)
    def amend(self,request):
        old_name=request.data.get('old_name')
        new_name=request.data.get('new_name')
        models.Shop.objects.filter(shop_name=old_name).update(shop_name=new_name)
        return Response({'code':200})

    @action(methods=["POST"],detail=False)
    def search(self,request):
        shop_name=request.data.get('shop_name')
        self.queryset=models.Shop.objects.filter(shop_name='{}'.format(shop_name)).first().goods.all()
        goods_name= [x.goods_name for x in self.queryset]
        res={'shop_name':shop_name,'goods_name':goods_name} 
        return Response(res)

        

# class HelloWorldViewSet(GenericViewSet):
#     """hello"""
#     @action(methods=["POST"],detail=False)
#     def world(self, request, *args, **kwargs):
#         name=request.data.get('username')
#         # print(name)
#         return Response({"code": 200, "msg": "hello world!"})
    
#     @action(detail=False)
#     def bye(self,request):
#         return Response({'code':200})


# class UserViewSet(GenericViewSet):
#     """学生表"""
#     queryset = models.Student.objects.all()  #数据的queryset
#     pagination_class = Mypagination #分页类，前面章节也已经介绍

#     @action(detail=False)
#     def get_total_page_num(self,request,*args,**kwargs):
#         total_page=len(self.queryset)//2 if len(self.queryset)%2==0 else len(self.queryset)//2+1
#         # print(total_page)
#         return Response({'total_page':total_page})

#     @action(detail=False)
#     def get_page_res(self,request,*args,**kwargs):  #与url中映射的方法名称相同
#         page_res=self.paginate_queryset(queryset=self.queryset)  #分页结果
#         res=StudentSerializer(page_res,many=True)  #序列化
#         # print(res.data)
#         return Response(res.data)  #返回结果

    # @action(detail=False)
    # def info(self,request):
    #     stu = StudentSerializer(self.queryset,many=True)
    #     return Response(stu.data)


# def get_ip(request):
#     if 'HTTP_X_FORWARDED_FOR' in request.META:
#         ip =  request.META['HTTP_X_FORWARDED_FOR']
#     else:
#         ip = request.META['REMOTE_ADDR']
#     mes={'code':200,'ip':ip}
#     # print(request.path)
#     # print(request.META)
#     return HttpResponse(json.dumps(mes,ensure_ascii=False))



# def is_login(func):
#     def inner(self,request):
#         if request.session.get('account',None):
#             return func(request)
#         else:
#             return redirect(reverse('get_ip'))
#     return inner


# class Start(View):
#     def __init__(self):
#         self.mes={}
#     @is_login
#     def get(self,request):
#         self.mes={'code':200}
#         return HttpResponse(json.dumps(self.mes,ensure_ascii=False))
#     @is_login
#     def post(self,request):
#         pass