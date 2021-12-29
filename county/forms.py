
from django import forms
from county.models import countyMap, mapGeometry, mapMetaData
from django.contrib.postgres.search import TrigramSimilarity
import csv
def set_field_html_name(cls, new_name):
    old_render = cls.widget.render
    def _widget_render_wrapper(name, value, attrs=None):
        return old_render(new_name, value, attrs)
    cls.widget.render = _widget_render_wrapper

MAP_CHOICES = [
    ('countyMap', 'Illinois'),
    ('stateTiger', 'US States')
    ]


class MapGeometryInput(forms.Form):
    import_file = forms.FileField()
    text = forms.CharField()
    form_select = forms.ChoiceField(choices=MAP_CHOICES)


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
        csvfile = self.cleaned_data["import_file"]
        import codecs
        records = csv.reader(codecs.iterdecode(csvfile, 'utf-8'))
        next(records)
        for line in records:
           metadata = mapMetaData.objects.get_or_create(
                mapname = self.cleaned_data["text"],
                description = self.cleaned_data["text"]
           )
           if self.cleaned_data["form_select"] == 'countyMap':
                polygon_name = line[0]
                try: 
                    map_object = countyMap.objects.get(name=(polygon_name))
                except(countyMap.DoesNotExist):
                    try:
                        map_object = countyMap.objects.annotate( similarity = TrigramSimilarity('name', polygon_name), ).filter(similarity__gt=0.3).order_by('similarity')[0]
                    except():
                        pass
                input_data = mapGeometry()
                input_data.countyname = line[0]
                input_data.fips = map_object.countyfp
                input_data.floatdata = line[1].replace(",", "")
                input_data.description = line[2]
                input_data.geometry = map_object.geometry
                input_data.mapname = mapMetaData.objects.get(mapname=self.cleaned_data["text"])
                input_data.save()
           elif self.cleaned_data["form_select"] == 'countyMap':
               input_data = mapGeometry()
               input_data.countyname = line[0]
               input_data.fips = stateTiger.objects.get(name=(line[0])).statefp
               input_data.floatdata = line[1].replace(",", "")
               input_data.description = line[2]
               input_data.geometry = stateTiger.objects.get(name=(line[0])).geometry
               input_data.mapname = mapMetaData.objects.get(mapname=self.cleaned_data["text"])
               input_data.save()
