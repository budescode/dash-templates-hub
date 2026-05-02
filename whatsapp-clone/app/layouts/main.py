from dash import html, dcc
import dash_bootstrap_components as dbc


def get_main_layout():
    return html.Div([
        dcc.Location(id='url', refresh=False),
        dcc.Store(id='session-store', storage_type='local'),
        dcc.Store(id='current-user-store', storage_type='session'),
        dcc.Store(id='active-conversation-store', storage_type='session'),
        dcc.Store(id='messages-store', storage_type='memory'),
        dcc.Store(id='conversations-store', storage_type='memory'),
        dcc.Store(id='last-message-id-store', storage_type='memory', data=0),
        dcc.Interval(id='poll-interval', interval=1500, n_intervals=0),
        html.Div(id='page-content', className='h-100'),
        html.Div(id='typing-send-dummy', style={'display': 'none'}),
        html.Div(
            id='toast-container',
            style={
                'position': 'fixed', 'top': '20px',
                'right': '20px', 'zIndex': 9999,
            },
        ),
    ], style={'height': '100vh', 'overflow': 'hidden'})
