from dash import html
import dash_bootstrap_components as dbc

departments = [
    {'name': 'Computer Science',       'head': 'Dr. Sarah Johnson', 'professors': 12, 'students': 320, 'courses': 24, 'color': 'primary'},
    {'name': 'Mathematics',            'head': 'Dr. Michael Chen',  'professors': 8,  'students': 280, 'courses': 18, 'color': 'success'},
    {'name': 'Biology',                'head': 'Dr. Lisa Thompson', 'professors': 10, 'students': 190, 'courses': 20, 'color': 'info'},
    {'name': 'Engineering',            'head': 'Dr. David Wilson',  'professors': 15, 'students': 250, 'courses': 30, 'color': 'warning'},
    {'name': 'Physics',                'head': 'Dr. Emma Davis',    'professors': 7,  'students': 160, 'courses': 14, 'color': 'danger'},
    {'name': 'Business Administration','head': 'Dr. James Lee',     'professors': 11, 'students': 300, 'courses': 22, 'color': 'secondary'},
]

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(dbc.Row([
            dbc.Col(html.H4('Departments', className='mb-0')),
            dbc.Col(dbc.Button([html.I(className='bi bi-plus-circle me-2'), 'Add Department'],
                               href='/add-department', color='primary'), width='auto'),
        ], align='center')),
    ]), className='mb-3')),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(html.Div(className=f'rounded-circle bg-{d["color"]} bg-opacity-10',
                                     style={'width':'12px','height':'12px','marginTop':'4px'}), width='auto'),
                    dbc.Col(html.H5(d['name'], className='mb-0')),
                    dbc.Col(dbc.ButtonGroup([
                        dbc.Button(html.I(className='bi bi-pencil'), href='/edit-department', color='outline-primary', size='sm'),
                        dbc.Button(html.I(className='bi bi-trash'), color='outline-danger', size='sm'),
                    ]), width='auto'),
                ], align='center', className='mb-3'),
                html.Div(f'Head: {d["head"]}', className='text-muted small mb-2'),
                dbc.Row([
                    dbc.Col([html.Div(str(d['professors']), className='fw-bold'), html.Div('Professors', className='text-muted small')], className='text-center'),
                    dbc.Col([html.Div(str(d['students']),   className='fw-bold'), html.Div('Students',   className='text-muted small')], className='text-center'),
                    dbc.Col([html.Div(str(d['courses']),    className='fw-bold'), html.Div('Courses',    className='text-muted small')], className='text-center'),
                ]),
            ]),
        ]), md=4, className='mb-3')
        for d in departments
    ]),
], fluid=True)
