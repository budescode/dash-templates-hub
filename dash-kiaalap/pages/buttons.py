from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    html.Div([
        html.H1('Buttons', className='h3 font-bold'),
        html.P('Various button styles and sizes.', className='text-muted text-sm')
    ], className='mb-3'),
    
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H5('Button Colors', className='dashboard-card-title')
                ], className='dashboard-card-header'),
                html.Div([
                    html.Div([
                        dbc.Button('Primary', color='primary', className='me-2'),
                        dbc.Button('Secondary', color='secondary', className='me-2'),
                        dbc.Button('Success', color='success', className='me-2'),
                        dbc.Button('Danger', color='danger', className='me-2'),
                        dbc.Button('Warning', color='warning', className='me-2'),
                        dbc.Button('Info', color='info', className='me-2'),
                        dbc.Button('Light', color='light', className='me-2'),
                        dbc.Button('Dark', color='dark', className='me-2'),
                    ], className='mb-3'),
                ], className='dashboard-card-body')
            ], className='dashboard-card'),
            
            html.Div([
                html.Div([
                    html.H5('Outline Buttons', className='dashboard-card-title')
                ], className='dashboard-card-header'),
                html.Div([
                    html.Div([
                        dbc.Button('Primary', outline=True, color='primary', className='me-2'),
                        dbc.Button('Secondary', outline=True, color='secondary', className='me-2'),
                        dbc.Button('Success', outline=True, color='success', className='me-2'),
                        dbc.Button('Danger', outline=True, color='danger', className='me-2'),
                        dbc.Button('Warning', outline=True, color='warning', className='me-2'),
                        dbc.Button('Info', outline=True, color='info', className='me-2'),
                    ], className='mb-3'),
                ], className='dashboard-card-body')
            ], className='dashboard-card'),
            
            html.Div([
                html.Div([
                    html.H5('Button Sizes', className='dashboard-card-title')
                ], className='dashboard-card-header'),
                html.Div([
                    html.Div([
                        dbc.Button('Large Button', color='primary', size='lg', className='me-2'),
                        dbc.Button('Default Button', color='primary', className='me-2'),
                        dbc.Button('Small Button', color='primary', size='sm', className='me-2'),
                    ], className='mb-3'),
                ], className='dashboard-card-body')
            ], className='dashboard-card'),
            
            html.Div([
                html.Div([
                    html.H5('Icon Buttons', className='dashboard-card-title')
                ], className='dashboard-card-header'),
                html.Div([
                    html.Div([
                        dbc.Button([html.I(className='bi bi-heart-fill me-2'), 'Like'], color='danger', className='me-2'),
                        dbc.Button([html.I(className='bi bi-share-fill me-2'), 'Share'], color='primary', className='me-2'),
                        dbc.Button([html.I(className='bi bi-download me-2'), 'Download'], color='success', className='me-2'),
                        dbc.Button([html.I(className='bi bi-trash-fill me-2'), 'Delete'], color='danger', outline=True, className='me-2'),
                    ], className='mb-3'),
                ], className='dashboard-card-body')
            ], className='dashboard-card'),
        ], className='dashboard-grid grid-cols-1')
    ], className='dashboard-row')
])
