from django.db import models

class GoodsType(models.Model):
    title=models.CharField('名称',max_length=20)
    desc=models.CharField('描述',max_length=200,default='商品描述',db_column='desc')
    flag=models.IntegerField(default=0)
    picture=models.ImageField(upload_to='static/',default="normal.png")
    isDelete=models.BooleanField(default=False)
    class Meta:
        db_table='goods_type'
    def __str__(self):
        return self.title


class Goods(models.Model):
    title=models.CharField('名称',max_length=20)
    price=models.DecimalField('价格',max_digits=8,decimal_places=2,default=0)
    desc=models.CharField('描述',max_length=1000,db_column='desc')
    picture=models.ImageField(upload_to='static/')
    isDelete=models.BooleanField(default=False)
    type=models.ForeignKey(GoodsType,related_name='goods')

    class Meta:
        db_table='goods'
    def __str__(self):
        return self.title



