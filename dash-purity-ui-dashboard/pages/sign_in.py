from dash import dcc, html
import dash_bootstrap_components as dbc

_NAV_LINKS = [
    ("PURITY UI DASHBOARD", "/"),
    ("DASHBOARD", "/"),
    ("PROFILE", "/profile"),
    ("SIGN UP", "/sign-up"),
    ("SIGN IN", "/sign-in"),
]

layout = html.Div(
    className="auth-shell",
    children=[
        html.Div(
            className="auth-nav",
            children=[
                html.Div(
                    className="pill",
                    children=[dcc.Link(label, href=href, className="pill-link") for label, href in _NAV_LINKS],
                )
            ],
        ),
        html.Div(
            className="auth-main",
            children=[
                html.Div(
                    className="auth-form",
                    children=[
                        html.Div(
                            style={"width": "100%", "maxWidth": "360px"},
                            children=[
                                html.H2("Welcome Back", style={"color": "#4fd1c5"}),
                                html.P("Enter your email and password to sign in", className="stat-label"),
                                html.Div(className="auth-field", children=[
                                    html.Label("Email", className="auth-label"),
                                    dcc.Input(type="email", placeholder="Your email address", className="auth-input"),
                                ]),
                                html.Div(className="auth-field", children=[
                                    html.Label("Password", className="auth-label"),
                                    dcc.Input(type="password", placeholder="Your password", className="auth-input"),
                                ]),
                                dbc.Switch(
                                    id="signin-remember",
                                    label="Remember me",
                                    value=True,
                                    className="purity-switch",
                                    style={"margin": "16px 0"},
                                ),
                                html.Button("SIGN IN", className="btn-mint", style={"width": "100%"}),
                                html.Div(
                                    style={"marginTop": "14px", "textAlign": "center"},
                                    children=[
                                        html.Span("Don't have an account? ", className="stat-label"),
                                        dcc.Link("Sign up", href="/sign-up", style={"color": "#4fd1c5", "fontWeight": "600"}),
                                    ],
                                ),
                            ],
                        )
                    ],
                ),
                html.Div(
                    className="auth-panel",
                    children=[
                        html.Div(
                            style={"position": "relative", "zIndex": 1, "textAlign": "center"},
                            children=[
                                html.Div(
                                    style={"display": "flex", "alignItems": "center", "gap": "12px", "justifyContent": "center"},
                                    children=[
                                        html.Div(
                                            style={"width": "58px", "height": "58px", "borderRadius": "20px", "background": "rgba(255,255,255,0.2)", "display": "grid", "placeItems": "center"},
                                            children=html.I(className="fa-solid fa-bolt", style={"fontSize": "26px"}),
                                        ),
                                        html.Div("chakra", style={"fontSize": "32px", "fontWeight": "700"}),
                                    ],
                                )
                            ],
                        )
                    ],
                ),
            ],
        ),
    ],
)
