from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

# Progress bars with stats
progress_cards = dbc.Row([
    dbc.Col([
        dbc.Card([
            dbc.CardBody([
                html.H5('Web Design', className='mb-3'),
                html.H2('85%', className='mb-3'),
                dbc.Progress(value=85, color='success', style={'height': '5px'})
            ])
        ])
    ], md=4),
    dbc.Col([
        dbc.Card([
            dbc.CardBody([
                html.H5('Development', className='mb-3'),
                html.H2('70%', className='mb-3'),
                dbc.Progress(value=70, color='danger', style={'height': '5px'})
            ])
        ])
    ], md=4),
    dbc.Col([
        dbc.Card([
            dbc.CardBody([
                html.H5('Marketing', className='mb-3'),
                html.H2('90%', className='mb-3'),
                dbc.Progress(value=90, color='info', style={'height': '5px'})
            ])
        ])
    ], md=4),
], className='mb-4')

# Charts
charts_row = dbc.Row([
    dbc.Col([
        dbc.Card([
            dbc.CardHeader(html.H5('Revenue Analytics')),
            dbc.CardBody([
                dcc.Graph(
                    figure=go.Figure(
                        data=[
                            go.Bar(x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], 
                                  y=[20, 35, 30, 45, 40, 55],
                                  marker=dict(color='#24caa1'))
                        ],
                        layout=go.Layout(
                            paper_bgcolor='#1b2a47',
                            plot_bgcolor='#1b2a47',
                            font=dict(color='#ffffff'),
                            xaxis=dict(showgrid=False),
                            yaxis=dict(showgrid=True, gridcolor='#152036'),
                            height=300,
                            margin=dict(l=40, r=40, t=20, b=40)
                        )
                    ),
                    config={'displayModeBar': False}
                )
            ])
        ])
    ], md=6),
    dbc.Col([
        dbc.Card([
            dbc.CardHeader(html.H5('Sales Distribution')),
            dbc.CardBody([
                dcc.Graph(
                    figure=go.Figure(
                        data=[
                            go.Pie(labels=['Product A', 'Product B', 'Product C', 'Product D'],
                                  values=[30, 25, 25, 20],
                                  marker=dict(colors=['#24caa1', '#2eb7f3', '#f8ac59', '#eb4b4b']))
                        ],
                        layout=go.Layout(
                            paper_bgcolor='#1b2a47',
                            plot_bgcolor='#1b2a47',
                            font=dict(color='#ffffff'),
                            height=300,
                            margin=dict(l=40, r=40, t=20, b=40),
                            showlegend=True
                        )
                    ),
                    config={'displayModeBar': False}
                )
            ])
        ])
    ], md=6),
], className='mb-4')

# Stats table
stats_table = dbc.Card([
    dbc.CardHeader(html.H5('Performance Metrics')),
    dbc.CardBody([
        dbc.Table([
            html.Thead([
                html.Tr([
                    html.Th('Metric'),
                    html.Th('Current'),
                    html.Th('Previous'),
                    html.Th('Change'),
                ])
            ]),
            html.Tbody([
                html.Tr([
                    html.Td('Page Views'),
                    html.Td('45,678'),
                    html.Td('42,345'),
                    html.Td(dbc.Badge('+7.8%', color='success')),
                ]),
                html.Tr([
                    html.Td('Unique Visitors'),
                    html.Td('12,456'),
                    html.Td('13,234'),
                    html.Td(dbc.Badge('-5.9%', color='danger')),
                ]),
                html.Tr([
                    html.Td('Bounce Rate'),
                    html.Td('32.5%'),
                    html.Td('35.2%'),
                    html.Td(dbc.Badge('-2.7%', color='success')),
                ]),
                html.Tr([
                    html.Td('Avg. Session'),
                    html.Td('3:45'),
                    html.Td('3:12'),
                    html.Td(dbc.Badge('+10.3%', color='success')),
                ]),
            ], )
        ], bordered=True, hover=True, responsive=True, striped=True, color="dark",
        style={'color': '#ffffff'}, 
        
        className='table-dark')
    ])
], className='mb-4')

# Line chart for trends
trend_chart = dbc.Card([
    dbc.CardHeader(html.H5('Traffic Trends')),
    dbc.CardBody([
        dcc.Graph(
            figure=go.Figure(
                data=[
                    go.Scatter(
                        x=['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6'],
                        y=[1200, 1900, 1500, 2100, 2400, 2800],
                        mode='lines+markers',
                        name='Visitors',
                        line=dict(color='#24caa1', width=3),
                        marker=dict(size=8)
                    ),
                    go.Scatter(
                        x=['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6'],
                        y=[800, 1200, 1000, 1400, 1600, 1900],
                        mode='lines+markers',
                        name='Conversions',
                        line=dict(color='#2eb7f3', width=3),
                        marker=dict(size=8)
                    )
                ],
                layout=go.Layout(
                    paper_bgcolor='#1b2a47',
                    plot_bgcolor='#1b2a47',
                    font=dict(color='#ffffff'),
                    xaxis=dict(showgrid=False),
                    yaxis=dict(showgrid=True, gridcolor='#152036'),
                    height=300,
                    margin=dict(l=40, r=40, t=20, b=40),
                    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
                )
            ),
            config={'displayModeBar': False}
        )
    ])
], className='mb-4')

