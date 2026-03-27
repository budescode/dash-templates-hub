from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    html.Div([
        html.H1('Alerts', className='h3 font-bold'),
        html.P('Alert messages for different contexts.', className='text-muted text-sm')
    ], className='mb-3'),
    
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H5('Alert Styles', className='dashboard-card-title')
                ], className='dashboard-card-header'),
                html.Div([
                    dbc.Alert('This is a primary alert—check it out!', color='primary', className='mb-3'),
                    dbc.Alert('This is a secondary alert—check it out!', color='secondary', className='mb-3'),
                    dbc.Alert('This is a success alert—check it out!', color='success', className='mb-3'),
                    dbc.Alert('This is a danger alert—check it out!', color='danger', className='mb-3'),
                    dbc.Alert('This is a warning alert—check it out!', color='warning', className='mb-3'),
                    dbc.Alert('This is an info alert—check it out!', color='info', className='mb-3'),
                    dbc.Alert('This is a light alert—check it out!', color='light', className='mb-3'),
                    dbc.Alert('This is a dark alert—check it out!', color='dark', className='mb-3'),
                ], className='dashboard-card-body')
            ], className='dashboard-card'),
            
            html.Div([
                html.Div([
                    html.H5('Dismissible Alerts', className='dashboard-card-title')
                ], className='dashboard-card-header'),
                html.Div([
                    dbc.Alert('This is a dismissible alert!', color='success', dismissable=True, className='mb-3'),
                    dbc.Alert('You can close this alert by clicking the × button.', color='info', dismissable=True, className='mb-3'),
                ], className='dashboard-card-body')
            ], className='dashboard-card'),
        ], className='dashboard-grid grid-cols-1')
    ], className='dashboard-row')
])
