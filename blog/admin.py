import imp
from statistics import mode
from django.contrib import admin
from blog.models import Post,Contact,UserProfile
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserCreateForm,UserChangeForm




class PostAdmin(admin.ModelAdmin):
   date_hierarchy='created_date'
   empty_value_display='-empty-'
    # fields=('title',)
   list_display =('title','author','published_date','updated_time','counted_views','status','rate_views')
#    ordering=('updated_time',)
   list_filter = ('status','author')
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



class UserProfileAdmin(admin.ModelAdmin):
    list_display =('address','about','user',)
# class CustomeUserAdmin(UserAdmin):
    # add_form = UserCreateForm
    # form = UserChangeForm
    # model = CustomeUser
    # list_display =('pk','email','username','first_name','last_name')
    # add_fieldsets = UserAdmin.add_fieldsets + (None,{'fields':('email','first_name','last_name','')})





admin.site.register(Post,PostAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(UserProfile,UserProfileAdmin)


#  Register your models here.
