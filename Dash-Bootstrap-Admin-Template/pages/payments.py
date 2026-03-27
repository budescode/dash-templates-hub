from dash import register_page, dcc, html
import dash_bootstrap_components as dbc
from config.helpers import loadDataSet
import plotly.express as px

register_page(
    __name__,
    path='/payments',
    name='Payments'
)

payments_df = loadDataSet("order_payments")
type_counts = payments_df["payment_type"].value_counts().reset_index()
type_counts.columns = ["Method", "Count"]
total_payments_df = len(payments_df)
total_payments_value = payments_df["payment_value"].sum()

layout = dbc.Container([

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
                                                    html.H6("Total Payments", className="text-muted"),
                                                    html.H3(f"{total_payments_df:,}", className="text-dark"),
                                                    html.Span("All time payment", className="text-success"),
                                                    ]
                                                ),
                                                html.I(className="bi bi-cash fs-1 text-primary"),
                                            ],
                                            className="d-flex justify-content-between align-items-center",
                                            )
                                            ]
                                        )
                                    ),
                                    md=6
                                ),
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                            html.Div([
                                                html.Div(
                                                    [
                                                    html.H6("Total Payment Value", className="text-muted"),
                                                    html.H3(f"${total_payments_value:,.2f}", className="text-dark"),
                                                    html.Span("All time payment", className="text-success"),
                                                    ]
                                                ),
                                                html.I(className="bi bi-bank2 fs-1 text-primary"),
                                            ],
                                            className="d-flex justify-content-between align-items-center",
                                            )
                                            ]
                                        )
                                    ),
                                    md=6
                                ),
                            ], className="mt-4"),]),
    dbc.Row(
        children=[
            dbc.Col(
                md=8,
                children=[
                    dbc.Card(
                        dbc.CardBody(
                            children=[
                                dcc.Graph(
                                    figure=px.histogram(
                                    payments_df,
                                    x="payment_installments",
                                    title="Installment Distribution (How many months?)",
                                    nbins=24, # Adjust based on max installments (usually 12 or 24)
                                    text_auto=True # Shows the count on top of bars
                                )
                                )
                            ]
                        )
                    )
                ]
            ),
            dbc.Col(md=4, children=[
                dbc.Card(
                    dbc.CardBody(
                        children=[
                            dcc.Graph(
                                figure=px.pie(
                                    type_counts,
                                    names="Method",
                                    values="Count",
                                    hole=0.4, # Makes it a donut
                                    title="Payment Method Preference",
                                    color_discrete_sequence=px.colors.qualitative.Pastel # Soft colors
                                )
                            )
                        ]
                        
                    )
                )
            ])
        ], className="mt-4"
    ),
    dbc.Row(
        children=[
            dbc.Col(
                md=12,
                children=[
                    dcc.Graph(
                        figure=px.box(
                            payments_df,
                            x="payment_type",
                            y="payment_value",
                            title="Transaction Value by Payment Method",
                            points=False # Hide individual dots if dataset is huge to keep it fast
                        )
                                            )
                ]
            )
        ],className='mt-4'
    )
], fluid=True)
