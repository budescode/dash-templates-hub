from dash import html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Breadcrumb(items=[
        {'label': 'Home', 'href': '/', 'active': False},
        {'label': 'Maps', 'active': True},
    ], className='breadcrumb'),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Interactive Map')),
                dbc.CardBody([
                    html.Iframe(
                        src='https://www.openstreetmap.org/export/embed.html?bbox=-0.1,51.5,0.1,51.6&layer=mapnik',
                        style={'width': '100%', 'height': '500px', 'border': 'none'}
                    )
                ])
            ])
        ], md=12)
    ])
])
