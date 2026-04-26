from dash import html, register_page, dcc
import dash_bootstrap_components as dbc
from config.helpers import loadDataSet
import plotly.express as px
import plotly.graph_objects as go

register_page(
    __name__,
    path='/geo-location',
    name='GeoLocation'
)

geo_locattion_df = loadDataSet("geo_location")


def _geo_map(df):
    df = df.dropna(subset=["geolocation_lat", "geolocation_lng", "geolocation_state"])
    colors = px.colors.qualitative.Plotly
    states = df["geolocation_state"].unique()
    fig = go.Figure()
    for i, state in enumerate(states):
        sdf = df[df["geolocation_state"] == state]
        fig.add_trace(go.Scattermapbox(
            lat=sdf["geolocation_lat"],
            lon=sdf["geolocation_lng"],
            mode="markers",
            marker=dict(size=5, color=colors[i % len(colors)]),
            name=state,
            hovertext=sdf["geolocation_city"],
            hoverinfo="text+name",
        ))
    fig.update_layout(
        mapbox_style="open-street-map",
        mapbox_zoom=3,
        mapbox_center={"lat": -14.2, "lon": -51.9},
        margin={"r": 0, "t": 40, "l": 0, "b": 0},
        height=700,
        title="Geo Location",
    )
    return fig


layout = dbc.Container([
    dbc.Row(
        dbc.Col(
            md=12,
            children=[
                dcc.Graph(figure=_geo_map(geo_locattion_df))
            ]
        ), className="mt-4"
    )
], fluid=True)
