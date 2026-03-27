from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(dbc.Row([
            dbc.Col(html.H5('Compose Message', className='mb-0')),
            dbc.Col(dbc.Button([html.I(className='bi bi-inbox me-1'), 'Inbox'], href='/mailbox',
                               color='outline-secondary', size='sm'), width='auto'),
        ], align='center')),
        dbc.CardBody(dbc.Form([
            dbc.Row([dbc.Col([dbc.Label('To'), dbc.Input(type='email', placeholder='recipient@email.com')], className='mb-3')]),
            dbc.Row([dbc.Col([dbc.Label('CC'), dbc.Input(type='email', placeholder='cc@email.com')], className='mb-3')]),
            dbc.Row([dbc.Col([dbc.Label('Subject'), dbc.Input(type='text', placeholder='Email subject')], className='mb-3')]),
            dbc.Row([dbc.Col([dbc.Label('Message'), dbc.Textarea(placeholder='Write your message here...', rows=10)], className='mb-3')]),
            dbc.Row([
                dbc.Col(dbc.ButtonGroup([
                    dbc.Button([html.I(className='bi bi-send me-1'), 'Send'], color='primary'),
                    dbc.Button([html.I(className='bi bi-file me-1'), 'Save Draft'], color='outline-secondary'),
                    dbc.Button([html.I(className='bi bi-paperclip me-1'), 'Attach'], color='outline-secondary'),
                ])),
                dbc.Col(dbc.Button([html.I(className='bi bi-trash me-1'), 'Discard'],
                                    color='outline-danger'), width='auto'),
            ], align='center'),
        ])),
    ]))),
], fluid=True)
