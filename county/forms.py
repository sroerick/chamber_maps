
from django import forms
from county.models import countyMap, mapGeometry, mapMetaData
import csv
'''`
def set_field_html_name(cls, new_name):
    old_render = cls.widget.render
    def _widget_render_wrapper(name, value, attrs=None):
        return old_render(new_name, value, attrs)
    cls.widget.render = _widget_render_wrapper
'''
class MapGeometryInput(forms.Form):
    import_file = forms.FileField()
    #set_field_html_name(import_file, 'import_file')
    text = forms.CharField()


    #class Meta: 
        #model = mapGeometry 
        
        # not sure if this is necessary but i'm pasting it here for reference
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(MapGeometryInput, self).__init__(*args, **kwargs)
            #if self.instance.id is not None:
                #selected_items = [ values[0] for values in Application.objects.filter(project=self.instance) ]
                #self.fields['project_apps'].initial = selected_items
    
    def save(self):
        #form_input = mapGeometryInput()
        #csvfile = request.FILES['import_file']
        csvfile = self.cleaned_data["import_file"]
        #with open(self.cleaned_data["import_file"], "rb") as csvfile:
        import codecs
        records = csv.reader(codecs.iterdecode(csvfile, 'utf-8'))
        #import ipdb; ipdb.set_trace()
        next(records)
        for line in records:
           #metadata = mapMetaData()
           #metadata.mapname = self.cleaned_data["text"]
           #metadata.description = self.cleaned_data["text"]
           #metadata.save()
           metadata = mapMetaData.objects.get_or_create(
               mapname = self.cleaned_data["text"],
               description = self.cleaned_data["text"]
           )
           
           input_data = mapGeometry()
           input_data.countyname = line[0]
           input_data.fips = countyMap.objects.get(name=(line[0])).countyfp
           input_data.floatdata = line[1].replace(",", "")
           input_data.description = line[2]
           input_data.geometry = countyMap.objects.get(name=(line[0])).geometry
           #input_data.mapname = metadata
           #import ipdb; ipdb.set_trace()
           
           input_data.mapname = mapMetaData.objects.get(mapname=self.cleaned_data["text"])
           input_data.save()

