from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(html.H4('Add Library Asset', className='mb-0')),
        dbc.CardBody(dbc.Form([
            dbc.Row([
                dbc.Col([dbc.Label('Title'), dbc.Input(type='text', placeholder='Book/Asset title')], md=8, className='mb-3'),
                dbc.Col([dbc.Label('ISBN'), dbc.Input(type='text', placeholder='ISBN number')],       md=4, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Author'), dbc.Input(type='text', placeholder='Author name')], md=6, className='mb-3'),
                dbc.Col([dbc.Label('Publisher'), dbc.Input(type='text', placeholder='Publisher')], md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Category'), dbc.Select(options=[
                    {'label': 'Select Category', 'value': ''},
                    {'label': 'Textbook', 'value': 'textbook'},
                    {'label': 'Reference', 'value': 'reference'},
                    {'label': 'Journal', 'value': 'journal'},
                    {'label': 'Magazine', 'value': 'magazine'},
                ])], md=4, className='mb-3'),
                dbc.Col([dbc.Label('Number of Copies'), dbc.Input(type='number', placeholder='1', min=1)], md=4, className='mb-3'),
                dbc.Col([dbc.Label('Year Published'), dbc.Input(type='number', placeholder='2024')],       md=4, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Description'), dbc.Textarea(placeholder='Brief description...', rows=3)], className='mb-3'),
            ]),
            dbc.ButtonGroup([
                dbc.Button('Save Asset', color='primary'),
                dbc.Button('Cancel', href='/library-assets', color='secondary', outline=True),
            ]),
        ])),
    ]))),
], fluid=True)
