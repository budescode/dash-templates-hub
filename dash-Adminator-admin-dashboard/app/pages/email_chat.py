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


def create_compose_page():
    return html.Div(
        className="full-container",
        children=html.Div(
            className="email-app",
            children=[
                _email_side_nav(),
                html.Div(
                    className="email-wrapper row remain-height pos-r scrollable bgc-white",
                    children=html.Div(
                        className="email-content open no-inbox-view",
                        children=html.Div(
                            className="email-compose",
                            children=html.Form(
                                className="email-compose-body",
                                children=[
                                    html.H4("Send Message", className="c-grey-900 mB-20"),
                                    html.Div(
                                        className="send-header",
                                        children=[
                                            html.Div(dbc.Input(type="text", placeholder="To"), className="mb-3"),
                                            html.Div(dbc.Input(type="text", placeholder="CC"), className="mb-3"),
                                            html.Div(dbc.Input(type="text", placeholder="Email Subject"), className="mb-3"),
                                            html.Div(
                                                html.Textarea(placeholder="Say Hi...", className="form-control", rows=10),
                                                className="mb-3"
                                            ),
                                        ]
                                    ),
                                    html.Div(
                                        html.Button("Send", className="btn btn-danger btn-color"),
                                        className="text-end mrg-top-30"
                                    )
                                ]
                            )
                        )
                    )
                )
            ]
        )
    )


