from django.contrib import admin
from blog.models import Post,Contact




class PostAdmin(admin.ModelAdmin):
   date_hierarchy='created_date'
   empty_value_display='-empty-'
    # fields=('title',)
   list_display =('title','author','published_date','updated_time','counted_views','status','rate_views')
#    ordering=('updated_time',)
   list_filter = ('status',)
   search_fields=['content','title',]
   
   # add rate for view
   def rate_views(self,obj):
        if obj.counted_views > 50:
            return "Gold"
        else:
            return "silver"

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    list_display =('name','email','subject','message','created_date','updated_date',)
    list_filter = ('email',)
    search_fields =('name','message',)


admin.site.register(Post,PostAdmin)
admin.site.register(Contact,ContactAdmin)




#  Register your models here.
