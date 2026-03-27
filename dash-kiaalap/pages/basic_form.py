from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    html.Div([
        html.H1('Basic Forms', className='h3 font-bold'),
        html.P('Basic form elements and inputs.', className='text-muted text-sm')
    ], className='mb-3'),
    
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H5('Form Example', className='dashboard-card-title')
                ], className='dashboard-card-header'),
                html.Div([
                    dbc.Form([
                        dbc.Row([
                            dbc.Col([
                                dbc.Label('First Name'),
                                dbc.Input(type='text', placeholder='Enter first name'),
                            ], width=6),
                            dbc.Col([
                                dbc.Label('Last Name'),
                                dbc.Input(type='text', placeholder='Enter last name'),
                            ], width=6),
                        ], className='mb-3'),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label('Email'),
                                dbc.Input(type='email', placeholder='Enter email'),
                            ], width=12),
                        ], className='mb-3'),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label('Password'),
                                dbc.Input(type='password', placeholder='Enter password'),
                            ], width=12),
                        ], className='mb-3'),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label('Department'),
                                dbc.Select(options=[
                                    {'label': 'Select Department', 'value': ''},
                                    {'label': 'Computer Science', 'value': 'cs'},
                                    {'label': 'Engineering', 'value': 'eng'},
                                    {'label': 'Business', 'value': 'bus'},
                                ]),
                            ], width=12),
                        ], className='mb-3'),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label('Message'),
                                dbc.Textarea(placeholder='Enter your message', rows=4),
                            ], width=12),
                        ], className='mb-3'),
                        dbc.Row([
                            dbc.Col([
                                dbc.Checkbox(label='I agree to the terms and conditions'),
                            ], width=12),
                        ], className='mb-3'),
                        dbc.Button('Submit', color='primary', className='me-2'),
                        dbc.Button('Reset', color='secondary', outline=True),
                    ])
                ], className='dashboard-card-body')
            ], className='dashboard-card')
        ], className='dashboard-grid grid-cols-1')
    ], className='dashboard-row')
])
