from dash import html
import dash_bootstrap_components as dbc

def create_navbar():
    return dbc.Navbar([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    dbc.Button(html.I(className='fas fa-bars'), color='primary', size='sm', className='me-3'),
                    dbc.Input(type='search', placeholder='Search...', className='d-inline-block', style={'width': '300px'})
                ], width='auto'),
                dbc.Col([
                    dbc.Nav([
                        dbc.NavItem(dbc.NavLink([html.I(className='fas fa-envelope'), html.Span('3', className='badge bg-danger ms-1')], href='#')),
                        dbc.NavItem(dbc.NavLink([html.I(className='fas fa-bell'), html.Span('5', className='badge bg-danger ms-1')], href='#')),
                        dbc.DropdownMenu([
                            dbc.DropdownMenuItem('Profile', href='#'),
                            dbc.DropdownMenuItem('Settings', href='#'),
                            dbc.DropdownMenuItem(divider=True),
                            dbc.DropdownMenuItem('Logout', href='/login'),
                        ], label=[html.I(className='fas fa-user me-2'), 'Admin'], nav=True, in_navbar=True),
                    ], className='ms-auto', navbar=True)
                ], className='ms-auto')
            ], className='w-100 align-items-center')
        ], fluid=True)
    ], color='dark', dark=True, className='navbar')
