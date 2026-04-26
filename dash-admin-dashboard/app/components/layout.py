from dash import html, dcc
import dash_bootstrap_components as dbc

NOTIFICATION_ITEMS = [
    {
        "name": "John Doe",
        "time": "5 mins ago",
        "avatar": "https://randomuser.me/api/portraits/men/1.jpg",
        "message": "liked your post"
    },
    {
        "name": "Moo Doe",
        "time": "7 mins ago",
        "avatar": "https://randomuser.me/api/portraits/men/2.jpg",
        "message": "liked your cover image"
    },
    {
        "name": "Lee Doe",
        "time": "10 mins ago",
        "avatar": "https://randomuser.me/api/portraits/men/3.jpg",
        "message": "commented on your video"
    }
]

EMAIL_ITEMS = [
    {
        "name": "John Doe",
        "time": "5 mins ago",
        "avatar": "https://randomuser.me/api/portraits/men/1.jpg",
        "subject": "Want to create your own customized data generator for your app..."
    },
    {
        "name": "Moo Doe",
        "time": "15 mins ago",
        "avatar": "https://randomuser.me/api/portraits/men/2.jpg",
        "subject": "Want to create your own customized data generator for your app..."
    },
    {
        "name": "Lee Doe",
        "time": "25 mins ago",
        "avatar": "https://randomuser.me/api/portraits/men/3.jpg",
        "subject": "Want to create your own customized data generator for your app..."
    }
]


def _build_dropdown_items(items, is_notification=True):
    """Render dropdown list items for notifications/emails"""
    children = []
    for entry in items:
        children.append(
            html.Li([
                html.A(
                    className='peers fxw-nw td-n p-20 bdB c-grey-800 cH-blue bgcH-grey-100',
                    href='#',
                    children=[
                        html.Div(
                            html.Img(className='w-3r bdrs-50p', src=entry['avatar'], alt=entry['name']),
                            className='peer mR-15'
                        ),
                        html.Div(
                            className='peer peer-greed',
                            children=[
                                html.Span([
                                    html.Span(entry['name'], className='fw-500'),
                                    html.Span(' '),
                                    html.Span(
                                        entry['message'] if is_notification else entry['subject'],
                                        className='c-grey-600'
                                    )
                                ]),
                                html.P(html.Small(entry['time'], className='fsz-xs'), className='m-0')
                            ]
                        )
                    ]
                )
            ])
        )
    return children


