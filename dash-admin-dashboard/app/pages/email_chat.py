from dash import html
import dash_bootstrap_components as dbc


def _email_list_item():
    return html.Div(
        className="email-list-item peers fxw-nw p-20 bdB bgcH-grey-100 cur-p",
        children=[
            html.Div(
                className="peer mR-10",
                children=html.Div(
                    className="checkbox checkbox-circle checkbox-info peers ai-c",
                    children=[
                        dbc.Input(type="checkbox", className="peer"),
                        html.Label(className="form-label peers peer-greed js-sb ai-c")
                    ]
                )
            ),
            html.Div(
                className="peer peer-greed ov-h",
                children=[
                    html.Div(className="peers ai-c", children=[
                        html.Div(html.H6("John Doe"), className="peer peer-greed"),
                        html.Div(html.Small("1 min ago"), className="peer")
                    ]),
                    html.H5("title goes here", className="fsz-def tt-c c-grey-900"),
                    html.Span("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod",
                              className="whs-nw w-100 ov-h tov-e d-b")
                ]
            )
        ]
    )


def _toolbar():
    """Email toolbar: folder/tag buttons + dropdown + pagination"""
    return html.Div(
        className="bgc-grey-100 peers ai-c jc-sb p-20 fxw-nw",
        children=[
            html.Div(
                className="peer",
                children=html.Div(
                    className="btn-group",
                    role="group",
                    children=[
                        html.Button(html.I(className="ti-folder"), className="btn bgc-white bdrs-2 mR-3 cur-p"),
                        html.Button(html.I(className="ti-tag"), className="btn bgc-white bdrs-2 mR-3 cur-p"),
                        html.Div(
                            className="btn-group",
                            role="group",
                            children=[
                                html.Button(
                                    html.I(className="ti-more-alt"),
                                    id="email-dropdown-btn",
                                    className="btn cur-p bgc-white no-after dropdown-toggle",
                                    **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}
                                ),
                                html.Ul(
                                    className="dropdown-menu fsz-sm",
                                    children=[
                                        html.Li(html.A([html.I(className="ti-trash mR-10"), html.Span("Delete")],
                                                       href="#", className="d-b td-n pY-5 pX-10 bgcH-grey-100 c-grey-700")),
                                        html.Li(html.A([html.I(className="ti-alert mR-10"), html.Span("Mark as Spam")],
                                                       href="#", className="d-b td-n pY-5 pX-10 bgcH-grey-100 c-grey-700")),
                                        html.Li(html.A([html.I(className="ti-star mR-10"), html.Span("Star")],
                                                       href="#", className="d-b td-n pY-5 pX-10 bgcH-grey-100 c-grey-700")),
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),
            html.Div(
                className="peer",
                children=html.Div(
                    className="btn-group",
                    role="group",
                    children=[
                        html.Button(html.I(className="ti-angle-left"), className="fsz-xs btn bgc-white bdrs-2 mR-3 cur-p"),
                        html.Button(html.I(className="ti-angle-right"), className="fsz-xs btn bgc-white bdrs-2 mR-3 cur-p"),
                    ]
                )
            )
        ]
    )


def create_email_page():
    return html.Div(
        className="full-container",
        children=html.Div(
            className="email-app",
            children=[
                _email_side_nav(),
                # Email list + content wrapper
                html.Div(
                    className="email-wrapper row remain-height bgc-white ov-h",
                    children=[
                        # Middle: email list
                        html.Div(
                            className="email-list h-100 layers",
                            children=[
                                html.Div(className="layer w-100", children=_toolbar()),
                                html.Div(
                                    className="layer w-100",
                                    children=html.Div(
                                        className="bdT bdB",
                                        children=dbc.Input(type="text", placeholder="Search...", className="m-0 bdw-0 pY-15 pX-20")
                                    )
                                ),
                                html.Div(
                                    className="layer w-100 fxg-1 scrollable pos-r",
                                    children=[_email_list_item() for _ in range(11)]
                                )
                            ]
                        ),
                        # Right: email content
                        html.Div(
                            className="email-content h-100",
                            children=html.Div(
                                className="h-100 scrollable pos-r",
                                children=html.Div(
                                    className="email-content-wrapper",
                                    children=[
                                        # Email header
                                        html.Div(
                                            className="peers ai-c jc-sb pX-40 pY-30",
                                            children=[
                                                html.Div(
                                                    className="peers peer-greed",
                                                    children=[
                                                        html.Div(
                                                            html.Img(className="bdrs-50p w-3r h-3r",
                                                                     src="https://randomuser.me/api/portraits/men/11.jpg", alt=""),
                                                            className="peer mR-20"
                                                        ),
                                                        html.Div(
                                                            className="peer",
                                                            children=[
                                                                html.Small("Nov, 02 2024"),
                                                                html.H5("John Doe", className="c-grey-900 mB-5"),
                                                                html.Span("To: email@gmail.com")
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                html.Div(
                                                    html.A(html.I(className="fa fa-reply"),
                                                           href="#", className="btn btn-danger bdrs-50p p-15 lh-0"),
                                                    className="peer"
                                                )
                                            ]
                                        ),
                                        # Email body
                                        html.Div(
                                            className="bdT pX-40 pY-30",
                                            children=[
                                                html.H4("Title of this email goes here"),
                                                html.P("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod "
                                                       "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, "
                                                       "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo "
                                                       "consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse "
                                                       "cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non "
                                                       "proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
                                                html.P("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod "
                                                       "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, "
                                                       "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo"),
                                                html.P("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod "
                                                       "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam"),
                                            ]
                                        )
                                    ]
                                )
                            )
                        )
                    ]
                )
            ]
        )
    )


def _email_side_nav():
    """Shared email sidebar used by email and compose pages."""
    return html.Div(
        className="email-side-nav remain-height ov-h",
        children=html.Div(
            className="h-100 layers",
            children=[
                html.Div(
                    className="p-20 bgc-grey-100 layer w-100",
                    children=html.A("New Message", href="/compose", className="btn btn-danger d-grid")
                ),
                html.Div(
                    className="scrollable pos-r bdT layer w-100 fxg-1",
                    children=html.Ul(
                        className="p-20 nav flex-column",
                        children=[
                            html.Li(html.A(html.Div(className="peers ai-c jc-sb", children=[
                                html.Div([html.I(className="mR-10 ti-email"), html.Span("Inbox")], className="peer peer-greed"),
                                html.Div(html.Span("+99", className="badge rounded-pill bgc-deep-purple-50 c-deep-purple-700"), className="peer")
                            ]), href="#", className="nav-link c-grey-800 cH-blue-500 actived"), className="nav-item"),
                            html.Li(html.A(html.Div(className="peers ai-c jc-sb", children=[
                                html.Div([html.I(className="mR-10 ti-share"), html.Span("Sent")], className="peer peer-greed"),
                                html.Div(html.Span("12", className="badge rounded-pill bgc-green-50 c-green-700"), className="peer")
                            ]), href="#", className="nav-link c-grey-800 cH-blue-500"), className="nav-item"),
                            html.Li(html.A(html.Div(className="peers ai-c jc-sb", children=[
                                html.Div([html.I(className="mR-10 ti-star"), html.Span("Important")], className="peer peer-greed"),
                                html.Div(html.Span("3", className="badge rounded-pill bgc-blue-50 c-blue-700"), className="peer")
                            ]), href="#", className="nav-link c-grey-800 cH-blue-500"), className="nav-item"),
                            html.Li(html.A(html.Div(className="peers ai-c jc-sb", children=[
                                html.Div([html.I(className="mR-10 ti-file"), html.Span("Drafts")], className="peer peer-greed"),
                                html.Div(html.Span("5", className="badge rounded-pill bgc-amber-50 c-amber-700"), className="peer")
                            ]), href="#", className="nav-link c-grey-800 cH-blue-500"), className="nav-item"),
                            html.Li(html.A(html.Div(className="peers ai-c jc-sb", children=[
                                html.Div([html.I(className="mR-10 ti-alert"), html.Span("Spam")], className="peer peer-greed"),
                                html.Div(html.Span("1", className="badge rounded-pill bgc-red-50 c-red-700"), className="peer")
                            ]), href="#", className="nav-link c-grey-800 cH-blue-500"), className="nav-item"),
                            html.Li(html.A(html.Div(className="peers ai-c jc-sb", children=[
                                html.Div([html.I(className="mR-10 ti-trash"), html.Span("Trash")], className="peer peer-greed"),
                                html.Div(html.Span("+99", className="badge rounded-pill bgc-red-50 c-red-700"), className="peer")
                            ]), href="#", className="nav-link c-grey-800 cH-blue-500"), className="nav-item"),
                        ]
                    )
                )
            ]
        )
    )
