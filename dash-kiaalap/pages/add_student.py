from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(html.H4('Add New Student', className='mb-0')),
        dbc.CardBody(dbc.Form([
            dbc.Row([
                dbc.Col([dbc.Label('First Name'), dbc.Input(type='text', placeholder='First name')], md=6, className='mb-3'),
                dbc.Col([dbc.Label('Last Name'),  dbc.Input(type='text', placeholder='Last name')],  md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Email'), dbc.Input(type='email', placeholder='student@email.com')], md=6, className='mb-3'),
                dbc.Col([dbc.Label('Phone'), dbc.Input(type='tel', placeholder='+1 234 567 8900')],    md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Department'), dbc.Select(options=[
                    {'label': 'Select Department', 'value': ''},
                    {'label': 'Computer Science', 'value': 'cs'},
                    {'label': 'Engineering', 'value': 'eng'},
                    {'label': 'Business', 'value': 'bus'},
                    {'label': 'Medicine', 'value': 'med'},
                ])], md=6, className='mb-3'),
                dbc.Col([dbc.Label('Year'), dbc.Select(options=[
                    {'label': 'Select Year', 'value': ''},
                    {'label': 'First Year', 'value': '1'},
                    {'label': 'Second Year', 'value': '2'},
                    {'label': 'Third Year', 'value': '3'},
                    {'label': 'Fourth Year', 'value': '4'},
                ])], md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Date of Birth'), dbc.Input(type='date')], md=6, className='mb-3'),
                dbc.Col([dbc.Label('Gender'), dbc.Select(options=[
                    {'label': 'Select Gender', 'value': ''},
                    {'label': 'Male', 'value': 'male'},
                    {'label': 'Female', 'value': 'female'},
                    {'label': 'Other', 'value': 'other'},
                ])], md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Address'), dbc.Textarea(placeholder='Enter address', rows=3)], className='mb-3'),
            ]),
            dbc.ButtonGroup([
                dbc.Button('Save Student', color='primary'),
                dbc.Button('Cancel', href='/all-students', color='secondary', outline=True),
            ]),
        ])),
    ]))),
], fluid=True)
