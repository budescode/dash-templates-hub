from dash import html, callback, Input, Output, State
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Breadcrumb(items=[
        {'label': 'Home', 'href': '/', 'active': False},
        {'label': 'Modals', 'active': True},
    ], className='breadcrumb'),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Modal Examples')),
                dbc.CardBody([
                    dbc.Button('Basic Modal', id='open-basic', color='primary', className='me-2'),
                    dbc.Button('Scrollable Modal', id='open-scroll', color='success', className='me-2'),
                    dbc.Button('Centered Modal', id='open-centered', color='info'),
                ])
            ])
        ], md=12)
    ]),
    
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Basic Modal')),
        dbc.ModalBody('This is a basic modal dialog.'),
        dbc.ModalFooter([
            dbc.Button('Close', id='close-basic', color='secondary'),
            dbc.Button('Save', color='primary'),
        ]),
    ], id='modal-basic', is_open=False),
    
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Scrollable Modal')),
        dbc.ModalBody([html.P('Lorem ipsum dolor sit amet. ' * 50)]),
        dbc.ModalFooter(dbc.Button('Close', id='close-scroll', color='secondary')),
    ], id='modal-scroll', scrollable=True, is_open=False),
    
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Centered Modal')),
        dbc.ModalBody('This modal is vertically centered.'),
        dbc.ModalFooter(dbc.Button('Close', id='close-centered', color='secondary')),
    ], id='modal-centered', centered=True, is_open=False),
])

@callback(
    Output('modal-basic', 'is_open'),
    [Input('open-basic', 'n_clicks'), Input('close-basic', 'n_clicks')],
    State('modal-basic', 'is_open'),
)
def toggle_basic(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@callback(
    Output('modal-scroll', 'is_open'),
    [Input('open-scroll', 'n_clicks'), Input('close-scroll', 'n_clicks')],
    State('modal-scroll', 'is_open'),
)
def toggle_scroll(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@callback(
    Output('modal-centered', 'is_open'),
    [Input('open-centered', 'n_clicks'), Input('close-centered', 'n_clicks')],
    State('modal-centered', 'is_open'),
)
def toggle_centered(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
