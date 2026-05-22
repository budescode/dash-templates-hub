from dash import html
import dash_bootstrap_components as dbc


layout = dbc.Container(
    fluid=True,
    children=[
        html.Div(
            className="wave-banner",
            children=[
                html.Div("Pages / Profile", style={"fontSize": "12px", "opacity": "0.8"}),
                html.H2("Profile"),
            ],
        ),
        html.Div(
            className="card-surface profile-card",
            children=[
                html.Div(
                    className="profile-chip",
                    children=[
                        html.Img(src="https://i.pravatar.cc/80?img=32", className="avatar"),
                        html.Div(
                            children=[
                                html.Div("Esthera Jackson", style={"fontWeight": "700"}),
                                html.Div("esthera@simmmple.com", className="stat-label"),
                            ]
                        ),
                    ],
                ),
                html.Div(
                    style={"display": "flex", "gap": "10px"},
                    children=[
                        html.Button("Overview", className="btn btn-light btn-sm"),
                        html.Button("Teams", className="btn btn-light btn-sm"),
                        html.Button("Projects", className="btn btn-light btn-sm"),
                    ],
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
                            html.Div("Platform Settings", className="chart-title"),
                            html.Div("ACCOUNT", className="stat-label"),
                            html.Div(
                                className="switch-group",
                                children=[
                                    html.Div(
                                        className="switch-row",
                                        children=[
                                            dbc.Switch(id="acct-follow", value=True, className="purity-switch"),
                                            html.Span("Email me when someone follows me", className="stat-label"),
                                        ],
                                    ),
                                    html.Div(
                                        className="switch-row",
                                        children=[
                                            dbc.Switch(id="acct-answers", value=False, className="purity-switch"),
                                            html.Span("Email me when someone answers", className="stat-label"),
                                        ],
                                    ),
                                    html.Div(
                                        className="switch-row",
                                        children=[
                                            dbc.Switch(id="acct-mentions", value=True, className="purity-switch"),
                                            html.Span("Email me when someone mentions me", className="stat-label"),
                                        ],
                                    ),
                                ],
                            ),
                            html.Div("APPLICATION", className="stat-label", style={"marginTop": "16px"}),
                            html.Div(
                                className="switch-group",
                                children=[
                                    html.Div(
                                        className="switch-row",
                                        children=[
                                            dbc.Switch(id="app-launches", value=False, className="purity-switch"),
                                            html.Span("New launches and projects", className="stat-label"),
                                        ],
                                    ),
                                    html.Div(
                                        className="switch-row",
                                        children=[
                                            dbc.Switch(id="app-updates", value=True, className="purity-switch"),
                                            html.Span("Monthly product updates", className="stat-label"),
                                        ],
                                    ),
                                    html.Div(
                                        className="switch-row",
                                        children=[
                                            dbc.Switch(id="app-newsletter", value=True, className="purity-switch"),
                                            html.Span("Subscribe to newsletter", className="stat-label"),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                    xs=12,
                    md=4,
                ),
                dbc.Col(
                    html.Div(
                        className="card-surface chart-card",
                        children=[
                            html.Div("Profile Information", className="chart-title"),
                            html.P(
                                "Hi, I'm Alec Thompson, Decisions: If you can't decide, the answer is no."
                                " If two equally difficult paths, choose the one more painful in the short term.",
                                style={"fontSize": "12px", "color": "#718096", "lineHeight": "1.6"},
                            ),
                            html.Div("Full Name: Alec M. Thompson", className="stat-label"),
                            html.Div("Mobile: (44) 123 1234 123", className="stat-label"),
                            html.Div("Email: alec@simmmple.com", className="stat-label"),
                            html.Div("Location: United States", className="stat-label"),
                        ],
                    ),
                    xs=12,
                    md=4,
                ),
                dbc.Col(
                    html.Div(
                        className="card-surface chart-card",
                        children=[
                            html.Div("Conversations", className="chart-title"),
                            html.Div(
                                style={"display": "grid", "gap": "12px"},
                                children=[
                                    html.Div(
                                        style={"display": "flex", "gap": "10px", "alignItems": "center"},
                                        children=[
                                            html.Img(src="https://i.pravatar.cc/60?img=48", className="avatar"),
                                            html.Div(
                                                children=[
                                                    html.Div("Esthera Jackson", style={"fontWeight": "600"}),
                                                    html.Div("Hi! I need more information...", className="stat-label"),
                                                ]
                                            ),
                                            html.Span("REPLY", className="stat-label", style={"marginLeft": "auto"}),
                                        ],
                                    ),
                                    html.Div(
                                        style={"display": "flex", "gap": "10px", "alignItems": "center"},
                                        children=[
                                            html.Img(src="https://i.pravatar.cc/60?img=18", className="avatar"),
                                            html.Div(
                                                children=[
                                                    html.Div("Esthera Jackson", style={"fontWeight": "600"}),
                                                    html.Div("Awesome work, can you change...", className="stat-label"),
                                                ]
                                            ),
                                            html.Span("REPLY", className="stat-label", style={"marginLeft": "auto"}),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                    xs=12,
                    md=4,
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
                            dbc.Row(
                                className="g-3",
                                children=[
                                    dbc.Col(
                                        html.Div(
                                            className="card-surface",
                                            style={"padding": "10px"},
                                            children=[
                                                html.Img(
                                                    src="https://images.unsplash.com/photo-1505691938895-1758d7feb511?auto=format&fit=crop&w=400&q=80",
                                                    style={"width": "100%", "borderRadius": "12px", "height": "120px", "objectFit": "cover"},
                                                ),
                                                html.Div("Modern", style={"fontWeight": "600", "marginTop": "8px"}),
                                                html.Div("As Uber works through a huge amount of internal management turmoil.", className="stat-label"),
                                                html.Button("VIEW ALL", className="btn btn-outline-info btn-sm", style={"marginTop": "8px"}),
                                            ],
                                        ),
                                        xs=12,
                                        md=3,
                                    ),
                                    dbc.Col(
                                        html.Div(
                                            className="card-surface",
                                            style={"padding": "10px"},
                                            children=[
                                                html.Img(
                                                    src="https://images.unsplash.com/photo-1493809842364-78817add7ffb?auto=format&fit=crop&w=800&q=80",
                                                    style={"width": "100%", "borderRadius": "12px", "height": "120px", "objectFit": "cover"},
                                                ),
                                                html.Div("Scandinavian", style={"fontWeight": "600", "marginTop": "8px"}),
                                                html.Div("Music is something that every person has his or her own opinion about.", className="stat-label"),
                                                html.Button("VIEW ALL", className="btn btn-outline-info btn-sm", style={"marginTop": "8px"}),
                                            ],
                                        ),
                                        xs=12,
                                        md=3,
                                    ),
                                    dbc.Col(
                                        html.Div(
                                            className="card-surface",
                                            style={"padding": "10px"},
                                            children=[
                                                html.Img(
                                                    src="https://images.unsplash.com/photo-1502005097973-6a7082348e28?auto=format&fit=crop&w=800&q=80",
                                                    style={"width": "100%", "borderRadius": "12px", "height": "120px", "objectFit": "cover"},
                                                ),
                                                html.Div("Minimalist", style={"fontWeight": "600", "marginTop": "8px"}),
                                                html.Div("Different people have different taste, and various types of music.", className="stat-label"),
                                                html.Button("VIEW ALL", className="btn btn-outline-info btn-sm", style={"marginTop": "8px"}),
                                            ],
                                        ),
                                        xs=12,
                                        md=3,
                                    ),
                                    dbc.Col(
                                        html.Div(
                                            className="card-surface",
                                            style={"padding": "10px", "display": "grid", "placeItems": "center", "height": "100%"},
                                            children=[
                                                html.Div("Create a New Project", className="stat-label"),
                                                html.I(className="fa-solid fa-plus"),
                                            ],
                                        ),
                                        xs=12,
                                        md=3,
                                    ),
                                ],
                            ),
                        ],
                    ),
                    xs=12,
                ),
            ],
        ),
    ],
)
