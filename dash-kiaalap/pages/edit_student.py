from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(html.H4('Edit Student', className='mb-0')),
        dbc.CardBody(dbc.Form([
            dbc.Row([
                dbc.Col([dbc.Label('First Name'), dbc.Input(type='text', value='Alex')],    md=6, className='mb-3'),
                dbc.Col([dbc.Label('Last Name'),  dbc.Input(type='text', value='Johnson')], md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Email'), dbc.Input(type='email', value='alex.johnson@email.com')], md=6, className='mb-3'),
                dbc.Col([dbc.Label('Phone'), dbc.Input(type='tel', value='+1 234 567 8900')],          md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Department'), dbc.Select(options=[
                    {'label': 'Computer Science', 'value': 'cs'},
                    {'label': 'Engineering', 'value': 'eng'},
                    {'label': 'Business', 'value': 'bus'},
                    {'label': 'Medicine', 'value': 'med'},
                ], value='cs')], md=6, className='mb-3'),
                dbc.Col([dbc.Label('Year'), dbc.Select(options=[
                    {'label': 'First Year', 'value': '1'},
                    {'label': 'Second Year', 'value': '2'},
                    {'label': 'Third Year', 'value': '3'},
                    {'label': 'Fourth Year', 'value': '4'},
                ], value='2')], md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Address'), dbc.Textarea(value='123 Main St, City', rows=3)], className='mb-3'),
            ]),
            dbc.ButtonGroup([
                dbc.Button('Update Student', color='primary'),
                dbc.Button('Cancel', href='/all-students', color='secondary', outline=True),
            ]),
        ])),
    ]))),
], fluid=True)
