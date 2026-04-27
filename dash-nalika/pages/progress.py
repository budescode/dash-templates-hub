from dash import html, callback, Input, Output, dcc
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Breadcrumb(items=[
        {'label': 'Home', 'href': '/', 'active': False},
        {'label': 'Progress & Spinners', 'active': True},
    ], className='breadcrumb'),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Progress Bars')),
                dbc.CardBody([
                    html.P('Basic Progress'),
                    dbc.Progress(value=25, className='mb-3'),
                    html.P('Colored Progress'),
                    dbc.Progress(value=50, color='success', className='mb-3'),
                    dbc.Progress(value=75, color='warning', className='mb-3'),
                    dbc.Progress(value=100, color='danger', className='mb-3'),
                    html.P('Striped Progress'),
                    dbc.Progress(value=60, striped=True, color='info', className='mb-3'),
                    html.P('Animated Progress'),
                    dbc.Progress(value=80, striped=True, animated=True, color='success'),
                ])
            ], className='mb-4')
        ], md=6),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Spinners')),
                dbc.CardBody([
                    html.P('Border Spinners'),
                    html.Div([
                        dbc.Spinner(color='primary', spinner_class_name='me-2'),
                        dbc.Spinner(color='success', spinner_class_name='me-2'),
                        dbc.Spinner(color='warning', spinner_class_name='me-2'),
                        dbc.Spinner(color='danger', spinner_class_name='me-2'),
                        dbc.Spinner(color='info'),
                    ], className='mb-4'),
                    html.P('Grow Spinners'),
                    html.Div([
                        dbc.Spinner(color='primary', type='grow', spinner_class_name='me-2'),
                        dbc.Spinner(color='success', type='grow', spinner_class_name='me-2'),
                        dbc.Spinner(color='warning', type='grow', spinner_class_name='me-2'),
                        dbc.Spinner(color='danger', type='grow', spinner_class_name='me-2'),
                        dbc.Spinner(color='info', type='grow'),
                    ]),
                ])
            ])
        ], md=6),
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Loading States')),
                dbc.CardBody([
                    dbc.Button('Load Data', id='loading-button', color='primary', className='mb-3'),
                    dbc.Spinner(html.Div(id='loading-output'), color='primary'),
                ])
            ])
        ], md=12)
    ])
])

@callback(
    Output('loading-output', 'children'),
    Input('loading-button', 'n_clicks'),
)
def load_data(n):
    if n:
        return html.Div('Data loaded successfully!', className='alert alert-success')
    return html.Div('Click the button to load data.')
