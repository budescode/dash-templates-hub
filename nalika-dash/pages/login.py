from dash import html, dcc
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Div([
                            html.H3('PLEASE LOGIN TO APP', className='text-center mb-3'),
                            html.P('This is the best app ever!', className='text-center text-muted mb-4'),
                        ]),
                        dbc.Form([
                            dbc.Label('Username'),
                            dbc.Input(type='email', placeholder='example@gmail.com', className='mb-3'),
                            html.Small('Your unique username to app', className='text-muted d-block mb-3'),
                            
                            dbc.Label('Password'),
                            dbc.Input(type='password', placeholder='******', className='mb-3'),
                            html.Small('Your strong password', className='text-muted d-block mb-3'),
                            
                            dbc.Checkbox(id='remember-me', label='Remember me', className='mb-3'),
                            html.Small('(if this is a private computer)', className='text-muted d-block mb-3'),
                            
                            dbc.Button('Login', color='success', className='w-100 mb-2'),
                            dbc.Button('Register', color='secondary', outline=True, className='w-100'),
                        ])
                    ])
                ], className='login-card')
            ], md=4, className='mx-auto')
        ]),
        dbc.Row([
            dbc.Col([
                html.P('Copyright © 2024 Nalika. All rights reserved.', className='text-center mt-4')
            ])
        ])
    ], className='login-container')
])
