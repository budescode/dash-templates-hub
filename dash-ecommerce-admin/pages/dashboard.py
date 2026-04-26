# File: pages/dashboard.py (The main view)

from dash import html, register_page, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from config.helpers import loadDataSet

# This gets the directory where your current script (app.py or page.py) is located

customers_df = loadDataSet("customers")

#remove the duplicates geolocation_zip_code_prefix. and take just the first one, then resets the index.
geo_location_df = loadDataSet("geo_location")
geo_clean = geo_location_df.groupby('geolocation_zip_code_prefix').first().reset_index() 
geo_clean = geo_clean[[
    'geolocation_zip_code_prefix', 
    'geolocation_lat', 
    'geolocation_lng', 
    'geolocation_city', 
    'geolocation_state'
]]

customers_merge_df = customers_df.merge(
    geo_clean,
    how="left",
    left_on="customer_zip_code_prefix",
    right_on="geolocation_zip_code_prefix"

)


customers_df = customers_merge_df
total_customers = len(customers_df)
orders_df = loadDataSet("orders")
total_orders = len(orders_df)
sellers_df = loadDataSet("sellers")
total_sellers = len(sellers_df)
order_payments_df = loadDataSet("order_payments")
total_order_payments= len(order_payments_df)




def _customer_map():
    map_df = customers_df.dropna(subset=["geolocation_lat", "geolocation_lng", "geolocation_state"])
    colors = px.colors.qualitative.Plotly
    states = map_df["geolocation_state"].unique()
    fig = go.Figure()
    for i, state in enumerate(states):
        df = map_df[map_df["geolocation_state"] == state]
        fig.add_trace(go.Scattermapbox(
            lat=df["geolocation_lat"],
            lon=df["geolocation_lng"],
            mode="markers",
            marker=dict(size=5, color=colors[i % len(colors)]),
            name=state,
            hovertext=df["geolocation_city"],
            hoverinfo="text+name",
        ))
    fig.update_layout(
        mapbox_style="open-street-map",
        mapbox_zoom=3,
        mapbox_center={"lat": -14.2, "lon": -51.9},
        margin={"r": 0, "t": 40, "l": 0, "b": 0},
        height=700,
        title="Customers Location",
    )
    return fig


# --- 1. Register as the Root Path ---
register_page(
    __name__,
    path='/',           # Sets this as the default home page
    name='Dashboard'
)

layout =        dbc.Container([

                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Dashboard", className="text-dark"),
                                    html.P("Welcome back! Here's what's happening.!"),
                                ]
                            ),
                  
                            
                            # Add more content here as needed
                        ],
                       
                        className="mt-4"
                    ),

                    # metrics
                    html.Div([
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                            html.Div([
                                                html.Div(
                                                    [
                                                    html.H6("Total Users", className="text-muted"),
                                                    html.H3(f"{total_customers:,}", className="text-dark"),
                                                    html.Span("All time users", className="text-success"),
                                                    ]
                                                ),
                                                html.I(className="bi bi-people-fill fs-1 text-primary"),
                                            ],
                                            className="d-flex justify-content-between align-items-center",
                                            )
                                            ]
                                        )
                                    ),
                                    md=3
                                ),
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                            html.Div([
                                                html.Div(
                                                    [
                                                    html.H6("Total Orders", className="text-muted"),
                                                    html.H3(f"{total_orders:,}", className="text-dark"),
                                                    html.Span("All time orders", className="text-success"),
                                                    ]
                                                ),
                                                html.I(className="bi bi-gift fs-1 text-primary"),
                                            ],
                                            className="d-flex justify-content-between align-items-center",
                                            )
                                            ]
                                        )
                                    ),
                                    md=3
                                ),
                                dbc.Col(
                                    dbc.Card(
                                       dbc.CardBody(
                                            [
                                            html.Div([
                                                html.Div(
                                                    [
                                                    html.H6("Total Sellers", className="text-muted"),
                                                    html.H3(f"{total_sellers:,}", className="text-dark"),
                                                    html.Span("All time sellers", className="text-success"),
                                                    ]
                                                ),
                                                html.I(className="bi bi-shop fs-1 text-primary"),
                                            ],
                                            className="d-flex justify-content-between align-items-center",
                                            )
                                            ]
                                        )
                                    ),
                                    md=3
                                ),
                                dbc.Col(
                                    dbc.Card(
                                         dbc.CardBody(
                                            [
                                            html.Div([
                                                html.Div(
                                                    [
                                                    html.H6("Total Payment", className="text-muted"),
                                                    html.H3(f"{total_order_payments:,}", className="text-dark"),
                                                    html.Span("All time sellers", className="text-success"),
                                                    ]
                                                ),
                                                html.I(className="bi bi-bank fs-1 text-primary"),
                                            ],
                                            className="d-flex justify-content-between align-items-center",
                                            )
                                            ]
                                        )
                                    ),
                                    md=3
                                ),
                            ],
                            className="g-4"
                        )
                    ]),
                    html.Br(),
                    #row for revenue overview and recent activity      
                    dbc.Row([
                        dbc.Col(md=12, children=[
                               
                    dcc.Graph(
                    figure=_customer_map()
                    )
                        ]),
                    
                    ]),

                    html.Br(),   
            

                ], className="px-0", fluid=True)

