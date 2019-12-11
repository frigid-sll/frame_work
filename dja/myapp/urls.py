from rest_framework.routers import DefaultRouter
from myapp import views

router = DefaultRouter()
router.register('goods',views.Manage_Goods,base_name="goods")
router.register('shop',views.Manage_Shop,base_name="shop")
router.register('user',views.Manage_User,base_name="user")
router.register('stu',views.UserViewSet,base_name="stu")
router.register('hello',views.HelloWorldViewSet,base_name="hello")

urlpatterns = router.urls



