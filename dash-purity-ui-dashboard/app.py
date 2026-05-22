import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State

from components.sidebar import create_sidebar
from components.topbar import create_topbar
from components.footer import create_footer
from pages import dashboard, tables, billing, profile, rtl, sign_in, sign_up

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css",
    ],
    suppress_callback_exceptions=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

app.title = "Purity UI Dashboard"

app.layout = html.Div(
    className="app-root",
    children=[
        dcc.Location(id="url", refresh=False),
        dcc.Store(id="sidebar-open", data=False),
        # Auth pages rendered here (sign-in, sign-up)
        html.Div(id="auth-content"),
        # Static app shell — always in the DOM so sidebar-toggle callback works
        dbc.Container(
            id="main-shell",
            fluid=True,
            className="app-shell",
            style={"display": "none"},
            children=[
                dbc.Row(
                    className="g-0 flex-nowrap align-items-stretch",
                    children=[
                        dbc.Col(
                            html.Div(
                                id="sidebar-container",
                                className="sidebar-container",
                                children=create_sidebar("/"),
                            ),
                            width="auto",
                            className="sidebar-col",
                        ),
                        dbc.Col(
                            html.Div(
                                className="app-main",
                                children=[
                                    html.Div(id="topbar-container", children=create_topbar("/")),
                                    html.Div(className="page-wrap", id="page-content"),
                                    create_footer(),
                                ],
                            ),
                            className="app-main-col",
                        ),
                    ],
                )
            ],
        ),
    ],
)


@app.callback(
    Output("auth-content", "children"),
    Output("main-shell", "style"),
    Output("page-content", "children"),
    Output("sidebar-container", "children"),
    Output("topbar-container", "children"),
    Input("url", "pathname"),
)
def route_page(pathname):
    if pathname in ("/sign-in", "/sign-up"):
        auth_layout = sign_in.layout if pathname == "/sign-in" else sign_up.layout
        return auth_layout, {"display": "none"}, dash.no_update, dash.no_update, dash.no_update

    page_map = {
        "/": dashboard.layout,
        "/tables": tables.layout,
        "/billing": billing.layout,
        "/profile": profile.layout,
        "/rtl": rtl.layout,
    }
    content = page_map.get(pathname, dashboard.layout)
    return None, {}, content, create_sidebar(pathname), create_topbar(pathname)


@app.callback(
    Output("sidebar-open", "data"),
    Input("sidebar-toggle", "n_clicks"),
    Input("sidebar-close", "n_clicks"),
    Input("url", "pathname"),
    State("sidebar-open", "data"),
    prevent_initial_call=True,
)
def toggle_sidebar(n_toggle, n_close, pathname, is_open):
    triggered = dash.callback_context.triggered_id
    if triggered == "sidebar-toggle":
        return not is_open
    if triggered in ("sidebar-close", "url"):
        return False
    return is_open


@app.callback(
    Output("sidebar-container", "className"),
    Input("sidebar-open", "data"),
)
def set_sidebar_class(is_open):
    return "sidebar-container open" if is_open else "sidebar-container"


if __name__ == "__main__":
    app.run(debug=True, port=8053)
