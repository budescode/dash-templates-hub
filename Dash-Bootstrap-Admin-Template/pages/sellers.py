from dash import register_page, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from config.helpers import loadDataSet
import plotly.express as px
# --- 1. Register with a Unique Path ---
register_page(
    __name__,
    path='/sellers', # Set a unique path
    name='Sellers'
)
sellers_df = loadDataSet("sellers")

geo_location_df = loadDataSet("geo_location")

#remove the duplicates geolocation_zip_code_prefix. and take just the first one, then resets the index.
geo_clean = geo_location_df.groupby('geolocation_zip_code_prefix').first().reset_index() 
geo_clean = geo_clean[[
    'geolocation_zip_code_prefix', 
    'geolocation_lat', 
    'geolocation_lng', 
    'geolocation_city', 
    'geolocation_state'
]]

sellers_with_geo = sellers_df.merge(
    geo_clean, 
    how='left', 
    left_on='seller_zip_code_prefix', 
    right_on='geolocation_zip_code_prefix'
)

sellers_df = sellers_with_geo
seller_state = sellers_df["seller_state"]
seller_city = sellers_df["seller_city"]
total_seller_state = len(seller_state.unique())
total_seller_city = len(seller_city.unique())


total_sellers = len(sellers_df)
seller_counts = sellers_df["seller_state"].value_counts().reset_index()
seller_counts.columns = ["State", "Seller Count"]

state_options = sorted(sellers_df["seller_state"].unique())
city_options = sorted(sellers_df["seller_city"].unique())

# --- 2. Define the Page Layout ---
# This is the content specific to this second page.
layout = dbc.Container([

        html.Br(),
    
    # --- NEW: Filter Section ---
    dbc.Row([
        dbc.Col(
            dcc.Dropdown(
                multi=True,
                id="state-filter",
                options=state_options,
                placeholder="Select State...",
                clearable=True,
                className="mb-2"
            ), md=3
        ),
        dbc.Col(
            dcc.Dropdown(
                multi=True,
                id="city-filter",
                options=city_options,
                placeholder="Select City...",
                clearable=True,
                className="mb-2"
            ), md=3
        ),
    ], className="mb-4"),


    dbc.Row(
        
        children=[
        dbc.Col(md=4, children=[
            dbc.Card(
                    dbc.CardBody(
                        [
                        html.Div([
                            html.Div(
                                [
                                html.H6("Total Sellers", className="text-muted"),
                                html.H3(id="total-sellers", className="text-dark"),
                                html.Span("All time sellers", className="text-success"),
                                ]
                            ),
                            html.I(className="bi bi-people-fill fs-1 text-primary"),
                        ],
                        className="d-flex justify-content-between align-items-center",
                        )
                        ]
                    )
            ),
        ]),
        dbc.Col(md=4, children=[
            dbc.Card(
                    dbc.CardBody(
                        [
                        html.Div([
                            html.Div(
                                [
                                html.H6("Total States", className="text-muted"),
                                html.H3(id="total-states", className="text-dark"),
                                html.Span("All time sellers", className="text-success"),
                                ]
                            ),
                            html.I(className="bi bi-globe fs-1 text-primary"),
                        ],
                        className="d-flex justify-content-between align-items-center",
                        )
                        ]
                    )
            ),
        ]),
        dbc.Col(md=4, children=[
            dbc.Card(
                    dbc.CardBody(
                        [
                        html.Div([
                            html.Div(
                                [
                                html.H6("Total Cities", className="text-muted"),
                                html.H3(id="total-cities", className="text-dark"),
                                html.Span("All time sellers", className="text-success"),
                                ]
                            ),
                            html.I(className="bi bi-globe2 fs-1 text-primary"),
                        ],
                        className="d-flex justify-content-between align-items-center",
                        )
                        ]
                    )
            ),
        ]),
        
        ], className="mt-4"),


    dbc.Row(
        dbc.Col(
            md=12, 
            children=[
                dcc.Graph(
                    id='sellers-graph'
                )
            ]
        ), className="mt-4"
    ),

    dbc.Row(
        children=[
            dbc.Col(
                md=12,
                children=[
                    dbc.Card(
                        dbc.CardBody(
                            children = [
                                dcc.Graph(
                                    id='sellers-bar'
                                )
                            ]
                        )
                    )
                   
                ], className="mt-4"
            )
        ]
    )
  
], fluid=True)

@callback(
    Output("total-sellers", "children"),
    Output("total-states", "children"),
    Output("total-cities", "children"),
    Output("sellers-graph", "figure"),
    Output("sellers-bar", "figure"),
    Input("state-filter", "value"),
    Input("city-filter", "value"),
)
def update_dashboard(state, city):

    df = sellers_df.copy()
    if state:
        df = df[ df["seller_state"].isin(state)]
    if city:
        df = df[df["seller_city"].isin(city)]

    seller_state = df["seller_state"]
    seller_city = df["seller_city"]

    total_seller_state = len(seller_state.unique())
    total_seller_city = len(seller_city.unique())


    total_sellers = len(df)
    seller_counts = df["seller_state"].value_counts().reset_index()
    seller_counts.columns = ["State", "Seller Count"]

    figure_scatter=px.scatter_mapbox(
    df,
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
    
    figure_bar=px.bar(
        seller_counts,
        x="State",
        y="Seller Count",
        title="Distribution of Sellers by State",
        color="Seller Count", # Makes higher bars darker
        color_continuous_scale=[(0, "#e0e7ff"), (1, "#6366f1")]
    )

    return total_sellers, total_seller_state, total_seller_city, figure_scatter, figure_bar #








   