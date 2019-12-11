from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=32)
    class Meta:
        verbose_name_plural='学生表'
    def __str__(self):
        return self.name

class Shop(models.Model):
	shop_name=models.CharField(max_length=50)
	def __str__(self):
		return self.shop_name

class Goods(models.Model):
	goods_name=models.CharField(max_length=50)
	shop=models.ManyToManyField(to='Shop',related_name='goods')
	def __str__(self):
		return self.goods_name