from rest_framework import serializers
from . import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields = '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Goods
        fields = '__all__'