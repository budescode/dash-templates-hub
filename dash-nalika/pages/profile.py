from dash import html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Breadcrumb(items=[
        {'label': 'Home', 'href': '/', 'active': False},
        {'label': 'Profile', 'active': True},
    ], className='breadcrumb'),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.Img(src='/assets/img/user.jpg', className='rounded-circle d-block mx-auto mb-3', width='120', height='120'),
                        html.H4('Lakian Das', className='text-center'),
                        html.P('Administrator', className='text-center text-muted'),
                        html.Hr(),
                        html.P([html.I(className='fas fa-envelope me-2'), 'lakian@example.com']),
                        html.P([html.I(className='fas fa-phone me-2'), '+1 234 567 8900']),
                        html.P([html.I(className='fas fa-map-marker-alt me-2'), 'New York, USA']),
                        html.Hr(),
                        dbc.Button('Edit Profile', color='primary', className='w-100'),
                    ])
                ])
            ])
        ], md=4),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('About')),
                dbc.CardBody([
                    html.P('Full Stack Developer with 5+ years of experience in building web applications.'),
                    html.Hr(),
                    html.H6('Skills'),
                    html.Div([
                        dbc.Badge('Python', color='primary', className='me-1 mb-1'),
                        dbc.Badge('JavaScript', color='warning', className='me-1 mb-1'),
                        dbc.Badge('React', color='info', className='me-1 mb-1'),
                        dbc.Badge('Dash', color='success', className='me-1 mb-1'),
                        dbc.Badge('SQL', color='secondary', className='me-1 mb-1'),
                    ]),
                ])
            ], className='mb-4'),
            
            dbc.Card([
                dbc.CardHeader(html.H5('Recent Activity')),
                dbc.CardBody([
                    dbc.ListGroup([
                        dbc.ListGroupItem([
                            html.Small('2 hours ago', className='text-muted'),
                            html.P('Updated dashboard analytics', className='mb-0'),
                        ]),
                        dbc.ListGroupItem([
                            html.Small('5 hours ago', className='text-muted'),
                            html.P('Created new report', className='mb-0'),
                        ]),
                        dbc.ListGroupItem([
                            html.Small('Yesterday', className='text-muted'),
                            html.P('Completed project milestone', className='mb-0'),
                        ]),
                    ])
                ])
            ])
        ], md=8),
    ])
])
