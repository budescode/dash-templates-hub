from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(html.H4('Add Department', className='mb-0')),
        dbc.CardBody(dbc.Form([
            dbc.Row([
                dbc.Col([dbc.Label('Department Name'), dbc.Input(type='text', placeholder='e.g. Computer Science')], md=8, className='mb-3'),
                dbc.Col([dbc.Label('Department Code'), dbc.Input(type='text', placeholder='e.g. CS')],               md=4, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Department Head'), dbc.Select(options=[
                    {'label': 'Select Professor', 'value': ''},
                    {'label': 'Dr. Sarah Johnson', 'value': '1'},
                    {'label': 'Dr. Michael Chen', 'value': '2'},
                    {'label': 'Dr. Lisa Thompson', 'value': '3'},
                ])], md=6, className='mb-3'),
                dbc.Col([dbc.Label('Established Year'), dbc.Input(type='number', placeholder='1990')], md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Description'), dbc.Textarea(placeholder='Department description...', rows=3)], className='mb-3'),
            ]),
            dbc.ButtonGroup([
                dbc.Button('Save Department', color='primary'),
                dbc.Button('Cancel', href='/departments', color='secondary', outline=True),
            ]),
        ])),
    ]))),
], fluid=True)
