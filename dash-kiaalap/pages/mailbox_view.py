from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(dbc.Row([
            dbc.Col(html.H5('Assignment Deadline Extended', className='mb-0')),
            dbc.Col(dbc.ButtonGroup([
                dbc.Button([html.I(className='bi bi-reply me-1'), 'Reply'], color='primary', size='sm'),
                dbc.Button([html.I(className='bi bi-forward me-1'), 'Forward'], color='outline-secondary', size='sm'),
                dbc.Button([html.I(className='bi bi-trash me-1'), 'Delete'], color='outline-danger', size='sm'),
            ]), width='auto'),
        ], align='center')),
        dbc.CardBody([
            dbc.Row([
                dbc.Col(html.Div('S', className='rounded-circle d-flex align-items-center justify-content-center text-white fw-bold bg-primary',
                                  style={'width':'48px','height':'48px'}), width='auto'),
                dbc.Col([
                    html.Div('Dr. Sarah Johnson', className='fw-bold'),
                    html.Div('sarah.johnson@university.edu', className='text-muted small'),
                ]),
                dbc.Col(html.Div('Today at 10:30 AM', className='text-muted small text-end'), width='auto'),
            ], align='center', className='mb-4'),
            html.Hr(),
            html.P('Dear Students,'),
            html.P('I hope this message finds you well. I wanted to inform you that the deadline for the upcoming programming assignment has been extended by one week.'),
            html.P('The new deadline is: March 28, 2024 at 11:59 PM'),
            html.P([
                'Please make sure to submit your work through the student portal. If you have any questions, feel free to reach out during office hours.',
                html.Br(), html.Br(),
                'Best regards,', html.Br(),
                'Dr. Sarah Johnson', html.Br(),
                'Computer Science Department',
            ]),
            html.Hr(),
            dbc.ButtonGroup([
                dbc.Button([html.I(className='bi bi-reply me-1'), 'Reply'], color='primary'),
                dbc.Button([html.I(className='bi bi-forward me-1'), 'Forward'], color='outline-secondary'),
            ]),
        ]),
    ]))),
], fluid=True)
