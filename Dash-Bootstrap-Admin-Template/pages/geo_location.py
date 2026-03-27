# File: pages/index.py (The second page)

from dash import html, register_page, dcc
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
from config.helpers import loadDataSet
import plotly.express as px
# --- 1. Register with a Unique Path ---
register_page(
    __name__,
    path='/geo-location', # Set a unique path
    name='GeoLocation'
)

geo_locattion_df = loadDataSet("geo_location")

# --- 2. Define the Page Layout ---
# This is the content specific to this second page.
layout = dbc.Container([
    dbc.Row(
        dbc.Col(
            md=12, 
            children=[
                dcc.Graph(
                    figure=px.scatter_mapbox(
                        geo_locattion_df,
                        lat="geolocation_lat",
                        lon="geolocation_lng",
                        hover_name="geolocation_city",
                        hover_data=["geolocation_state"],
                        color="geolocation_state", # Color dots by State
                        zoom=3, 
                        height=700,
                        mapbox_style="open-street-map", # Detailed street view
                        title="Geo Location"
                    )
                )
            ]
        ), className="mt-4"
    )
  
], fluid=True)