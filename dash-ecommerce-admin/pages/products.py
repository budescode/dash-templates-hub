# File: pages/index.py (The second page)

from dash import html, register_page, dcc
import dash_bootstrap_components as dbc
import dash_ag_grid as dag 
import plotly.express as px
from config.helpers import loadDataSet

# --- 1. Register with a Unique Path ---
register_page(
    __name__,
    path='/products', # Set a unique path
    name='Products'
)

products_df = loadDataSet("products")
products_categories = products_df["product_category_name"].value_counts().reset_index()
  # Top 10 categories
products_categories.columns = ["Product Category", "count"]
total_products = len(products_df)
total_categories = len(products_df["product_category_name"].unique())
total_quantity = int(products_df["product_photos_qty"].sum())

# --- 2. Define the Page Layout ---
# This is the content specific to this second page.
layout = dbc.Container([
        dbc.Row(
        
        children=[
        dbc.Col(md=4, children=[
            dbc.Card(
                    dbc.CardBody(
                        [
                        html.Div([
                            html.Div(
                                [
                                html.H6("Total Products", className="text-muted"),
                                html.H3(f"{total_products:,}", className="text-dark"),
                                html.Span("All time products", className="text-success"),
                                ]
                            ),
                            html.I(className="bi bi-file fs-1 text-primary"),
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
                                html.H6("Total Categories", className="text-muted"),
                                html.H3(f"{total_categories:,}", className="text-dark"),
                                html.Span("All categories", className="text-success"),
                                ]
                            ),
                            html.I(className="bi bi-list fs-1 text-success"),
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
                                html.H6("Total Quantity", className="text-muted"),
                                html.H3(f"{total_quantity:,}", className="text-dark"),
                                html.Span("Total Products", className="text-success"),
                                ]
                            ),
                            html.I(className="bi bi-handbag fs-1 text-warning"),
                        ],
                        className="d-flex justify-content-between align-items-center",
                        )
                        ]
                    )
            ),
        ]),
     
        ],
        className="mt-4"
    ), # end row

    dbc.Row(
        children=[
            dbc.Col(
                md=12,
                children=[
                    dbc.Card(
                        dbc.CardBody(
                            children = [
                                html.H5("Products", className="card-title mb-3"),
                                dag.AgGrid( 
                                    columnDefs = list({"headerName":x, "field":x, "sortable":True, "filter":True} for x in products_df.columns),
                                    rowData = products_df.to_dict("records"),
                                    style={"height":"500px"}
                                    )
                            ]
                        )
                    )
                    
                ]

            )
        ], class_name="mt-4 mb-4"
    )
  
], fluid=True)