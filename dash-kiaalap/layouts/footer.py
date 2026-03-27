from dash import html

layout = html.Footer([
    html.Div([
        html.Div([
            html.Div([
                html.P('© 2024 Kiaalap. All rights reserved.', className='mb-0')
            ], className='col-md-6'),
            html.Div([
                html.P([
                    'Made with ',
                    html.I(className='bi bi-heart-fill text-danger'),
                    ' by Kiaalap Team'
                ], className='mb-0 text-md-end')
            ], className='col-md-6')
        ], className='row')
    ], className='container-fluid')
], className='dashboard-footer')
