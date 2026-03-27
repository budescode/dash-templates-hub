from dash import html
import dash_bootstrap_components as dbc

students = [
    {'name': 'Alex Johnson',   'dept': 'Computer Science',       'age': 20, 'color': '6366f1'},
    {'name': 'Sarah Miller',   'dept': 'Business Administration', 'age': 21, 'color': 'ec4899'},
    {'name': 'Mike Chen',      'dept': 'Engineering',             'age': 19, 'color': '10b981'},
    {'name': 'Emma Wilson',    'dept': 'Medicine',                'age': 22, 'color': 'f59e0b'},
    {'name': 'James Brown',    'dept': 'Psychology',              'age': 20, 'color': '8b5cf6'},
    {'name': 'Lisa Anderson',  'dept': 'Mathematics',             'age': 21, 'color': 'ef4444'},
    {'name': 'David Lee',      'dept': 'Physics',                 'age': 19, 'color': '14b8a6'},
    {'name': 'Amy Garcia',     'dept': 'Chemistry',               'age': 20, 'color': 'f97316'},
]

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(dbc.Row([
            dbc.Col(html.H4('All Students', className='mb-0')),
            dbc.Col(dbc.Button([html.I(className='bi bi-plus-circle me-2'), 'Add New Student'],
                               href='/add-student', color='primary'), width='auto'),
        ], align='center')),
        dbc.CardBody(dbc.Row([
            dbc.Col(dbc.InputGroup([
                dbc.InputGroupText(html.I(className='bi bi-search')),
                dbc.Input(type='text', placeholder='Search students...'),
            ]), md=6),
            dbc.Col(dbc.Select(options=[
                {'label': 'All Departments', 'value': 'all'},
                {'label': 'Computer Science', 'value': 'cs'},
                {'label': 'Engineering', 'value': 'eng'},
                {'label': 'Business', 'value': 'bus'},
                {'label': 'Medicine', 'value': 'med'},
            ], value='all'), md=3),
            dbc.Col(dbc.Select(options=[
                {'label': 'All Years', 'value': 'all'},
                {'label': 'First Year', 'value': '1'},
                {'label': 'Second Year', 'value': '2'},
                {'label': 'Third Year', 'value': '3'},
                {'label': 'Fourth Year', 'value': '4'},
            ], value='all'), md=3),
        ], className='g-2')),
    ]), className='mb-3')),

    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.Img(src=f"https://ui-avatars.com/api/?name={s['name'].replace(' ','+')}&background={s['color']}&color=fff",
                     className='rounded-circle mb-3', width='100', height='100'),
            html.H5(s['name'], className='mb-1'),
            html.P(s['dept'], className='text-muted mb-2'),
            html.P([html.Strong('Age: '), f"{s['age']} Years"], className='text-muted small mb-3'),
            dbc.ButtonGroup([
                dbc.Button([html.I(className='bi bi-eye'), ' View'], href='/student-profile',
                            color='outline-primary', size='sm'),
                dbc.Button([html.I(className='bi bi-pencil'), ' Edit'], href='/edit-student',
                            color='outline-secondary', size='sm'),
            ]),
        ], className='text-center'), className='h-100'), md=3, className='mb-3')
        for s in students
    ]),

    dbc.Row(dbc.Col(dbc.Pagination(
        max_value=3, active_page=1, fully_expanded=False, className='justify-content-center'
    ), className='mt-2')),
], fluid=True)
