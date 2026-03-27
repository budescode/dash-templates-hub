from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

def card_stats(title, percentage, badge_color, value, progress_value, progress_color):
    return dbc.Card([
            dbc.CardBody([
                html.H6(title, className='text-uppercase mb-3'),
                html.Div([
                    
                    dbc.Badge(percentage, color=badge_color, className='ms-1'),
                    html.H4(value, className='mb-0'),
                ], className="d-flex justify-content-between align-items-center"),
                dbc.Progress(value=progress_value, color=progress_color, className='mt-4', style={'height': '5px'})
            ])
        ], className='stat-card')
# Stats Cards
stats_cards = dbc.Row([
    
    dbc.Col([
        card_stats("Orders", '31% ↑', 'success', '$10,000', 78, 'success')
    ], md=3),

    dbc.Col([
        card_stats("Tax Deduction", '15% ↓', 'danger', '$5,000', 38, 'danger'),
    ], md=3),
    dbc.Col([
        card_stats("Revenue", '50% ↑', 'info', '$70,000', 60, 'info'),
    ], md=3),
    dbc.Col([
        card_stats("Yearly Sales", '80% ↑', 'warning', '$100,000', 60, 'warning'),
    ], md=3),
], className='mb-4')

# Product Sales Chart
sales_chart = dbc.Card([
    dbc.CardHeader([
        dbc.Row([
            dbc.Col(html.H5('Product Sales', className='mb-0'), width=6),
            dbc.Col([
                dbc.ButtonGroup([
                    dbc.Button('Today', color='secondary', size='sm'),
                    dbc.Button('Week', color='secondary', size='sm', outline=True),
                ])
            ], width=6, className='text-end')
        ])
    ]),
    dbc.CardBody([
        dcc.Graph(
            figure=go.Figure(
                data=[go.Scatter(x=[1,2,3,4,5,6,7], y=[10,15,13,17,20,18,25], mode='lines+markers', 
                                line=dict(color='#24caa1', width=3))],
                layout=go.Layout(
                    paper_bgcolor='#1b2a47',
                    plot_bgcolor='#1b2a47',
                    font=dict(color='#ffffff'),
                    xaxis=dict(showgrid=False),
                    yaxis=dict(showgrid=True, gridcolor='#152036'),
                    height=400,
                    margin=dict(l=40, r=40, t=20, b=40)
                )
            ),
            config={'displayModeBar': False}
        )
    ])
])

# Analytics Cards
analytics_cards = [
    dbc.Card([
        dbc.CardBody([
            html.H6('Total Visit', className='mb-2'),
            html.Div([
                html.Div([html.I(className='fas fa-chart-bar text-success me-1') for _ in range(5)]),
                html.H4('8659', className='mb-0')
            ], className='d-flex justify-content-between align-items-center')
        ], className='mb-3')
    ]),
    dbc.Card([
        dbc.CardBody([
            html.H6('Total Page Views', className='mb-2'),
            html.Div([
                html.Div([html.I(className='fas fa-chart-bar text-success me-1') for _ in range(5)]),
                html.H4('7469', className='mb-0')
            ], className='d-flex justify-content-between align-items-center')
        ], className='mb-3')
    ]),
    dbc.Card([
        dbc.CardBody([
            html.H6('Unique Visitor', className='mb-2'),
            html.Div([
                html.Div([html.I(className='fas fa-chart-bar text-success me-1') for _ in range(5)]),
                html.H4('6011', className='mb-0')
            ], className='d-flex justify-content-between align-items-center')
        ], className='mb-3')
    ]),
    dbc.Card([
        dbc.CardBody([
            html.H6('Bounce Rate', className='mb-2'),
            html.Div([
                html.Div([html.I(className='fas fa-chart-bar text-danger me-1') for _ in range(5)]),
                html.H4('18%', className='mb-0')
            ], className='d-flex justify-content-between align-items-center')
        ])
    ])
]

