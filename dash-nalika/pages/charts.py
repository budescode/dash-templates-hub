from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

# Line Chart
line_chart = dbc.Card([
    dbc.CardHeader(html.H5('Line Chart')),
    dbc.CardBody([
        dcc.Graph(
            figure=go.Figure(
                data=[
                    go.Scatter(x=[1,2,3,4,5,6,7,8,9,10], 
                              y=[10,15,13,17,20,18,25,22,28,30],
                              mode='lines+markers',
                              name='Series 1',
                              line=dict(color='#24caa1', width=3)),
                    go.Scatter(x=[1,2,3,4,5,6,7,8,9,10], 
                              y=[8,12,10,14,16,15,20,18,23,25],
                              mode='lines+markers',
                              name='Series 2',
                              line=dict(color='#2eb7f3', width=3))
                ],
                layout=go.Layout(
                    paper_bgcolor='#1b2a47',
                    plot_bgcolor='#1b2a47',
                    font=dict(color='#ffffff'),
                    xaxis=dict(showgrid=False),
                    yaxis=dict(showgrid=True, gridcolor='#152036'),
                    height=350,
                    margin=dict(l=40, r=40, t=20, b=40),
                    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
                )
            ),
            config={'displayModeBar': False}
        )
    ])
], className='mb-4')

# Bar Chart
bar_chart = dbc.Card([
    dbc.CardHeader(html.H5('Bar Chart')),
    dbc.CardBody([
        dcc.Graph(
            figure=go.Figure(
                data=[
                    go.Bar(x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'], 
                          y=[20, 35, 30, 45, 40, 55, 50, 60],
                          marker=dict(color='#24caa1'),
                          name='Sales'),
                    go.Bar(x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'], 
                          y=[15, 30, 25, 40, 35, 50, 45, 55],
                          marker=dict(color='#eb4b4b'),
                          name='Revenue')
                ],
                layout=go.Layout(
                    paper_bgcolor='#1b2a47',
                    plot_bgcolor='#1b2a47',
                    font=dict(color='#ffffff'),
                    xaxis=dict(showgrid=False),
                    yaxis=dict(showgrid=True, gridcolor='#152036'),
                    height=350,
                    margin=dict(l=40, r=40, t=20, b=40),
                    barmode='group',
                    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
                )
            ),
            config={'displayModeBar': False}
        )
    ])
], className='mb-4')

# Area Chart
area_chart = dbc.Card([
    dbc.CardHeader(html.H5('Area Chart')),
    dbc.CardBody([
        dcc.Graph(
            figure=go.Figure(
                data=[
                    go.Scatter(x=[1,2,3,4,5,6,7,8,9,10], 
                              y=[10,15,13,17,20,18,25,22,28,30],
                              fill='tozeroy',
                              name='Dataset 1',
                              line=dict(color='#24caa1')),
                    go.Scatter(x=[1,2,3,4,5,6,7,8,9,10], 
                              y=[8,12,10,14,16,15,20,18,23,25],
                              fill='tozeroy',
                              name='Dataset 2',
                              line=dict(color='#2eb7f3'))
                ],
                layout=go.Layout(
                    paper_bgcolor='#1b2a47',
                    plot_bgcolor='#1b2a47',
                    font=dict(color='#ffffff'),
                    xaxis=dict(showgrid=False),
                    yaxis=dict(showgrid=True, gridcolor='#152036'),
                    height=350,
                    margin=dict(l=40, r=40, t=20, b=40),
                    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
                )
            ),
            config={'displayModeBar': False}
        )
    ])
], className='mb-4')

# Donut Chart
donut_chart = dbc.Card([
    dbc.CardHeader(html.H5('Donut Chart')),
    dbc.CardBody([
        dcc.Graph(
            figure=go.Figure(
                data=[
                    go.Pie(labels=['Desktop', 'Mobile', 'Tablet', 'Other'],
                          values=[45, 30, 15, 10],
                          hole=0.4,
                          marker=dict(colors=['#24caa1', '#2eb7f3', '#f8ac59', '#eb4b4b']))
                ],
                layout=go.Layout(
                    paper_bgcolor='#1b2a47',
                    plot_bgcolor='#1b2a47',
                    font=dict(color='#ffffff'),
                    height=350,
                    margin=dict(l=40, r=40, t=20, b=40),
                    showlegend=True
                )
            ),
            config={'displayModeBar': False}
        )
    ])
], className='mb-4')

layout = html.Div([
    dbc.Breadcrumb(items=[
        {'label': 'Home', 'href': '/', 'active': False},
        {'label': 'Charts', 'active': True},
    ], className='breadcrumb'),
    
    dbc.Row([
        dbc.Col(line_chart, md=6),
        dbc.Col(bar_chart, md=6),
    ]),
    
    dbc.Row([
        dbc.Col(area_chart, md=6),
        dbc.Col(donut_chart, md=6),
    ]),
])
