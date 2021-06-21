import pandas as pd
import folium

# initialize the map and store it in a m object
folium.map = folium.Map(location=[40, -95], zoom_start=4)

# show the map
print(folium.map)

url = (
    "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
)   #API로 데이터 넣기
state_geo = "./data/us-states.json"
state_unemployment = "./data/us_unemployment.csv"
state_data = pd.read_csv(state_unemployment)


folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "Unemployment"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=.1,
    legend_name="Unemployment Rate (%)",
).add_to(folium.map)

folium.LayerControl().add_to(folium.map)

folium.map.save('./saved_data/us_unemployment.html')