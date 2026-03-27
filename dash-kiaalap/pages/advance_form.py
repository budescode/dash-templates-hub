from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5('Input Validation', className='mb-0')),
            dbc.CardBody(dbc.Form([
                dbc.Row([
                    dbc.Col([
                        dbc.Label('Valid Input'),
                        dbc.Input(type='text', value='Looks good!', valid=True),
                        dbc.FormFeedback('Looks good!', type='valid'),
                    ], md=6, className='mb-3'),
                    dbc.Col([
                        dbc.Label('Invalid Input'),
                        dbc.Input(type='text', value='Wrong value', invalid=True),
                        dbc.FormFeedback('Please provide a valid value.', type='invalid'),
                    ], md=6, className='mb-3'),
                ]),
                dbc.Row([
                    dbc.Col([
                        dbc.Label('Required Field'),
                        dbc.Input(type='text', placeholder='This field is required'),
                        dbc.FormText('This field cannot be empty.'),
                    ], className='mb-3'),
                ]),
                dbc.Button('Submit', color='primary'),
            ])),
        ]), md=6, className='mb-3'),

        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5('Input Groups', className='mb-0')),
            dbc.CardBody(dbc.Form([
                dbc.Row([dbc.Col([
                    dbc.Label('Username'),
                    dbc.InputGroup([dbc.InputGroupText('@'), dbc.Input(type='text', placeholder='username')]),
                ], className='mb-3')]),
                dbc.Row([dbc.Col([
                    dbc.Label('Website'),
                    dbc.InputGroup([dbc.Input(type='text', placeholder='yoursite'), dbc.InputGroupText('.com')]),
                ], className='mb-3')]),
                dbc.Row([dbc.Col([
                    dbc.Label('Price'),
                    dbc.InputGroup([dbc.InputGroupText('$'), dbc.Input(type='number', placeholder='0.00'), dbc.InputGroupText('.00')]),
                ], className='mb-3')]),
                dbc.Row([dbc.Col([
                    dbc.Label('Search'),
                    dbc.InputGroup([dbc.Input(type='text', placeholder='Search...'), dbc.Button('Go', color='primary')]),
                ], className='mb-3')]),
            ])),
        ]), md=6, className='mb-3'),
    ]),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5('Checkboxes & Radios', className='mb-0')),
            dbc.CardBody([
                html.H6('Checkboxes', className='mb-2'),
                dbc.Checklist(options=[
                    {'label': 'Computer Science', 'value': 'cs'},
                    {'label': 'Mathematics', 'value': 'math'},
                    {'label': 'Engineering', 'value': 'eng'},
                    {'label': 'Biology', 'value': 'bio'},
                ], value=['cs'], className='mb-3'),
                html.H6('Radio Buttons', className='mb-2'),
                dbc.RadioItems(options=[
                    {'label': 'First Year', 'value': '1'},
                    {'label': 'Second Year', 'value': '2'},
                    {'label': 'Third Year', 'value': '3'},
                    {'label': 'Fourth Year', 'value': '4'},
                ], value='1'),
            ]),
        ]), md=6, className='mb-3'),

        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5('Switches & Range', className='mb-0')),
            dbc.CardBody([
                html.H6('Toggle Switches', className='mb-2'),
                dbc.Checklist(options=[
                    {'label': 'Enable Notifications', 'value': 'notif'},
                    {'label': 'Dark Mode', 'value': 'dark'},
                    {'label': 'Auto-save', 'value': 'save'},
                ], value=['notif', 'save'], switch=True, className='mb-3'),
                html.H6('Range Slider', className='mb-2'),
                dbc.Label('Volume: 60%'),
                dbc.Input(type='range', className='form-range', min=0, max=100, value=60),
            ]),
        ]), md=6, className='mb-3'),
    ]),
], fluid=True)