# Heatmap for activity
heatmap_chart = dbc.Card([
    dbc.CardHeader(html.H5('User Activity Heatmap')),
    dbc.CardBody([
        dcc.Graph(
            figure=go.Figure(
                data=[
                    go.Heatmap(
                        z=[[10, 20, 30, 40, 50, 60, 70],
                           [20, 30, 40, 50, 60, 70, 80],
                           [30, 40, 50, 60, 70, 80, 90],
                           [40, 50, 60, 70, 80, 90, 100],
                           [50, 60, 70, 80, 90, 100, 110]],
                        x=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                        y=['00:00', '06:00', '12:00', '18:00', '23:00'],
                        colorscale='Teal',
                        showscale=True
                    )
                ],
                layout=go.Layout(
                    paper_bgcolor='#1b2a47',
                    plot_bgcolor='#1b2a47',
                    font=dict(color='#ffffff'),
                    height=300,
                    margin=dict(l=60, r=40, t=20, b=40)
                )
            ),
            config={'displayModeBar': False}
        )
    ])
], className='mb-4')

# Geographic distribution
geo_stats = dbc.Card([
    dbc.CardHeader(html.H5('Top Locations')),
    dbc.CardBody([
        dbc.ListGroup([
            dbc.ListGroupItem([
                dbc.Row([
                    dbc.Col(html.Span('🇺🇸 United States'), width=6),
                    dbc.Col(html.Span('45.2%'), width=3),
                    dbc.Col(dbc.Progress(value=45, color='success', style={'height': '10px'}), width=3)
                ])
            ], style={'backgroundColor': '#1b2a47', 'color': '#ffffff', 'border': '1px solid #152036'}),
            dbc.ListGroupItem([
                dbc.Row([
                    dbc.Col(html.Span('🇬🇧 United Kingdom'), width=6),
                    dbc.Col(html.Span('22.8%'), width=3),
                    dbc.Col(dbc.Progress(value=23, color='info', style={'height': '10px'}), width=3)
                ])
            ], style={'backgroundColor': '#1b2a47', 'color': '#ffffff', 'border': '1px solid #152036'}),
            dbc.ListGroupItem([
                dbc.Row([
                    dbc.Col(html.Span('🇨🇦 Canada'), width=6),
                    dbc.Col(html.Span('15.5%'), width=3),
                    dbc.Col(dbc.Progress(value=16, color='warning', style={'height': '10px'}), width=3)
                ])
            ], style={'backgroundColor': '#1b2a47', 'color': '#ffffff', 'border': '1px solid #152036'}),
            dbc.ListGroupItem([
                dbc.Row([
                    dbc.Col(html.Span('🇩🇪 Germany'), width=6),
                    dbc.Col(html.Span('10.3%'), width=3),
                    dbc.Col(dbc.Progress(value=10, color='danger', style={'height': '10px'}), width=3)
                ])
            ], style={'backgroundColor': '#1b2a47', 'color': '#ffffff', 'border': '1px solid #152036'}),
            dbc.ListGroupItem([
                dbc.Row([
                    dbc.Col(html.Span('🇦🇺 Australia'), width=6),
                    dbc.Col(html.Span('6.2%'), width=3),
                    dbc.Col(dbc.Progress(value=6, color='primary', style={'height': '10px'}), width=3)
                ])
            ], style={'backgroundColor': '#1b2a47', 'color': '#ffffff', 'border': '1px solid #152036'}),
        ], flush=True)
    ])
], className='mb-4')

# Device breakdown
device_chart = dbc.Card([
    dbc.CardHeader(html.H5('Device Distribution')),
    dbc.CardBody([
        dcc.Graph(
            figure=go.Figure(
                data=[
                    go.Bar(
                        x=['Desktop', 'Mobile', 'Tablet'],
                        y=[55, 35, 10],
                        marker=dict(color=['#24caa1', '#2eb7f3', '#f8ac59']),
                        text=['55%', '35%', '10%'],
                        textposition='auto'
                    )
                ],
                layout=go.Layout(
                    paper_bgcolor='#1b2a47',
                    plot_bgcolor='#1b2a47',
                    font=dict(color='#ffffff'),
                    xaxis=dict(showgrid=False),
                    yaxis=dict(showgrid=True, gridcolor='#152036', title='Percentage'),
                    height=300,
                    margin=dict(l=40, r=40, t=20, b=40)
                )
            ),
            config={'displayModeBar': False}
        )
    ])
], className='mb-4')

layout = html.Div([
    dbc.Breadcrumb(items=[
        {'label': 'Home', 'href': '/', 'active': False},
        {'label': 'Analytics', 'active': True},
    ], className='breadcrumb'),
    
    progress_cards,
    charts_row,
    stats_table,
    
    trend_chart,
    
    dbc.Row([
        dbc.Col([heatmap_chart], md=8),
        dbc.Col([geo_stats], md=4),
    ], className='mb-4'),
    
    device_chart,
])
