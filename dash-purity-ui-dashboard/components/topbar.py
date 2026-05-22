from dash import html, dcc


def _page_title(pathname):
    mapping = {
        "/": "Dashboard",
        "/tables": "Tables",
        "/billing": "Billing",
        "/profile": "Profile",
        "/rtl": "RTL",
    }
    return mapping.get(pathname, "Dashboard")


def create_topbar(pathname):
    title = _page_title(pathname)
    return html.Div(
        className="topbar",
        children=[
            html.Div(
                className="topbar-left",
                children=[
                    html.Button(html.I(className="fa-solid fa-bars", style={"margin":"auto"}), id="sidebar-toggle", className="icon-button mobile-toggle",),
                    html.Div("Pages / " + title, className="topbar-breadcrumb"),
                    html.Div(title, className="topbar-title"),
                ],
            ),
            html.Div(
                className="topbar-right",
                children=[
                    html.Div(
                        className="search-pill",
                        children=[
                            html.I(className="fa-solid fa-magnifying-glass"),
                            dcc.Input(type="text", placeholder="Type here...", className="search-input"),
                        ],
                    ),
                    html.A("Sign In", href="/sign-in", className="topbar-link"),
                    html.Button(html.I(className="fa-regular fa-bell"), className="icon-button"),
                    html.Button(html.I(className="fa-solid fa-gear"), className="icon-button"),
                ],
            ),
        ],
    )