def create_header():
    """Create Adminator-style header"""
    return html.Div(
        className='header navbar',
        children=html.Div(
            className='header-container',
            children=[
                html.Ul(
                    className='nav-left',
                    children=[
                        html.Li(
                            html.A(html.I(className='ti-menu'), id='sidebar-toggle', className='sidebar-toggle', href='#')
                        ),
                        html.Li(
                            className='search-box',
                            children=html.A(
                                className='search-toggle no-pdd-right',
                                href='#',
                                children=[
                                    html.I(className='search-icon ti-search pdd-right-10'),
                                    html.I(className='search-icon-close ti-close pdd-right-10')
                                ]
                            )
                        ),
                        html.Li(
                            className='search-input',
                            children=dbc.Input(className='form-control', placeholder='Search...', type='text')
                        )
                    ]
                ),
                html.Ul(
                    className='nav-right',
                    children=[
                        html.Li(
                            className='notifications dropdown',
                            children=[
                                html.Span('3', className='counter bgc-red'),
                                html.A(
                                    html.I(className='ti-bell'),
                                    className='dropdown-toggle no-after',
                                    href='',
                                    **{'data-bs-toggle': 'dropdown', 'aria-expanded': 'false'}
                                ),
                                html.Ul(
                                    className='dropdown-menu',
                                    children=[
                                        html.Li([
                                            html.I(className='ti-bell pR-10'),
                                            html.Span('Notifications', className='fsz-sm fw-600 c-grey-900')
                                        ], className='pX-20 pY-15 bdB'),
                                        html.Li(
                                            html.Ul(
                                                className='ovY-a pos-r scrollable lis-n p-0 m-0 fsz-sm',
                                                children=_build_dropdown_items(NOTIFICATION_ITEMS)
                                            )
                                        ),
                                        html.Li(
                                            html.Span(
                                                dcc.Link('View All Notifications', href='/', className='c-grey-600 cH-blue fsz-sm td-n'),
                                                className='c-grey-600 cH-blue fsz-sm td-n'
                                            ),
                                            className='pX-20 pY-15 ta-c bdT'
                                        )
                                    ]
                                )
                            ]
                        ),
                        html.Li(
                            className='notifications dropdown',
                            children=[
                                html.Span('3', className='counter bgc-blue'),
                                html.A(
                                    html.I(className='ti-email'),
                                    className='dropdown-toggle no-after',
                                    href='',
                                    **{'data-bs-toggle': 'dropdown', 'aria-expanded': 'false'}
                                ),
                                html.Ul(
                                    className='dropdown-menu',
                                    children=[
                                        html.Li([
                                            html.I(className='ti-email pR-10'),
                                            html.Span('Emails', className='fsz-sm fw-600 c-grey-900')
                                        ], className='pX-20 pY-15 bdB'),
                                        html.Li(
                                            html.Ul(
                                                className='ovY-a pos-r scrollable lis-n p-0 m-0 fsz-sm',
                                                children=_build_dropdown_items(EMAIL_ITEMS, is_notification=False)
                                            )
                                        ),
                                        html.Li(
                                            html.Span(
                                                dcc.Link('View All Email', href='/email', className='c-grey-600 cH-blue fsz-sm td-n'),
                                                className='c-grey-600 cH-blue fsz-sm td-n'
                                            ),
                                            className='pX-20 pY-15 ta-c bdT'
                                        )
                                    ]
                                )
                            ]
                        ),
                        html.Li(
                            className='mR-20',
                            children=html.A(
                                html.I(id='theme-icon', className='fa fa-moon-o'),
                                id='theme-toggle',
                                href='#',
                                className='td-n c-grey-700 cH-blue-500 fsz-md',
                                title='Toggle dark mode'
                            )
                        ),
                        html.Li(
                            className='dropdown',
                            children=[
                                html.A(
                                    className='dropdown-toggle no-after peers fxw-nw ai-c lh-1',
                                    href='',
                                    **{'data-bs-toggle': 'dropdown', 'aria-expanded': 'false'},
                                    children=[
                                        html.Div(
                                            html.Img(className='w-2r bdrs-50p', src='https://randomuser.me/api/portraits/men/10.jpg', alt='John Doe'),
                                            className='peer mR-10'
                                        ),
                                        html.Div(html.Span('John Doe', className='fsz-sm c-grey-900'), className='peer')
                                    ]
                                ),
                                html.Ul(
                                    className='dropdown-menu fsz-sm',
                                    children=[
                                        html.Li(html.A([
                                            html.I(className='ti-settings mR-10'),
                                            html.Span('Setting')
                                        ], href='', className='d-b td-n pY-5 bgcH-grey-100 c-grey-700')),
                                        html.Li(html.A([
                                            html.I(className='ti-user mR-10'),
                                            html.Span('Profile')
                                        ], href='', className='d-b td-n pY-5 bgcH-grey-100 c-grey-700')),
                                        html.Li(dcc.Link([
                                            html.I(className='ti-email mR-10'),
                                            html.Span('Messages')
                                        ], href='/email', className='d-b td-n pY-5 bgcH-grey-100 c-grey-700')),
                                        html.Li(role='separator', className='divider'),
                                        html.Li(html.A([
                                            html.I(className='ti-power-off mR-10'),
                                            html.Span('Logout')
                                        ], href='', className='d-b td-n pY-5 bgcH-grey-100 c-grey-700'))
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    )


def create_sidebar():
    """Create Adminator sidebar shell with logo and menu placeholder"""
    logo_section = html.Div(
        className='sidebar-logo',
        children=html.Div(
            className='peers ai-c fxw-nw',
            children=[
                html.Div(
                    className='peer peer-greed',
                    children=dcc.Link(
                        className='sidebar-link td-n',
                        href='/',
                        children=html.Div(
                            className='peers ai-c fxw-nw',
                            children=[
                                html.Div(
                                    className='peer',
                                    children=html.Div(
                                        className='logo',
                                        children=html.Img(src='/assets/static/images/logo.svg', alt='Adminator Logo')
                                    )
                                ),
                                html.Div(
                                    className='peer peer-greed',
                                    children=html.H5('Adminator', className='lh-1 mB-0 logo-text')
                                )
                            ]
                        )
                    )
                ),
                html.Div(
                    className='peer',
                    children=html.Div(
                        className='mobile-toggle sidebar-toggle',
                        children=html.A(html.I(className='ti-arrow-circle-left'), href='#', className='td-n')
                    )
                )
            ]
        )
    )

    return html.Div(
        className='sidebar',
        children=html.Div(
            className='sidebar-inner',
            children=[
                logo_section,
                html.Ul(id='sidebar-menu', className='sidebar-menu scrollable pos-r')
            ]
        )
    )

