# Generated by Django 2.2.1 on 2019-12-10 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_goods_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='shop',
            field=models.ManyToManyField(related_name='goods', to='myapp.Shop'),
        ),
    ]
