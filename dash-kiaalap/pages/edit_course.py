from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(html.H4('Edit Course', className='mb-0')),
        dbc.CardBody(dbc.Form([
            dbc.Row([
                dbc.Col([dbc.Label('Course Name'), dbc.Input(type='text', value='Advanced Programming')], md=6, className='mb-3'),
                dbc.Col([dbc.Label('Course Code'), dbc.Input(type='text', value='CS401')],                md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Department'), dbc.Select(options=[
                    {'label': 'Computer Science', 'value': 'cs'},
                    {'label': 'Mathematics', 'value': 'math'},
                    {'label': 'Engineering', 'value': 'eng'},
                ], value='cs')], md=6, className='mb-3'),
                dbc.Col([dbc.Label('Professor'), dbc.Select(options=[
                    {'label': 'Dr. Sarah Johnson', 'value': '1'},
                    {'label': 'Dr. Michael Chen', 'value': '2'},
                ], value='1')], md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Credits'), dbc.Input(type='number', value=3)],       md=4, className='mb-3'),
                dbc.Col([dbc.Label('Max Students'), dbc.Input(type='number', value=50)], md=4, className='mb-3'),
                dbc.Col([dbc.Label('Duration'), dbc.Input(type='text', value='16 weeks')], md=4, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Description'), dbc.Textarea(value='An advanced course covering programming concepts.', rows=3)], className='mb-3'),
            ]),
            dbc.ButtonGroup([
                dbc.Button('Update Course', color='primary'),
                dbc.Button('Cancel', href='/all-courses', color='secondary', outline=True),
            ]),
        ])),
    ]))),
], fluid=True)
