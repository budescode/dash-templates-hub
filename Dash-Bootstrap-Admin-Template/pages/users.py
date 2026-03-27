# File: pages/index.py (The second page)

from dash import html, register_page, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from config.helpers import loadDataSet
import dash_ag_grid as dag
import plotly.express as px
# --- 1. Register with a Unique Path --- 
register_page(
    __name__,
    path='/users', # Set a unique path
    name='Users'
)

customers_df = loadDataSet("customers")
state_options = sorted(customers_df["customer_state"].unique())
city_options = sorted(customers_df["customer_city"].unique())

# ---Define the Page Layout ---
layout = dbc.Container([
    html.Br(),

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

    #cards
    dbc.Row(
        
        children=[
        dbc.Col(md=6, children=[
            dbc.Card(
                    dbc.CardBody(
                        [
                        html.Div([
                            html.Div(
                                [
                                html.H6("Total Users", className="text-muted"),
                                html.H3(id="total-users-kpi", className="text-dark"),
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
        ]),
        dbc.Col(md=6, children=[
            dbc.Card(
                    dbc.CardBody(
                        [
                        html.Div([
                            html.Div(
                                [
                                html.H6("Active Users", className="text-muted"),
                                html.H3(id="active-users-kpi", className="text-dark"),
                                html.Span("Users active", className="text-success"),
                                ]
                            ),
                            html.I(className="bi bi-person-check-fill fs-1 text-success"),
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
            dbc.Col(md=9, children=[
                dbc.Card(
                    dbc.CardBody(
                        children=[  
                        html.Div(
                            children=[
                                html.H6("User Growth Over Time"),
                                # Placeholder for a graph or chart
                                html.Div(
                                    [
                                        dbc.RadioItems(
                                            id="date-filter-radio",
                                            className="btn-group",
                                            inputClassName="btn-check",
                                            labelClassName="btn btn-outline-secondary",
                                            labelCheckedClassName="active",
                                            options=[
                                                {"label": "7D", "value": "7D"},
                                                {"label": "30D", "value": "30D"},
                                                {"label": "90D", "value": "90D"},
                                            ],
                                            value="90D",  # Default value
                                        ),
                                    ],
                                    className="radio-group",
                                ),
                            ], className="d-flex justify-content-between align-items-center"
                        ),
                        
                        html.Div(
                            dcc.Graph(
                                id="customers-state-graph",
                                config={"displayModeBar": False}
                            )
                        )
                        ]
                    )
                )
            ]),
            dbc.Col(md=3, children=[
                dbc.Card(
                    dbc.CardBody(
                        children=[
                            html.H6("Users by State"),
                            dag.AgGrid(
                                id="users-by-state-grid",
                                columnDefs=[
                                    {"headerName": "State", "field": "Number of Customers", "sortable": True, "filter": True},
                                    {"headerName": "Count", "field": "Count", "sortable": True, "filter": True},
                                ],
                                defaultColDef={"resizable": True, "flex": 1},
                                # style={"height": "400px", "width": "100%"},
                            )
                        ]
                    ))
            ]),
        ], className="mt-4"
    ),

 
  
], fluid=True)

@callback(
    Output("total-users-kpi", "children"),
    Output("active-users-kpi", "children"),
    Output("customers-state-graph", "figure"),
    Output("users-by-state-grid", "rowData"),
    Input("state-filter", "value"),
    Input("city-filter", "value"),



)
def update_dashboard(selected_state, selected_city):
    print("state selected!", selected_state)
    dff = customers_df.copy()
    if selected_state:
        dff = dff[dff["customer_state"].isin(selected_state)]

    #Filter by City if selected
    if selected_city:
        dff = dff[dff["customer_city"].isin(selected_city)]

    total_customers = len(dff)
    # Formatted with commas
    total_customers_fmt = f"{total_customers:,}"
    customers_state_df = dff["customer_state"].value_counts().reset_index()
    customers_state_df.columns = ["Number of Customers", "Count"]

    figure = px.bar(
        customers_state_df,
        x=customers_state_df.columns[0],
        y=customers_state_df.columns[1],
        labels={"x": "Count", "y": "Number of Customers"},
        title="Customers by State"
    )

    rowData=customers_state_df.to_dict('records')

    return total_customers_fmt, total_customers_fmt, figure, rowData