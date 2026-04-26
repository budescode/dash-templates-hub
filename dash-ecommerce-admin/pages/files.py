from dash import html, register_page
import dash_bootstrap_components as dbc

register_page(
    __name__,
    path='/files',
    name='Files'
)

layout = dbc.Container([
    html.H1("Files"),
    html.P("File manager and uploads placeholder."),
], fluid=True)
