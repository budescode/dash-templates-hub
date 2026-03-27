# File: pages/index.py (The second page)

from dash import html, register_page, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from config.helpers import loadDataSet
import dash_ag_grid as dag 
import plotly.express as px
import pandas as pd
# --- 1. Register with a Unique Path ---
register_page(
    __name__,
    path='/orders', # Set a unique path
    name='Orders'
)

orders_df = loadDataSet("orders")
orders_df["order_purchase_timestamp"] = pd.to_datetime(orders_df["order_purchase_timestamp"])
total_orders = len(orders_df)
total_processing_orders = len(orders_df[ orders_df["order_status"] == "processing"])
total_delivered_orders = len(orders_df[ orders_df["order_status"] == "delivered"])
total_canceled_orders = len(orders_df[ orders_df["order_status"] == "canceled"])
order_status = orders_df["order_status"].unique()

min_date = orders_df["order_purchase_timestamp"].min()
max_date = orders_df["order_purchase_timestamp"].max()

print("date datatypoe is ", orders_df["order_purchase_timestamp"].dtype)
# . Define the Page Layout ---
layout = dbc.Container([


    dbc.Row(
        
        children=[
        dbc.Col(md=3, children=[
            dbc.Card(
                    dbc.CardBody(
                        [
                        html.Div([
                            html.Div(
                                [
                                html.H6("Total Orders", className="text-muted"),
                                html.H3(f"{total_orders:,}", className="text-dark"),
                                html.Span("Alltime orders", className="text-success"),
                                ]
                            ),
                            html.I(className="bi bi-gift fs-1 text-primary"),
                        ],
                        className="d-flex justify-content-between align-items-center",
                        )
                        ]
                    )
            ),
        ]),
        dbc.Col(md=3, children=[
            dbc.Card(
                    dbc.CardBody(
                        [
                        html.Div([
                            html.Div(
                                [
                                html.H6("Processing Orders", className="text-muted"),
                                html.H3(f"{total_processing_orders:,}", className="text-dark"),
                                html.Span("Total Processing Orders.", className="text-success"),
                                ]
                            ),
                            html.I(className="bi bi-gift fs-1 text-success"),
                        ],
                        className="d-flex justify-content-between align-items-center",
                        )
                        ]
                    )
            ),
        ]),
        dbc.Col(md=3, children=[
            dbc.Card(
                    dbc.CardBody(
                        [
                        html.Div([
                            html.Div(
                                [
                                html.H6("Delivered Orders", className="text-muted"),
                                html.H3(f"{total_delivered_orders:,}", className="text-dark"),
                                html.Span("Total Delivered Orders", className="text-success"),
                                ]
                            ),
                            html.I(className="bi bi-gift fs-1 text-primary"),
                        ],
                        className="d-flex justify-content-between align-items-center",
                        )
                        ]
                    )
            ),
        ]),

        dbc.Col(md=3, children=[
            dbc.Card(
                    dbc.CardBody(
                        [
                        html.Div([
                            html.Div(
                                [
                                html.H6("Cancelled Orders", className="text-muted"),
                                html.H3(f"{total_canceled_orders:,}", className="text-dark"),
                                html.Span("Total Cancelled Orders", className="text-success"),
                                ]
                            ),
                            html.I(className="bi bi-gift fs-1 text-warning"),
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
    # dbc.Row(
    #    children = [ dbc.Col(
    #        md=12,
    #        children=[
    #            dcc.Graph(
    #                figure=px.scatter(
    #                     orders_df,
    #                     x="order_estimated_delivery_date",
    #                     y="order_delivered_customer_date",
    #                     color="order_status",
    #                     title="Estimated Delivery vs. Actual Delivery",
    #                     labels={
    #                         "order_estimated_delivery_date": "Promised Date",
    #                         "order_delivered_customer_date": "Actual Arrival Date"
    #                     }
    #                 ), style={"height":"600px"}
    #            )
    #        ]
    #    )],
    #    class_name="mt-4"
    # ),
    dbc.Row([
        dbc.Col(
            dcc.Dropdown(
                multi=True,
                id="order-status",
                options=order_status,
                placeholder="Select Status...",
                clearable=True,
                className="mb-2"
            ), md=3
        ),
        dbc.Col(
            dcc.DatePickerRange(
                id='order-date-range',
                min_date_allowed=min_date,
                max_date_allowed=max_date,
                start_date=min_date,  # Default start
                end_date=max_date,    # Default end
                display_format='YYYY-MM-DD',
                className="mb-2"
            ), md=4
        ),
      
    ], className="mt-4"),
    dbc.Row(
        children=[
            dbc.Col(
                md=12, children=[
                    dbc.Card(
                        dbc.CardBody(
                            children = [
                                html.H6( id="table-title", className="text-black card-title"),
                                    dag.AgGrid(
                                        id="ag-table",
                                        columnDefs = list({"headerName":x, "field":x} for x in orders_df.columns),
                                                    
                                                    style={"height":"500px"}
                                    )
                            ]
                        )
                    )
                    
                ]
            )
        ],
        class_name="mt-4"
    )
  
], fluid=True)

@callback(
Output("table-title", "children"),
Output("ag-table", "rowData"),
Input("order-status", "value"),
Input("order-date-range", "start_date"),
Input("order-date-range", "end_date"),
)

def update_dashboard(status, start_date, end_date):
    print(f"date rangee {start_date}.... {end_date}")
    new_order = orders_df.copy()
    total_orders = new_order
    if status:
        total_orders = new_order[ new_order["order_status"].isin(status)]
    
    
    if start_date and end_date:
        date_filters = (total_orders['order_purchase_timestamp'] >= start_date) & (total_orders['order_purchase_timestamp'] <= end_date)
        total_orders = total_orders[date_filters]

    rowData = total_orders.to_dict("records")
    return f"Order Records ({len(total_orders):,})", rowData
