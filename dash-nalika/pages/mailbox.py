from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc

# Email list
email_list = [
    {'from': 'John Smith', 'subject': 'Project Update', 'preview': 'The latest updates on the project...', 'time': '10:30 AM', 'unread': True},
    {'from': 'Sarah Johnson', 'subject': 'Meeting Tomorrow', 'preview': 'Don\'t forget about our meeting...', 'time': '9:15 AM', 'unread': True},
    {'from': 'Mike Wilson', 'subject': 'Budget Approval', 'preview': 'Please review the attached budget...', 'time': 'Yesterday', 'unread': False},
    {'from': 'Emily Davis', 'subject': 'Design Review', 'preview': 'I\'ve completed the design mockups...', 'time': 'Yesterday', 'unread': False},
    {'from': 'Robert Brown', 'subject': 'Client Feedback', 'preview': 'The client has provided feedback...', 'time': '2 days ago', 'unread': False},
    {'from': 'Lisa Anderson', 'subject': 'Team Lunch', 'preview': 'Let\'s schedule a team lunch...', 'time': '3 days ago', 'unread': False},
]

# Sidebar with email folders
sidebar = dbc.Card([
    dbc.CardBody([
        dbc.Button('Compose', color='success', className='w-100 mb-3'),
        dbc.Nav([
            dbc.NavLink([html.I(className='fas fa-inbox me-2'), 'Inbox ', dbc.Badge('6', color='primary', className='ms-2')], href='#', active=True),
            dbc.NavLink([html.I(className='fas fa-star me-2'), 'Starred'], href='#'),
            dbc.NavLink([html.I(className='fas fa-paper-plane me-2'), 'Sent'], href='#'),
            dbc.NavLink([html.I(className='fas fa-file-alt me-2'), 'Drafts'], href='#'),
            dbc.NavLink([html.I(className='fas fa-trash me-2'), 'Trash'], href='#'),
        ], vertical=True, pills=True),
    ])
], style={'height': '100%'})

# Email list items
email_items = [
    dbc.ListGroupItem([
        dbc.Row([
            dbc.Col([
                html.Strong(email['from'], style={'color': '#ffffff' if email['unread'] else '#8899a6'}),
                html.Div(email['subject'], style={'color': '#ffffff' if email['unread'] else '#8899a6', 'fontSize': '14px'}),
                html.Small(email['preview'], style={'color': '#8899a6', 'fontSize': '12px'}),
            ], width=10),
            dbc.Col([
                html.Small(email['time'], style={'color': '#8899a6'}),
            ], width=2, className='text-end'),
        ]),
    ], style={
        'backgroundColor': '#1b2a47' if email['unread'] else '#152036',
        'border': '1px solid #152036',
        'cursor': 'pointer'
    }, className='mb-1')
    for email in email_list
]

# Main email list
email_list_panel = dbc.Card([
    dbc.CardHeader([
        dbc.Row([
            dbc.Col(html.H5('Inbox'), width=6),
            dbc.Col([
                dbc.ButtonGroup([
                    dbc.Button(html.I(className='fas fa-sync'), size='sm', color='secondary', outline=True),
                    dbc.Button(html.I(className='fas fa-trash'), size='sm', color='secondary', outline=True),
                ])
            ], width=6, className='text-end'),
        ])
    ]),
    dbc.CardBody([
        dbc.ListGroup(email_items, flush=True)
    ], style={'maxHeight': '600px', 'overflowY': 'auto'})
])

layout = html.Div([
    dbc.Breadcrumb(items=[
        {'label': 'Home', 'href': '/', 'active': False},
        {'label': 'Mailbox', 'active': True},
    ], className='breadcrumb'),
    
    dbc.Row([
        dbc.Col([sidebar], md=3),
        dbc.Col([email_list_panel], md=9),
    ])
])
