from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

earnings_chart = dcc.Graph(
    figure=go.Figure(
        data=[
            go.Scatter(x=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
                       y=[30000,45000,40000,30000,50000,60000,65000,70000,65000,80000,85000,90000],
                       mode='lines+markers', name='CSE', line=dict(color='#3b82f6', width=3),
                       marker=dict(size=8), fill='tonexty', fillcolor='rgba(59,130,246,0.1)'),
            go.Scatter(x=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
                       y=[20000,30000,25000,20000,40000,45000,50000,55000,50000,60000,65000,70000],
                       mode='lines+markers', name='Accounting', line=dict(color='#8b5cf6', width=3),
                       marker=dict(size=8), fill='tonexty', fillcolor='rgba(139,92,246,0.1)'),
            go.Scatter(x=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
                       y=[10000,20000,25000,28000,35000,38000,40000,42000,45000,48000,50000,52000],
                       mode='lines+markers', name='Electrical', line=dict(color='#10b981', width=3),
                       marker=dict(size=8), fill='tozeroy', fillcolor='rgba(16,185,129,0.1)'),
        ],
        layout=go.Layout(
            margin=dict(l=60, r=40, t=20, b=60), height=400,
            plot_bgcolor='#f8f9fc', paper_bgcolor='white',
            xaxis=dict(showgrid=True, gridcolor='#e5e7eb'),
            yaxis=dict(showgrid=True, gridcolor='#e5e7eb', tickformat='$,.0f'),
            legend=dict(orientation='h', yanchor='bottom', y=-0.2, xanchor='center', x=0.5),
            hovermode='x unified'
        )
    ),
    config={'displayModeBar': False}, style={'height': '400px'}
)

