from dash import html

layout = html.Footer([
    html.Div([
        html.Div([
            html.Div([
                html.P('© 2025 Inspired by Kiaalap · Built with Dash by budescode. All rights reserved.', className='mb-0')
            ], className='col-md-6'),
            html.Div([
                html.P([
                    'Inspired by Kiaalap · Built with Dash by ',
                    html.A('budescode', href='https://github.com/budescode', target='_blank'),
                ], className='mb-0 text-md-end')
            ], className='col-md-6')
        ], className='row')
    ], className='container-fluid')
], className='dashboard-footer')
