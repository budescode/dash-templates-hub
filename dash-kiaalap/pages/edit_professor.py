from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(html.H4('Edit Professor', className='mb-0')),
        dbc.CardBody(dbc.Form([
            dbc.Row([
                dbc.Col([dbc.Label('First Name'), dbc.Input(type='text', value='Sarah')],    md=6, className='mb-3'),
                dbc.Col([dbc.Label('Last Name'),  dbc.Input(type='text', value='Johnson')],  md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Email'), dbc.Input(type='email', value='sarah.johnson@university.edu')], md=6, className='mb-3'),
                dbc.Col([dbc.Label('Phone'), dbc.Input(type='tel', value='+1 234 567 8900')],                md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Department'), dbc.Select(options=[
                    {'label': 'Computer Science', 'value': 'cs'},
                    {'label': 'Mathematics', 'value': 'math'},
                    {'label': 'Biology', 'value': 'bio'},
                    {'label': 'Engineering', 'value': 'eng'},
                ], value='cs')], md=6, className='mb-3'),
                dbc.Col([dbc.Label('Qualification'), dbc.Input(type='text', value='PhD in Computer Science')], md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Bio'), dbc.Textarea(value='Experienced professor with 10+ years in academia.', rows=3)], className='mb-3'),
            ]),
            dbc.ButtonGroup([
                dbc.Button('Update Professor', color='primary'),
                dbc.Button('Cancel', href='/all-professors', color='secondary', outline=True),
            ]),
        ])),
    ]))),
], fluid=True)
