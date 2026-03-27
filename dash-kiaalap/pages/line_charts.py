from dash import html, dcc
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

# Line chart
line_chart = dcc.Graph(
    figure=go.Figure(
        data=[
            go.Scatter(x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], 
                      y=[65, 59, 80, 81, 56, 55], mode='lines+markers', name='Dataset 1', line=dict(color='#6366f1', width=3)),
            go.Scatter(x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], 
                      y=[28, 48, 40, 19, 86, 27], mode='lines+markers', name='Dataset 2', line=dict(color='#10b981', width=3)),
        ],
        layout=go.Layout(title='Line Chart Example', height=400, margin=dict(l=40, r=40, t=60, b=40))
    ),
    config={'displayModeBar': False}
)

layout = dbc.Container([
    html.Div([
        html.H1('Line Charts', className='h3 font-bold'),
        html.P('Interactive line charts using Plotly.', className='text-muted text-sm')
    ], className='mb-3'),
    
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H5('Line Chart', className='dashboard-card-title')
                ], className='dashboard-card-header'),
                html.Div([line_chart], className='dashboard-card-body')
            ], className='dashboard-card')
        ], className='dashboard-grid grid-cols-1')
    ], className='dashboard-row')
])
