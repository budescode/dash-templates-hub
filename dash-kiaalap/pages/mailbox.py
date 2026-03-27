from dash import html
import dash_bootstrap_components as dbc

emails = [
    {'from': 'Dr. Sarah Johnson', 'subject': 'Assignment Deadline Extended', 'time': '10:30 AM', 'read': False},
    {'from': 'Admin Office',      'subject': 'Semester Schedule Update',     'time': '9:15 AM',  'read': False},
    {'from': 'Dr. Michael Chen',  'subject': 'Calculus II Study Materials',  'time': 'Yesterday','read': True},
    {'from': 'Library',           'subject': 'Book Return Reminder',         'time': 'Yesterday','read': True},
    {'from': 'Student Council',   'subject': 'Annual Sports Day Invitation', 'time': 'Mon',      'read': True},
    {'from': 'IT Department',     'subject': 'System Maintenance Notice',    'time': 'Sun',      'read': True},
]

layout = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                dbc.Button([html.I(className='bi bi-pencil-square me-2'), 'Compose'],
                            href='/mailbox-compose', color='primary', className='w-100 mb-3'),
                dbc.Nav([
                    dbc.NavLink([html.I(className='bi bi-inbox me-2'), 'Inbox',
                                 dbc.Badge('2', color='primary', className='ms-auto')],
                                href='/mailbox', active=True, className='d-flex align-items-center'),
                    dbc.NavLink([html.I(className='bi bi-send me-2'), 'Sent'],       href='#'),
                    dbc.NavLink([html.I(className='bi bi-file me-2'), 'Drafts'],     href='#'),
                    dbc.NavLink([html.I(className='bi bi-star me-2'), 'Starred'],    href='#'),
                    dbc.NavLink([html.I(className='bi bi-trash me-2'), 'Trash'],     href='#'),
                ], vertical=True, pills=True),
            ]),
        ]), md=3, className='mb-3'),

        dbc.Col(dbc.Card([
            dbc.CardHeader(dbc.Row([
                dbc.Col(html.H5('Inbox', className='mb-0')),
                dbc.Col(dbc.InputGroup([
                    dbc.InputGroupText(html.I(className='bi bi-search')),
                    dbc.Input(type='text', placeholder='Search mail...'),
                ], size='sm'), md=5),
            ], align='center')),
            dbc.CardBody([
                *[dbc.Row([
                    dbc.Col(html.Div(e['from'][0], className='rounded-circle d-flex align-items-center justify-content-center text-white fw-bold bg-primary',
                                     style={'width':'38px','height':'38px','flexShrink':'0'}), width='auto'),
                    dbc.Col([
                        html.Div(e['from'], className=f"small {'fw-bold' if not e['read'] else ''}"),
                        html.Div(e['subject'], className=f"small {'fw-semibold' if not e['read'] else 'text-muted'}"),
                    ]),
                    dbc.Col([
                        html.Div(e['time'], className='text-muted small text-end'),
                        dbc.Badge('New', color='primary', className='mt-1') if not e['read'] else html.Span(),
                    ], width='auto', className='text-end'),
                ], align='center', className='py-2 border-bottom',
                   style={'cursor':'pointer', 'background': '#f8f9fa' if not e['read'] else 'white'})
                for e in emails],
            ]),
        ]), md=9, className='mb-3'),
    ]),
], fluid=True)
