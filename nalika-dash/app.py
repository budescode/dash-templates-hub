import dash
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

app = Dash(__name__, 
           external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME],
           suppress_callback_exceptions=True)

server = app.server

from components.sidebar import create_sidebar
from components.navbar import create_navbar
from pages import dashboard, login, analytics, charts, tables, forms, widgets, mailbox, maps, tabs_accordions, calendar, buttons, modals, profile, progress, cards, notifications

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/login':
        return login.layout
    elif pathname == '/analytics':
        return html.Div([create_sidebar(), html.Div([create_navbar(), analytics.layout], className='main-content')])
    elif pathname == '/charts':
        return html.Div([create_sidebar(), html.Div([create_navbar(), charts.layout], className='main-content')])
    elif pathname == '/tables':
        return html.Div([create_sidebar(), html.Div([create_navbar(), tables.layout], className='main-content')])
    elif pathname == '/forms':
        return html.Div([create_sidebar(), html.Div([create_navbar(), forms.layout], className='main-content')])
    elif pathname == '/widgets':
        return html.Div([create_sidebar(), html.Div([create_navbar(), widgets.layout], className='main-content')])
    elif pathname == '/mailbox':
        return html.Div([create_sidebar(), html.Div([create_navbar(), mailbox.layout], className='main-content')])
    elif pathname == '/maps':
        return html.Div([create_sidebar(), html.Div([create_navbar(), maps.layout], className='main-content')])
    elif pathname == '/tabs-accordions':
        return html.Div([create_sidebar(), html.Div([create_navbar(), tabs_accordions.layout], className='main-content')])
    elif pathname == '/calendar':
        return html.Div([create_sidebar(), html.Div([create_navbar(), calendar.layout], className='main-content')])
    elif pathname == '/buttons':
        return html.Div([create_sidebar(), html.Div([create_navbar(), buttons.layout], className='main-content')])
    elif pathname == '/modals':
        return html.Div([create_sidebar(), html.Div([create_navbar(), modals.layout], className='main-content')])
    elif pathname == '/profile':
        return html.Div([create_sidebar(), html.Div([create_navbar(), profile.layout], className='main-content')])
    elif pathname == '/progress':
        return html.Div([create_sidebar(), html.Div([create_navbar(), progress.layout], className='main-content')])
    elif pathname == '/cards':
        return html.Div([create_sidebar(), html.Div([create_navbar(), cards.layout], className='main-content')])
    elif pathname == '/notifications':
        return html.Div([create_sidebar(), html.Div([create_navbar(), notifications.layout], className='main-content')])
    else:
        return html.Div([create_sidebar(), html.Div([create_navbar(), dashboard.layout], className='main-content')])

if __name__ == '__main__':
    app.run(debug=True, port=8054)
