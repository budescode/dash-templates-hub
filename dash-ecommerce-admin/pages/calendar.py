from dash import html, register_page
import dash_bootstrap_components as dbc

register_page(
    __name__,
    path='/calendar',
    name='Calendar'
)

layout = dbc.Container([
    html.H1("Calendar"),
    html.P("Calendar and scheduling placeholder."),
], fluid=True)
