from django.contrib import admin

from .models import Youtuber
from django.utils.html import format_html

class YTAdmin(admin.ModelAdmin):
     def myphoto(self, obj):
          return format_html('<img src = {} width="40">'.format(obj.photo.url))

     list_display = ('id','name','myphoto','subs_count','is_featured')
     list_filter = ('city', 'camera_type')
     search_fields = ('name', 'camera_type')
     list_display_links = ('id', 'name')
     list_editable = ('is_featured',)

# Register your models here.
admin.site.register(Youtuber, YTAdmin)