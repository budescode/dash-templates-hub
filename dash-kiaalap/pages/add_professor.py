from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(html.H4('Add New Professor', className='mb-0')),
        dbc.CardBody(dbc.Form([
            dbc.Row([
                dbc.Col([dbc.Label('First Name'), dbc.Input(type='text', placeholder='First name')], md=6, className='mb-3'),
                dbc.Col([dbc.Label('Last Name'),  dbc.Input(type='text', placeholder='Last name')],  md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Email'), dbc.Input(type='email', placeholder='professor@university.edu')], md=6, className='mb-3'),
                dbc.Col([dbc.Label('Phone'), dbc.Input(type='tel', placeholder='+1 234 567 8900')],            md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Department'), dbc.Select(options=[
                    {'label': 'Select Department', 'value': ''},
                    {'label': 'Computer Science', 'value': 'cs'},
                    {'label': 'Mathematics', 'value': 'math'},
                    {'label': 'Biology', 'value': 'bio'},
                    {'label': 'Engineering', 'value': 'eng'},
                    {'label': 'Physics', 'value': 'phys'},
                    {'label': 'Chemistry', 'value': 'chem'},
                ])], md=6, className='mb-3'),
                dbc.Col([dbc.Label('Qualification'), dbc.Input(type='text', placeholder='e.g. PhD in Computer Science')], md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Bio'), dbc.Textarea(placeholder='Brief biography...', rows=3)], className='mb-3'),
            ]),
            dbc.ButtonGroup([
                dbc.Button('Save Professor', color='primary'),
                dbc.Button('Cancel', href='/all-professors', color='secondary', outline=True),
            ]),
        ])),
    ]))),
], fluid=True)
