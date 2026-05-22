from dash import html
import dash_bootstrap_components as dbc


layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row(
            className="g-3",
            children=[
                dbc.Col(
                    children=[
                        dbc.Row(
                            className="g-3",
                            children=[
                                dbc.Col(
                                    html.Div(
                                        className="credit-card",
                                        children=[
                                            html.Div("Purity UI", style={"fontWeight": "700", "fontSize": "14px"}),
                                            html.Div(
                                                "7812 2139 0823 XXXX",
                                                style={"fontSize": "18px", "letterSpacing": "2px", "marginTop": "30px"},
                                            ),
                                            html.Div("VALID THRU 05/24", style={"fontSize": "10px", "marginTop": "20px"}),
                                        ],
                                    ),
                                    xs=12,
                                    md=6,
                                ),
                                dbc.Col(
                                    html.Div(
                                        className="card-surface billing-card",
                                        children=[
                                            html.Div(className="mini-icon", children=html.I(className="fa-solid fa-wallet")),
                                            html.Div("Salary", className="section-title"),
                                            html.Div("+$2000", style={"fontWeight": "700"}),
                                        ],
                                    ),
                                    xs=6,
                                    md=3,
                                ),
                                dbc.Col(
                                    html.Div(
                                        className="card-surface billing-card",
                                        children=[
                                            html.Div(className="mini-icon", children=html.I(className="fa-brands fa-paypal")),
                                            html.Div("Paypal", className="section-title"),
                                            html.Div("$455.00", style={"fontWeight": "700"}),
                                        ],
                                    ),
                                    xs=6,
                                    md=3,
                                ),
                            ],
                        ),
                        dbc.Row(
                            className="g-3 row-gap",
                            children=[
                                dbc.Col(
                                    html.Div(
                                        className="card-surface chart-card payment-method-card",
                                        children=[
                                            html.Div(
                                                className="card-header-row",
                                                children=[
                                                    html.Div("Payment Method", className="chart-title"),
                                                    html.Button("ADD A NEW CARD", className="btn-dark-pill"),
                                                ],
                                            ),
                                            dbc.Row(
                                                className="g-3",
                                                children=[
                                                    dbc.Col(
                                                        html.Div(
                                                            className="payment-pill",
                                                            children=[
                                                                html.Div(
                                                                    className="payment-left",
                                                                    children=[
                                                                        html.Div(
                                                                            className="card-dots",
                                                                            children=[
                                                                                html.Span(className="dot dot-red"),
                                                                                html.Span(className="dot dot-orange"),
                                                                            ],
                                                                        ),
                                                                        html.Span("7812 2139 0823 XXXX", className="stat-label"),
                                                                    ],
                                                                ),
                                                                html.I(className="fa-regular fa-pen-to-square"),
                                                            ],
                                                        ),
                                                        xs=12,
                                                        md=6,
                                                    ),
                                                    dbc.Col(
                                                        html.Div(
                                                            className="payment-pill",
                                                            children=[
                                                                html.Div(
                                                                    className="payment-left",
                                                                    children=[
                                                                        html.Span("VISA", className="brand-chip"),
                                                                        html.Span("7812 2139 0823 XXXX", className="stat-label"),
                                                                    ],
                                                                ),
                                                                html.I(className="fa-regular fa-pen-to-square"),
                                                            ],
                                                        ),
                                                        xs=12,
                                                        md=6,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    xs=12,
                                )
                            ],
                        ),
                        dbc.Row(
                            className="g-3 row-gap",
                            children=[
                                dbc.Col(
                                    html.Div(
                                        className="card-surface chart-card",
                                        children=[
                                            html.Div("Billing Information", className="chart-title"),
                                            html.Div(
                                                className="billing-item",
                                                children=[
                                                    html.Div(
                                                        children=[
                                                            html.Div("Oliver Liam", style={"fontWeight": "600"}),
                                                            html.Div("Company Name: Viking Burrito", className="stat-label"),
                                                            html.Div("Email Address: oliver@burrito.com", className="stat-label"),
                                                            html.Div("VAT Number: FRB1235476", className="stat-label"),
                                                        ]
                                                    ),
                                                    html.Div(
                                                        className="billing-actions",
                                                        children=[
                                                            html.Span("DELETE", className="action-delete"),
                                                            html.Span("EDIT", className="action-edit"),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            html.Div(
                                                className="billing-item",
                                                children=[
                                                    html.Div(
                                                        children=[
                                                            html.Div("Oliver Liam", style={"fontWeight": "600"}),
                                                            html.Div("Company Name: Viking Burrito", className="stat-label"),
                                                            html.Div("Email Address: oliver@burrito.com", className="stat-label"),
                                                            html.Div("VAT Number: FRB1235476", className="stat-label"),
                                                        ]
                                                    ),
                                                    html.Div(
                                                        className="billing-actions",
                                                        children=[
                                                            html.Span("DELETE", className="action-delete"),
                                                            html.Span("EDIT", className="action-edit"),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            html.Div(
                                                className="billing-item",
                                                children=[
                                                    html.Div(
                                                        children=[
                                                            html.Div("Oliver Liam", style={"fontWeight": "600"}),
                                                            html.Div("Company Name: Viking Burrito", className="stat-label"),
                                                            html.Div("Email Address: oliver@burrito.com", className="stat-label"),
                                                            html.Div("VAT Number: FRB1235476", className="stat-label"),
                                                        ]
                                                    ),
                                                    html.Div(
                                                        className="billing-actions",
                                                        children=[
                                                            html.Span("DELETE", className="action-delete"),
                                                            html.Span("EDIT", className="action-edit"),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    xs=12,
                                )
                            ],
                        ),
                    ],
                    xs=12,
                    md=8,
                ),
                dbc.Col(
                    children=[
                        dbc.Row(
                            className="g-3",
                            children=[
                                dbc.Col(
                                    html.Div(
                                        className="card-surface chart-card",
                                        children=[
                                            html.Div(
                                                className="card-header-row",
                                                children=[
                                                    html.Div("Invoices", className="chart-title"),
                                                    html.Button("VIEW ALL", className="btn-outline-pill"),
                                                ],
                                            ),
                                            html.Div(
                                                className="invoice-list",
                                                children=[
                                                    html.Div(
                                                        className="invoice-item",
                                                        children=[
                                                            html.Div(
                                                                children=[
                                                                    html.Div("March, 01, 2020", style={"fontWeight": "600"}),
                                                                    html.Div("#MS-415646", className="invoice-meta"),
                                                                ]
                                                            ),
                                                            html.Div(
                                                                className="invoice-actions",
                                                                children=[
                                                                    html.Span("$180", className="stat-label"),
                                                                    html.Span("PDF", className="pdf-tag"),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    html.Div(
                                                        className="invoice-item",
                                                        children=[
                                                            html.Div(
                                                                children=[
                                                                    html.Div("February, 10, 2021", style={"fontWeight": "600"}),
                                                                    html.Div("#RV-126749", className="invoice-meta"),
                                                                ]
                                                            ),
                                                            html.Div(
                                                                className="invoice-actions",
                                                                children=[
                                                                    html.Span("$250", className="stat-label"),
                                                                    html.Span("PDF", className="pdf-tag"),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    html.Div(
                                                        className="invoice-item",
                                                        children=[
                                                            html.Div(
                                                                children=[
                                                                    html.Div("April, 05, 2020", style={"fontWeight": "600"}),
                                                                    html.Div("#FB-212562", className="invoice-meta"),
                                                                ]
                                                            ),
                                                            html.Div(
                                                                className="invoice-actions",
                                                                children=[
                                                                    html.Span("$560", className="stat-label"),
                                                                    html.Span("PDF", className="pdf-tag"),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    html.Div(
                                                        className="invoice-item",
                                                        children=[
                                                            html.Div(
                                                                children=[
                                                                    html.Div("June, 25, 2019", style={"fontWeight": "600"}),
                                                                    html.Div("#QW-103578", className="invoice-meta"),
                                                                ]
                                                            ),
                                                            html.Div(
                                                                className="invoice-actions",
                                                                children=[
                                                                    html.Span("$120", className="stat-label"),
                                                                    html.Span("PDF", className="pdf-tag"),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    html.Div(
                                                        className="invoice-item",
                                                        children=[
                                                            html.Div(
                                                                children=[
                                                                    html.Div("March, 01, 2019", style={"fontWeight": "600"}),
                                                                    html.Div("#AR-803481", className="invoice-meta"),
                                                                ]
                                                            ),
                                                            html.Div(
                                                                className="invoice-actions",
                                                                children=[
                                                                    html.Span("$300", className="stat-label"),
                                                                    html.Span("PDF", className="pdf-tag"),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    xs=12,
                                ),
                                dbc.Col(
                                    html.Div(
                                        className="card-surface chart-card",
                                        children=[
                                            html.Div(
                                                className="card-header-row",
                                                children=[
                                                    html.Div("Your Transactions", className="chart-title"),
                                                    html.Div("23 - 30 March 2020", className="stat-label"),
                                                ],
                                            ),
                                            html.Div(
                                                className="transaction-list",
                                                children=[
                                                    html.Div("NEWEST", className="stat-label"),
                                                    html.Div(
                                                        className="transaction-item",
                                                        children=[
                                                            html.Div(
                                                                className="transaction-left",
                                                                children=[
                                                                    html.Span("-", className="txn-icon negative"),
                                                                    html.Div(
                                                                        children=[
                                                                            html.Div("Netflix", style={"fontWeight": "600"}),
                                                                            html.Div("27 March 2020, 12:30 PM", className="stat-label"),
                                                                        ]
                                                                    ),
                                                                ],
                                                            ),
                                                            html.Div("-$2500", className="amount-negative"),
                                                        ],
                                                    ),
                                                    html.Div(
                                                        className="transaction-item",
                                                        children=[
                                                            html.Div(
                                                                className="transaction-left",
                                                                children=[
                                                                    html.Span("+", className="txn-icon positive"),
                                                                    html.Div(
                                                                        children=[
                                                                            html.Div("Apple", style={"fontWeight": "600"}),
                                                                            html.Div("27 March 2020, 12:30 PM", className="stat-label"),
                                                                        ]
                                                                    ),
                                                                ],
                                                            ),
                                                            html.Div("+$2500", className="amount-positive"),
                                                        ],
                                                    ),
                                                    html.Div("YESTERDAY", className="stat-label"),
                                                    html.Div(
                                                        className="transaction-item",
                                                        children=[
                                                            html.Div(
                                                                className="transaction-left",
                                                                children=[
                                                                    html.Span("+", className="txn-icon positive"),
                                                                    html.Div(
                                                                        children=[
                                                                            html.Div("Stripe", style={"fontWeight": "600"}),
                                                                            html.Div("26 March 2020, 13:45 PM", className="stat-label"),
                                                                        ]
                                                                    ),
                                                                ],
                                                            ),
                                                            html.Div("+$800", className="amount-positive"),
                                                        ],
                                                    ),
                                                    html.Div(
                                                        className="transaction-item",
                                                        children=[
                                                            html.Div(
                                                                className="transaction-left",
                                                                children=[
                                                                    html.Span("+", className="txn-icon positive"),
                                                                    html.Div(
                                                                        children=[
                                                                            html.Div("HubSpot", style={"fontWeight": "600"}),
                                                                            html.Div("26 March 2020, 12:30 PM", className="stat-label"),
                                                                        ]
                                                                    ),
                                                                ],
                                                            ),
                                                            html.Div("+$1700", className="amount-positive"),
                                                        ],
                                                    ),
                                                    html.Div(
                                                        className="transaction-item",
                                                        children=[
                                                            html.Div(
                                                                className="transaction-left",
                                                                children=[
                                                                    html.Span("!", className="txn-icon neutral"),
                                                                    html.Div(
                                                                        children=[
                                                                            html.Div("Webflow", style={"fontWeight": "600"}),
                                                                            html.Div("26 March 2020, 05:00 AM", className="stat-label"),
                                                                        ]
                                                                    ),
                                                                ],
                                                            ),
                                                            html.Div("Pending", className="stat-label"),
                                                        ],
                                                    ),
                                                    html.Div(
                                                        className="transaction-item",
                                                        children=[
                                                            html.Div(
                                                                className="transaction-left",
                                                                children=[
                                                                    html.Span("-", className="txn-icon negative"),
                                                                    html.Div(
                                                                        children=[
                                                                            html.Div("Microsoft", style={"fontWeight": "600"}),
                                                                            html.Div("25 March 2020, 16:30 PM", className="stat-label"),
                                                                        ]
                                                                    ),
                                                                ],
                                                            ),
                                                            html.Div("-$987", className="amount-negative"),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    xs=12,
                                ),
                            ],
                        ),
                    ],
                    xs=12,
                    md=4,
                ),
            ],
        ),
    ],
)
