from dash import html, dcc
import dash_bootstrap_components as dbc

# Basic Form
basic_form = dbc.Card([
    dbc.CardHeader(html.H5('Basic Form Elements')),
    dbc.CardBody([
        dbc.Form([
            dbc.Row([
                dbc.Col([
                    dbc.Label('First Name'),
                    dbc.Input(type='text', placeholder='Enter first name'),
                ], md=6),
                dbc.Col([
                    dbc.Label('Last Name'),
                    dbc.Input(type='text', placeholder='Enter last name'),
                ], md=6),
            ], className='mb-3'),
            
            dbc.Row([
                dbc.Col([
                    dbc.Label('Email'),
                    dbc.Input(type='email', placeholder='Enter email'),
                ], md=6),
                dbc.Col([
                    dbc.Label('Phone'),
                    dbc.Input(type='tel', placeholder='Enter phone'),
                ], md=6),
            ], className='mb-3'),
            
            dbc.Label('Address'),
            dbc.Textarea(placeholder='Enter address', className='mb-3'),
            
            dbc.Row([
                dbc.Col([
                    dbc.Label('City'),
                    dbc.Input(type='text', placeholder='Enter city'),
                ], md=4),
                dbc.Col([
                    dbc.Label('State'),
                    dbc.Select(options=[
                        {'label': 'Select State', 'value': ''},
                        {'label': 'California', 'value': 'CA'},
                        {'label': 'New York', 'value': 'NY'},
                        {'label': 'Texas', 'value': 'TX'},
                    ]),
                ], md=4),
                dbc.Col([
                    dbc.Label('Zip Code'),
                    dbc.Input(type='text', placeholder='Enter zip'),
                ], md=4),
            ], className='mb-3'),
            
            dbc.Button('Submit', color='primary', className='me-2'),
            dbc.Button('Reset', color='secondary', outline=True),
        ])
    ])
], className='mb-4')

# Advanced Form
advanced_form = dbc.Card([
    dbc.CardHeader(html.H5('Advanced Form Elements')),
    dbc.CardBody([
        dbc.Form([
            dbc.Label('Select Options'),
            dbc.Select(
                options=[
                    {'label': 'Option 1', 'value': '1'},
                    {'label': 'Option 2', 'value': '2'},
                    {'label': 'Option 3', 'value': '3'},
                ],
                className='mb-3'
            ),
            
            dbc.Label('Multiple Select'),
            dcc.Dropdown(
                options=[
                    {'label': 'Choice 1', 'value': '1'},
                    {'label': 'Choice 2', 'value': '2'},
                    {'label': 'Choice 3', 'value': '3'},
                    {'label': 'Choice 4', 'value': '4'},
                ],
                multi=True,
                className='mb-3',
                style={'color': '#000'}
            ),
            
            dbc.Label('Date Picker'),
            dbc.Input(type='date', className='mb-3'),
            
            dbc.Label('Range Slider'),
            dcc.RangeSlider(
                min=0,
                max=100,
                step=10,
                value=[20, 80],
                marks={i: str(i) for i in range(0, 101, 20)},
                className='mb-4'
            ),
            
            dbc.Label('Checkboxes'),
            dbc.Checklist(
                options=[
                    {'label': 'Option 1', 'value': '1'},
                    {'label': 'Option 2', 'value': '2'},
                    {'label': 'Option 3', 'value': '3'},
                ],
                value=['1'],
                className='mb-3'
            ),
            
            dbc.Label('Radio Buttons'),
            dbc.RadioItems(
                options=[
                    {'label': 'Radio 1', 'value': '1'},
                    {'label': 'Radio 2', 'value': '2'},
                    {'label': 'Radio 3', 'value': '3'},
                ],
                value='1',
                className='mb-3'
            ),
            
            dbc.Label('Switch'),
            dbc.Switch(label='Enable notifications', value=True, className='mb-3'),
            
            dbc.Button('Save', color='success', className='me-2'),
            dbc.Button('Cancel', color='danger', outline=True),
        ])
    ])
], className='mb-4')

# Input Groups
input_groups = dbc.Card([
    dbc.CardHeader(html.H5('Input Groups')),
    dbc.CardBody([
        dbc.Label('With Icon'),
        dbc.InputGroup([
            dbc.InputGroupText(html.I(className='fas fa-user')),
            dbc.Input(placeholder='Username'),
        ], className='mb-3'),
        
        dbc.Label('With Button'),
        dbc.InputGroup([
            dbc.Input(placeholder='Search...'),
            dbc.Button('Search', color='primary'),
        ], className='mb-3'),
        
        dbc.Label('With Dropdown'),
        dbc.InputGroup([
            dbc.DropdownMenu([
                dbc.DropdownMenuItem('Action 1'),
                dbc.DropdownMenuItem('Action 2'),
            ], label='Options'),
            dbc.Input(placeholder='Enter text'),
        ], className='mb-3'),
    ])
], className='mb-4')

layout = html.Div([
    dbc.Breadcrumb(items=[
        {'label': 'Home', 'href': '/', 'active': False},
        {'label': 'Forms', 'active': True},
    ], className='breadcrumb'),
    
    basic_form,
    advanced_form,
    input_groups,
])
