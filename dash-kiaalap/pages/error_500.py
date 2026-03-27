from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('500 Error', className='text-center mb-4'),
                    html.P('This is the 500 Error page.', className='text-center text-muted')
                ], className='card-body p-5')
            ], className='card shadow-lg', style={'max-width': '400px', 'width': '100%'})
        ], className='d-flex justify-content-center align-items-center', style={'min-height': '100vh'})
    ], className='container')
])
