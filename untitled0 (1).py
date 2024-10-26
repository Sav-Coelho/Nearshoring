import pandas as pd

base = pd.read_excel('larrain.xlsx')
base

import folium as fol

map = fol.Map([15.00,-86.30],tiles="cartodbpositron",zoom_start=8)

fol.Choropleth(geo_data=geodata,data=base,columns=["País","Nota Reashoring"],key_on="properties.name",fill_color="OrRd").add_to(map)

legend_html = '''
<div style="position: fixed;
     bottom: 50px; right: 50px; width: 200px; height: auto;
     border:2px solid grey; z-index:9999; font-size:14px;
     background-color:white; opacity: 0.85; padding: 10px;">
     <b>Nota Nearshoring</b><br>
     <div style="width: 100%; height: 20px; background: linear-gradient(to right,
         #f7f4f9 0%, #f0ebeb 25%, #fee8c8 50%, #fcbba1 75%, #d7301f 100%);">
     </div>
     <div style="display: flex; justify-content: space-between; font-size: 12px;">
         <span>-2</span>
         <span>0</span>
         <span>2</span>
     </div>
</div>
'''

map.get_root().html.add_child(fol.Element(legend_html))

map.save("Nota_Nearshoring.html")