# Traffic Analysis
traffic_cards = dbc.Row([
    dbc.Col([
        dbc.Card([
            dbc.CardBody([
                html.H5('Site Traffic', className='mb-3'),
                html.Small('↑ 18% Last Month', className='text-success'),
                html.Div([
                    html.Div([html.Span('Overall Growth', className='d-block'), html.Strong('80.40%')], className='me-3'),
                    html.Div([html.Span('Monthly', className='d-block'), html.Strong('15.40%')], className='me-3'),
                    html.Div([html.Span('Day', className='d-block'), html.Strong('5.50%')]),
                ], className='d-flex mt-3'),
                dcc.Graph(
                    figure=go.Figure(
                        data=[go.Scatter(
                            x=[1,2,3,4,5,6,7,8,9,10],
                            y=[8,12,10,14,11,15,13,16,14,12],
                            fill='tozeroy',
                            fillcolor='rgba(36, 202, 161, 0.3)',
                            line=dict(color='#24caa1', width=2),
                            mode='lines'
                        )],
                        layout=go.Layout(
                            paper_bgcolor='rgba(0,0,0,0)',
                            plot_bgcolor='rgba(0,0,0,0)',
                            font=dict(color='#ffffff'),
                            xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
                            yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
                            height=100,
                            margin=dict(l=0, r=0, t=10, b=0)
                        )
                    ),
                    config={'displayModeBar': False}
                )
            ])
        ])
    ], md=4),
    dbc.Col([
        dbc.Card([
            dbc.CardBody([
                html.H5('Site Traffic', className='mb-3'),
                html.Small('↓ 18% Last Month', className='text-info'),
                html.Div([
                    html.Div([html.Span('Overall Growth', className='d-block'), html.Strong('80.40%')], className='me-3'),
                    html.Div([html.Span('Monthly', className='d-block'), html.Strong('15.40%')], className='me-3'),
                    html.Div([html.Span('Day', className='d-block'), html.Strong('5.50%')]),
                ], className='d-flex mt-3'),
                dcc.Graph(
                    figure=go.Figure(
                        data=[go.Scatter(
                            x=[1,2,3,4,5,6,7,8,9,10],
                            y=[10,8,12,9,13,10,14,11,13,10],
                            fill='tozeroy',
                            fillcolor='rgba(52, 152, 219, 0.3)',
                            line=dict(color='#3498db', width=2),
                            mode='lines'
                        )],
                        layout=go.Layout(
                            paper_bgcolor='rgba(0,0,0,0)',
                            plot_bgcolor='rgba(0,0,0,0)',
                            font=dict(color='#ffffff'),
                            xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
                            yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
                            height=100,
                            margin=dict(l=0, r=0, t=10, b=0)
                        )
                    ),
                    config={'displayModeBar': False}
                )
            ])
        ])
    ], md=4),
    dbc.Col([
        dbc.Card([
            dbc.CardBody([
                html.H5('Site Traffic', className='mb-3'),
                html.Small('↑ 18% Last Month', className='text-primary'),
                html.Div([
                    html.Div([html.Span('Overall Growth', className='d-block'), html.Strong('80.40%')], className='me-3'),
                    html.Div([html.Span('Monthly', className='d-block'), html.Strong('15.40%')], className='me-3'),
                    html.Div([html.Span('Day', className='d-block'), html.Strong('5.50%')]),
                ], className='d-flex mt-3'),
                dcc.Graph(
                    figure=go.Figure(
                        data=[go.Scatter(
                            x=[1,2,3,4,5,6,7,8,9,10],
                            y=[9,11,10,13,12,15,13,16,15,14],
                            fill='tozeroy',
                            fillcolor='rgba(155, 89, 182, 0.3)',
                            line=dict(color='#9b59b6', width=2),
                            mode='lines'
                        )],
                        layout=go.Layout(
                            paper_bgcolor='rgba(0,0,0,0)',
                            plot_bgcolor='rgba(0,0,0,0)',
                            font=dict(color='#ffffff'),
                            xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
                            yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
                            height=100,
                            margin=dict(l=0, r=0, t=10, b=0)
                        )
                    ),
                    config={'displayModeBar': False}
                )
            ])
        ])
    ], md=4),
], className='mb-4')

# Footer
footer = html.Div([
    html.P('Copyright © 2024 Nalika Dashboard. All rights reserved.', className='mb-0')
], className='footer')

layout = html.Div([
    # Breadcrumb
    dbc.Breadcrumb(items=[
        {'label': 'Home', 'href': '/', 'active': False},
        {'label': 'Dashboard', 'active': True},
    ], className='breadcrumb p-0'),
    
    stats_cards,
    
    dbc.Row([
        dbc.Col(sales_chart, md=9),
        dbc.Col(analytics_cards, md=3),
    ], className='mb-4'),
    
    traffic_cards,
    footer
])
