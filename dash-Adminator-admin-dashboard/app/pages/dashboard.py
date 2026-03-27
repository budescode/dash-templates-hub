from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go


def _sparkline_bars(data, color):
    """Div-based bar sparkline — works in any flex layout."""
    max_val = max(data) or 1
    bars = [
        html.Div(style={
            "width": "8px",
            "height": f"{max(3, int((val / max_val) * 40))}px",
            "backgroundColor": color,
            "borderRadius": "2px",
            "flexShrink": "0"
        })
        for val in data
    ]
    return html.Div(
        bars,
        style={
            "display": "flex",
            "alignItems": "flex-end",
            "gap": "3px",
            "height": "40px",
            "width": "100%"
        }
    )


def _donut(value, color):
    fig = go.Figure(
        data=[
            go.Pie(
                values=[value, 100 - value],
                hole=0.7,
                marker=dict(colors=[color, "#f3f5f7"]),
                textinfo="none",
                hoverinfo="skip",
                sort=False
            )
        ]
    )
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        height=140,
        font=dict(color="#313435"),
        showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )
    return fig


def _world_map():
    fig = go.Figure(
        data=[
            go.Scattergeo(
                lon=[-100, -3, 78, 103, 145],
                lat=[40, 48, 22, 20, -25],
                text=["USA", "Europe", "India", "Asia", "Australia"],
                mode="markers",
                marker=dict(size=14, color="#4b7cf3", opacity=0.9)
            )
        ]
    )
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        geo=dict(
            projection_type="equirectangular",
            showland=True,
            landcolor="#b8cce4",
            showocean=True,
            oceancolor="#eef2f7",
            showlakes=False,
            showcountries=True,
            countrycolor="#ffffff",
            countrywidth=0.5,
            showframe=False,
            bgcolor="rgba(0,0,0,0)"
        ),
        height=360,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    return fig


def _monthly_line(months):
    sales = [140000, 165000, 180000, 195000, 210000, 220000, 215000, 225000, 240000, 230000, 200000, 185000]
    profit = [50000, 55000, 60000, 62000, 68000, 70000, 72000, 75000, 80000, 82000, 78000, 72000]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=months, y=sales, name="Sales ($K)", mode="lines+markers",
        line=dict(color="#4caf50", width=2),
        marker=dict(size=6, color="#4caf50"),
        hovertemplate="%{y:$,.0f}<extra></extra>"
    ))
    fig.add_trace(go.Scatter(
        x=months, y=profit, name="Profit ($K)", mode="lines+markers",
        line=dict(color="#2196f3", width=2),
        marker=dict(size=6, color="#2196f3"),
        hovertemplate="%{y:$,.0f}<extra></extra>"
    ))
    fig.update_layout(
        margin=dict(l=40, r=20, t=30, b=20),
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
        hovermode="x unified",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=True, zeroline=False, tickformat="$,.0s", gridcolor="#f0f0f0")
    )
    return fig


