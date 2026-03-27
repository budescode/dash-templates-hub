from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.Div(html.I(className='bi bi-code-slash', style={'fontSize':'40px','color':'#0d6efd'}),
                     className='rounded-circle d-flex align-items-center justify-content-center mx-auto mb-3',
                     style={'width':'80px','height':'80px','background':'rgba(13,110,253,0.1)'}),
            html.H4('Advanced Programming', className='text-center mb-1'),
            html.P('CS401 · Computer Science', className='text-center text-muted mb-3'),
            dbc.Badge('85% Full', color='success', className='d-block text-center mb-3'),
            html.Hr(),
            dbc.Row([dbc.Col(html.Span('Professor', className='text-muted small')), dbc.Col('Dr. Sarah Johnson', className='small')], className='mb-2'),
            dbc.Row([dbc.Col(html.Span('Credits', className='text-muted small')),   dbc.Col('3 Credits', className='small')], className='mb-2'),
            dbc.Row([dbc.Col(html.Span('Duration', className='text-muted small')),  dbc.Col('16 Weeks', className='small')], className='mb-2'),
            dbc.Row([dbc.Col(html.Span('Schedule', className='text-muted small')),  dbc.Col('Mon/Wed 9AM', className='small')], className='mb-2'),
            dbc.Row([dbc.Col(html.Span('Enrolled', className='text-muted small')),  dbc.Col('45 / 53 Students', className='small')], className='mb-2'),
            html.Hr(),
            dbc.ButtonGroup([
                dbc.Button([html.I(className='bi bi-pencil me-1'), 'Edit'], href='/edit-course', color='primary', size='sm'),
                dbc.Button([html.I(className='bi bi-credit-card me-1'), 'Payment'], href='/course-payment', color='outline-secondary', size='sm'),
            ], className='w-100'),
        ])), md=3, className='mb-3'),

        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Course Description', className='mb-0')),
                dbc.CardBody(html.P('An advanced course covering modern programming paradigms, design patterns, algorithms, and software engineering best practices. Students will work on real-world projects and develop production-quality code.')),
            ], className='mb-3'),
            dbc.Card([
                dbc.CardHeader(html.H5('Enrolled Students', className='mb-0')),
                dbc.CardBody(dbc.Table([
                    html.Thead(html.Tr([html.Th('Student'), html.Th('Department'), html.Th('Grade'), html.Th('Attendance')])),
                    html.Tbody([
                        html.Tr([html.Td('Alex Johnson'), html.Td('Computer Science'), html.Td('A'),  html.Td('95%')]),
                        html.Tr([html.Td('Sarah Miller'), html.Td('Computer Science'), html.Td('B+'), html.Td('88%')]),
                        html.Tr([html.Td('Mike Chen'),    html.Td('Engineering'),      html.Td('A-'), html.Td('92%')]),
                        html.Tr([html.Td('Emma Wilson'),  html.Td('Computer Science'), html.Td('B'),  html.Td('85%')]),
                    ]),
                ], striped=True, hover=True, responsive=True)),
            ]),
        ], md=9),
    ]),
], fluid=True)
