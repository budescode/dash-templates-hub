from dash import html, dcc
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

bar_chart = dcc.Graph(
    figure=go.Figure(
        data=[
            go.Bar(x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], 
                   y=[65, 59, 80, 81, 56, 55], name='Dataset 1', marker_color='#6366f1'),
            go.Bar(x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], 
                   y=[28, 48, 40, 19, 86, 27], name='Dataset 2', marker_color='#10b981'),
        ],
        layout=go.Layout(title='Bar Chart Example', height=400, margin=dict(l=40, r=40, t=60, b=40), barmode='group')
    ),
    config={'displayModeBar': False}
)

layout = dbc.Container([
    html.Div([
        html.H1('Bar Charts', className='h3 font-bold'),
        html.P('Interactive bar charts using Plotly.', className='text-muted text-sm')
    ], className='mb-3'),
    
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H5('Bar Chart', className='dashboard-card-title')
                ], className='dashboard-card-header'),
                html.Div([bar_chart], className='dashboard-card-body')
            ], className='dashboard-card')
        ], className='dashboard-grid grid-cols-1')
    ], className='dashboard-row')
])
