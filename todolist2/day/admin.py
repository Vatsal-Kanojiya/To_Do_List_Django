from django.contrib import admin
from .models import activity

# Register your models here.
class ActivityAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('task',)} 
    list_filter=('day','month','year','status','task')
    list_display=('order','task','status')
    list_display_links=('task',)

admin.site.register(activity,ActivityAdmin)


