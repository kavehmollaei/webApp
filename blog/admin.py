from django.contrib import admin
from blog.models import Post



class PostAdmin(admin.ModelAdmin):
   date_hierarchy='created_date'
   empty_value_display='-empty-'
    # fields=('title',)
   list_display =('title','published_date','updated_time','counted_views','status','rate_views')
   ordering=('updated_time',)
   list_filter = ('status',)
   search_fields=['content','title',]
   
   # add rate for view
   def rate_views(self,obj):
        if obj.counted_views > 50:
            return "Gold"
        else:
            return "silver"


admin.site.register(Post,PostAdmin)





#  Register your models here.
