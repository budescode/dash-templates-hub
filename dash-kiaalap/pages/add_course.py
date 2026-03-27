from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(html.H4('Add New Course', className='mb-0')),
        dbc.CardBody(dbc.Form([
            dbc.Row([
                dbc.Col([dbc.Label('Course Name'), dbc.Input(type='text', placeholder='e.g. Advanced Programming')], md=6, className='mb-3'),
                dbc.Col([dbc.Label('Course Code'), dbc.Input(type='text', placeholder='e.g. CS401')],               md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Department'), dbc.Select(options=[
                    {'label': 'Select Department', 'value': ''},
                    {'label': 'Computer Science', 'value': 'cs'},
                    {'label': 'Mathematics', 'value': 'math'},
                    {'label': 'Biology', 'value': 'bio'},
                    {'label': 'Engineering', 'value': 'eng'},
                ])], md=6, className='mb-3'),
                dbc.Col([dbc.Label('Professor'), dbc.Select(options=[
                    {'label': 'Select Professor', 'value': ''},
                    {'label': 'Dr. Sarah Johnson', 'value': '1'},
                    {'label': 'Dr. Michael Chen', 'value': '2'},
                    {'label': 'Dr. Lisa Thompson', 'value': '3'},
                ])], md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Credits'), dbc.Input(type='number', placeholder='3', min=1, max=6)], md=4, className='mb-3'),
                dbc.Col([dbc.Label('Max Students'), dbc.Input(type='number', placeholder='50')],         md=4, className='mb-3'),
                dbc.Col([dbc.Label('Duration'), dbc.Input(type='text', placeholder='e.g. 16 weeks')],   md=4, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Description'), dbc.Textarea(placeholder='Course description...', rows=3)], className='mb-3'),
            ]),
            dbc.ButtonGroup([
                dbc.Button('Save Course', color='primary'),
                dbc.Button('Cancel', href='/all-courses', color='secondary', outline=True),
            ]),
        ])),
    ]))),
], fluid=True)
