from dash import html
import dash_bootstrap_components as dbc


def create_forms_page():
    def _checkbox(label, id_, extra_class=""):
        return html.Div(
            className=f"checkbox checkbox-circle checkbox-info peers ai-c{' ' + extra_class if extra_class else ''}",
            children=[
                dbc.Input(type="checkbox", id=id_, className="peer"),
                html.Label(
                    htmlFor=id_,
                    className="form-label peers peer-greed js-sb ai-c",
                    children=html.Span(label, className="peer peer-greed")
                )
            ]
        )

    return html.Div(
        className="row gap-20 masonry pos-r",
        children=[
            html.Div(className="masonry-sizer col-md-6 pos-a"),

            # Basic Form
            html.Div(
                className="masonry-item col-md-6",
                children=html.Div(
                    className="bgc-white p-20 bd",
                    children=[
                        html.H6("Basic Form", className="c-grey-900"),
                        html.Div(
                            className="mT-30",
                            children=html.Form([
                                html.Div([
                                    html.Label("Email address", htmlFor="exampleInputEmail1", className="form-label"),
                                    dbc.Input(type="email", id="exampleInputEmail1",
                                              placeholder="Enter email"),
                                    html.Small("We'll never share your email with anyone else.",
                                               id="emailHelp", className="text-muted")
                                ], className="mb-3"),
                                html.Div([
                                    html.Label("Password", htmlFor="exampleInputPassword1", className="form-label"),
                                    dbc.Input(type="password", id="exampleInputPassword1", placeholder="Password"),
                                ], className="mb-3"),
                                _checkbox("Call John for Dinner", "inputCall1", extra_class="mB-15"),
                                html.Button("Submit", type="submit", className="btn btn-primary btn-color")
                            ])
                        )
                    ]
                )
            ),

            # Complex Form Layout
            html.Div(
                className="masonry-item col-md-6",
                children=html.Div(
                    className="bgc-white p-20 bd",
                    children=[
                        html.H6("Complex Form Layout", className="c-grey-900"),
                        html.Div(
                            className="mT-30",
                            children=html.Form([
                                html.Div(className="row", children=[
                                    html.Div([
                                        html.Label("Email", htmlFor="inputEmail4", className="form-label"),
                                        dbc.Input(type="email", id="inputEmail4", placeholder="Email")
                                    ], className="mb-3 col-md-6"),
                                    html.Div([
                                        html.Label("Password", htmlFor="inputPassword4", className="form-label"),
                                        dbc.Input(type="password", id="inputPassword4", placeholder="Password")
                                    ], className="mb-3 col-md-6"),
                                ]),
                                html.Div([
                                    html.Label("Address", htmlFor="inputAddress", className="form-label"),
                                    dbc.Input(type="text", id="inputAddress", placeholder="1234 Main St")
                                ], className="mb-3"),
                                html.Div([
                                    html.Label("Address 2", htmlFor="inputAddress2", className="form-label"),
                                    dbc.Input(type="text", id="inputAddress2",
                                              placeholder="Apartment, studio, or floor")
                                ], className="mb-3"),
                                html.Div(className="row", children=[
                                    html.Div([
                                        html.Label("City", htmlFor="inputCity", className="form-label"),
                                        dbc.Input(type="text", id="inputCity")
                                    ], className="mb-3 col-md-6"),
                                    html.Div([
                                        html.Label("State", htmlFor="inputState", className="form-label"),
                                        html.Select(
                                            [html.Option("Choose...", selected=True), html.Option("...")],
                                            id="inputState", className="form-control"
                                        )
                                    ], className="mb-3 col-md-4"),
                                    html.Div([
                                        html.Label("Zip", htmlFor="inputZip", className="form-label"),
                                        dbc.Input(type="text", id="inputZip")
                                    ], className="mb-3 col-md-2"),
                                ]),
                                html.Div(className="row", children=[
                                    html.Div([
                                        html.Label("Birthdate", className="form-label fw-500"),
                                        html.Div(
                                            className="timepicker-input input-icon mb-3",
                                            children=html.Div(
                                                className="input-group",
                                                children=[
                                                    html.Div(
                                                        html.I(className="ti-calendar"),
                                                        className="input-group-text bgc-white bd bdwR-0"
                                                    ),
                                                    dbc.Input(type="text", placeholder="Select Date",
                                                              className="bdc-grey-200 start-date")
                                                ]
                                            )
                                        )
                                    ], className="mb-3 col-md-6"),
                                ]),
                                html.Div(
                                    _checkbox("Call John for Dinner", "inputCall2"),
                                    className="mb-3"
                                ),
                                html.Button("Sign in", type="submit", className="btn btn-primary btn-color")
                            ])
                        )
                    ]
                )
            ),

            # Horizontal Form
            html.Div(
                className="masonry-item col-md-6",
                children=html.Div(
                    className="bgc-white p-20 bd",
                    children=[
                        html.H6("Horizontal Form", className="c-grey-900"),
                        html.Div(
                            className="mT-30",
                            children=html.Form([
                                html.Div(className="mb-3 row", children=[
                                    html.Label("Email", htmlFor="inputEmail3",
                                               className="form-label col-sm-2 col-form-label"),
                                    html.Div(
                                        dbc.Input(type="email", id="inputEmail3", placeholder="Email"),
                                        className="col-sm-10"
                                    ),
                                ]),
                                html.Div(className="mb-3 row", children=[
                                    html.Label("Password", htmlFor="inputPassword3",
                                               className="form-label col-sm-2 col-form-label"),
                                    html.Div(
                                        dbc.Input(type="password", id="inputPassword3", placeholder="Password"),
                                        className="col-sm-10"
                                    ),
                                ]),
                                html.Fieldset(className="mb-3", children=html.Div(className="row", children=[
                                    html.Legend("Radios", className="col-form-legend col-sm-2"),
                                    html.Div([
                                        html.Div(html.Label([
                                            dbc.Input(type="radio", name="gridRadios", id="gridRadios1",
                                                      value="option1",
                                                      className="form-check-input"),
                                            " Option one is this and that\u2014be sure to include why it's great"
                                        ], className="form-label form-check-label"), className="form-check"),
                                        html.Div(html.Label([
                                            dbc.Input(type="radio", name="gridRadios", id="gridRadios2",
                                                      value="option2", className="form-check-input"),
                                            " Option two can be something else and selecting it will deselect option one"
                                        ], className="form-label form-check-label"), className="form-check"),
                                        html.Div(html.Label([
                                            dbc.Input(type="radio", name="gridRadios", id="gridRadios3",
                                                      value="option3", disabled=True,
                                                      className="form-check-input"),
                                            " Option three is disabled"
                                        ], className="form-label form-check-label"), className="form-check disabled"),
                                    ], className="col-sm-10"),
                                ])),
                                html.Div(className="mb-3 row", children=[
                                    html.Div("Checkbox", className="col-sm-2"),
                                    html.Div(
                                        html.Div(html.Label([
                                            dbc.Input(type="checkbox", className="form-check-input"),
                                            " Check me out"
                                        ], className="form-label form-check-label"), className="form-check"),
                                        className="col-sm-10"
                                    ),
                                ]),
                                html.Div(className="mb-3 row", children=[
                                    html.Div(
                                        html.Button("Sign in", type="submit",
                                                    className="btn btn-primary btn-color"),
                                        className="col-sm-10"
                                    ),
                                ]),
                            ])
                        )
                    ]
                )
            ),

            # Disabled Forms
            html.Div(
                className="masonry-item col-md-6",
                children=html.Div(
                    className="bgc-white p-20 bd",
                    children=[
                        html.H6("Disabled Forms", className="c-grey-900"),
                        html.Div(
                            className="mT-30",
                            children=html.Form([
                                html.Fieldset(disabled=True, children=[
                                    html.Div([
                                        html.Label("Disabled input", htmlFor="disabledTextInput",
                                                   className="form-label"),
                                        dbc.Input(type="text", id="disabledTextInput",
                                                  placeholder="Disabled input")
                                    ], className="mb-3"),
                                    html.Div([
                                        html.Label("Disabled select menu", htmlFor="disabledSelect",
                                                   className="form-label"),
                                        html.Select(
                                            html.Option("Disabled select"),
                                            id="disabledSelect", className="form-control"
                                        )
                                    ], className="mb-3"),
                                    html.Div(
                                        html.Label([
                                            dbc.Input(type="checkbox", className="form-check-input"),
                                            " Can't check this"
                                        ], className="form-label form-check-label"),
                                        className="form-check"
                                    ),
                                    html.Button("Submit", type="submit", className="btn btn-primary btn-color")
                                ])
                            ])
                        )
                    ]
                )
            ),

            # Validation
            html.Div(
                className="masonry-item col-md-6",
                children=html.Div(
                    className="bgc-white p-20 bd",
                    children=[
                        html.H6("Validation", className="c-grey-900"),
                        html.Div(
                            className="mT-30",
                            children=html.Form(
                                className="container",
                                id="needs-validation",
                                children=[
                                    html.Div(className="row", children=[
                                        html.Div([
                                            html.Label("First name", htmlFor="validationCustom01",
                                                       className="form-label"),
                                            dbc.Input(type="text", id="validationCustom01",
                                                      placeholder="First name", value="Mark", required=True)
                                        ], className="col-md-6 mb-3"),
                                        html.Div([
                                            html.Label("Last name", htmlFor="validationCustom02",
                                                       className="form-label"),
                                            dbc.Input(type="text", id="validationCustom02",
                                                      placeholder="Last name", value="Otto", required=True)
                                        ], className="col-md-6 mb-3"),
                                    ]),
                                    html.Div(className="row", children=[
                                        html.Div([
                                            html.Label("City", htmlFor="validationCustom03",
                                                       className="form-label"),
                                            dbc.Input(type="text", id="validationCustom03",
                                                      placeholder="City", required=True),
                                            html.Div("Please provide a valid city.",
                                                     className="invalid-feedback")
                                        ], className="col-md-6 mb-3"),
                                        html.Div([
                                            html.Label("State", htmlFor="validationCustom04",
                                                       className="form-label"),
                                            dbc.Input(type="text", id="validationCustom04",
                                                      placeholder="State", required=True),
                                            html.Div("Please provide a valid state.",
                                                     className="invalid-feedback")
                                        ], className="col-md-3 mb-3"),
                                        html.Div([
                                            html.Label("Zip", htmlFor="validationCustom05",
                                                       className="form-label"),
                                            dbc.Input(type="text", id="validationCustom05",
                                                      placeholder="Zip", required=True),
                                            html.Div("Please provide a valid zip.",
                                                     className="invalid-feedback")
                                        ], className="col-md-3 mb-3"),
                                    ]),
                                    html.Button("Submit form", type="submit",
                                                className="btn btn-primary btn-color")
                                ]
                            )
                        )
                    ]
                )
            ),
        ]
    )
