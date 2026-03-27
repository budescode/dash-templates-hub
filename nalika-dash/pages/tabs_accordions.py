from dash import html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Breadcrumb(items=[
        {'label': 'Home', 'href': '/', 'active': False},
        {'label': 'Tabs & Accordions', 'active': True},
    ], className='breadcrumb'),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Tabs')),
                dbc.CardBody([
                    dbc.Tabs([
                        dbc.Tab(label='Tab 1', tab_id='tab-1'),
                        dbc.Tab(label='Tab 2', tab_id='tab-2'),
                        dbc.Tab(label='Tab 3', tab_id='tab-3'),
                    ], id='tabs', active_tab='tab-1'),
                    html.Div(id='tab-content', className='p-4')
                ])
            ], className='mb-4')
        ], md=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Accordion')),
                dbc.CardBody([
                    dbc.Accordion([
                        dbc.AccordionItem([
                            html.P('This is the content of the first accordion item.')
                        ], title='Accordion Item 1'),
                        dbc.AccordionItem([
                            html.P('This is the content of the second accordion item.')
                        ], title='Accordion Item 2'),
                        dbc.AccordionItem([
                            html.P('This is the content of the third accordion item.')
                        ], title='Accordion Item 3'),
                    ], start_collapsed=True)
                ])
            ])
        ], md=6),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('List Group')),
                dbc.CardBody([
                    dbc.ListGroup([
                        dbc.ListGroupItem('First item', color='primary'),
                        dbc.ListGroupItem('Second item', color='success'),
                        dbc.ListGroupItem('Third item', color='warning'),
                        dbc.ListGroupItem('Fourth item', color='danger'),
                        dbc.ListGroupItem('Fifth item', color='info'),
                    ])
                ])
            ])
        ], md=6),
    ])
])
