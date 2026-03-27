from dash import html
import dash_bootstrap_components as dbc

# Alert Widgets
alerts = dbc.Card([
    dbc.CardHeader(html.H5('Alerts')),
    dbc.CardBody([
        dbc.Alert('This is a success alert!', color='success', className='mb-2'),
        dbc.Alert('This is an info alert!', color='info', className='mb-2'),
        dbc.Alert('This is a warning alert!', color='warning', className='mb-2'),
        dbc.Alert('This is a danger alert!', color='danger', className='mb-2'),
    ])
], className='mb-4')

# Badges
badges = dbc.Card([
    dbc.CardHeader(html.H5('Badges')),
    dbc.CardBody([
        dbc.Badge('Primary', color='primary', className='me-2'),
        dbc.Badge('Success', color='success', className='me-2'),
        dbc.Badge('Info', color='info', className='me-2'),
        dbc.Badge('Warning', color='warning', className='me-2'),
        dbc.Badge('Danger', color='danger', className='me-2'),
        dbc.Badge('Secondary', color='secondary', className='me-2'),
    ])
], className='mb-4')

# Buttons
buttons = dbc.Card([
    dbc.CardHeader(html.H5('Buttons')),
    dbc.CardBody([
        html.Div([
            dbc.Button('Primary', color='primary', className='me-2 mb-2'),
            dbc.Button('Success', color='success', className='me-2 mb-2'),
            dbc.Button('Info', color='info', className='me-2 mb-2'),
            dbc.Button('Warning', color='warning', className='me-2 mb-2'),
            dbc.Button('Danger', color='danger', className='me-2 mb-2'),
        ], className='mb-3'),
        html.H6('Outline Buttons'),
        html.Div([
            dbc.Button('Primary', color='primary', outline=True, className='me-2 mb-2'),
            dbc.Button('Success', color='success', outline=True, className='me-2 mb-2'),
            dbc.Button('Info', color='info', outline=True, className='me-2 mb-2'),
            dbc.Button('Warning', color='warning', outline=True, className='me-2 mb-2'),
            dbc.Button('Danger', color='danger', outline=True, className='me-2 mb-2'),
        ], className='mb-3'),
        html.H6('Button Sizes'),
        html.Div([
            dbc.Button('Large', color='primary', size='lg', className='me-2 mb-2'),
            dbc.Button('Medium', color='primary', className='me-2 mb-2'),
            dbc.Button('Small', color='primary', size='sm', className='me-2 mb-2'),
        ])
    ])
], className='mb-4')

# Progress Bars
progress_bars = dbc.Card([
    dbc.CardHeader(html.H5('Progress Bars')),
    dbc.CardBody([
        html.P('Success Progress'),
        dbc.Progress(value=75, color='success', className='mb-3'),
        
        html.P('Info Progress'),
        dbc.Progress(value=50, color='info', className='mb-3'),
        
        html.P('Warning Progress'),
        dbc.Progress(value=60, color='warning', className='mb-3'),
        
        html.P('Danger Progress'),
        dbc.Progress(value=40, color='danger', className='mb-3'),
        
        html.P('Striped Progress'),
        dbc.Progress(value=65, color='success', striped=True, className='mb-3'),
        
        html.P('Animated Progress'),
        dbc.Progress(value=80, color='info', striped=True, animated=True),
    ])
], className='mb-4')

# Cards
cards_row = dbc.Row([
    dbc.Col([
        dbc.Card([
            dbc.CardHeader('Card Header'),
            dbc.CardBody([
                html.H5('Card Title', className='card-title'),
                html.P('This is a card with some content.'),
                dbc.Button('Action', color='primary'),
            ])
        ])
    ], md=4),
    dbc.Col([
        dbc.Card([
            dbc.CardBody([
                html.H5('Simple Card', className='card-title'),
                html.P('This is a simple card without header.'),
                dbc.Button('Click Me', color='success'),
            ])
        ])
    ], md=4),
    dbc.Col([
        dbc.Card([
            dbc.CardBody([
                html.H5('Info Card', className='card-title'),
                html.P('This card has important information.'),
                dbc.Button('Learn More', color='info'),
            ])
        ])
    ], md=4),
], className='mb-4')

# Spinners
spinners = dbc.Card([
    dbc.CardHeader(html.H5('Spinners')),
    dbc.CardBody([
        dbc.Spinner(color='primary', spinnerClassName='me-3'),
        dbc.Spinner(color='success', spinnerClassName='me-3'),
        dbc.Spinner(color='info', spinnerClassName='me-3'),
        dbc.Spinner(color='warning', spinnerClassName='me-3'),
        dbc.Spinner(color='danger', spinnerClassName='me-3'),
    ])
], className='mb-4')

# Tooltips and Popovers
tooltips = dbc.Card([
    dbc.CardHeader(html.H5('Interactive Elements')),
    dbc.CardBody([
        html.Div([
            dbc.Button('Hover for Tooltip', id='tooltip-target', color='primary', className='me-2'),
            dbc.Tooltip('This is a tooltip!', target='tooltip-target'),
            
            dbc.Button('Click for Popover', id='popover-target', color='success'),
            dbc.Popover([
                dbc.PopoverHeader('Popover Header'),
                dbc.PopoverBody('This is the popover content!'),
            ], target='popover-target', trigger='click'),
        ])
    ])
], className='mb-4')

layout = html.Div([
    dbc.Breadcrumb(items=[
        {'label': 'Home', 'href': '/', 'active': False},
        {'label': 'Widgets', 'active': True},
    ], className='breadcrumb'),
    
    alerts,
    badges,
    buttons,
    progress_bars,
    cards_row,
    spinners,
    tooltips,
])
