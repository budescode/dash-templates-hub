from dash import html

layout = html.Footer([
    html.Div([
        html.Div([
            html.Div([
                html.P('© 2025 Kiaalap · Ported to Dash by budescode. All rights reserved.', className='mb-0')
            ], className='col-md-6'),
            html.Div([
                html.P([
                    'Ported to Dash by ',
                    html.A('budescode', href='https://github.com/budescode', target='_blank'),
                    ' · Original design by Kiaalap'
                ], className='mb-0 text-md-end')
            ], className='col-md-6')
        ], className='row')
    ], className='container-fluid')
], className='dashboard-footer')
