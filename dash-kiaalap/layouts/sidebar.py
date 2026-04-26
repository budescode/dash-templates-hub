from dash import html, dcc
import dash_bootstrap_components as dbc

layout = html.Aside([
    html.Div([
        html.Div([
            html.H5([
                html.I(className='bi bi-mortarboard-fill'),
                ' Kiaalap'
            ]),
            html.Button([
                html.I(className='bi bi-x-lg')
            ], className='sidebar-close', id='sidebarClose')
        ], className='sidebar-brand')
    ], className='sidebar-header'),
    
    html.Nav([
        # Main Section
        html.Div([
            html.Div('Main', className='menu-section-title'),
            html.Ul([
                html.Li([
                    dcc.Link([
                        html.I(className='bi bi-speedometer2'),
                        html.Span('Dashboard')
                    ], href='/', className='nav-link', id='nav-dashboard')
                ], className='nav-item'),
                html.Li([
                    dcc.Link([
                        html.I(className='bi bi-bar-chart-line'),
                        html.Span('Analytics')
                    ], href='/analytics', className='nav-link', id='nav-analytics')
                ], className='nav-item'),
                html.Li([
                    dcc.Link([
                        html.I(className='bi bi-grid-3x3-gap'),
                        html.Span('Widgets')
                    ], href='/widgets', className='nav-link', id='nav-widgets')
                ], className='nav-item'),
                html.Li([
                    dcc.Link([
                        html.I(className='bi bi-calendar-event'),
                        html.Span('Events')
                    ], href='/events', className='nav-link', id='nav-events')
                ], className='nav-item'),
            ], className='nav flex-column')
        ], className='menu-section'),
        
        # Academic Section
        html.Div([
            html.Div('Academic', className='menu-section-title'),
            html.Ul([
                html.Li([
                    dcc.Link([
                        html.I(className='bi bi-person-badge'),
                        html.Span('All Professors')
                    ], href='/all-professors', className='nav-link', id='nav-all-professors')
                ], className='nav-item'),
                html.Li([
                    dcc.Link([
                        html.I(className='bi bi-people'),
                        html.Span('All Students')
                    ], href='/all-students', className='nav-link', id='nav-all-students')
                ], className='nav-item'),
                html.Li([
                    dcc.Link([
                        html.I(className='bi bi-book'),
                        html.Span('All Courses')
                    ], href='/all-courses', className='nav-link', id='nav-all-courses')
                ], className='nav-item'),
                html.Li([
                    dcc.Link([
                        html.I(className='bi bi-journal-bookmark'),
                        html.Span('Library Assets')
                    ], href='/library-assets', className='nav-link', id='nav-library-assets')
                ], className='nav-item'),
                html.Li([
                    dcc.Link([
                        html.I(className='bi bi-building'),
                        html.Span('Departments')
                    ], href='/departments', className='nav-link', id='nav-departments')
                ], className='nav-item'),
            ], className='nav flex-column')
        ], className='menu-section'),
        
        # Communication Section
        html.Div([
            html.Div('Communication', className='menu-section-title'),
            html.Ul([
                html.Li([
                    dcc.Link([
                        html.I(className='bi bi-envelope'),
                        html.Span('Mailbox')
                    ], href='/mailbox', className='nav-link', id='nav-mailbox')
                ], className='nav-item'),
            ], className='nav flex-column')
        ], className='menu-section'),
        
        # Interface Section
        html.Div([
            html.Div('Interface', className='menu-section-title'),
            html.Ul([
                html.Li([
                    dcc.Link([
                        html.I(className='bi bi-layout-wtf'),
                        html.Span('Buttons')
                    ], href='/buttons', className='nav-link', id='nav-buttons')
                ], className='nav-item'),
                html.Li([
                    dcc.Link([
                        html.I(className='bi bi-card-list'),
                        html.Span('Forms')
                    ], href='/basic-form-element', className='nav-link', id='nav-forms')
                ], className='nav-item'),
                html.Li([
                    dcc.Link([
                        html.I(className='bi bi-bar-chart'),
                        html.Span('Charts')
                    ], href='/line-charts', className='nav-link', id='nav-charts')
                ], className='nav-item'),
                html.Li([
                    dcc.Link([
                        html.I(className='bi bi-table'),
                        html.Span('Tables')
                    ], href='/static-table', className='nav-link', id='nav-tables')
                ], className='nav-item'),
            ], className='nav flex-column')
        ], className='menu-section'),
        
        # Developer Tools Section
        html.Div([
            html.Div('Developer Tools', className='menu-section-title'),
            html.Ul([
                html.Li([
                    dcc.Link([
                        html.I(className='bi bi-tools'),
                        html.Span('Tools')
                    ], href='/tools', className='nav-link', id='nav-tools')
                ], className='nav-item'),
            ], className='nav flex-column')
        ], className='menu-section'),

        # Pages Section
        html.Div([
            html.Div('Pages', className='menu-section-title'),
            html.Ul([
                html.Li([
                    dcc.Link([
                        html.I(className='bi bi-shield-lock'),
                        html.Span('Login')
                    ], href='/login', className='nav-link', id='nav-login')
                ], className='nav-item'),
            ], className='nav flex-column')
        ], className='menu-section'),
    ], className='sidebar-nav')
], className='sidebar', id='sidebar')
