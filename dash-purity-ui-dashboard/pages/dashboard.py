from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go


def _bar_chart():
    fig = go.Figure(
        data=[
            go.Bar(
                x=["S", "M", "T", "W", "T", "F", "S", "S", "M", "T"],
                y=[12, 18, 10, 22, 14, 28, 16, 24, 14, 12],
                marker_color="#ffffff",
                marker_line_width=0,
                width=0.45,
            )
        ]
    )
    fig.update_layout(
        height=180,
        margin=dict(l=10, r=10, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
    )
    return fig


def _area_chart():
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
            y=[200, 180, 210, 160, 190, 170, 200, 220, 180, 190, 170, 210],
            mode="lines",
            line=dict(color="#2c7a7b", width=2),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
            y=[120, 140, 110, 160, 130, 150, 140, 170, 150, 160, 140, 150],
            mode="lines",
            line=dict(color="#81e6d9", width=3),
            fill="tozeroy",
            fillcolor="rgba(79, 209, 197, 0.2)",
        )
    )
    fig.update_layout(
        height=220,
        margin=dict(l=10, r=10, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=True, tickfont=dict(size=9, color="#a0aec0")),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        showlegend=False,
    )
    return fig


layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row(
            className="g-3",
            children=[
                dbc.Col(
                    html.Div(
                        className="card-surface stat-card",
                        children=[
                            html.Div(
                                children=[
                                    html.Div("Today's Money", className="stat-label"),
                                    html.Div("$53,000", className="stat-value"),
                                    html.Div("+55%", className="stat-delta"),
                                ]
                            ),
                            html.Div(className="stat-icon", children=html.I(className="fa-solid fa-wallet")),
                        ],
                    ),
                    xs=12,
                    md=3,
                ),
                dbc.Col(
                    html.Div(
                        className="card-surface stat-card",
                        children=[
                            html.Div(
                                children=[
                                    html.Div("Today's Users", className="stat-label"),
                                    html.Div("2,300", className="stat-value"),
                                    html.Div("+3%", className="stat-delta"),
                                ]
                            ),
                            html.Div(className="stat-icon", children=html.I(className="fa-solid fa-users")),
                        ],
                    ),
                    xs=12,
                    md=3,
                ),
                dbc.Col(
                    html.Div(
                        className="card-surface stat-card",
                        children=[
                            html.Div(
                                children=[
                                    html.Div("New Clients", className="stat-label"),
                                    html.Div("+3,052", className="stat-value"),
                                    html.Div("-14%", className="stat-delta negative"),
                                ]
                            ),
                            html.Div(className="stat-icon", children=html.I(className="fa-regular fa-user")),
                        ],
                    ),
                    xs=12,
                    md=3,
                ),
                dbc.Col(
                    html.Div(
                        className="card-surface stat-card",
                        children=[
                            html.Div(
                                children=[
                                    html.Div("Total Sales", className="stat-label"),
                                    html.Div("$173,000", className="stat-value"),
                                    html.Div("+8%", className="stat-delta"),
                                ]
                            ),
                            html.Div(className="stat-icon", children=html.I(className="fa-solid fa-cart-shopping")),
                        ],
                    ),
                    xs=12,
                    md=3,
                ),
            ],
        ),
        dbc.Row(
            className="g-3 row-gap",
            children=[
                dbc.Col(
                    html.Div(
                        className="card-surface",
                        children=[
                            dbc.Row(
                                className="g-3",
                                children=[
                                    dbc.Col(
                                        html.Div(
                                            style={"padding": "20px"},
                                            children=[
                                                html.Div("Built by developers", className="stat-label"),
                                                html.Div("Purity UI Dashboard", className="section-title"),
                                                html.P(
                                                    "From colors, cards, typography to complex elements, you will find the full documentation.",
                                                    style={"fontSize": "12px", "color": "#718096", "lineHeight": "1.6"},
                                                ),
                                                html.Div("Read more", className="stat-label"),
                                            ],
                                        ),
                                        xs=12,
                                        md=7,
                                    ),
                                    dbc.Col(
                                        html.Div(
                                            className="mint-box",
                                            children=[
                                                html.Div(
                                                    style={"display": "flex", "alignItems": "center", "gap": "10px"},
                                                    children=[
                                                        html.Div(
                                                            style={
                                                                "width": "38px",
                                                                "height": "38px",
                                                                "background": "rgba(255,255,255,0.2)",
                                                                "borderRadius": "14px",
                                                                "display": "grid",
                                                                "placeItems": "center",
                                                            },
                                                            children=html.I(className="fa-solid fa-bolt"),
                                                        ),
                                                        html.Div("chakra", style={"fontSize": "22px", "fontWeight": "700"}),
                                                    ],
                                                )
                                            ],
                                        ),
                                        xs=12,
                                        md=5,
                                    ),
                                ],
                            )
                        ],
                    ),
                    xs=12,
                    md=6,
                ),
                dbc.Col(
                    html.Div(
                        className="hero-card",
                        style={
                            "backgroundImage": "url('https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=1200&q=80')",
                        },
                        children=[
                            html.Div(className="hero-overlay"),
                            html.Div(
                                className="hero-content",
                                children=[
                                    html.Div("Work with the Rockets", style={"fontWeight": "700"}),
                                    html.Div(
                                        "Wealth creation is an evolutionarily recent positive-sum game. It is all about who takes the opportunity first.",
                                        style={"fontSize": "12px", "maxWidth": "260px", "lineHeight": "1.5"},
                                    ),
                                    html.Div("Read more", style={"fontSize": "12px", "fontWeight": "600"}),
                                ],
                            ),
                        ],
                    ),
                    xs=12,
                    md=6,
                ),
            ],
        ),
        dbc.Row(
            className="g-3 row-gap",
            children=[
                dbc.Col(
                    html.Div(
                        className="card-surface chart-card",
                        children=[
                            html.Div("Active Users", className="chart-title"),
                            html.Div("(+23) than last week", className="chart-sub"),
                            html.Div(
                                className="card-surface",
                                style={"background": "#1b1f3a", "borderRadius": "16px", "padding": "12px"},
                                children=dcc.Graph(figure=_bar_chart(), config={"displayModeBar": False}),
                            ),
                            dbc.Row(
                                className="g-3",
                                style={"marginTop": "16px"},
                                children=[
                                    dbc.Col(html.Div(children=[html.Div("Users", className="stat-label"), html.Div("32,984", className="stat-value")]), xs=6, md=3),
                                    dbc.Col(html.Div(children=[html.Div("Clicks", className="stat-label"), html.Div("2,42m", className="stat-value")]), xs=6, md=3),
                                    dbc.Col(html.Div(children=[html.Div("Sales", className="stat-label"), html.Div("2,400$", className="stat-value")]), xs=6, md=3),
                                    dbc.Col(html.Div(children=[html.Div("Items", className="stat-label"), html.Div("320", className="stat-value")]), xs=6, md=3),
                                ],
                            ),
                        ],
                    ),
                    xs=12,
                    md=6,
                ),
                dbc.Col(
                    html.Div(
                        className="card-surface chart-card",
                        children=[
                            html.Div("Sales overview", className="chart-title"),
                            html.Div("(+5) more in 2021", className="chart-sub"),
                            dcc.Graph(figure=_area_chart(), config={"displayModeBar": False}),
                        ],
                    ),
                    xs=12,
                    md=6,
                ),
            ],
        ),
        dbc.Row(
            className="g-3 row-gap",
            children=[
                dbc.Col(
                    html.Div(
                        className="card-surface chart-card",
                        children=[
                            html.Div("Projects", className="chart-title"),
                            html.Div("30 done this month", className="chart-sub"),
                            html.Table(
                                className="table",
                                children=[
                                    html.Thead(
                                        html.Tr(
                                            children=[
                                                html.Th("COMPANIES"),
                                                html.Th("MEMBERS"),
                                                html.Th("BUDGET"),
                                                html.Th("COMPLETION"),
                                            ]
                                        )
                                    ),
                                    html.Tbody(
                                        children=[
                                            html.Tr(
                                                children=[
                                                    html.Td("Chakra Soft UI Version"),
                                                    html.Td("••••"),
                                                    html.Td("$14,000"),
                                                    html.Td(html.Div([html.Div("60%", className="stat-label"), html.Div(className="progress-track", children=html.Div(className="progress-fill", style={"width": "60%"}))])),
                                                ]
                                            ),
                                            html.Tr(
                                                children=[
                                                    html.Td("Add Progress Track"),
                                                    html.Td("•••"),
                                                    html.Td("$3,000"),
                                                    html.Td(html.Div([html.Div("10%", className="stat-label"), html.Div(className="progress-track", children=html.Div(className="progress-fill", style={"width": "10%"}))])),
                                                ]
                                            ),
                                            html.Tr(
                                                children=[
                                                    html.Td("Fix Platform Errors"),
                                                    html.Td("••"),
                                                    html.Td("Not set"),
                                                    html.Td(html.Div([html.Div("100%", className="stat-label"), html.Div(className="progress-track", children=html.Div(className="progress-fill", style={"width": "100%"}))])),
                                                ]
                                            ),
                                            html.Tr(
                                                children=[
                                                    html.Td("Launch our Mobile App"),
                                                    html.Td("••••"),
                                                    html.Td("$32,000"),
                                                    html.Td(html.Div([html.Div("100%", className="stat-label"), html.Div(className="progress-track", children=html.Div(className="progress-fill", style={"width": "100%"}))])),
                                                ]
                                            ),
                                        ]
                                    ),
                                ],
                            ),
                        ],
                    ),
                    xs=12,
                    md=6,
                ),
                dbc.Col(
                    html.Div(
                        className="card-surface chart-card",
                        children=[
                            html.Div("Orders overview", className="chart-title"),
                            html.Div("+30% this month", className="chart-sub"),
                            html.Ul(
                                style={"listStyle": "none", "padding": 0, "margin": 0, "display": "grid", "gap": "12px"},
                                children=[
                                    html.Li("$2,400, Design changes", className="stat-label"),
                                    html.Li("New order #4219423", className="stat-label"),
                                    html.Li("Server Payments for April", className="stat-label"),
                                    html.Li("New card added for order #3210145", className="stat-label"),
                                    html.Li("Unlock packages for Development", className="stat-label"),
                                    html.Li("New order #9851258", className="stat-label"),
                                ],
                            ),
                        ],
                    ),
                    xs=12,
                    md=6,
                ),
            ],
        ),
    ],
)
