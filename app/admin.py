from django.contrib import admin

# Register your models here.
from app.models import *

class CustomWebPage(admin.ModelAdmin):
    list_display=['topic_name','name','url','email']
    list_display_links=['name']
    list_editable=['email']
    list_filter=['name','url']
    #list_per_page=1
    search_fields=['name']

admin.site.register(Topic)
admin.site.register(WebPage,CustomWebPage)
admin.site.register(AccessRecord)