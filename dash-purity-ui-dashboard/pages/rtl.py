from dash import html
import dash_bootstrap_components as dbc


layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row(
            className="g-3",
            children=[
                dbc.Col(
                    html.Div(
                        className="card-surface chart-card",
                        children=[
                            html.Div("RTL", className="chart-title"),
                            html.Div("This page is a placeholder for RTL content.", className="stat-label"),
                        ],
                    ),
                    xs=12,
                )
            ],
        )
    ],
)
