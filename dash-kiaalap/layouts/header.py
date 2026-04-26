from dash import html, dcc
import dash_bootstrap_components as dbc

def create_header(page_title='Dashboard'):
    return html.Nav([
        html.Div([
            html.Button([
                html.I(className='bi bi-list')
            ], className='hamburger-menu', id='sidebarToggle'),

            html.Nav([
                html.Ol([
                    html.Li([
                        dcc.Link('Home', href='/')
                    ], className='breadcrumb-item'),
                    html.Li(page_title, className='breadcrumb-item active')
                ], className='breadcrumb mb-0')
            ], **{'aria-label': 'breadcrumb'}, className='d-none d-lg-block ms-3'),
        
        html.Div('Kiaalap', className='navbar-brand d-lg-none fw-bold me-auto'),
        
        html.Div(className='flex-grow-1 d-none d-lg-block'),
        
        html.Div([
            dbc.Button([
                html.I(className='bi bi-search')
            ], color='light', className='btn-icon me-2'),
            
            dbc.DropdownMenu([
                dbc.DropdownMenuItem([
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Div('New Event', className='fw-semibold'),
                                html.Div('Science Fair on March 15', className='text-muted small'),
                                html.Div('5 minutes ago', className='text-muted small')
                            ], className='flex-grow-1')
                        ], className='d-flex align-items-center')
                    ])
                ]),
            ], label=[
                html.I(className='bi bi-bell'),
                html.Span('3', className='position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger', style={'font-size': '0.6rem'})
            ], color='light', className='btn-icon position-relative me-2'),
            
            dbc.DropdownMenu([
                dbc.DropdownMenuItem([html.I(className='bi bi-person-plus me-2'), 'Add Student'], href='/add-student'),
                dbc.DropdownMenuItem([html.I(className='bi bi-book me-2'), 'Add Course'], href='/add-course'),
                dbc.DropdownMenuItem([html.I(className='bi bi-person-badge me-2'), 'Add Professor'], href='/add-professor'),
            ], label=html.I(className='bi bi-plus-lg'), color='light', className='btn-icon me-2'),
            
            dbc.DropdownMenu([
                dbc.DropdownMenuItem([html.I(className='bi bi-person me-2'), 'Profile']),
                dbc.DropdownMenuItem([html.I(className='bi bi-gear me-2'), 'Settings']),
                dbc.DropdownMenuItem([html.I(className='bi bi-question-circle me-2'), 'Help Center']),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem([html.I(className='bi bi-box-arrow-right me-2'), 'Logout']),
            ], label=[
                html.Img(src='https://ui-avatars.com/api/?name=Admin+User&background=6366f1&color=fff&size=32', 
                        className='rounded-circle me-2', width='32', height='32'),
                html.Span('Admin', className='d-none d-md-inline'),
                html.I(className='bi bi-chevron-down ms-1')
            ], color='light', className='d-flex align-items-center'),
        ], className='d-flex align-items-center gap-2')
        ], className='container-fluid d-flex align-items-center h-100')
    ], className='navbar top-navbar')
