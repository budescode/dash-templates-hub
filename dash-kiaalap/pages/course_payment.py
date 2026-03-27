from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5('Payment Summary', className='mb-0')),
            dbc.CardBody([
                dbc.Row([dbc.Col(html.Span('Course', className='text-muted small')),   dbc.Col('Advanced Programming', className='small fw-semibold')], className='mb-2'),
                dbc.Row([dbc.Col(html.Span('Credits', className='text-muted small')),  dbc.Col('3 Credits', className='small')], className='mb-2'),
                dbc.Row([dbc.Col(html.Span('Fee/Credit', className='text-muted small')), dbc.Col('$500', className='small')], className='mb-2'),
                html.Hr(),
                dbc.Row([dbc.Col(html.Span('Total Fee', className='fw-bold')), dbc.Col('$1,500', className='fw-bold text-primary')], className='mb-2'),
                dbc.Row([dbc.Col(html.Span('Paid', className='text-muted small')),     dbc.Col('$1,000', className='small text-success')], className='mb-2'),
                dbc.Row([dbc.Col(html.Span('Balance', className='text-muted small')),  dbc.Col('$500', className='small text-danger')], className='mb-2'),
            ]),
        ]), md=4, className='mb-3'),

        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5('Payment History', className='mb-0')),
            dbc.CardBody(dbc.Table([
                html.Thead(html.Tr([html.Th('Date'), html.Th('Amount'), html.Th('Method'), html.Th('Status')])),
                html.Tbody([
                    html.Tr([html.Td('Jan 15, 2024'), html.Td('$500'), html.Td('Credit Card'), html.Td(dbc.Badge('Paid', color='success'))]),
                    html.Tr([html.Td('Feb 15, 2024'), html.Td('$500'), html.Td('Bank Transfer'), html.Td(dbc.Badge('Paid', color='success'))]),
                    html.Tr([html.Td('Mar 15, 2024'), html.Td('$500'), html.Td('—'), html.Td(dbc.Badge('Pending', color='warning'))]),
                ]),
            ], striped=True, hover=True, responsive=True)),
        ]), md=8, className='mb-3'),
    ]),

    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(html.H5('Make a Payment', className='mb-0')),
        dbc.CardBody(dbc.Form([
            dbc.Row([
                dbc.Col([dbc.Label('Amount'), dbc.Input(type='number', placeholder='500')], md=4, className='mb-3'),
                dbc.Col([dbc.Label('Payment Method'), dbc.Select(options=[
                    {'label': 'Credit Card', 'value': 'cc'},
                    {'label': 'Bank Transfer', 'value': 'bank'},
                    {'label': 'Cash', 'value': 'cash'},
                ])], md=4, className='mb-3'),
                dbc.Col([dbc.Label('Date'), dbc.Input(type='date')], md=4, className='mb-3'),
            ]),
            dbc.Button('Submit Payment', color='primary'),
        ])),
    ]))),
], fluid=True)
