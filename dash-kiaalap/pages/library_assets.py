from dash import html
import dash_bootstrap_components as dbc

assets = [
    {'title': 'Introduction to Algorithms', 'author': 'Cormen et al.', 'category': 'Textbook', 'copies': 5, 'available': 3},
    {'title': 'Clean Code',                 'author': 'Robert C. Martin', 'category': 'Reference', 'copies': 3, 'available': 1},
    {'title': 'The Pragmatic Programmer',   'author': 'Hunt & Thomas',   'category': 'Reference', 'copies': 4, 'available': 4},
    {'title': 'Design Patterns',            'author': 'Gang of Four',    'category': 'Textbook',  'copies': 2, 'available': 0},
    {'title': 'Calculus: Early Transcendentals', 'author': 'James Stewart', 'category': 'Textbook', 'copies': 8, 'available': 5},
    {'title': 'Organic Chemistry',          'author': 'Paula Bruice',    'category': 'Textbook',  'copies': 6, 'available': 2},
]

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(dbc.Row([
            dbc.Col(html.H4('Library Assets', className='mb-0')),
            dbc.Col(dbc.Button([html.I(className='bi bi-plus-circle me-2'), 'Add Asset'],
                               href='/add-library-assets', color='primary'), width='auto'),
        ], align='center')),
        dbc.CardBody(dbc.Row([
            dbc.Col(dbc.InputGroup([
                dbc.InputGroupText(html.I(className='bi bi-search')),
                dbc.Input(type='text', placeholder='Search assets...'),
            ]), md=8),
            dbc.Col(dbc.Select(options=[
                {'label': 'All Categories', 'value': 'all'},
                {'label': 'Textbook', 'value': 'textbook'},
                {'label': 'Reference', 'value': 'reference'},
                {'label': 'Journal', 'value': 'journal'},
            ], value='all'), md=4),
        ], className='g-2')),
    ]), className='mb-3')),

    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardBody(dbc.Table([
            html.Thead(html.Tr([html.Th('Title'), html.Th('Author'), html.Th('Category'), html.Th('Copies'), html.Th('Available'), html.Th('Actions')])),
            html.Tbody([
                html.Tr([
                    html.Td(a['title']),
                    html.Td(a['author']),
                    html.Td(dbc.Badge(a['category'], color='primary')),
                    html.Td(a['copies']),
                    html.Td(dbc.Badge(str(a['available']), color='success' if a['available'] > 0 else 'danger')),
                    html.Td(dbc.ButtonGroup([
                        dbc.Button(html.I(className='bi bi-pencil'), href='/edit-library-assets', color='outline-primary', size='sm'),
                        dbc.Button(html.I(className='bi bi-trash'), color='outline-danger', size='sm'),
                    ])),
                ]) for a in assets
            ]),
        ], striped=True, hover=True, responsive=True)),
    ]))),
], fluid=True)
