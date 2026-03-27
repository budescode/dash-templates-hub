from dash import html
import dash_bootstrap_components as dbc

professors = [
    {'name': 'Dr. Sarah Johnson', 'dept': 'Computer Science', 'courses': 3, 'students': 120, 'color': '6366f1'},
    {'name': 'Dr. Michael Chen',  'dept': 'Mathematics',      'courses': 4, 'students': 150, 'color': '10b981'},
    {'name': 'Dr. Lisa Thompson', 'dept': 'Biology',           'courses': 2, 'students': 80,  'color': 'ec4899'},
    {'name': 'Dr. David Wilson',  'dept': 'Engineering',       'courses': 3, 'students': 110, 'color': 'f59e0b'},
    {'name': 'Dr. Emma Davis',    'dept': 'Physics',           'courses': 2, 'students': 90,  'color': 'ef4444'},
    {'name': 'Dr. James Lee',     'dept': 'Chemistry',         'courses': 3, 'students': 100, 'color': '8b5cf6'},
]

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(dbc.Row([
            dbc.Col(html.H4('All Professors', className='mb-0')),
            dbc.Col(dbc.Button([html.I(className='bi bi-plus-circle me-2'), 'Add New Professor'],
                               href='/add-professor', color='primary'), width='auto'),
        ], align='center')),
        dbc.CardBody(dbc.Row([
            dbc.Col(dbc.InputGroup([
                dbc.InputGroupText(html.I(className='bi bi-search')),
                dbc.Input(type='text', placeholder='Search professors...'),
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
            html.Img(src=f"https://ui-avatars.com/api/?name={p['name'].replace(' ','+')}&background={p['color']}&color=fff",
                     className='rounded-circle mb-3', width='100', height='100'),
            html.H5(p['name'], className='mb-1'),
            html.P(p['dept'], className='text-muted mb-2'),
            html.Div([
                html.Span([html.I(className='bi bi-book me-1'), f"{p['courses']} Courses"],
                          className='text-muted small me-3'),
                html.Span([html.I(className='bi bi-people me-1'), f"{p['students']} Students"],
                          className='text-muted small'),
            ], className='mb-3'),
            dbc.ButtonGroup([
                dbc.Button([html.I(className='bi bi-eye'), ' View'], href='/professor-profile',
                            color='outline-primary', size='sm'),
                dbc.Button([html.I(className='bi bi-pencil'), ' Edit'], href='/edit-professor',
                            color='outline-secondary', size='sm'),
            ]),
        ], className='text-center'), className='h-100'), md=4, className='mb-3')
        for p in professors
    ]),
], fluid=True)