def sparkline(y_data, color):
    return dcc.Graph(
        figure=go.Figure(
            data=[go.Scatter(x=list(range(len(y_data))), y=y_data, mode='lines',
                             line=dict(color=color, width=2), fill='tozeroy',
                             fillcolor=color.replace(')', ',0.15)').replace('rgb', 'rgba'))],
            layout=go.Layout(margin=dict(l=0,r=0,t=0,b=0), height=60, showlegend=False,
                             xaxis=dict(visible=False), yaxis=dict(visible=False),
                             plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        ),
        config={'displayModeBar': False}
    )

visits_sparkline   = sparkline([100,130,120,150,140,160,155,170,165,180,175,190,185,200,195,210,205,220,215,230], 'rgb(139,92,246)')
pageviews_sparkline = sparkline([200,210,230,220,250,240,270,260,290,280,310,300,330,320,350,340,370,360,390,380], 'rgb(59,130,246)')
bounce_sparkline   = sparkline([50,48,51,49,52,50,48,47,49,48,46,47,45,46,44,45,43,44,42,42], 'rgb(239,68,68)')

def stat_mini_card(label, value, icon, icon_color, sparkline_graph):
    return dbc.Card(dbc.CardBody([
        dbc.Row([
            dbc.Col([
                html.Div(label, className='text-uppercase text-muted small fw-semibold'),
                html.Div(value, className='fs-4 fw-bold'),
            ]),
            dbc.Col(html.I(className=f'bi {icon}', style={'fontSize': '24px', 'color': icon_color}),
                    className='text-end', width='auto'),
        ], align='center', className='mb-2'),
        sparkline_graph,
    ]), className='mb-3')

layout = dbc.Container([
    # Stats row
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.Div('Computer Technologies', className='text-muted small text-uppercase fw-semibold'),
            html.Div('$5,000', className='fs-4 fw-bold'),
            html.Span('+20%', className='text-success small'),
            dbc.Progress(value=20, color='success', className='mt-2', style={'height': '4px'}),
        ])), md=3, className='mb-3'),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.Div('Accounting', className='text-muted small text-uppercase fw-semibold'),
            html.Div('$3,000', className='fs-4 fw-bold'),
            html.Span('+30%', className='text-danger small'),
            dbc.Progress(value=30, color='danger', className='mt-2', style={'height': '4px'}),
        ])), md=3, className='mb-3'),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.Div('Electrical Engineering', className='text-muted small text-uppercase fw-semibold'),
            html.Div('$2,000', className='fs-4 fw-bold'),
            html.Span('+60%', className='text-info small'),
            dbc.Progress(value=60, color='info', className='mt-2', style={'height': '4px'}),
        ])), md=3, className='mb-3'),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.Div('Chemical Engineering', className='text-muted small text-uppercase fw-semibold'),
            html.Div('$3,500', className='fs-4 fw-bold'),
            html.Span('+80%', className='text-warning small'),
            dbc.Progress(value=80, color='warning', className='mt-2', style={'height': '4px'}),
        ])), md=3, className='mb-3'),
    ]),

    # Chart + sparklines row
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5('University Earnings', className='mb-0')),
            dbc.CardBody(earnings_chart),
        ]), md=8, className='mb-3'),
        dbc.Col([
            stat_mini_card('Total Visits', '1,500', 'bi-eye', '#8b5cf6', visits_sparkline),
            stat_mini_card('Page Views', '3,000', 'bi-file-text', '#3b82f6', pageviews_sparkline),
            stat_mini_card('Bounce Rate', '42%', 'bi-arrow-up-circle', '#ef4444', bounce_sparkline),
        ], md=4, className='mb-3'),
    ]),

    # Recent students + popular courses
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader(dbc.Row([
                dbc.Col(html.H5('Recent Students', className='mb-0')),
                dbc.Col(dbc.Button('View All', href='/all-students', color='outline-primary', size='sm'), width='auto'),
            ], align='center')),
            dbc.CardBody([
                *[dbc.Row([
                    dbc.Col(html.Span(initials, className='rounded-circle d-flex align-items-center justify-content-center text-white fw-bold',
                                      style={'width':'40px','height':'40px','background':bg,'flexShrink':'0'}), width='auto'),
                    dbc.Col([
                        html.Div(name, className='fw-semibold small'),
                        html.Div(dept, className='text-muted', style={'fontSize':'12px'}),
                        html.Div(time, className='text-muted', style={'fontSize':'11px'}),
                    ]),
                    dbc.Col(dbc.Badge(status, color=badge), width='auto', className='align-self-center'),
                ], align='center', className='py-2 border-bottom')
                for initials, name, dept, time, status, badge, bg in [
                    ('JS','John Smith','Computer Science - Freshman','Enrolled 2 hours ago','Active','success','#3b82f6'),
                    ('ED','Emily Davis','Biology - Sophomore','Enrolled 1 day ago','Active','success','#10b981'),
                    ('MB','Michael Brown','Mathematics - Junior','Enrolled 3 days ago','Pending','warning','#ef4444'),
                ]],
            ]),
        ]), md=6, className='mb-3'),

        dbc.Col(dbc.Card([
            dbc.CardHeader(dbc.Row([
                dbc.Col(html.H5('Popular Courses', className='mb-0')),
                dbc.Col(dbc.Button('View All', href='/all-courses', color='outline-primary', size='sm'), width='auto'),
            ], align='center')),
            dbc.CardBody([
                *[dbc.Row([
                    dbc.Col(html.Div(html.I(className=f'bi {icon}', style={'fontSize':'20px','color':color}),
                                     className='rounded d-flex align-items-center justify-content-center',
                                     style={'width':'40px','height':'40px','background':bg,'flexShrink':'0'}), width='auto'),
                    dbc.Col([
                        html.Div(name, className='fw-semibold small'),
                        html.Div(prof, className='text-muted', style={'fontSize':'12px'}),
                        html.Div(students, className='text-muted', style={'fontSize':'11px'}),
                    ]),
                    dbc.Col(dbc.Badge(full, color=badge), width='auto', className='align-self-center'),
                ], align='center', className='py-2 border-bottom')
                for icon, color, bg, name, prof, students, full, badge in [
                    ('bi-code-slash','#3b82f6','rgba(59,130,246,0.1)','Advanced Programming','Prof. Sarah Johnson','45 enrolled students','85% Full','success'),
                    ('bi-calculator','#10b981','rgba(16,185,129,0.1)','Calculus II','Prof. Michael Chen','38 enrolled students','76% Full','success'),
                    ('bi-microscope','#06b6d4','rgba(6,182,212,0.1)','Biology Lab','Prof. Lisa Thompson','28 enrolled students','56% Full','warning'),
                ]],
            ]),
        ]), md=6, className='mb-3'),
    ]),
], fluid=True)
