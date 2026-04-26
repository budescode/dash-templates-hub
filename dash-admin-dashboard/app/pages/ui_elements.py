from dash import html


def _card(title, content):
    return html.Div(
        className="masonry-item col-md-6",
        children=html.Div(
            className="bgc-white p-20 bd",
            children=[
                html.H6(title, className="c-grey-900"),
                html.Div(className="mT-30", children=content)
            ]
        )
    )


def _btn(label, color, extra=""):
    return html.Div(
        html.Button(label, type="button",
                    className=f"btn cur-p btn-{color}{' btn-color' if color not in ('warning','light') else ''}{' ' + extra if extra else ''}"),
        className="peer"
    )


def create_ui_elements_page():
    return html.Div(
        className="row gap-20 masonry pos-r",
        children=[
            html.Div(className="masonry-sizer col-md-6 pos-a"),

            # Alerts
            _card("Alerts", [
                html.Div("This is a primary alert\u2014check it out!", className="alert alert-primary", role="alert"),
                html.Div("This is a secondary alert\u2014check it out!", className="alert alert-secondary", role="alert"),
                html.Div("This is a success alert\u2014check it out!", className="alert alert-success", role="alert"),
                html.Div("This is a danger alert\u2014check it out!", className="alert alert-danger", role="alert"),
                html.Div("This is a warning alert\u2014check it out!", className="alert alert-warning", role="alert"),
                html.Div("This is a info alert\u2014check it out!", className="alert alert-info", role="alert"),
                html.Div("This is a light alert\u2014check it out!", className="alert alert-light", role="alert"),
                html.Div("This is a dark alert\u2014check it out!", className="alert alert-dark", role="alert"),
            ]),

            # Buttons
            _card("Buttons", [
                html.Div(className="gap-10 peers", children=[
                    _btn("Primary", "primary"),
                    _btn("Secondary", "secondary"),
                    _btn("Success", "success"),
                    _btn("Danger", "danger"),
                    _btn("Warning", "warning"),
                    _btn("Info", "info"),
                    _btn("Light", "light"),
                    _btn("Dark", "dark"),
                ]),
                html.Div(className="w-100 gap-10 peers mY-20", children=[
                    html.Div(html.Button("Primary", type="button", className="btn cur-p btn-outline-primary"), className="peer"),
                    html.Div(html.Button("Secondary", type="button", className="btn cur-p btn-outline-secondary"), className="peer"),
                    html.Div(html.Button("Success", type="button", className="btn cur-p btn-outline-success"), className="peer"),
                    html.Div(html.Button("Danger", type="button", className="btn cur-p btn-outline-danger"), className="peer"),
                    html.Div(html.Button("Warning", type="button", className="btn cur-p btn-outline-warning"), className="peer"),
                    html.Div(html.Button("Info", type="button", className="btn cur-p btn-outline-info"), className="peer"),
                    html.Div(html.Button("Light", type="button", className="btn cur-p btn-outline-light"), className="peer"),
                    html.Div(html.Button("Dark", type="button", className="btn cur-p btn-outline-dark"), className="peer"),
                ]),
                html.Div(className="btn-toolbar", role="toolbar", children=[
                    html.Div(className="btn-group me-2", role="group", children=[
                        html.Button("1", type="button", className="btn btn-success btn-color"),
                        html.Button("2", type="button", className="btn btn-success btn-color"),
                        html.Button("3", type="button", className="btn btn-success btn-color"),
                        html.Button("4", type="button", className="btn btn-success btn-color"),
                    ]),
                    html.Div(className="btn-group me-2", role="group", children=[
                        html.Button("5", type="button", className="btn btn-success btn-color"),
                        html.Button("6", type="button", className="btn btn-success btn-color"),
                        html.Button("7", type="button", className="btn btn-success btn-color"),
                    ]),
                    html.Div(className="btn-group", role="group", children=[
                        html.Button("8", type="button", className="btn btn-success btn-color"),
                    ]),
                ]),
            ]),

            # Dropdowns
            _card("Dropdowns", [
                html.Div(className="dropdown", children=[
                    html.Button("Dropdown button", type="button",
                                className="btn btn-secondary dropdown-toggle",
                                id="dropdownMenuButton",
                                **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}),
                    html.Div(className="dropdown-menu", **{"aria-labelledby": "dropdownMenuButton"}, children=[
                        html.A("Action", className="dropdown-item", href="#"),
                        html.A("Another action", className="dropdown-item", href="#"),
                        html.A("Something else here", className="dropdown-item", href="#"),
                    ]),
                ]),
                html.Div(className="btn-group mT-20", children=[
                    html.Button("Action", type="button", className="btn btn-danger btn-color"),
                    html.Button(
                        html.Span("Toggle Dropdown", className="visually-hidden"),
                        type="button",
                        className="btn btn-danger dropdown-toggle dropdown-toggle-split",
                        **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}
                    ),
                    html.Div(className="dropdown-menu", children=[
                        html.A("Action", className="dropdown-item", href="#"),
                        html.A("Another action", className="dropdown-item", href="#"),
                        html.A("Something else here", className="dropdown-item", href="#"),
                        html.Div(className="dropdown-divider"),
                        html.A("Separated link", className="dropdown-item", href="#"),
                    ]),
                ]),
            ]),

            # List Group
            _card("List Group", [
                html.Div(className="list-group", children=[
                    html.A("The current link item", href="#",
                           className="list-group-item list-group-item-action active",
                           **{"aria-current": "true"}),
                    html.A("A second link item", href="#", className="list-group-item list-group-item-action"),
                    html.A("A third link item", href="#", className="list-group-item list-group-item-action"),
                    html.A("A fourth link item", href="#", className="list-group-item list-group-item-action"),
                    html.A("A disabled link item", href="#",
                           className="list-group-item list-group-item-action disabled",
                           tabIndex="-1", **{"aria-disabled": "true"}),
                ]),
            ]),

            # Modal
            _card("Modal", [
                html.Button("Launch demo modal", type="button",
                            className="btn btn-primary btn-color",
                            **{"data-bs-toggle": "modal", "data-bs-target": "#exampleModal"}),
                html.Div(
                    className="modal fade", id="exampleModal", tabIndex="-1",
                    **{"aria-labelledby": "exampleModalLabel", "aria-hidden": "true"},
                    children=html.Div(className="modal-dialog", children=html.Div(className="modal-content", children=[
                        html.Div(className="modal-header", children=[
                            html.H5("Modal title", className="modal-title", id="exampleModalLabel"),
                            html.Button(type="button", className="btn-close",
                                        **{"data-bs-dismiss": "modal", "aria-label": "Close"}),
                        ]),
                        html.Div("...", className="modal-body"),
                        html.Div(className="modal-footer", children=[
                            html.Button("Close", type="button", className="btn btn-secondary",
                                        **{"data-bs-dismiss": "modal"}),
                            html.Button("Save changes", type="button", className="btn btn-primary"),
                        ]),
                    ]))
                ),
            ]),

            # Popover
            _card("Popover", [
                html.Button("Click to toggle popover", type="button",
                            className="btn btn-lg btn-danger btn-color",
                            **{"data-bs-toggle": "popover",
                               "title": "Popover title",
                               "data-bs-content": "And here's some amazing content. It's very engaging. Right?"}),
            ]),

            # Progress
            _card("Progress", [
                html.Div(className="layers", children=[
                    html.Div(className="layer w-100", children=[
                        html.H5("100k", className="mB-5"),
                        html.Small("Visitors From USA", className="fw-600 c-grey-700"),
                        html.Span("50%", className="pull-right c-grey-600 fsz-sm"),
                        html.Div(className="progress mT-10", children=html.Div(
                            className="progress-bar bgc-deep-purple-500", role="progressbar",
                            style={"width": "50%"},
                            **{"aria-valuenow": "50", "aria-valuemin": "0", "aria-valuemax": "100"},
                            children=html.Span("50% Complete", className="visually-hidden")
                        )),
                    ]),
                    html.Div(className="layer w-100 mT-15", children=[
                        html.H5("1M", className="mB-5"),
                        html.Small("Visitors From Europe", className="fw-600 c-grey-700"),
                        html.Span("80%", className="pull-right c-grey-600 fsz-sm"),
                        html.Div(className="progress mT-10", children=html.Div(
                            className="progress-bar bgc-green-500", role="progressbar",
                            style={"width": "80%"},
                            **{"aria-valuenow": "80", "aria-valuemin": "0", "aria-valuemax": "100"},
                            children=html.Span("80% Complete", className="visually-hidden")
                        )),
                    ]),
                    html.Div(className="layer w-100 mT-15", children=[
                        html.H5("450k", className="mB-5"),
                        html.Small("Visitors From Australia", className="fw-600 c-grey-700"),
                        html.Span("40%", className="pull-right c-grey-600 fsz-sm"),
                        html.Div(className="progress mT-10", children=html.Div(
                            className="progress-bar bgc-light-blue-500", role="progressbar",
                            style={"width": "40%"},
                            **{"aria-valuenow": "40", "aria-valuemin": "0", "aria-valuemax": "100"},
                            children=html.Span("40% Complete", className="visually-hidden")
                        )),
                    ]),
                    html.Div(className="layer w-100 mT-15", children=[
                        html.H5("1B", className="mB-5"),
                        html.Small("Visitors From India", className="fw-600 c-grey-700"),
                        html.Span("90%", className="pull-right c-grey-600 fsz-sm"),
                        html.Div(className="progress mT-10", children=html.Div(
                            className="progress-bar bgc-blue-grey-500", role="progressbar",
                            style={"width": "90%"},
                            **{"aria-valuenow": "90", "aria-valuemin": "0", "aria-valuemax": "100"},
                            children=html.Span("90% Complete", className="visually-hidden")
                        )),
                    ]),
                ]),
            ]),

            # Tooltips
            _card("Tooltips", [
                html.Button("Tooltip on top", type="button",
                            className="btn btn-primary btn-color",
                            **{"data-bs-toggle": "tooltip", "data-bs-placement": "top", "title": "Tooltip on top"}),
                html.Button("Tooltip on right", type="button",
                            className="btn btn-secondary btn-color",
                            **{"data-bs-toggle": "tooltip", "data-bs-placement": "right", "title": "Tooltip on right"}),
                html.Button("Tooltip on bottom", type="button",
                            className="btn btn-success btn-color",
                            **{"data-bs-toggle": "tooltip", "data-bs-placement": "bottom", "title": "Tooltip on bottom"}),
                html.Button("Tooltip on left", type="button",
                            className="btn btn-danger btn-color",
                            **{"data-bs-toggle": "tooltip", "data-bs-placement": "left", "title": "Tooltip on left"}),
            ]),

            # Button Sizes
            _card("Button Sizes", [
                html.Button("Large button", type="button", className="btn btn-primary btn-lg btn-color mR-10"),
                html.Button("Large button", type="button", className="btn btn-secondary btn-lg mR-10"),
                html.Br(), html.Br(),
                html.Button("Default button", type="button", className="btn btn-primary btn-color mR-10"),
                html.Button("Default button", type="button", className="btn btn-secondary mR-10"),
                html.Br(), html.Br(),
                html.Button("Small button", type="button", className="btn btn-primary btn-sm btn-color mR-10"),
                html.Button("Small button", type="button", className="btn btn-secondary btn-sm mR-10"),
            ]),

            # Badges
            _card("Badges", [
                html.H5(["Example heading ", html.Span("New", className="badge bg-primary")]),
                html.H5(["Example heading ", html.Span("2", className="badge bg-secondary")]),
                html.H5(["Example heading ", html.Span("Success", className="badge bg-success")]),
                html.H5(["Example heading ", html.Span("Danger", className="badge bg-danger")]),
                html.H5(["Example heading ", html.Span("Warning", className="badge bg-warning text-dark")]),
                html.H5(["Example heading ", html.Span("Info", className="badge bg-info")]),
                html.H5(["Example heading ", html.Span("Light", className="badge bg-light text-dark")]),
                html.H5(["Example heading ", html.Span("Dark", className="badge bg-dark")]),
            ]),

            # Accordion
            _card("Accordion", [
                html.Div(className="accordion", id="accordionExample", children=[
                    html.Div(className="accordion-item", children=[
                        html.H2(
                            html.Button("Accordion Item #1", className="accordion-button", type="button",
                                        **{"data-bs-toggle": "collapse", "data-bs-target": "#collapseOne",
                                           "aria-expanded": "true", "aria-controls": "collapseOne"}),
                            className="accordion-header", id="headingOne"
                        ),
                        html.Div(
                            html.Div(
                                "This is the first item's accordion body. It is shown by default, until the collapse plugin adds the appropriate classes.",
                                className="accordion-body"
                            ),
                            className="accordion-collapse collapse show", id="collapseOne",
                            **{"aria-labelledby": "headingOne", "data-bs-parent": "#accordionExample"}
                        ),
                    ]),
                    html.Div(className="accordion-item", children=[
                        html.H2(
                            html.Button("Accordion Item #2", className="accordion-button collapsed", type="button",
                                        **{"data-bs-toggle": "collapse", "data-bs-target": "#collapseTwo",
                                           "aria-expanded": "false", "aria-controls": "collapseTwo"}),
                            className="accordion-header", id="headingTwo"
                        ),
                        html.Div(
                            html.Div(
                                "This is the second item's accordion body. It is hidden by default, until the collapse plugin adds the appropriate classes.",
                                className="accordion-body"
                            ),
                            className="accordion-collapse collapse", id="collapseTwo",
                            **{"aria-labelledby": "headingTwo", "data-bs-parent": "#accordionExample"}
                        ),
                    ]),
                ]),
            ]),

            # Cards
            _card("Cards", [
                html.Div(className="card", style={"width": "18rem"}, children=html.Div(className="card-body", children=[
                    html.H5("Card title", className="card-title"),
                    html.H6("Card subtitle", className="card-subtitle mb-2 text-muted"),
                    html.P("Some quick example text to build on the card title and make up the bulk of the card's content.",
                           className="card-text"),
                    html.A("Card link", href="#", className="card-link"),
                    html.A("Another link", href="#", className="card-link"),
                ])),
            ]),

            # List Groups
            _card("List Groups", [
                html.Ul(className="list-group", children=[
                    html.Li("An item", className="list-group-item"),
                    html.Li("A second item", className="list-group-item"),
                    html.Li("A third item", className="list-group-item"),
                    html.Li("A fourth item", className="list-group-item"),
                    html.Li("And a fifth one", className="list-group-item"),
                ]),
                html.Br(),
                html.Div(className="list-group", children=[
                    html.A("The current link item", href="#", className="list-group-item list-group-item-action active"),
                    html.A("A second link item", href="#", className="list-group-item list-group-item-action"),
                    html.A("A third link item", href="#", className="list-group-item list-group-item-action"),
                    html.A("A fourth link item", href="#", className="list-group-item list-group-item-action"),
                ]),
            ]),

            # Spinners
            _card("Spinners", [
                *[html.Div(html.Span("Loading...", className="visually-hidden"),
                           className=f"spinner-border text-{c}", role="status")
                  for c in ["primary", "secondary", "success", "danger", "warning", "info", "light", "dark"]],
                html.Br(), html.Br(),
                *[html.Div(html.Span("Loading...", className="visually-hidden"),
                           className=f"spinner-grow text-{c}", role="status")
                  for c in ["primary", "secondary", "success", "danger"]],
            ]),
        ]
    )
