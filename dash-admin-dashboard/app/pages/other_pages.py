from dash import html
import dash_bootstrap_components as dbc


def create_blank_page():
    return html.Div(
        className="container-fluid",
        children=[
            html.H4("Blank Page", className="c-grey-900 mT-10 mB-30"),
            html.Div(className="row", children=[
                html.Div(className="col-md-12", children=html.Div(
                    className="bgc-white bd bdrs-3 p-20",
                    children=[
                        html.P("This is a blank page template. Add your content here."),
                        html.P("Use this as a starting point for new pages.", className="c-grey-600")
                    ]
                ))
            ])
        ]
    )


def create_error_404_page():
    return html.Div(
        className="pos-a t-0 l-0 bgc-white w-100 h-100 d-f fxd-r fxw-w ai-c jc-c pos-r p-30",
        style={"minHeight": "calc(100vh - 140px)"},
        children=[
            html.Div(
                className="d-f jc-c fxd-c",
                children=[
                    html.H1("404", className="mB-30 fw-900 lh-1 c-red-500", style={"fontSize": "60px"}),
                    html.H3("Oops Page Not Found", className="mB-10 fsz-lg c-grey-900 tt-c"),
                    html.P("The page you are looking for does not exist or has been moved.", className="mB-30 fsz-def c-grey-700"),
                    html.Div(html.A("Go to Home", href="/", className="btn btn-primary"))
                ]
            )
        ]
    )


def create_error_500_page():
    return html.Div(
        className="pos-a t-0 l-0 bgc-white w-100 h-100 d-f fxd-r fxw-w ai-c jc-c pos-r p-30",
        style={"minHeight": "calc(100vh - 140px)"},
        children=[
            html.Div(
                className="d-f jc-c fxd-c",
                children=[
                    html.H1("500", className="mB-30 fw-900 lh-1 c-red-500", style={"fontSize": "60px"}),
                    html.H3("Internal Server Error", className="mB-10 fsz-lg c-grey-900 tt-c"),
                    html.P("Something went wrong on our servers. Please try again later.", className="mB-30 fsz-def c-grey-700"),
                    html.Div(html.A("Go to Home", href="/", className="btn btn-primary"))
                ]
            )
        ]
    )


def _auth_input(icon, type_, placeholder, id_=None):
    return html.Div(
        style={
            "display": "flex", "alignItems": "center",
            "border": "1px solid #e0e0e0", "borderRadius": "8px",
            "padding": "0 14px", "marginBottom": "16px",
            "background": "#fafafa", "transition": "border 0.2s"
        },
        children=[
            html.I(className=f"ti-{icon}", style={"color": "#aaa", "marginRight": "10px", "fontSize": "15px"}),
            dbc.Input(
                type=type_, placeholder=placeholder, id=id_,
                style={
                    "border": "none", "boxShadow": "none", "background": "transparent",
                    "padding": "12px 0", "fontSize": "14px"
                }
            )
        ]
    )


