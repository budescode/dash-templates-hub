from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(html.H5('Password Strength Meter', className='mb-0')),
        dbc.CardBody([
            dbc.Form([
                dbc.Row([dbc.Col([
                    dbc.Label('New Password'),
                    dbc.Input(type='password', id='password-input', placeholder='Enter password'),
                    html.Div(className='mt-2', children=[
                        dbc.Progress(id='password-strength', value=0, className='mb-1', style={'height': '6px'}),
                        html.Small('Password strength: Enter a password', className='text-muted', id='password-label'),
                    ]),
                ], className='mb-3')]),
                dbc.Row([dbc.Col([
                    dbc.Label('Confirm Password'),
                    dbc.Input(type='password', placeholder='Confirm password'),
                ], className='mb-3')]),
                html.Div([
                    html.P('Password requirements:', className='small fw-semibold mb-1'),
                    html.Ul([
                        html.Li('At least 8 characters', className='small text-muted'),
                        html.Li('At least one uppercase letter', className='small text-muted'),
                        html.Li('At least one number', className='small text-muted'),
                        html.Li('At least one special character', className='small text-muted'),
                    ]),
                ], className='mb-3'),
                dbc.Button('Update Password', color='primary'),
            ]),
        ]),
    ]))),
], fluid=True)
