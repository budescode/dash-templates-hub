from dash import html
import dash_bootstrap_components as dbc

courses = [
    {'name': 'Advanced Programming', 'prof': 'Prof. Sarah Johnson', 'students': 45, 'icon': 'code-slash',  'color': '#0d6efd', 'bg': 'rgba(13,110,253,0.1)',  'full': '85%', 'badge': 'primary'},
    {'name': 'Calculus II',           'prof': 'Prof. Michael Chen',  'students': 38, 'icon': 'calculator',  'color': '#198754', 'bg': 'rgba(25,135,84,0.1)',   'full': '76%', 'badge': 'success'},
    {'name': 'Biology Lab',           'prof': 'Prof. Lisa Thompson', 'students': 28, 'icon': 'microscope',  'color': '#0dcaf0', 'bg': 'rgba(13,202,240,0.1)',  'full': '56%', 'badge': 'info'},
    {'name': 'Data Structures',       'prof': 'Prof. David Wilson',  'students': 42, 'icon': 'diagram-3',   'color': '#ffc107', 'bg': 'rgba(255,193,7,0.1)',   'full': '84%', 'badge': 'warning'},
    {'name': 'Physics I',             'prof': 'Prof. Emma Davis',    'students': 35, 'icon': 'lightning',   'color': '#dc3545', 'bg': 'rgba(220,53,69,0.1)',   'full': '70%', 'badge': 'danger'},
    {'name': 'Chemistry Lab',         'prof': 'Prof. James Lee',     'students': 30, 'icon': 'flask',       'color': '#6f42c1', 'bg': 'rgba(111,66,193,0.1)',  'full': '60%', 'badge': 'secondary'},
]

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(dbc.Row([
            dbc.Col(html.H4('All Courses', className='mb-0')),
            dbc.Col(dbc.Button([html.I(className='bi bi-plus-circle me-2'), 'Add New Course'],
                               href='/add-course', color='primary'), width='auto'),
        ], align='center')),
        dbc.CardBody(dbc.Row([
            dbc.Col(dbc.InputGroup([
                dbc.InputGroupText(html.I(className='bi bi-search')),
                dbc.Input(type='text', placeholder='Search courses...'),
            ]), md=8),
            dbc.Col(dbc.Select(options=[
                {'label': 'All Departments', 'value': 'all'},
                {'label': 'Computer Science', 'value': 'cs'},
                {'label': 'Engineering', 'value': 'eng'},
                {'label': 'Science', 'value': 'sci'},
            ], value='all'), md=4),
        ], className='g-2')),
    ]), className='mb-3')),

    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            dbc.Row([
                dbc.Col(html.Div(
                    html.I(className=f"bi bi-{c['icon']}", style={'fontSize': '24px', 'color': c['color']}),
                    className='rounded-circle d-flex align-items-center justify-content-center',
                    style={'width': '52px', 'height': '52px', 'background': c['bg'], 'flexShrink': '0'}
                ), width='auto'),
                dbc.Col([
                    html.H6(c['name'], className='mb-1'),
                    html.Div(c['prof'], className='text-muted small'),
                    html.Div([html.I(className='bi bi-people me-1'), f"{c['students']} enrolled"],
                             className='text-muted small'),
                ]),
            ], align='center', className='mb-3'),
            dbc.Row([
                dbc.Col(dbc.Badge(c['full'] + ' Full', color=c['badge'])),
                dbc.Col(dbc.ButtonGroup([
                    dbc.Button([html.I(className='bi bi-eye'), ' View'], href='/course-info',
                                color='outline-primary', size='sm'),
                    dbc.Button([html.I(className='bi bi-pencil'), ' Edit'], href='/edit-course',
                                color='outline-secondary', size='sm'),
                ]), width='auto'),
            ], align='center'),
        ])), md=4, className='mb-3')
        for c in courses
    ]),
], fluid=True)
