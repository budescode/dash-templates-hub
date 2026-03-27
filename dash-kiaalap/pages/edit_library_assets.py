from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(html.H4('Edit Library Asset', className='mb-0')),
        dbc.CardBody(dbc.Form([
            dbc.Row([
                dbc.Col([dbc.Label('Title'), dbc.Input(type='text', value='Introduction to Algorithms')], md=8, className='mb-3'),
                dbc.Col([dbc.Label('ISBN'), dbc.Input(type='text', value='978-0262033848')],              md=4, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Author'), dbc.Input(type='text', value='Cormen et al.')],    md=6, className='mb-3'),
                dbc.Col([dbc.Label('Publisher'), dbc.Input(type='text', value='MIT Press')],     md=6, className='mb-3'),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label('Category'), dbc.Select(options=[
                    {'label': 'Textbook', 'value': 'textbook'},
                    {'label': 'Reference', 'value': 'reference'},
                    {'label': 'Journal', 'value': 'journal'},
                ], value='textbook')], md=4, className='mb-3'),
                dbc.Col([dbc.Label('Number of Copies'), dbc.Input(type='number', value=5)], md=4, className='mb-3'),
                dbc.Col([dbc.Label('Year Published'), dbc.Input(type='number', value=2022)], md=4, className='mb-3'),
            ]),
            dbc.ButtonGroup([
                dbc.Button('Update Asset', color='primary'),
                dbc.Button('Cancel', href='/library-assets', color='secondary', outline=True),
            ]),
        ])),
    ]))),
], fluid=True)
