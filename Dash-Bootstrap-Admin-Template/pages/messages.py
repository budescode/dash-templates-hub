from dash import html, register_page
import dash_bootstrap_components as dbc

register_page(
    __name__,
    path='/messages',
    name='Messages'
)

layout = dbc.Container([
    html.H1("Messages"),
    html.P("Inbox and message center placeholder."),
], fluid=True)
