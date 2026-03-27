from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.Div([
                html.Img(src='https://ui-avatars.com/api/?name=Dr+Sarah+Johnson&background=6366f1&color=fff&size=100',
                         className='rounded-circle mb-3', width='100', height='100'),
                html.H4('Dr. Sarah Johnson', className='mb-1'),
                html.P('Computer Science Department', className='text-muted mb-2'),
                dbc.Badge('Active', color='success', className='mb-3'),
            ], className='text-center'),
            html.Hr(),
            html.Div([
                dbc.Row([dbc.Col(html.Span('Email', className='text-muted small')),        dbc.Col('sarah.johnson@university.edu', className='small')], className='mb-2'),
                dbc.Row([dbc.Col(html.Span('Phone', className='text-muted small')),        dbc.Col('+1 234 567 8900', className='small')], className='mb-2'),
                dbc.Row([dbc.Col(html.Span('Qualification', className='text-muted small')), dbc.Col('PhD Computer Science', className='small')], className='mb-2'),
                dbc.Row([dbc.Col(html.Span('Courses', className='text-muted small')),      dbc.Col('3 Active', className='small')], className='mb-2'),
                dbc.Row([dbc.Col(html.Span('Students', className='text-muted small')),     dbc.Col('120 Total', className='small')], className='mb-2'),
            ]),
            html.Hr(),
            dbc.ButtonGroup([
                dbc.Button([html.I(className='bi bi-pencil me-1'), 'Edit'], href='/edit-professor', color='primary', size='sm'),
                dbc.Button([html.I(className='bi bi-envelope me-1'), 'Message'], color='outline-secondary', size='sm'),
            ], className='w-100'),
        ])), md=3, className='mb-3'),

        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Courses Teaching', className='mb-0')),
                dbc.CardBody(dbc.Table([
                    html.Thead(html.Tr([html.Th('Course'), html.Th('Students'), html.Th('Schedule'), html.Th('Status')])),
                    html.Tbody([
                        html.Tr([html.Td('Advanced Programming'), html.Td('45'), html.Td('Mon/Wed 9AM'), html.Td(dbc.Badge('Active', color='success'))]),
                        html.Tr([html.Td('Data Structures'),      html.Td('42'), html.Td('Tue/Thu 11AM'), html.Td(dbc.Badge('Active', color='success'))]),
                        html.Tr([html.Td('Algorithms'),           html.Td('33'), html.Td('Fri 2PM'),      html.Td(dbc.Badge('Active', color='success'))]),
                    ]),
                ], striped=True, hover=True, responsive=True)),
            ], className='mb-3'),

            dbc.Card([
                dbc.CardHeader(html.H5('Recent Activity', className='mb-0')),
                dbc.CardBody([
                    *[dbc.Row([
                        dbc.Col(html.Div(className=f'rounded-circle bg-{color} bg-opacity-10',
                                         style={'width':'10px','height':'10px','marginTop':'6px','flexShrink':'0'}), width='auto'),
                        dbc.Col([html.Div(text, className='small fw-semibold'), html.Div(time, className='text-muted small')]),
                    ], className='mb-3')
                    for text, time, color in [
                        ('Graded midterm exams for Advanced Programming', '2 hours ago', 'primary'),
                        ('Posted assignment for Data Structures', '1 day ago', 'success'),
                        ('Updated course syllabus for Algorithms', '3 days ago', 'warning'),
                    ]],
                ]),
            ]),
        ], md=9),
    ]),
], fluid=True)
