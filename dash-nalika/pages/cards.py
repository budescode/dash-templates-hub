from dash import html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Breadcrumb(items=[
        {'label': 'Home', 'href': '/', 'active': False},
        {'label': 'Cards', 'active': True},
    ], className='breadcrumb'),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src='https://placehold.co/300x200', top=True),
                dbc.CardBody([
                    html.H4('Card with Image', className='card-title'),
                    html.P('This card has an image at the top.'),
                    dbc.Button('Learn More', color='primary'),
                ])
            ])
        ], md=4),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader('Featured'),
                dbc.CardBody([
                    html.H4('Special Card', className='card-title'),
                    html.P('This card has a header.'),
                    dbc.Button('Go', color='success'),
                ])
            ])
        ], md=4),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Colored Card', className='card-title'),
                    html.P('This card has a colored background.'),
                    dbc.Button('Action', color='light', outline=True),
                ])
            ], color='info', inverse=True)
        ], md=4),
    ], className='mb-4'),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.I(className='fas fa-users fa-3x text-primary'),
                        ], width=3, className='text-center'),
                        dbc.Col([
                            html.H3('1,234'),
                            html.P('Total Users', className='text-muted'),
                        ], width=9),
                    ])
                ])
            ])
        ], md=3),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.I(className='fas fa-shopping-cart fa-3x text-success'),
                        ], width=3, className='text-center'),
                        dbc.Col([
                            html.H3('567'),
                            html.P('Orders', className='text-muted'),
                        ], width=9),
                    ])
                ])
            ])
        ], md=3),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.I(className='fas fa-dollar-sign fa-3x text-warning'),
                        ], width=3, className='text-center'),
                        dbc.Col([
                            html.H3('$45K'),
                            html.P('Revenue', className='text-muted'),
                        ], width=9),
                    ])
                ])
            ])
        ], md=3),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.I(className='fas fa-chart-line fa-3x text-danger'),
                        ], width=3, className='text-center'),
                        dbc.Col([
                            html.H3('89%'),
                            html.P('Growth', className='text-muted'),
                        ], width=9),
                    ])
                ])
            ])
        ], md=3),
    ])
])
