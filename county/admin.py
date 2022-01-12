from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import countyMap, countyData, exampleData, mapControl, mapMetaData, mapGeometry
from django.conf.urls import url 
from django.urls import path
from county.forms import MapGeometryInput
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

# Register your models here.
@admin.register(countyMap)
class AcountyMapAdmin(admin.ModelAdmin):
    list_display=['countyfp', 'name']


#admin.site.register(exampleData)

@admin.register(countyData)
#@admin.register(mapMetaData)
class countyAdmin(admin.ModelAdmin):
   list_display=['county','data','collection']

class mapControlAdmin(admin.TabularInline):
    model = mapControl
    extra = 0

class csvDataTypeAdmin(admin.TabularInline):
    model = mapGeometry 
    fields = ('mapname', 'countyname', 'fips', 'floatdata', 'description')
    extra = 0 

class mapAdmin(admin.ModelAdmin):
    model = mapMetaData
    inlines = (mapControlAdmin, csvDataTypeAdmin)
    fields = ('mapname', 'description', 'slug')
    readonly_fields=['map_url']
    list_display=['mapname', 'description']
    change_list_template = 'county/mapMetaData/change_list.html'

    




admin.site.register(mapMetaData, mapAdmin)

class importComplete(TemplateView):
    template_name = 'county/upload_done.html'
    def post(self, request, **kwargs):
        print(request)
        return render(request, 'county/upload_done.html')

class csvImport(AdminSite):
    #need to fix permissions here:
    #@staff_member_required
    def custom_view(self, request):
        if request.method == "POST":
            form = MapGeometryInput(request.POST, request.FILES)
            #import ipdb;ipdb.set_trace()
            if form.is_valid():
                form.is_valid()
                form.save()
                success = True
                context = {"form": form, "success": success}
                return render(request, "county/upload_done.html", context)
        else:
            form = MapGeometryInput()
            context = {"form": form}
            return render(request, "county/upload.html", context)
    def get_urls(self):
        urls = super().get_urls()
        csv_urls = [
            #path('import/', self.admin_site.admin_view(self.custom_view))
            path('', self.custom_view, name='importform'),
            ]
        return csv_urls + urls

admin_csv_import = csvImport()
