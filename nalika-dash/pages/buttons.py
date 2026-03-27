from dash import html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Breadcrumb(items=[
        {'label': 'Home', 'href': '/', 'active': False},
        {'label': 'Buttons', 'active': True},
    ], className='breadcrumb'),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Button Colors')),
                dbc.CardBody([
                    dbc.Button('Primary', color='primary', className='me-2 mb-2'),
                    dbc.Button('Secondary', color='secondary', className='me-2 mb-2'),
                    dbc.Button('Success', color='success', className='me-2 mb-2'),
                    dbc.Button('Warning', color='warning', className='me-2 mb-2'),
                    dbc.Button('Danger', color='danger', className='me-2 mb-2'),
                    dbc.Button('Info', color='info', className='me-2 mb-2'),
                    dbc.Button('Light', color='light', className='me-2 mb-2'),
                    dbc.Button('Dark', color='dark', className='me-2 mb-2'),
                ])
            ], className='mb-4')
        ], md=6),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Outline Buttons')),
                dbc.CardBody([
                    dbc.Button('Primary', color='primary', outline=True, className='me-2 mb-2'),
                    dbc.Button('Secondary', color='secondary', outline=True, className='me-2 mb-2'),
                    dbc.Button('Success', color='success', outline=True, className='me-2 mb-2'),
                    dbc.Button('Warning', color='warning', outline=True, className='me-2 mb-2'),
                    dbc.Button('Danger', color='danger', outline=True, className='me-2 mb-2'),
                    dbc.Button('Info', color='info', outline=True, className='me-2 mb-2'),
                ])
            ], className='mb-4')
        ], md=6),
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Button Sizes')),
                dbc.CardBody([
                    dbc.Button('Large', size='lg', color='primary', className='me-2'),
                    dbc.Button('Normal', color='primary', className='me-2'),
                    dbc.Button('Small', size='sm', color='primary'),
                ])
            ], className='mb-4')
        ], md=6),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Button Groups')),
                dbc.CardBody([
                    dbc.ButtonGroup([
                        dbc.Button('Left', color='primary'),
                        dbc.Button('Middle', color='primary'),
                        dbc.Button('Right', color='primary'),
                    ], className='mb-2'),
                    html.Br(),
                    dbc.ButtonGroup([
                        dbc.Button(html.I(className='fas fa-align-left'), color='secondary'),
                        dbc.Button(html.I(className='fas fa-align-center'), color='secondary'),
                        dbc.Button(html.I(className='fas fa-align-right'), color='secondary'),
                    ]),
                ])
            ], className='mb-4')
        ], md=6),
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Icon Buttons')),
                dbc.CardBody([
                    dbc.Button([html.I(className='fas fa-download me-2'), 'Download'], color='success', className='me-2'),
                    dbc.Button([html.I(className='fas fa-upload me-2'), 'Upload'], color='info', className='me-2'),
                    dbc.Button([html.I(className='fas fa-trash me-2'), 'Delete'], color='danger', className='me-2'),
                    dbc.Button([html.I(className='fas fa-edit me-2'), 'Edit'], color='warning'),
                ])
            ])
        ], md=12)
    ])
])