def create_signin_page():
    return html.Div(
        style={
            "minHeight": "calc(100vh - 140px)", "margin": "-30px",
            "display": "flex", "alignItems": "center", "justifyContent": "center",
            "background": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
        },
        children=html.Div(
            style={
                "background": "#fff", "borderRadius": "16px",
                "boxShadow": "0 20px 60px rgba(0,0,0,0.15)",
                "padding": "48px 40px", "width": "100%", "maxWidth": "420px"
            },
            children=[
                # Logo + brand
                html.Div(
                    style={"textAlign": "center", "marginBottom": "32px"},
                    children=[
                        html.Div(
                            html.Img(src="/assets/static/images/logo.svg", style={"width": "44px", "height": "44px"}),
                            style={
                                "width": "72px", "height": "72px", "borderRadius": "50%",
                                "background": "linear-gradient(135deg, #667eea, #764ba2)",
                                "display": "flex", "alignItems": "center", "justifyContent": "center",
                                "margin": "0 auto 16px"
                            }
                        ),
                        html.H4("Welcome back", style={"fontWeight": "700", "color": "#1a1a2e", "marginBottom": "4px"}),
                        html.P("Sign in to your account", style={"color": "#888", "fontSize": "14px", "margin": "0"})
                    ]
                ),
                # Fields
                _auth_input("email", "email", "Email address", "si-email"),
                _auth_input("lock", "password", "Password", "si-password"),
                # Remember + button
                html.Div(
                    style={"display": "flex", "alignItems": "center", "justifyContent": "space-between", "marginBottom": "24px"},
                    children=[
                        html.Label(
                            [dbc.Input(type="checkbox", id="si-remember", style={"marginRight": "6px"}), "Remember me"],
                            style={"display": "flex", "alignItems": "center", "fontSize": "13px", "color": "#555", "margin": "0", "cursor": "pointer"}
                        ),
                        html.A("Forgot password?", href="#", style={"fontSize": "13px", "color": "#667eea", "textDecoration": "none"})
                    ]
                ),
                html.Button(
                    "Sign In",
                    className="btn btn-primary btn-color w-100",
                    style={"borderRadius": "8px", "padding": "12px", "fontSize": "15px", "fontWeight": "600", "marginBottom": "24px"}
                ),
                html.P(
                    ["Don't have an account? ", html.A("Sign Up", href="/pages/signup", style={"color": "#667eea", "fontWeight": "600", "textDecoration": "none"})],
                    style={"textAlign": "center", "fontSize": "13px", "color": "#888", "margin": "0"}
                )
            ]
        )
    )


def create_signup_page():
    return html.Div(
        style={
            "minHeight": "calc(100vh - 140px)", "margin": "-30px",
            "display": "flex", "alignItems": "center", "justifyContent": "center",
            "background": "linear-gradient(135deg, #4bc0c0 0%, #4b7cf3 100%)"
        },
        children=html.Div(
            style={
                "background": "#fff", "borderRadius": "16px",
                "boxShadow": "0 20px 60px rgba(0,0,0,0.15)",
                "padding": "48px 40px", "width": "100%", "maxWidth": "440px"
            },
            children=[
                # Logo + brand
                html.Div(
                    style={"textAlign": "center", "marginBottom": "32px"},
                    children=[
                        html.Div(
                            html.Img(src="/assets/static/images/logo.svg", style={"width": "44px", "height": "44px"}),
                            style={
                                "width": "72px", "height": "72px", "borderRadius": "50%",
                                "background": "linear-gradient(135deg, #4bc0c0, #4b7cf3)",
                                "display": "flex", "alignItems": "center", "justifyContent": "center",
                                "margin": "0 auto 16px"
                            }
                        ),
                        html.H4("Create account", style={"fontWeight": "700", "color": "#1a1a2e", "marginBottom": "4px"}),
                        html.P("Join us today, it's free!", style={"color": "#888", "fontSize": "14px", "margin": "0"})
                    ]
                ),
                # Fields
                _auth_input("user", "text", "Username", "su-username"),
                _auth_input("email", "email", "Email address", "su-email"),
                _auth_input("lock", "password", "Password", "su-password"),
                _auth_input("lock", "password", "Confirm password", "su-confirm"),
                html.Button(
                    "Create Account",
                    className="btn btn-primary btn-color w-100",
                    style={"borderRadius": "8px", "padding": "12px", "fontSize": "15px", "fontWeight": "600", "marginBottom": "24px", "background": "linear-gradient(135deg, #4bc0c0, #4b7cf3)", "border": "none"}
                ),
                html.P(
                    ["Already have an account? ", html.A("Sign In", href="/pages/signin", style={"color": "#4b7cf3", "fontWeight": "600", "textDecoration": "none"})],
                    style={"textAlign": "center", "fontSize": "13px", "color": "#888", "margin": "0"}
                )
            ]
        )
    )
