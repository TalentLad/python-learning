from django.contrib import admin

# Register your models here.
from .models import BookInfo,HeroInfo,Areas,PicTest,GoodsInfo

class BookInfoAdmin(admin.ModelAdmin):
    #是一个可迭代对象
    list_display = ['id','btitle','bpub_date']

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hgender','hcomment','hbook_id']

class AreasInfoAdmin(admin.ModelAdmin):
    list_per_page = 10 #每页显示10条数据
    list_display = ['id','atitle','parent']
    actions_on_top = False
    actions_on_bottom = True
    list_filter = ['atitle']
    search_fields = ['atitle']

class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id']

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
admin.site.register(Areas,AreasInfoAdmin)
admin.site.register(PicTest)
admin.site.register(GoodsInfo,GoodsInfoAdmin)