def create_dashboard_page():
    """Replicate the Adminator dashboard layout"""

    stat_cards = [
        {
            "title": "Total Visits",
            "spark": [10, 12, 8, 15, 10, 12, 9],
            "badge": "+10%",
            "badge_class": "bgc-green-50 c-green-500",
            "color": "#4caf50"
        },
        {
            "title": "Total Page Views",
            "spark": [8, 10, 12, 10, 14, 11, 12],
            "badge": "-7%",
            "badge_class": "bgc-red-50 c-red-500",
            "color": "#6f42c1"
        },
        {
            "title": "Unique Visitor",
            "spark": [11, 9, 12, 10, 13, 11, 10],
            "badge": "~12%",
            "badge_class": "bgc-purple-50 c-purple-500",
            "color": "#2196f3"
        },
        {
            "title": "Bounce Rate",
            "spark": [12, 10, 8, 10, 7, 9, 8],
            "badge": "33%",
            "badge_class": "bgc-blue-50 c-blue-500",
            "color": "#ff6f00"
        }
    ]

    progress_stats = [
        {"label": "100k", "subtitle": "Visitors From USA", "value": 50, "bar_class": "bgc-deep-purple-500"},
        {"label": "1M", "subtitle": "Visitors From Europe", "value": 80, "bar_class": "bgc-green-500"},
        {"label": "450k", "subtitle": "Visitors From Australia", "value": 40, "bar_class": "bgc-light-blue-500"},
        {"label": "1B", "subtitle": "Visitors From India", "value": 90, "bar_class": "bgc-blue-grey-500"}
    ]

    donut_stats = [
        {"label": "New Users", "value": 75, "color": "#f44336"},
        {"label": "New Purchases", "value": 50, "color": "#2196f3"},
        {"label": "Bounce Rate", "value": 90, "color": "#ff9800"}
    ]

    monthly_highlights = [
        {"value": "54%", "label": "Sales Growth"},
        {"value": "$185K", "label": "Dec Sales"},
        {"value": "60%", "label": "Profit Growth"},
        {"value": "$72K", "label": "Dec Profit"}
    ]

    todo_items = [
        {"label": "Call John for Dinner"},
        {"label": "Book Boss Flight", "badge": "2 Days", "badge_class": "bg-success"},
        {"label": "Hit the Gym", "badge": "3 Minutes", "badge_class": "bg-danger"},
        {"label": "Give Purchase Report", "badge": "not important", "badge_class": "bg-warning"},
        {"label": "Watch Game of Thrones Episode", "badge": "Tomorrow", "badge_class": "bg-info"},
        {"label": "Give Purchase report", "badge": "Done", "badge_class": "bg-success"}
    ]

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    stat_cards_dom = [
        html.Div(
            className="col-md-3 col-sm-6",
            children=html.Div(
                className="layers bd bgc-white p-20",
                children=[
                    html.Div(html.H6(card["title"], className="lh-1"), className="layer w-100 mB-10"),
                    html.Div(
                        className="layer w-100",
                        children=html.Div(
                            className="peers ai-sb fxw-nw",
                            children=[
                                html.Div(
                                    className="peer peer-greed",
                                    style={"minWidth": 0},
                                    children=_sparkline_bars(card["spark"], card["color"])
                                ),
                                html.Div(
                                    className="peer",
                                    children=html.Span(
                                        card["badge"],
                                        className=f"d-ib lh-0 va-m fw-600 bdrs-10em pX-15 pY-15 {card['badge_class']}"
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )
        for card in stat_cards
    ]

    progress_dom = [
        html.Div(
            className="layer w-100" + (" mT-15" if idx else ""),
            children=[
                html.H5(stat["label"], className="mB-5"),
                html.Small(stat["subtitle"], className="fw-600 c-grey-700"),
                html.Span(f"{stat['value']}%", className="pull-right c-grey-600 fsz-sm"),
                html.Div(
                    className="progress mT-10",
                    children=html.Div(
                        className=f"progress-bar {stat['bar_class']}",
                        **{"role": "progressbar", "aria-valuenow": str(stat['value']), "aria-valuemin": "0", "aria-valuemax": "100"},
                        style={"width": f"{stat['value']}%"}
                    )
                )
            ]
        )
        for idx, stat in enumerate(progress_stats)
    ]

    donut_dom = [
        html.Div(
            className="peer",
            children=[
                dcc.Graph(figure=_donut(entry['value'], entry['color']), config={"displayModeBar": False}),
                html.H6(entry["label"], className="fsz-sm")
            ]
        )
        for entry in donut_stats
    ]

    todo_dom = [
        html.Li(
            className="list-group-item bdw-0",
            children=html.Div(
                className="peers ai-c",
                children=[
                    html.Span(
                        dbc.Input(type="checkbox", className="checkbox-circle"),
                        className="peer mR-10"
                    ),
                    html.Div(
                        className="peer peer-greed peers js-sb ai-c",
                        children=[
                            html.Span(item["label"], className="peer peer-greed"),
                            html.Span(
                                html.Span(
                                    item["badge"],
                                    className=f"badge rounded-pill fl-r {item.get('badge_class', 'bg-secondary')} lh-0 p-10"
                                ) if item.get("badge") else None,
                                className="peer"
                            )
                        ]
                    )
                ]
            )
        )
        for item in todo_items
    ]

    return html.Div(
        className="row gap-20 masonry pos-r",
        children=[
            html.Div(className="masonry-sizer col-md-6"),
            html.Div(className="masonry-item w-100", children=html.Div(className="row gap-20", children=stat_cards_dom)),
            html.Div(
                className="masonry-item col-12",
                children=html.Div(
                    className="bd bgc-white",
                    children=html.Div(
                        className="peers fxw-nw@lg+ ai-s",
                        children=[
                            html.Div(
                                className="peer peer-greed w-70p@lg+ w-100@lg- p-20",
                                children=[
                                    html.Div(className="layers", children=[
                                        html.Div(html.H6("Site Visits", className="lh-1"), className="layer w-100 mB-10"),
                                        html.Div(dcc.Graph(figure=_world_map(), config={"displayModeBar": False}), className="layer w-100")
                                    ])
                                ]
                            ),
                            html.Div(
                                className="peer bdL p-20 w-30p@lg+ w-100p@lg-",
                                children=html.Div(
                                    className="layers",
                                    children=progress_dom + [
                                        html.Div(
                                            className="peers pT-20 mT-20 bdT fxw-nw@lg+ jc-sb ta-c gap-10",
                                            children=donut_dom
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ),
            html.Div(
                className="masonry-item col-md-6",
                children=html.Div(
                    className="bd bgc-white",
                    children=[
                        html.Div(html.H6("Monthly Stats", className="lh-1"), className="layer w-100 pX-20 pT-20"),
                        html.Div(dcc.Graph(figure=_monthly_line(months), config={"displayModeBar": False}), className="layer w-100 p-20"),
                        html.Div(
                            className="layer bdT p-20 w-100",
                            children=html.Div(
                                className="peers ai-c jc-c gapX-20",
                                children=[
                                    html.Div([
                                        html.Span([highlight["value"], " ", html.I(className="fa fa-level-up c-green-500")], className="fsz-def fw-600 mR-10 c-grey-800"),
                                        html.Small(highlight["label"], className="c-grey-500 fw-600")
                                    ], className="peer")
                                    for highlight in monthly_highlights
                                ]
                            )
                        )
                    ]
                )
            ),
            html.Div(
                className="masonry-item col-md-6",
                children=html.Div(
                    className="bd bgc-white p-20",
                    children=[
                        html.Div(html.H6("Todo List", className="lh-1"), className="layer w-100 mB-10"),
                        html.Div(html.Ul(todo_dom, className="list-task list-group"), className="layer w-100")
                    ]
                )
            ),
            html.Div(
                className="masonry-item col-md-6",
                children=html.Div(
                    className="bd bgc-white",
                    children=[
                        html.Div(
                            className="layers",
                            children=[
                                html.Div(html.H6("Sales Report", className="lh-1"), className="layer w-100 p-20"),
                                html.Div(
                                    className="layer w-100",
                                    children=[
                                        html.Div(
                                            className="sales-report-header p-20",
                                            children=html.Div(
                                                className="peers ai-c jc-sb gap-40",
                                                children=[
                                                    html.Div([
                                                        html.H5("November 2029"),
                                                        html.P("Sales Report", className="mB-0")
                                                    ], className="peer peer-greed"),
                                                    html.Div(html.H3("$6,000", className="text-end"), className="peer")
                                                ]
                                            )
                                        ),
                                        html.Div(
                                            className="table-responsive p-20",
                                            children=html.Table(
                                                className="table",
                                                children=[
                                                    html.Thead(html.Tr([
                                                        html.Th("Name", className="bdwT-0"),
                                                        html.Th("Status", className="bdwT-0"),
                                                        html.Th("Date", className="bdwT-0"),
                                                        html.Th("Price", className="bdwT-0"),
                                                    ])),
                                                    html.Tbody([
                                                        html.Tr([
                                                            html.Td("Item #1 Name", className="fw-600"),
                                                            html.Td(html.Span("Unavailable", className="badge bgc-red-50 c-red-700 p-10 lh-0 tt-c rounded-pill")),
                                                            html.Td("Nov 18"),
                                                            html.Td(html.Span("$12", className="text-success"))
                                                        ]),
                                                        html.Tr([
                                                            html.Td("Item #2 Name", className="fw-600"),
                                                            html.Td(html.Span("New", className="badge bgc-deep-purple-50 c-deep-purple-700 p-10 lh-0 tt-c rounded-pill")),
                                                            html.Td("Nov 19"),
                                                            html.Td(html.Span("$34", className="text-info"))
                                                        ]),
                                                        html.Tr([
                                                            html.Td("Item #3 Name", className="fw-600"),
                                                            html.Td(html.Span("New", className="badge bgc-pink-50 c-pink-700 p-10 lh-0 tt-c rounded-pill")),
                                                            html.Td("Nov 20"),
                                                            html.Td(html.Span("-$45", className="text-danger"))
                                                        ]),
                                                        html.Tr([
                                                            html.Td("Item #4 Name", className="fw-600"),
                                                            html.Td(html.Span("Unavailable", className="badge bgc-green-50 c-green-700 p-10 lh-0 tt-c rounded-pill")),
                                                            html.Td("Nov 21"),
                                                            html.Td(html.Span("$65", className="text-success"))
                                                        ]),
                                                        html.Tr([
                                                            html.Td("Item #5 Name", className="fw-600"),
                                                            html.Td(html.Span("Used", className="badge bgc-red-50 c-red-700 p-10 lh-0 tt-c rounded-pill")),
                                                            html.Td("Nov 22"),
                                                            html.Td(html.Span("$78", className="text-success"))
                                                        ]),
                                                        html.Tr([
                                                            html.Td("Item #6 Name", className="fw-600"),
                                                            html.Td(html.Span("Used", className="badge bgc-orange-50 c-orange-700 p-10 lh-0 tt-c rounded-pill")),
                                                            html.Td("Nov 23"),
                                                            html.Td(html.Span("-$88", className="text-danger"))
                                                        ]),
                                                        html.Tr([
                                                            html.Td("Item #7 Name", className="fw-600"),
                                                            html.Td(html.Span("Old", className="badge bgc-yellow-50 c-yellow-700 p-10 lh-0 tt-c rounded-pill")),
                                                            html.Td("Nov 22"),
                                                            html.Td(html.Span("$56", className="text-success"))
                                                        ]),
                                                    ])
                                                ]
                                            )
                                        )
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            html.A("Check all the sales", href="#"),
                            className="ta-c bdT w-100 p-20"
                        )
                    ]
                )
            ),
            html.Div(
                className="masonry-item col-md-6",
                children=html.Div(
                    className="bd bgc-white p-20",
                    children=html.Div(
                        className="layers",
                        children=[
                            html.Div(html.H6("Weather", className="lh-1"), className="layer w-100 mB-20"),
                            html.Div(
                                className="layer w-100",
                                children=html.Div(
                                    className="peers ai-c jc-sb fxw-nw",
                                    children=[
                                        html.Div(
                                            className="peer peer-greed",
                                            children=html.Div(
                                                className="layers",
                                                children=[
                                                    html.Div(
                                                        className="layer w-100",
                                                        children=html.Div(
                                                            className="peers fxw-nw ai-c",
                                                            children=[
                                                                html.Div(html.H3(["32", html.Sup("°F")]), className="peer mR-20"),
                                                                html.Div(html.Canvas(className="sleet", width=44, height=44), className="peer")
                                                            ]
                                                        )
                                                    ),
                                                    html.Div(html.Span("Partly Clouds", className="fw-600 c-grey-600"), className="layer w-100")
                                                ]
                                            )
                                        ),
                                        html.Div(
                                            className="peer",
                                            children=html.Div(
                                                className="layers ai-fe",
                                                children=[
                                                    html.Div(html.H5("Monday", className="mB-5"), className="layer"),
                                                    html.Div(html.Span("Nov, 01 2032", className="fw-600 c-grey-600"), className="layer")
                                                ]
                                            )
                                        )
                                    ]
                                )
                            ),
                            html.Div(
                                className="layer w-100 mY-30",
                                children=html.Div(
                                    className="layers bdB",
                                    children=[
                                        html.Div(
                                            className="layer w-100 bdT pY-5",
                                            children=html.Div(
                                                className="peers ai-c jc-sb fxw-nw",
                                                children=[
                                                    html.Div(html.Span("Wind"), className="peer"),
                                                    html.Div(html.Span("10km/h", className="fw-600 c-grey-800"), className="peer ta-r")
                                                ]
                                            )
                                        ),
                                        html.Div(
                                            className="layer w-100 bdT pY-5",
                                            children=html.Div(
                                                className="peers ai-c jc-sb fxw-nw",
                                                children=[
                                                    html.Div(html.Span("Sunrise"), className="peer"),
                                                    html.Div(html.Span("05:00 AM", className="fw-600 c-grey-800"), className="peer ta-r")
                                                ]
                                            )
                                        ),
                                        html.Div(
                                            className="layer w-100 bdT pY-5",
                                            children=html.Div(
                                                className="peers ai-c jc-sb fxw-nw",
                                                children=[
                                                    html.Div(html.Span("Pressure"), className="peer"),
                                                    html.Div(html.Span("1B", className="fw-600 c-grey-800"), className="peer ta-r")
                                                ]
                                            )
                                        )
                                    ]
                                )
                            ),
                            html.Div(
                                className="layer w-100",
                                children=html.Div(
                                    className="peers peers-greed ai-fs ta-c",
                                    children=[
                                        html.Div([html.H6("MON", className="mB-10"), html.Canvas(className="sleet", width=30, height=30), html.Span(["32", html.Sup("°F")], className="d-b fw-600")], className="peer"),
                                        html.Div([html.H6("TUE", className="mB-10"), html.Canvas(className="clear-day", width=30, height=30), html.Span(["30", html.Sup("°F")], className="d-b fw-600")], className="peer"),
                                        html.Div([html.H6("WED", className="mB-10"), html.Canvas(className="partly-cloudy-day", width=30, height=30), html.Span(["28", html.Sup("°F")], className="d-b fw-600")], className="peer"),
                                        html.Div([html.H6("THR", className="mB-10"), html.Canvas(className="cloudy", width=30, height=30), html.Span(["32", html.Sup("°F")], className="d-b fw-600")], className="peer"),
                                        html.Div([html.H6("FRI", className="mB-10"), html.Canvas(className="snow", width=30, height=30), html.Span(["24", html.Sup("°F")], className="d-b fw-600")], className="peer"),
                                        html.Div([html.H6("SAT", className="mB-10"), html.Canvas(className="wind", width=30, height=30), html.Span(["28", html.Sup("°F")], className="d-b fw-600")], className="peer"),
                                        html.Div([html.H6("SUN", className="mB-10"), html.Canvas(className="sleet", width=30, height=30), html.Span(["32", html.Sup("°F")], className="d-b fw-600")], className="peer"),
                                    ]
                                )
                            )
                        ]
                    )
                )
            ),
            html.Div(
                className="masonry-item col-md-6",
                children=html.Div(
                    className="bd bgc-white",
                    children=html.Div(
                        className="layers",
                        children=[
                            html.Div(html.H6("Quick Chat", className="lh-1"), className="layer w-100 p-20"),
                            html.Div(
                                className="layer w-100",
                                children=[
                                    html.Div(
                                        className="bgc-grey-200 p-20 gapY-15",
                                        children=[
                                            html.Div(
                                                className="peers fxw-nw",
                                                children=[
                                                    html.Div(
                                                        html.Img(className="w-2r bdrs-50p", src="https://randomuser.me/api/portraits/men/11.jpg", alt=""),
                                                        className="peer mR-20"
                                                    ),
                                                    html.Div(
                                                        className="peer peer-greed",
                                                        children=html.Div(
                                                            className="layers ai-fs gapY-5",
                                                            children=[
                                                                html.Div(html.Div(className="peers fxw-nw ai-c pY-3 pX-10 bgc-white bdrs-2 lh-3/2", children=[html.Div(html.Small("10:00 AM"), className="peer mR-10"), html.Div(html.Span("Lorem Ipsum is simply dummy text of"), className="peer-greed")]), className="layer"),
                                                                html.Div(html.Div(className="peers fxw-nw ai-c pY-3 pX-10 bgc-white bdrs-2 lh-3/2", children=[html.Div(html.Small("10:00 AM"), className="peer mR-10"), html.Div(html.Span("the printing and typesetting industry."), className="peer-greed")]), className="layer"),
                                                                html.Div(html.Div(className="peers fxw-nw ai-c pY-3 pX-10 bgc-white bdrs-2 lh-3/2", children=[html.Div(html.Small("10:00 AM"), className="peer mR-10"), html.Div(html.Span("Lorem Ipsum has been the industry's"), className="peer-greed")]), className="layer"),
                                                            ]
                                                        )
                                                    )
                                                ]
                                            ),
                                            html.Div(
                                                className="peers fxw-nw ai-fe",
                                                children=[
                                                    html.Div(
                                                        html.Img(className="w-2r bdrs-50p", src="https://randomuser.me/api/portraits/men/12.jpg", alt=""),
                                                        className="peer ord-1 mL-20"
                                                    ),
                                                    html.Div(
                                                        className="peer peer-greed ord-0",
                                                        children=html.Div(
                                                            className="layers ai-fe gapY-10",
                                                            children=[
                                                                html.Div(html.Div(className="peers fxw-nw ai-c pY-3 pX-10 bgc-white bdrs-2 lh-3/2", children=[html.Div(html.Small("10:00 AM"), className="peer mL-10 ord-1"), html.Div(html.Span("Heloo"), className="peer-greed ord-0")]), className="layer"),
                                                                html.Div(html.Div(className="peers fxw-nw ai-c pY-3 pX-10 bgc-white bdrs-2 lh-3/2", children=[html.Div(html.Small("10:00 AM"), className="peer mL-10 ord-1"), html.Div(html.Span("??"), className="peer-greed ord-0")]), className="layer"),
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        ]
                                    ),
                                    html.Div(
                                        className="p-20 bdT bgc-white",
                                        children=html.Div(
                                            className="pos-r",
                                            children=[
                                                dbc.Input(type="text", className="form-control bdrs-10em m-0", placeholder="Say something..."),
                                                html.Button(
                                                    html.I(className="fa fa-paper-plane-o"),
                                                    type="button",
                                                    className="btn btn-primary bdrs-50p w-2r p-0 h-2r pos-a r-1 t-1"
                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        ]
                    )
                )
            )
        ]
    )
