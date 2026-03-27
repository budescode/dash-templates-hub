from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

analytics_chart = dcc.Graph(
    figure=go.Figure(
        data=[
            go.Scatter(x=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
                       y=[4200,5800,5200,6100,7400,6800,8200,7900,8800,9200,9800,10500],
                       mode='lines+markers', name='Revenue', line=dict(color='#6366f1', width=3), fill='tozeroy', fillcolor='rgba(99,102,241,0.1)'),
            go.Scatter(x=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
                       y=[3100,4200,3800,4500,5200,4900,6100,5800,6500,7000,7400,8000],
                       mode='lines+markers', name='Expenses', line=dict(color='#f59e0b', width=3), fill='tozeroy', fillcolor='rgba(245,158,11,0.1)'),
        ],
        layout=go.Layout(
            margin=dict(l=60,r=40,t=20,b=60), height=350,
            plot_bgcolor='#f8f9fc', paper_bgcolor='white',
            xaxis=dict(showgrid=True, gridcolor='#e5e7eb'),
            yaxis=dict(showgrid=True, gridcolor='#e5e7eb', tickformat='$,.0f'),
            legend=dict(orientation='h', yanchor='bottom', y=-0.25, xanchor='center', x=0.5),
            hovermode='x unified'
        )
    ),
    config={'displayModeBar': False}
)

enrollment_chart = dcc.Graph(
    figure=go.Figure(
        data=[go.Bar(
            x=['CS','Business','Engineering','Medicine','Psychology','Mathematics'],
            y=[320, 280, 250, 190, 160, 140],
            marker_color=['#6366f1','#10b981','#f59e0b','#ef4444','#8b5cf6','#06b6d4']
        )],
        layout=go.Layout(
            margin=dict(l=40,r=40,t=20,b=60), height=300,
            plot_bgcolor='#f8f9fc', paper_bgcolor='white',
            xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor='#e5e7eb'),
        )
    ),
    config={'displayModeBar': False}
)

layout = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.Div('Total Students', className='text-muted small text-uppercase fw-semibold'),
            html.Div('1,340', className='fs-3 fw-bold'),
            html.Span('+12% this month', className='text-success small'),
        ])), md=3, className='mb-3'),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.Div('Total Professors', className='text-muted small text-uppercase fw-semibold'),
            html.Div('86', className='fs-3 fw-bold'),
            html.Span('+3 new', className='text-primary small'),
        ])), md=3, className='mb-3'),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.Div('Active Courses', className='text-muted small text-uppercase fw-semibold'),
            html.Div('124', className='fs-3 fw-bold'),
            html.Span('+8 this semester', className='text-info small'),
        ])), md=3, className='mb-3'),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.Div('Revenue', className='text-muted small text-uppercase fw-semibold'),
            html.Div('$84,200', className='fs-3 fw-bold'),
            html.Span('+18% vs last year', className='text-success small'),
        ])), md=3, className='mb-3'),
    ]),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5('Revenue vs Expenses', className='mb-0')),
            dbc.CardBody(analytics_chart),
        ]), md=8, className='mb-3'),
        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5('Top Departments', className='mb-0')),
            dbc.CardBody([
                *[dbc.Row([
                    dbc.Col(html.Span(dept, className='small fw-semibold')),
                    dbc.Col(dbc.Progress(value=pct, color=color, style={'height':'8px'}), className='align-self-center'),
                    dbc.Col(html.Span(f'{pct}%', className='small text-muted'), width='auto'),
                ], align='center', className='mb-3')
                for dept, pct, color in [
                    ('Computer Science', 85, 'primary'),
                    ('Business Admin', 72, 'success'),
                    ('Engineering', 68, 'warning'),
                    ('Medicine', 55, 'danger'),
                    ('Psychology', 48, 'info'),
                ]],
            ]),
        ]), md=4, className='mb-3'),
    ]),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5('Enrollment by Department', className='mb-0')),
            dbc.CardBody(enrollment_chart),
        ]), className='mb-3'),
    ]),
], fluid=True)
