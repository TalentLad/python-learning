from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class BookInfoManager(models.Manager):
    def all(self):
        books = super().all()
        books = books.filter(isDelete=False)
        return books
    def create(self,btitle,bpub_date):
        res_cls = self.model
        book = res_cls()
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()
        return book



class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    #max_digits表示最大位数,decimal_places表示小数位数
    bprice = models.DecimalField(max_digits=10,decimal_places=2,default=0,null=True)

    objects = BookInfoManager()

    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE,)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.hname

class Areas(models.Model):
    atitle = models.CharField(max_length=20)
    aparent = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE,)

    def parent(self):
        if self.aparent is None:
            return ''
        else:
            return self.aparent.atitle
    parent.shor_description = '父级地区名称'

    def __str__(self):
        return self.atitle

class PicTest(models.Model):
    # 上传图片
    goods_pic = models.ImageField(upload_to='booktest')

class GoodsInfo(models.Model):
    gcontent = HTMLField()
