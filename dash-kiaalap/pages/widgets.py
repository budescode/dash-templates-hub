from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.Div([html.I(className='bi bi-people-fill', style={'fontSize':'32px','color':'#6366f1'})],
                     className='rounded-circle d-flex align-items-center justify-content-center mb-3',
                     style={'width':'64px','height':'64px','background':'rgba(99,102,241,0.1)'}),
            html.H3('1,340', className='fw-bold mb-1'),
            html.P('Total Students', className='text-muted mb-0'),
            html.Span('+12%', className='text-success small'),
        ])), md=3, className='mb-3'),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.Div([html.I(className='bi bi-person-badge-fill', style={'fontSize':'32px','color':'#10b981'})],
                     className='rounded-circle d-flex align-items-center justify-content-center mb-3',
                     style={'width':'64px','height':'64px','background':'rgba(16,185,129,0.1)'}),
            html.H3('86', className='fw-bold mb-1'),
            html.P('Total Professors', className='text-muted mb-0'),
            html.Span('+3 new', className='text-success small'),
        ])), md=3, className='mb-3'),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.Div([html.I(className='bi bi-book-fill', style={'fontSize':'32px','color':'#f59e0b'})],
                     className='rounded-circle d-flex align-items-center justify-content-center mb-3',
                     style={'width':'64px','height':'64px','background':'rgba(245,158,11,0.1)'}),
            html.H3('124', className='fw-bold mb-1'),
            html.P('Active Courses', className='text-muted mb-0'),
            html.Span('+8 this semester', className='text-warning small'),
        ])), md=3, className='mb-3'),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.Div([html.I(className='bi bi-building-fill', style={'fontSize':'32px','color':'#ef4444'})],
                     className='rounded-circle d-flex align-items-center justify-content-center mb-3',
                     style={'width':'64px','height':'64px','background':'rgba(239,68,68,0.1)'}),
            html.H3('12', className='fw-bold mb-1'),
            html.P('Departments', className='text-muted mb-0'),
            html.Span('2 new this year', className='text-danger small'),
        ])), md=3, className='mb-3'),
    ]),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5('Progress Widgets', className='mb-0')),
            dbc.CardBody([
                *[html.Div([
                    dbc.Row([dbc.Col(html.Span(label, className='small fw-semibold')), dbc.Col(html.Span(f'{val}%', className='small text-muted'), width='auto')], className='mb-1'),
                    dbc.Progress(value=val, color=color, style={'height':'8px'}, className='mb-3'),
                ]) for label, val, color in [
                    ('Computer Science', 85, 'primary'),
                    ('Engineering', 72, 'success'),
                    ('Business Admin', 68, 'warning'),
                    ('Medicine', 55, 'danger'),
                ]],
            ]),
        ]), md=6, className='mb-3'),

        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5('Quick Actions', className='mb-0')),
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(dbc.Button([html.I(className='bi bi-person-plus me-2'), 'Add Student'],   href='/add-student',   color='primary',   className='w-100 mb-2')),
                    dbc.Col(dbc.Button([html.I(className='bi bi-person-badge me-2'), 'Add Professor'], href='/add-professor', color='success',   className='w-100 mb-2')),
                ]),
                dbc.Row([
                    dbc.Col(dbc.Button([html.I(className='bi bi-book me-2'), 'Add Course'],           href='/add-course',    color='warning',   className='w-100 mb-2')),
                    dbc.Col(dbc.Button([html.I(className='bi bi-envelope me-2'), 'Compose Mail'],     href='/mailbox-compose', color='info',    className='w-100 mb-2')),
                ]),
            ]),
        ]), md=6, className='mb-3'),
    ]),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5('Notification Badges', className='mb-0')),
            dbc.CardBody([
                html.Div([
                    dbc.Badge('Primary', color='primary', className='me-2'),
                    dbc.Badge('Secondary', color='secondary', className='me-2'),
                    dbc.Badge('Success', color='success', className='me-2'),
                    dbc.Badge('Danger', color='danger', className='me-2'),
                    dbc.Badge('Warning', color='warning', className='me-2'),
                    dbc.Badge('Info', color='info', className='me-2'),
                    dbc.Badge('Light', color='light', text_color='dark', className='me-2'),
                    dbc.Badge('Dark', color='dark', className='me-2'),
                ]),
            ]),
        ]), className='mb-3'),
    ]),
], fluid=True)
