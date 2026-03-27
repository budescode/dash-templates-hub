from dash import html, dcc
import dash_bootstrap_components as dbc

def create_sidebar():
    return html.Div([
        # Logo
        html.Div([
            html.Img(src='/assets/img/logo.png', style={'width': '150px', 'padding': '20px'}, className='d-block mx-auto')
        ]),
        
        # Profile Section.
        html.Div([
            html.Img(src='/assets/img/user.jpg', className='rounded-circle d-block mx-auto mb-2', width='70', height="70"),
            html.H6('Lakian Das', className='text-center mb-0'),
            html.P('Admin', className='text-center text-muted small'),
            html.Div([
                html.I(className='fab fa-facebook mx-2'),
                html.I(className='fab fa-twitter mx-2'),
                html.I(className='fab fa-linkedin mx-2'),
            ], className='text-center mb-3')
        ], style={'padding': '20px', 'borderBottom': '1px solid #152036'}),
        
        # Navigation Menu
        dbc.Nav([
            dbc.NavLink([html.I(className='fas fa-home me-2'), 'Dashboard'], href='/', active='exact'),
            dbc.NavLink([html.I(className='fas fa-chart-line me-2'), 'Analytics'], href='/analytics', active='exact'),
            dbc.NavLink([html.I(className='fas fa-chart-bar me-2'), 'Charts'], href='/charts', active='exact'),
            dbc.NavLink([html.I(className='fas fa-table me-2'), 'Data Tables'], href='/tables', active='exact'),
            dbc.NavLink([html.I(className='fas fa-wpforms me-2'), 'Forms'], href='/forms', active='exact'),
            dbc.NavLink([html.I(className='fas fa-th me-2'), 'Widgets'], href='/widgets', active='exact'),
            
            html.Hr(style={'borderColor': '#152036', 'margin': '10px 0'}),
            html.P('Components', className='text-muted small px-3 mb-2'),
            
            dbc.NavLink([html.I(className='fas fa-square me-2'), 'Buttons'], href='/buttons', active='exact'),
            dbc.NavLink([html.I(className='fas fa-id-card me-2'), 'Cards'], href='/cards', active='exact'),
            dbc.NavLink([html.I(className='fas fa-window-maximize me-2'), 'Modals'], href='/modals', active='exact'),
            dbc.NavLink([html.I(className='fas fa-bell me-2'), 'Notifications'], href='/notifications', active='exact'),
            dbc.NavLink([html.I(className='fas fa-tasks me-2'), 'Progress'], href='/progress', active='exact'),
            dbc.NavLink([html.I(className='fas fa-folder me-2'), 'Tabs'], href='/tabs-accordions', active='exact'),
            
            html.Hr(style={'borderColor': '#152036', 'margin': '10px 0'}),
            html.P('Apps', className='text-muted small px-3 mb-2'),
            
            dbc.NavLink([html.I(className='fas fa-calendar me-2'), 'Calendar'], href='/calendar', active='exact'),
            dbc.NavLink([html.I(className='fas fa-envelope me-2'), 'Mailbox'], href='/mailbox', active='exact'),
            dbc.NavLink([html.I(className='fas fa-map me-2'), 'Maps'], href='/maps', active='exact'),
            dbc.NavLink([html.I(className='fas fa-user me-2'), 'Profile'], href='/profile', active='exact'),
        ], vertical=True, pills=True, className='flex-column')
    ], className='sidebar')
