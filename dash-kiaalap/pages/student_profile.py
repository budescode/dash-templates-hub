from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.Div([
                html.Img(src='https://ui-avatars.com/api/?name=Alex+Johnson&background=6366f1&color=fff&size=100',
                         className='rounded-circle mb-3', width='100', height='100'),
                html.H4('Alex Johnson', className='mb-1'),
                html.P('Computer Science - Second Year', className='text-muted mb-2'),
                dbc.Badge('Active', color='success', className='mb-3'),
            ], className='text-center'),
            html.Hr(),
            html.Div([
                dbc.Row([dbc.Col(html.Span('Email', className='text-muted small')), dbc.Col('alex.johnson@email.com', className='small')], className='mb-2'),
                dbc.Row([dbc.Col(html.Span('Phone', className='text-muted small')), dbc.Col('+1 234 567 8900', className='small')], className='mb-2'),
                dbc.Row([dbc.Col(html.Span('Age', className='text-muted small')),   dbc.Col('20 Years', className='small')], className='mb-2'),
                dbc.Row([dbc.Col(html.Span('Gender', className='text-muted small')), dbc.Col('Male', className='small')], className='mb-2'),
                dbc.Row([dbc.Col(html.Span('Enrolled', className='text-muted small')), dbc.Col('Sep 2023', className='small')], className='mb-2'),
            ]),
            html.Hr(),
            dbc.ButtonGroup([
                dbc.Button([html.I(className='bi bi-pencil me-1'), 'Edit'], href='/edit-student', color='primary', size='sm'),
                dbc.Button([html.I(className='bi bi-envelope me-1'), 'Message'], color='outline-secondary', size='sm'),
            ], className='w-100'),
        ])), md=3, className='mb-3'),

        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Academic Performance', className='mb-0')),
                dbc.CardBody(dbc.Table([
                    html.Thead(html.Tr([html.Th('Course'), html.Th('Grade'), html.Th('Credits'), html.Th('Status')])),
                    html.Tbody([
                        html.Tr([html.Td('Data Structures'), html.Td('A'), html.Td('3'), html.Td(dbc.Badge('Passed', color='success'))]),
                        html.Tr([html.Td('Calculus II'),     html.Td('B+'), html.Td('4'), html.Td(dbc.Badge('Passed', color='success'))]),
                        html.Tr([html.Td('Physics I'),       html.Td('A-'), html.Td('3'), html.Td(dbc.Badge('Passed', color='success'))]),
                        html.Tr([html.Td('English Comp'),    html.Td('B'),  html.Td('2'), html.Td(dbc.Badge('Passed', color='success'))]),
                    ]),
                ], striped=True, hover=True, responsive=True)),
            ], className='mb-3'),

            dbc.Card([
                dbc.CardHeader(html.H5('Enrolled Courses', className='mb-0')),
                dbc.CardBody([
                    *[dbc.Row([
                        dbc.Col(html.Div(html.I(className=f'bi bi-{icon}', style={'color': color}),
                                         className='rounded d-flex align-items-center justify-content-center',
                                         style={'width':'40px','height':'40px','background':bg}), width='auto'),
                        dbc.Col([html.Div(name, className='fw-semibold small'), html.Div(prof, className='text-muted small')]),
                        dbc.Col(dbc.Badge(grade, color=gc), width='auto', className='align-self-center'),
                    ], align='center', className='mb-3')
                    for icon, color, bg, name, prof, grade, gc in [
                        ('code-slash','#0d6efd','rgba(13,110,253,0.1)','Advanced Programming','Prof. Sarah Johnson','A','primary'),
                        ('calculator','#198754','rgba(25,135,84,0.1)','Calculus II','Prof. Michael Chen','B+','success'),
                        ('lightning','#dc3545','rgba(220,53,69,0.1)','Physics I','Prof. Emma Davis','A-','danger'),
                    ]],
                ]),
            ]),
        ], md=9),
    ]),
], fluid=True)
