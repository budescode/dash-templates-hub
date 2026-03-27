from dash import html
import dash_bootstrap_components as dbc


def _event_item(icon_color, title, date, category):
    return html.Li(
        className="bdB peers ai-c jc-sb fxw-nw",
        children=[
            html.A(
                className="td-n p-20 peers fxw-nw me-20 peer-greed c-grey-900",
                href="#",
                children=[
                    html.Div(html.I(className=f"fa fa-fw fa-clock-o {icon_color}"), className="peer mR-15"),
                    html.Div([
                        html.Span(title, className="fw-600"),
                        html.Div([
                            html.Span(date, className="c-grey-700"),
                            html.I(category)
                        ], className="c-grey-600")
                    ], className="peer")
                ]
            ),
            html.Div(
                className="peers mR-15",
                children=[
                    html.Div(html.A(html.I(className="ti-pencil"), href="#", className="td-n c-deep-purple-500 cH-blue-500 fsz-md p-5"), className="peer"),
                    html.Div(html.A(html.I(className="ti-trash"), href="#", className="td-n c-red-500 cH-blue-500 fsz-md p-5"), className="peer"),
                ]
            )
        ]
    )


def create_calendar_page():
    events = [
        ("c-red-500",    "All Day Event", "Nov 01 - ", "Website Development"),
        ("c-blue-500",   "All Day Event", "Nov 01 - ", "Website Development"),
        ("c-indigo-500", "All Day Event", "Nov 01 - ", "Website Development"),
        ("c-green-500",  "All Day Event", "Nov 01 - ", "Website Development"),
    ]

    return html.Div(
        className="container-fluid",
        children=html.Div(
            className="row",
            children=[
                # Left panel
                html.Div(
                    className="col-md-4",
                    children=html.Div(
                        className="bdrs-3 ov-h bgc-white bd",
                        children=[
                            html.Div(
                                className="bgc-deep-purple-500 ta-c p-30",
                                children=[
                                    html.H1(["01", html.Span("st", className="fsz-def")],
                                            className="fw-300 mB-5 lh-1 c-white"),
                                    html.H3("Monday", className="c-white")
                                ]
                            ),
                            html.Div(
                                className="pos-r",
                                children=[
                                    html.Button(
                                        html.I(className="ti-plus"),
                                        type="button",
                                        className="mT-nv-50 pos-a r-10 t-2 btn cur-p bdrs-50p p-0 w-3r h-3r btn-warning"
                                    ),
                                    html.Ul(
                                        className="m-0 p-0 mT-20",
                                        children=[_event_item(*e) for e in events]
                                    )
                                ]
                            )
                        ]
                    )
                ),
                # Right panel — FullCalendar
                html.Div(
                    className="col-md-8",
                    children=html.Div(id="fullcalendar", style={"minHeight": "600px"})
                )
            ]
        )
    )


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