def create_chat_page():
    contacts = [
        ("John Doe",   "Online",  "c-green-500",  "https://randomuser.me/api/portraits/men/1.jpg"),
        ("Moo Doe",    "Away",    "c-amber-500",  "https://randomuser.me/api/portraits/men/2.jpg"),
        ("Adam Jones", "Offline", "c-grey-500",   "https://randomuser.me/api/portraits/men/3.jpg"),
        ("Mizo Doe",   "Busy",    "c-red-500",    "https://randomuser.me/api/portraits/men/4.jpg"),
        ("John Doe",   "Online",  "c-green-500",  "https://randomuser.me/api/portraits/men/1.jpg"),
        ("Moo Doe",    "Away",    "c-amber-500",  "https://randomuser.me/api/portraits/men/2.jpg"),
        ("Adam Jones", "Offline", "c-grey-500",   "https://randomuser.me/api/portraits/men/3.jpg"),
        ("Mizo Doe",   "Busy",    "c-red-500",    "https://randomuser.me/api/portraits/men/4.jpg"),
    ]

    def _bubble(time, text, reverse=False):
        return html.Div(
            className="peers fxw-nw ai-c pY-3 pX-10 bgc-white bdrs-2 lh-3/2",
            children=[
                html.Div(html.Small(time), className=f"peer {'mL-10 ord-1' if reverse else 'mR-10'}"),
                html.Div(html.Span(text),  className=f"peer-greed {'ord-0' if reverse else ''}")
            ]
        )

    return html.Div(
        className="full-container",
        children=html.Div(
            className="peers fxw-nw pos-r",
            children=[
                # Left sidebar
                html.Div(
                    className="peer bdR",
                    id="chat-sidebar",
                    children=html.Div(
                        className="layers h-100",
                        children=[
                            html.Div(
                                className="bdB layer w-100",
                                children=dbc.Input(
                                    type="text",
                                    placeholder="Search contacts...",
                                    className="p-15 bdrs-0 w-100 bdw-0",
                                    style={"border": "none", "outline": "none", "boxShadow": "none"}
                                )
                            ),
                            html.Div(
                                className="layer w-100 fxg-1 scrollable pos-r",
                                children=[
                                    html.Div(
                                        className="peers fxw-nw ai-c p-20 bdB bgc-white bgcH-grey-50 cur-p",
                                        children=[
                                            html.Div(
                                                html.Img(src=avatar, alt="", className="w-3r h-3r bdrs-50p"),
                                                className="peer"
                                            ),
                                            html.Div(
                                                className="peer peer-greed pL-20",
                                                children=[
                                                    html.H6(name, className="mB-0 lh-1 fw-400"),
                                                    html.Small(status, className=f"lh-1 {color_class}")
                                                ]
                                            )
                                        ]
                                    )
                                    for name, status, color_class, avatar in contacts
                                ]
                            )
                        ]
                    )
                ),
                # Chat box
                html.Div(
                    className="peer peer-greed",
                    id="chat-box",
                    children=html.Div(
                        className="layers h-100",
                        children=[
                            # Header
                            html.Div(
                                className="layer w-100",
                                children=html.Div(
                                    className="peers fxw-nw jc-sb ai-c pY-20 pX-30 bgc-white",
                                    children=[
                                        html.Div(
                                            className="peers ai-c",
                                            children=[
                                                html.Div(
                                                    html.Img(src="https://randomuser.me/api/portraits/men/12.jpg",
                                                             alt="", className="w-3r h-3r bdrs-50p"),
                                                    className="peer mR-20"
                                                ),
                                                html.Div(
                                                    className="peer",
                                                    children=[
                                                        html.H6("John Doe", className="lh-1 mB-0"),
                                                        html.I("Typing...", className="fsz-sm lh-1")
                                                    ]
                                                )
                                            ]
                                        ),
                                        html.Div(
                                            className="peers",
                                            children=[
                                                html.A(html.I(className="ti-video-camera"), href="#",
                                                       className="peer td-n c-grey-900 cH-blue-500 fsz-md mR-30"),
                                                html.A(html.I(className="ti-headphone"), href="#",
                                                       className="peer td-n c-grey-900 cH-blue-500 fsz-md mR-30"),
                                                html.A(html.I(className="ti-more"), href="#",
                                                       className="peer td-n c-grey-900 cH-blue-500 fsz-md"),
                                            ]
                                        )
                                    ]
                                )
                            ),
                            # Messages
                            html.Div(
                                className="layer w-100 fxg-1 bgc-grey-200 scrollable pos-r",
                                children=html.Div(
                                    className="p-20 gapY-15",
                                    children=[
                                        # Incoming
                                        html.Div(
                                            className="peers fxw-nw",
                                            children=[
                                                html.Div(
                                                    html.Img(className="w-2r bdrs-50p",
                                                             src="https://randomuser.me/api/portraits/men/11.jpg", alt=""),
                                                    className="peer mR-20"
                                                ),
                                                html.Div(
                                                    className="peer peer-greed",
                                                    children=html.Div(
                                                        className="layers ai-fs gapY-5",
                                                        children=[
                                                            html.Div(_bubble("10:00 AM", "Lorem Ipsum is simply dummy text of"), className="layer"),
                                                            html.Div(_bubble("10:00 AM", "the printing and typesetting industry."), className="layer"),
                                                            html.Div(_bubble("10:00 AM", "Lorem Ipsum has been the industry's"), className="layer"),
                                                        ]
                                                    )
                                                )
                                            ]
                                        ),
                                        # Outgoing
                                        html.Div(
                                            className="peers fxw-nw ai-fe",
                                            children=[
                                                html.Div(
                                                    html.Img(className="w-2r bdrs-50p",
                                                             src="https://randomuser.me/api/portraits/men/12.jpg", alt=""),
                                                    className="peer ord-1 mL-20"
                                                ),
                                                html.Div(
                                                    className="peer peer-greed ord-0",
                                                    children=html.Div(
                                                        className="layers ai-fe gapY-10",
                                                        children=[
                                                            html.Div(_bubble("10:00 AM", "Heloo", reverse=True), className="layer"),
                                                            html.Div(_bubble("10:00 AM", "??",    reverse=True), className="layer"),
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ),
                            # Send bar
                            html.Div(
                                className="layer w-100",
                                children=html.Div(
                                    className="p-20 bdT bgc-white",
                                    children=html.Div(
                                        className="pos-r",
                                        children=[
                                            dbc.Input(type="text", className="form-control bdrs-10em m-0",
                                                      placeholder="Say something..."),
                                            html.Button(
                                                html.I(className="fa fa-paper-plane-o"),
                                                type="button",
                                                className="btn btn-primary bdrs-50p w-2r p-0 h-2r pos-a r-1 t-1 btn-color"
                                            )
                                        ]
                                    )
                                )
                            )
                        ]
                    )
                )
            ]
        )
    )
