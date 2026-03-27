from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    html.Div([
        html.H1('PDF Viewer', className='h3 font-bold'),
        html.P('This is the PDF Viewer page.', className='text-muted text-sm')
    ], className='mb-3'),
    
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H5('PDF Viewer', className='dashboard-card-title')
                ], className='dashboard-card-header'),
                html.Div([
                    html.P('Content for PDF Viewer will be displayed here.')
                ], className='dashboard-card-body')
            ], className='dashboard-card')
        ], className='dashboard-grid grid-cols-1')
    ], className='dashboard-row')
])
