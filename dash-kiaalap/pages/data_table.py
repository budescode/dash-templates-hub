from dash import html
import dash_bootstrap_components as dbc

rows = [
    ('Alex Johnson',   'Computer Science', 'Freshman',  'Active',   'A'),
    ('Sarah Miller',   'Business Admin',   'Sophomore', 'Active',   'B+'),
    ('Mike Chen',      'Engineering',      'Junior',    'Active',   'A-'),
    ('Emma Wilson',    'Medicine',         'Senior',    'Inactive', 'B'),
    ('James Brown',    'Psychology',       'Freshman',  'Active',   'B+'),
    ('Lisa Anderson',  'Mathematics',      'Sophomore', 'Active',   'A'),
    ('David Lee',      'Physics',          'Junior',    'Active',   'A-'),
    ('Amy Garcia',     'Chemistry',        'Senior',    'Inactive', 'C+'),
]

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(dbc.Row([
            dbc.Col(html.H5('Student Data Table', className='mb-0')),
            dbc.Col(dbc.InputGroup([
                dbc.InputGroupText(html.I(className='bi bi-search')),
                dbc.Input(type='text', placeholder='Search...', size='sm'),
            ], size='sm'), md=4),
        ], align='center')),
        dbc.CardBody([
            dbc.Table([
                html.Thead(html.Tr([
                    html.Th([dbc.Checkbox(className='form-check-input')]),
                    html.Th('Name'), html.Th('Department'), html.Th('Year'),
                    html.Th('Status'), html.Th('Grade'), html.Th('Actions'),
                ])),
                html.Tbody([
                    html.Tr([
                        html.Td(dbc.Checkbox(className='form-check-input')),
                        html.Td(name), html.Td(dept), html.Td(year),
                        html.Td(dbc.Badge(status, color='success' if status == 'Active' else 'secondary')),
                        html.Td(grade),
                        html.Td(dbc.ButtonGroup([
                            dbc.Button(html.I(className='bi bi-eye'),    href='/student-profile', color='outline-primary',   size='sm'),
                            dbc.Button(html.I(className='bi bi-pencil'), href='/edit-student',    color='outline-secondary', size='sm'),
                            dbc.Button(html.I(className='bi bi-trash'),                           color='outline-danger',    size='sm'),
                        ])),
                    ]) for name, dept, year, status, grade in rows
                ]),
            ], striped=True, hover=True, responsive=True, bordered=False),
            dbc.Row([
                dbc.Col(html.Small(f'Showing 1 to {len(rows)} of {len(rows)} entries', className='text-muted')),
                dbc.Col(dbc.Pagination(max_value=3, active_page=1, fully_expanded=False,
                                        className='justify-content-end mb-0'), ),
            ], align='center', className='mt-3'),
        ]),
    ]))),
], fluid=True)
