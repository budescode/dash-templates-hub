from dash import html


def _event_item(icon_color, title, date, category):
    return html.Li(
        className="bdB peers ai-c jc-sb fxw-nw",
        children=[
            html.A(
                className="td-n p-20 peers fxw-nw me-20 peer-greed c-grey-900",
                href="#",
                children=[
                    html.Div(html.I(className=f"fa fa-fw fa-clock-o {icon_color}"), className="peer mR-15"),
                    html.Div([
                        html.Span(title, className="fw-600"),
                        html.Div([
                            html.Span(date, className="c-grey-700"),
                            html.I(category)
                        ], className="c-grey-600")
                    ], className="peer")
                ]
            ),
            html.Div(
                className="peers mR-15",
                children=[
                    html.Div(html.A(html.I(className="ti-pencil"), href="#", className="td-n c-deep-purple-500 cH-blue-500 fsz-md p-5"), className="peer"),
                    html.Div(html.A(html.I(className="ti-trash"), href="#", className="td-n c-red-500 cH-blue-500 fsz-md p-5"), className="peer"),
                ]
            )
        ]
    )


def create_calendar_page():
    events = [
        ("c-red-500",    "All Day Event", "Nov 01 - ", "Website Development"),
        ("c-blue-500",   "All Day Event", "Nov 01 - ", "Website Development"),
        ("c-indigo-500", "All Day Event", "Nov 01 - ", "Website Development"),
        ("c-green-500",  "All Day Event", "Nov 01 - ", "Website Development"),
    ]

    return html.Div(
        className="container-fluid",
        children=html.Div(
            className="row",
            children=[
                # Left panel
                html.Div(
                    className="col-md-4",
                    children=html.Div(
                        className="bdrs-3 ov-h bgc-white bd",
                        children=[
                            html.Div(
                                className="bgc-deep-purple-500 ta-c p-30",
                                children=[
                                    html.H1(["01", html.Span("st", className="fsz-def")],
                                            className="fw-300 mB-5 lh-1 c-white"),
                                    html.H3("Monday", className="c-white")
                                ]
                            ),
                            html.Div(
                                className="pos-r",
                                children=[
                                    html.Button(
                                        html.I(className="ti-plus"),
                                        type="button",
                                        className="mT-nv-50 pos-a r-10 t-2 btn cur-p bdrs-50p p-0 w-3r h-3r btn-warning"
                                    ),
                                    html.Ul(
                                        className="m-0 p-0 mT-20",
                                        children=[_event_item(*e) for e in events]
                                    )
                                ]
                            )
                        ]
                    )
                ),
                # Right panel — FullCalendar
                html.Div(
                    className="col-md-8",
                    children=html.Div(id="fullcalendar", style={"minHeight": "600px"})
                )
            ]
        )
    )
