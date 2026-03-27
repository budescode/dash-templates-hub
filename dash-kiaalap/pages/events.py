from dash import html
import dash_bootstrap_components as dbc

events_list = [
    {'title': 'Science Fair 2024',        'date': 'March 15, 2024', 'time': '9:00 AM - 5:00 PM', 'location': 'Main Hall',       'color': 'primary'},
    {'title': 'Annual Sports Day',        'date': 'March 22, 2024', 'time': '8:00 AM - 6:00 PM', 'location': 'Sports Complex',  'color': 'success'},
    {'title': 'Graduation Ceremony',      'date': 'April 5, 2024',  'time': '10:00 AM - 2:00 PM','location': 'Auditorium',      'color': 'warning'},
    {'title': 'Tech Symposium',           'date': 'April 18, 2024', 'time': '9:00 AM - 4:00 PM', 'location': 'CS Building',    'color': 'info'},
    {'title': 'Cultural Festival',        'date': 'May 3, 2024',    'time': '12:00 PM - 8:00 PM','location': 'Campus Grounds',  'color': 'danger'},
    {'title': 'Alumni Meet & Greet',      'date': 'May 20, 2024',   'time': '6:00 PM - 9:00 PM', 'location': 'Conference Hall', 'color': 'secondary'},
]

layout = dbc.Container([
    dbc.Row(dbc.Col(dbc.Card([
        dbc.CardHeader(dbc.Row([
            dbc.Col(html.H4('Events Calendar', className='mb-0')),
            dbc.Col(dbc.Button([html.I(className='bi bi-plus-circle me-2'), 'Add Event'],
                               color='primary'), width='auto'),
        ], align='center')),
    ]), className='mb-3')),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(html.Div(className=f'rounded bg-{e["color"]}',
                                     style={'width':'4px','height':'100%','minHeight':'60px'}), width='auto'),
                    dbc.Col([
                        html.H6(e['title'], className='mb-1'),
                        html.Div([html.I(className='bi bi-calendar3 me-1'), e['date']], className='text-muted small'),
                        html.Div([html.I(className='bi bi-clock me-1'), e['time']], className='text-muted small'),
                        html.Div([html.I(className='bi bi-geo-alt me-1'), e['location']], className='text-muted small'),
                    ]),
                    dbc.Col(dbc.Badge(e['color'].capitalize(), color=e['color']), width='auto', className='align-self-start'),
                ], className='g-2'),
            ]),
        ]), md=6, className='mb-3')
        for e in events_list
    ]),
], fluid=True)
