from dash import html
import dash_bootstrap_components as dbc


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
