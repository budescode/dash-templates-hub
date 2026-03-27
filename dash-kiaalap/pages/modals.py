from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(html.H5('Modal Examples', className='mb-0')),
        dbc.CardBody([
            html.P('Click the buttons below to open different modal sizes.', className='text-muted mb-3'),
            dbc.ButtonGroup([
                dbc.Button('Small Modal',   id='open-sm',   color='primary',   className='me-2'),
                dbc.Button('Default Modal', id='open-md',   color='success',   className='me-2'),
                dbc.Button('Large Modal',   id='open-lg',   color='warning',   className='me-2'),
                dbc.Button('XL Modal',      id='open-xl',   color='info'),
            ]),

            dbc.Modal([
                dbc.ModalHeader(dbc.ModalTitle('Small Modal')),
                dbc.ModalBody('This is a small modal. It is useful for simple confirmations.'),
                dbc.ModalFooter([
                    dbc.Button('Close', id='close-sm', color='secondary'),
                    dbc.Button('Confirm', color='primary'),
                ]),
            ], id='modal-sm', size='sm'),

            dbc.Modal([
                dbc.ModalHeader(dbc.ModalTitle('Default Modal')),
                dbc.ModalBody([
                    html.P('This is a default-sized modal. You can put any content here.'),
                    dbc.Form([
                        dbc.Row([dbc.Col([dbc.Label('Name'), dbc.Input(type='text', placeholder='Your name')], className='mb-3')]),
                        dbc.Row([dbc.Col([dbc.Label('Email'), dbc.Input(type='email', placeholder='Your email')], className='mb-3')]),
                    ]),
                ]),
                dbc.ModalFooter([
                    dbc.Button('Close', id='close-md', color='secondary'),
                    dbc.Button('Save', color='success'),
                ]),
            ], id='modal-md'),

            dbc.Modal([
                dbc.ModalHeader(dbc.ModalTitle('Large Modal')),
                dbc.ModalBody('This is a large modal. Great for displaying more detailed content or forms.'),
                dbc.ModalFooter([dbc.Button('Close', id='close-lg', color='secondary')]),
            ], id='modal-lg', size='lg'),

            dbc.Modal([
                dbc.ModalHeader(dbc.ModalTitle('Extra Large Modal')),
                dbc.ModalBody('This is an extra-large modal. Ideal for complex layouts or data tables.'),
                dbc.ModalFooter([dbc.Button('Close', id='close-xl', color='secondary')]),
            ], id='modal-xl', size='xl'),
        ]),
    ]))),
], fluid=True)
