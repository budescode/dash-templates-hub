from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(html.H4('Edit Department', className='mb-0')),
        dbc.CardBody(dbc.Form([
            dbc.Row([
                dbc.Col([dbc.Label('Department Name'), dbc.Input(type='text', value='Computer Science')], md=8, className='mb-3'),
                dbc.Col([dbc.Label('Department Code'), dbc.Input(type='text', value='CS')],               md=4, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Department Head'), dbc.Select(options=[
                    {'label': 'Dr. Sarah Johnson', 'value': '1'},
                    {'label': 'Dr. Michael Chen', 'value': '2'},
                ], value='1')], md=6, className='mb-3'),
                dbc.Col([dbc.Label('Established Year'), dbc.Input(type='number', value=1985)], md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Description'), dbc.Textarea(value='Leading department in computing and software engineering.', rows=3)], className='mb-3'),
            ]),
            dbc.ButtonGroup([
                dbc.Button('Update Department', color='primary'),
                dbc.Button('Cancel', href='/departments', color='secondary', outline=True),
            ]),
        ])),
    ]))),
], fluid=True)
