from dash import html, callback, Input, Output
import dash_bootstrap_components as dbc
from dash import dcc
from datetime import datetime, timedelta

layout = html.Div([
    dbc.Breadcrumb(items=[
        {'label': 'Home', 'href': '/', 'active': False},
        {'label': 'Calendar', 'active': True},
    ], className='breadcrumb'),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Date Picker')),
                dbc.CardBody([
                    dcc.DatePickerSingle(
                        id='date-picker-single',
                        date=datetime.now().date(),
                        display_format='YYYY-MM-DD',
                        className='mb-3'
                    ),
                    html.Div(id='date-output')
                ])
            ], className='mb-4')
        ], md=6),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Date Range Picker')),
                dbc.CardBody([
                    dcc.DatePickerRange(
                        id='date-picker-range',
                        start_date=datetime.now().date(),
                        end_date=datetime.now().date() + timedelta(days=7),
                        display_format='YYYY-MM-DD',
                        className='mb-3'
                    ),
                    html.Div(id='date-range-output')
                ])
            ], className='mb-4')
        ], md=6),
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5('Upcoming Events')),
                dbc.CardBody([
                    dbc.ListGroup([
                        dbc.ListGroupItem([
                            html.Div([
                                html.Strong('Team Meeting'),
                                html.Br(),
                                html.Small('Today at 2:00 PM', className='text-muted'),
                            ])
                        ]),
                        dbc.ListGroupItem([
                            html.Div([
                                html.Strong('Project Deadline'),
                                html.Br(),
                                html.Small('Tomorrow at 5:00 PM', className='text-muted'),
                            ])
                        ]),
                        dbc.ListGroupItem([
                            html.Div([
                                html.Strong('Client Presentation'),
                                html.Br(),
                                html.Small('Friday at 10:00 AM', className='text-muted'),
                            ])
                        ]),
                    ])
                ])
            ])
        ], md=12)
    ])
])

@callback(
    Output('date-output', 'children'),
    Input('date-picker-single', 'date')
)
def update_date(date):
    if date:
        return dbc.Alert(f'Selected date: {date}', color='info')
    return ''

@callback(
    Output('date-range-output', 'children'),
    [Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date')]
)
def update_date_range(start, end):
    if start and end:
        return dbc.Alert(f'Date range: {start} to {end}', color='info')
    return ''
