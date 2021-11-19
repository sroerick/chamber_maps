from django.contrib import admin
from .models import countyMap, countyData

# Register your models here.
admin.site.register(countyMap)
@admin.register(countyData)
class countyAdmin(admin.ModelAdmin):
   list_display=['county','data','collection']

