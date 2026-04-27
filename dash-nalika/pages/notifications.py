from dash import html, callback, Input, Output, State
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Breadcrumb(items=[
        {'label': 'Home', 'href': '/', 'active': False},
        {'label': 'Notifications', 'active': True},
    ], className='breadcrumb'),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Alerts')),
                dbc.CardBody([
                    dbc.Alert('This is a primary alert', color='primary', className='mb-2'),
                    dbc.Alert('This is a success alert', color='success', className='mb-2'),
                    dbc.Alert('This is a warning alert', color='warning', className='mb-2'),
                    dbc.Alert('This is a danger alert', color='danger', className='mb-2'),
                    dbc.Alert([
                        html.H4('Well done!', className='alert-heading'),
                        html.P('You successfully read this important alert message.'),
                        html.Hr(),
                        html.P('Additional information here.', className='mb-0'),
                    ], color='info'),
                ])
            ], className='mb-4')
        ], md=6),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Badges')),
                dbc.CardBody([
                    html.H5(['Primary ', dbc.Badge('New', color='primary', className='ms-1')]),
                    html.H5(['Success ', dbc.Badge('5', color='success', className='ms-1')]),
                    html.H5(['Warning ', dbc.Badge('Alert', color='warning', className='ms-1')]),
                    html.H5(['Danger ', dbc.Badge('99+', color='danger', className='ms-1')]),
                    html.Hr(),
                    dbc.Button(['Notifications ', dbc.Badge('4', color='light', className='ms-2')], color='primary'),
                ])
            ], className='mb-4')
        ], md=6),
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Toast Notifications')),
                dbc.CardBody([
                    dbc.Button('Show Toast', id='toast-trigger', color='primary'),
                    dbc.Toast(
                        'This is a toast notification!',
                        id='toast',
                        header='Notification',
                        is_open=False,
                        dismissable=True,
                        icon='success',
                        duration=4000,
                        style={'position': 'fixed', 'top': 66, 'right': 10, 'width': 350}
                    ),
                ])
            ])
        ], md=12)
    ])
])

@callback(
    Output('toast', 'is_open'),
    Input('toast-trigger', 'n_clicks'),
    State('toast', 'is_open'),
)
def toggle_toast(n, is_open):
    if n:
        return not is_open
    return is_open
