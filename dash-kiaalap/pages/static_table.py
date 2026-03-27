from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    html.Div([
        html.H1('Static Tables', className='h3 font-bold'),
        html.P('Simple static tables with Bootstrap styling.', className='text-muted text-sm')
    ], className='mb-3'),
    
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H5('Student Grades', className='dashboard-card-title')
                ], className='dashboard-card-header'),
                html.Div([
                    dbc.Table([
                        html.Thead([
                            html.Tr([
                                html.Th('Student Name'),
                                html.Th('Course'),
                                html.Th('Grade'),
                                html.Th('Status'),
                            ])
                        ]),
                        html.Tbody([
                            html.Tr([
                                html.Td('John Smith'),
                                html.Td('Computer Science'),
                                html.Td('A'),
                                html.Td(html.Span('Passed', className='badge bg-success')),
                            ]),
                            html.Tr([
                                html.Td('Sarah Miller'),
                                html.Td('Mathematics'),
                                html.Td('B+'),
                                html.Td(html.Span('Passed', className='badge bg-success')),
                            ]),
                            html.Tr([
                                html.Td('Mike Chen'),
                                html.Td('Physics'),
                                html.Td('A-'),
                                html.Td(html.Span('Passed', className='badge bg-success')),
                            ]),
                            html.Tr([
                                html.Td('Emma Wilson'),
                                html.Td('Chemistry'),
                                html.Td('B'),
                                html.Td(html.Span('Passed', className='badge bg-success')),
                            ]),
                        ])
                    ], striped=True, bordered=True, hover=True)
                ], className='dashboard-card-body')
            ], className='dashboard-card')
        ], className='dashboard-grid grid-cols-1')
    ], className='dashboard-row')
])
