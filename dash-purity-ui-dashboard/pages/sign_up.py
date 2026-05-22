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
    className="auth-shell signup-shell",
    children=[
        html.Div(
            className="signup-hero",
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
                    className="signup-hero-text",
                    children=[
                        html.H2("Welcome!"),
                        html.P("Use these awesome forms to login or create a new account in your project for free."),
                    ],
                ),
            ],
        ),
        html.Div(
            className="signup-body",
            children=[
                html.Div(
                    className="auth-card",
                    children=[
                        html.Div("Register with", style={"fontWeight": "700", "textAlign": "center", "marginBottom": "14px"}),
                        html.Div(
                            style={"display": "flex", "gap": "10px", "justifyContent": "center", "marginBottom": "14px"},
                            children=[
                                html.Button(html.I(className="fa-brands fa-facebook"), className="icon-button"),
                                html.Button(html.I(className="fa-brands fa-apple"), className="icon-button"),
                                html.Button(html.I(className="fa-brands fa-google"), className="icon-button"),
                            ],
                        ),
                        html.Div("or", className="stat-label", style={"textAlign": "center", "marginBottom": "12px"}),
                        html.Div(className="auth-field", children=[
                            html.Label("Name", className="auth-label"),
                            dcc.Input(type="text", placeholder="Your full name", className="auth-input"),
                        ]),
                        html.Div(className="auth-field", children=[
                            html.Label("Email", className="auth-label"),
                            dcc.Input(type="email", placeholder="Your email address", className="auth-input"),
                        ]),
                        html.Div(className="auth-field", children=[
                            html.Label("Password", className="auth-label"),
                            dcc.Input(type="password", placeholder="Your password", className="auth-input"),
                        ]),
                        dbc.Switch(
                            id="signup-remember",
                            label="Remember me",
                            value=True,
                            className="purity-switch",
                            style={"margin": "16px 0"},
                        ),
                        html.Button("SIGN UP", className="btn-mint", style={"width": "100%"}),
                        html.Div(
                            style={"marginTop": "14px", "textAlign": "center"},
                            children=[
                                html.Span("Already have an account? ", className="stat-label"),
                                dcc.Link("Sign in", href="/sign-in", style={"color": "#4fd1c5", "fontWeight": "600"}),
                            ],
                        ),
                    ],
                )
            ],
        ),
    ],
)
