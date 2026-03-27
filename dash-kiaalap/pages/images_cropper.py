from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(html.H5('Image Cropper', className='mb-0')),
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    html.H6('Upload Image', className='mb-2'),
                    html.Div([
                        html.I(className='bi bi-image', style={'fontSize': '64px', 'color': '#d1d5db'}),
                        html.P('Upload an image to crop', className='text-muted mt-2'),
                        dbc.Button([html.I(className='bi bi-upload me-2'), 'Choose Image'], color='primary', size='sm'),
                    ], className='text-center p-4 border rounded', style={'background': '#f9fafb', 'minHeight': '200px',
                                                                           'display': 'flex', 'flexDirection': 'column',
                                                                           'alignItems': 'center', 'justifyContent': 'center'}),
                ], md=6, className='mb-3'),
                dbc.Col([
                    html.H6('Preview', className='mb-2'),
                    html.Div([
                        html.I(className='bi bi-crop', style={'fontSize': '64px', 'color': '#d1d5db'}),
                        html.P('Cropped image will appear here', className='text-muted mt-2'),
                    ], className='text-center p-4 border rounded', style={'background': '#f9fafb', 'minHeight': '200px',
                                                                           'display': 'flex', 'flexDirection': 'column',
                                                                           'alignItems': 'center', 'justifyContent': 'center'}),
                ], md=6, className='mb-3'),
            ]),
            html.H6('Crop Settings', className='mb-2'),
            dbc.Row([
                dbc.Col([dbc.Label('Aspect Ratio'), dbc.Select(options=[
                    {'label': 'Free', 'value': 'free'},
                    {'label': '1:1 (Square)', 'value': '1:1'},
                    {'label': '4:3', 'value': '4:3'},
                    {'label': '16:9', 'value': '16:9'},
                ])], md=4, className='mb-3'),
                dbc.Col([dbc.Label('Width (px)'), dbc.Input(type='number', placeholder='300')], md=4, className='mb-3'),
                dbc.Col([dbc.Label('Height (px)'), dbc.Input(type='number', placeholder='300')], md=4, className='mb-3'),
            ]),
            dbc.ButtonGroup([
                dbc.Button([html.I(className='bi bi-crop me-1'), 'Crop'], color='primary'),
                dbc.Button([html.I(className='bi bi-download me-1'), 'Download'], color='success'),
                dbc.Button([html.I(className='bi bi-arrow-counterclockwise me-1'), 'Reset'], color='outline-secondary'),
            ]),
        ]),
    ]))),
], fluid=True)
