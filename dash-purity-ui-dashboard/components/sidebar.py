from dash import dcc, html

NAV_ITEMS = [
    {"label": "Dashboard", "href": "/", "icon": "fa-solid fa-gauge"},
    {"label": "Tables", "href": "/tables", "icon": "fa-solid fa-table"},
    {"label": "Billing", "href": "/billing", "icon": "fa-regular fa-credit-card"},
    {"label": "RTL", "href": "/rtl", "icon": "fa-solid fa-rotate-right"},
]

ACCOUNT_ITEMS = [
    {"label": "Profile", "href": "/profile", "icon": "fa-regular fa-user"},
    {"label": "Sign In", "href": "/sign-in", "icon": "fa-solid fa-right-to-bracket"},
    {"label": "Sign Up", "href": "/sign-up", "icon": "fa-regular fa-pen-to-square"},
]


def _nav_link(item, pathname):
    is_active = pathname == item["href"]
    classes = "nav-link" + (" active" if is_active else "")
    return dcc.Link(
        className=classes,
        href=item["href"],
        children=[
            html.I(className=f"nav-icon {item['icon']}"),
            html.Span(item["label"], className="nav-text"),
        ],
    )


def create_sidebar(pathname):
    return html.Aside(
        className="sidebar",
        children=[
                html.Div(
                className="sidebar-logo",
                children=[
                    html.Div(className="logo-box", children=html.I(className="fa-solid fa-cube")),
                    html.Div(
                        children=[
                            html.Div("PURITY UI", className="logo-title"),
                            html.Div("DASHBOARD", className="logo-subtitle"),
                        ]
                    ),
                    html.Button(
                        html.I(className="fa-solid fa-xmark"),
                        id="sidebar-close",
                        className="icon-button sidebar-close-btn",
                    ),
                ],
            ),
            html.Div(
                className="sidebar-section",
                children=[_nav_link(item, pathname) for item in NAV_ITEMS],
            ),
            html.Div("ACCOUNT PAGES", className="sidebar-heading"),
            html.Div(
                className="sidebar-section",
                children=[_nav_link(item, pathname) for item in ACCOUNT_ITEMS],
            ),
            html.Div(
                className="sidebar-help",
                children=[
                    html.Div(className="help-icon", children=html.I(className="fa-regular fa-circle-question")),
                    html.Div("Need help?", className="help-title"),
                    html.Div("Please check our docs", className="help-subtitle"),
                    html.Button("DOCUMENTATION", className="btn btn-light btn-sm help-btn"),
                ],
            ),
        ],
    )
