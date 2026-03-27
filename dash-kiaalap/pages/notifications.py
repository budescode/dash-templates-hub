from dash import html
import dash_bootstrap_components as dbc

notifications = [
    {'icon': 'bi-person-plus',    'color': 'primary', 'text': 'New student Alex Johnson enrolled',          'time': '2 min ago'},
    {'icon': 'bi-book',           'color': 'success', 'text': 'Course "Advanced Programming" is now full',  'time': '15 min ago'},
    {'icon': 'bi-exclamation-triangle', 'color': 'warning', 'text': 'Assignment deadline in 2 days',        'time': '1 hour ago'},
    {'icon': 'bi-envelope',       'color': 'info',    'text': 'New message from Dr. Sarah Johnson',         'time': '3 hours ago'},
    {'icon': 'bi-calendar-event', 'color': 'danger',  'text': 'Science Fair scheduled for March 15',        'time': '1 day ago'},
    {'icon': 'bi-check-circle',   'color': 'success', 'text': 'Grades submitted for Calculus II',           'time': '2 days ago'},
]

layout = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader(dbc.Row([
                dbc.Col(html.H5('Notifications', className='mb-0')),
                dbc.Col(dbc.Button('Mark All Read', color='outline-primary', size='sm'), width='auto'),
            ], align='center')),
            dbc.CardBody([
                *[dbc.Row([
                    dbc.Col(html.Div(html.I(className=f'bi {n["icon"]}', style={'fontSize':'18px','color':f'var(--bs-{n["color"]})'}),
                                     className=f'rounded-circle d-flex align-items-center justify-content-center bg-{n["color"]} bg-opacity-10',
                                     style={'width':'42px','height':'42px','flexShrink':'0'}), width='auto'),
                    dbc.Col([
                        html.Div(n['text'], className='small fw-semibold'),
                        html.Div(n['time'], className='text-muted small'),
                    ]),
                    dbc.Col(dbc.Button(html.I(className='bi bi-x'), color='light', size='sm', className='border-0'), width='auto'),
                ], align='center', className='py-2 border-bottom')
                for n in notifications],
            ]),
        ]), md=8, className='mb-3'),

        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5('Notification Settings', className='mb-0')),
            dbc.CardBody([
                html.P('Configure which notifications you receive.', className='text-muted small mb-3'),
                *[dbc.Row([
                    dbc.Col(html.Span(label, className='small')),
                    dbc.Col(dbc.Switch(value=val, id=f'notif-{i}'), width='auto'),
                ], align='center', className='mb-3')
                for i, (label, val) in enumerate([
                    ('New Enrollments', True),
                    ('Course Updates', True),
                    ('Assignment Deadlines', True),
                    ('New Messages', False),
                    ('System Alerts', True),
                ])],
            ]),
        ]), md=4, className='mb-3'),
    ]),
], fluid=True)
