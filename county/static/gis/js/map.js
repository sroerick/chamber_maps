const copy = 'Illinois Chamber | © <a href="https://osm.org/copyright">OpenStreetMap</a> contributors'
const url = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
const osm = L.tileLayer(url, { attribution: copy })
const map = L.map('map', {
  printable: true,
  downloadable: true,
  center:L.latLng(40.6331,89.3985), 
  layers: [osm], 
  minZoom: 3 
	}).setView([40.6331, -89.3985], 6);

const parsed = JSON.parse(mapControl.replaceAll('&quot','"').replaceAll(';',''))
const upper_limit_array = [0]
const upper_limit_sort = function () {
	for (i=0; i < parsed.length; i++) {
	upper_limit_array.push(parsed[i].fields.upper_limit)
	}
}


function getColorLive(d) {
  for (i=0; i < parsed.length; i++) {
    if (d >=parsed[i].fields.lower_limit && d <=parsed[i].fields.upper_limit)
      return parsed[i].fields.color
  }
}

var info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info');
    this.update();
    return this._div;
};

info.update = function (props) {
this._div.innerHTML = '<h4>' + mapName + '</h4>' +  (props ?
'<b>' + props.countyname + '</b><br />' + props.floatdata + '<br />' + props.description
: 'Hover over a county');
  };
info.addTo(map);

function style(feature) {
    return {
    fillColor: getColorLive(feature.properties.floatdata),
    weight: 2,
    opacity: 1,
    color: 'white',
    dashArray: '3',
    fillOpacity: 0.7
    };
	
}

function highlightFeature(e) {
	    var layer = e.target;

	    layer.setStyle({
		            weight: 5,
		            color: '#665',
		            dashArray: '',
		            fillOpacity: 0.7
		        });

	    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
		            layer.bringToFront();
		        }
	info.update(layer.feature.properties);
			}
function resetHighlight(e) {
	    geojson.resetStyle(e.target);
	info.update(layer.feature.properties);
}
	function zoomToFeature(e) {
				map.fitBounds(e.target.getBounds());
			}


function onEachFeature(feature, layer) { 
      if (feature.properties.countyname == "Boone") {
      var size = [25, 40]
      }
      else {
      var size =  [35,20]}
	
	var label = L.marker(layer.getBounds().getCenter(), {
	      icon: L.divIcon({
                      iconSize: size,
	              className: 'label',
		      html: "<span style='font-size:8px;'>" + feature.properties.countyname + "</span>",
				            })
					        }).addTo(map);
      }
	/*
				  	  permanent: true,
				          direction: "center",
					  html: feature.properties.countyname,
					  iconSize: [100, 40]
					})
			}.addTo(map))kkk
		  }
}
	    //layer.on({
		            //mouseover: highlightFeature,
		            //mouseout: resetHighlight,
		            //click: zoomToFeature
		        //});
//*/

async function load_counties() {
  const pathArray = window.location.pathname.split('/')
  const slug = pathArray.at(-2)
  const counties_url = `/api/map/`+ slug + '/'
  const response = await fetch(counties_url)
  const json = await response.json()
  return json
}

async function render_counties() {
  const counties = await load_counties()
  geojson = L.geoJSON(counties, {
		  style: style,
		  onEachFeature: onEachFeature
	  }).addTo(map)
}

var legend = L.control({position: 'bottomright'});

legend.onAdd = function (map) {
upper_limit_sort()

    var div = L.DomUtil.create('div', 'info legend'),
		        grades = upper_limit_array,
		        labels = [];

		var from, to;

			for (var i = 0; i < grades.length; i++) {
							from = grades[i];
							to = grades[i + 1];

							labels.push(
												'<i style="background:' + getColorLive(from + 1) + '"></i> ' +
												from + (to ? '&ndash;' + to : '+'));
						}

	div.innerHTML = labels.join('<br>');
     return div;
}

legend.addTo(map);

L.Control.Watermark = L.Control.extend({
	    onAdd: function(map) {
		            var img = L.DomUtil.create('img');

		            img.src = 'static/images/chamberlogo.jpg';
		            img.style.width = '200px';

		            return img;
		        },

	    onRemove: function(map) {
		            // Nothing to do here
		         }
		         });
		    
		       L.control.watermark = function(opts) {
		             return new L.Control.Watermark(opts);
		             }
		           L.control.watermark({ position: 'bottomleft' }).addTo(map);
map.whenReady(render_counties)

