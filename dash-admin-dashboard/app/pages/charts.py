from dash import html, dcc
import plotly.graph_objects as go
import random


def _card(title, chart_id, fig):
    return html.Div(
        className="masonry-item col-md-6",
        children=html.Div(
            className="bgc-white p-20 bd",
            children=[
                html.H6(title, className="c-grey-900"),
                html.Div(
                    className="mT-30",
                    children=dcc.Graph(figure=fig, config={"displayModeBar": False}, id=chart_id)
                )
            ]
        )
    )


_MONTHS7 = ["January", "February", "March", "April", "May", "June", "July"]
_LINE_Y  = [62, 59, 80, 81, 56, 55, 40]


def _line_chart():
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=_MONTHS7, y=_LINE_Y,
        mode="lines+markers", name="Dataset 1",
        line=dict(color="#4bc0c0", width=2),
        marker=dict(size=5, color="#4bc0c0")
    ))
    fig.update_layout(
        margin=dict(l=30, r=10, t=40, b=30), height=280,
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False, tickfont=dict(size=11)),
        yaxis=dict(showgrid=True, gridcolor="#eeeeee", range=[0, 90]),
        legend=dict(orientation="h", y=1.15, x=0)
    )
    return fig


def _area_chart():
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=_MONTHS7, y=_LINE_Y,
        fill="tozeroy", mode="lines", name="Dataset 1",
        line=dict(color="#36a2eb", width=2),
        fillcolor="rgba(54,162,235,0.35)"
    ))
    fig.update_layout(
        margin=dict(l=30, r=10, t=40, b=30), height=280,
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False, tickfont=dict(size=11)),
        yaxis=dict(showgrid=True, gridcolor="#eeeeee", range=[0, 90]),
        legend=dict(orientation="h", y=1.15, x=0)
    )
    return fig


def _scatter_chart():
    random.seed(42)
    d1x = [random.uniform(-14, 19) for _ in range(20)]
    d1y = [random.uniform(1, 22) for _ in range(20)]
    d2x = [random.uniform(-14, 19) for _ in range(20)]
    d2y = [random.uniform(1, 22) for _ in range(20)]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=d1x, y=d1y, mode="markers", name="Dataset 1",
                             marker=dict(size=8, color="#ff6384", opacity=0.85)))
    fig.add_trace(go.Scatter(x=d2x, y=d2y, mode="markers", name="Dataset 2",
                             marker=dict(size=8, color="#36a2eb", opacity=0.85)))
    fig.update_layout(
        margin=dict(l=30, r=10, t=40, b=30), height=280,
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=True, gridcolor="#eeeeee", zeroline=True, zerolinecolor="#cccccc"),
        yaxis=dict(showgrid=True, gridcolor="#eeeeee"),
        legend=dict(orientation="h", y=1.15, x=0)
    )
    return fig


def _bar_chart():
    labels = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
    values = [12, 19, 3, 5, 2, 3]
    colors = ["#ff6384", "#36a2eb", "#ffce56", "#4bc0c0", "#9966ff", "#ff9f40"]
    fig = go.Figure(data=[go.Bar(
        x=labels, y=values,
        marker_color=colors,
        name="# of Votes"
    )])
    fig.update_layout(
        margin=dict(l=30, r=10, t=40, b=30), height=280,
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="#eeeeee"),
        showlegend=True,
        legend=dict(orientation="h", y=1.15, x=0)
    )
    return fig


_CHART_COLORS = ["#ff6384", "#36a2eb", "#ffce56", "#4bc0c0", "#9966ff", "#ff9f40"]


def _doughnut_chart():
    fig = go.Figure(data=[go.Pie(
        labels=["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
        values=[30, 25, 20, 15, 10, 8],
        hole=0.55,
        marker=dict(colors=_CHART_COLORS),
        textinfo="none"
    )])
    fig.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=280,
                      paper_bgcolor="rgba(0,0,0,0)", showlegend=True,
                      legend=dict(orientation="h", y=-0.15))
    return fig


def _polar_chart():
    fig = go.Figure(data=[go.Barpolar(
        r=[8, 7, 6, 5, 9, 4],
        theta=["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
        marker_color=_CHART_COLORS,
        opacity=0.85
    )])
    fig.update_layout(margin=dict(l=10, r=10, t=10, b=10), height=280,
                      paper_bgcolor="rgba(0,0,0,0)",
                      polar=dict(bgcolor="rgba(0,0,0,0)"))
    return fig


def _radar_chart():
    categories = ["Eating", "Drinking", "Sleeping", "Designing", "Coding", "Cycling", "Running"]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[65, 59, 90, 81, 56, 55, 40], theta=categories,
        fill="toself", name="My First dataset",
        line=dict(color="#ff6384"), fillcolor="rgba(255,99,132,0.2)"
    ))
    fig.add_trace(go.Scatterpolar(
        r=[28, 48, 40, 19, 96, 27, 100], theta=categories,
        fill="toself", name="My Second dataset",
        line=dict(color="#36a2eb"), fillcolor="rgba(54,162,235,0.2)"
    ))
    fig.update_layout(margin=dict(l=30, r=30, t=40, b=30), height=280,
                      paper_bgcolor="rgba(0,0,0,0)",
                      polar=dict(bgcolor="rgba(0,0,0,0)"),
                      legend=dict(orientation="h", y=1.15, x=0))
    return fig


def _mixed_chart():
    months = ["January", "February", "March", "April", "May", "June", "July"]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=months, y=[65, 59, 80, 81, 56, 55, 40],
        name="Dataset 1", marker_color="rgba(255,99,132,0.8)"
    ))
    fig.add_trace(go.Scatter(
        x=months, y=[28, 48, 40, 19, 86, 27, 90],
        mode="lines+markers", name="Dataset 2",
        line=dict(color="#36a2eb", width=2), marker=dict(size=5, color="#36a2eb")
    ))
    fig.update_layout(margin=dict(l=30, r=10, t=40, b=30), height=280,
                      paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      xaxis=dict(showgrid=False),
                      yaxis=dict(showgrid=True, gridcolor="#eeeeee"),
                      legend=dict(orientation="h", y=1.15, x=0))
    return fig


def _bubble_chart():
    fig = go.Figure(data=[go.Scatter(
        x=[1, 2, 3, 4, 5, 6, 7, 8],
        y=[10, 15, 13, 17, 12, 20, 18, 22],
        mode="markers",
        marker=dict(
            size=[20, 35, 25, 45, 30, 50, 40, 55],
            color=_CHART_COLORS + ["#607d8b", "#e91e63"],
            opacity=0.8
        )
    )])
    fig.update_layout(margin=dict(l=30, r=10, t=10, b=30), height=280,
                      paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      xaxis=dict(showgrid=True, gridcolor="#eeeeee"),
                      yaxis=dict(showgrid=True, gridcolor="#eeeeee"))
    return fig


def _donut_mini(value, color, label):
    fig = go.Figure(data=[go.Pie(
        values=[value, 100 - value], hole=0.7,
        marker=dict(colors=[color, "#f3f5f7"]),
        textinfo="none", hoverinfo="skip", sort=False
    )])
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), height=80,
                      showlegend=False, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    return html.Div([
        dcc.Graph(figure=fig, config={"displayModeBar": False}),
        html.H6(label, className="fsz-sm")
    ], className="peer")


def _spark_row(label, data, color, last=False):
    max_val = max(data) or 1
    bars = [
        html.Div(style={
            "width": "6px", "height": f"{max(2, int((v/max_val)*24))}px",
            "backgroundColor": color, "borderRadius": "1px", "flexShrink": "0"
        }) for v in data
    ]
    spark = html.Div(bars, style={"display": "flex", "alignItems": "flex-end", "gap": "2px", "height": "24px"})
    return html.Div(
        className=f"peers ai-c jc-sb fxw-nw {'bdB ' if not last else ''}pY-15",
        children=[
            html.Div(html.Span(label), className="peer"),
            html.Div(spark, className="peer")
        ]
    )


def create_charts_page():
    return html.Div(
        className="row gap-20 masonry pos-r",
        children=[
            html.Div(className="masonry-sizer col-md-6 pos-a"),
            _card("Line Chart", "line-chart-main", _line_chart()),
            _card("Area Chart", "area-chart-main", _area_chart()),
            _card("Scatter Chart", "scatter-chart-main", _scatter_chart()),
            _card("Bar Chart", "bar-chart-main", _bar_chart()),

            # Sparklines (static bar divs)
            html.Div(
                className="masonry-item col-md-6",
                children=html.Div(
                    className="bgc-white p-20 bd",
                    children=[
                        html.H6("Sparklines", className="c-grey-900"),
                        html.Div(className="mT-30", children=[
                            _spark_row("Spark Line",   [3,6,4,7,2,8,5,9,4,6], "#4b7cf3"),
                            _spark_row("Spark Bar",    [5,3,8,2,7,4,9,1,6,3], "#4caf50"),
                            _spark_row("Spark Tri",    [4,7,3,8,5,2,9,4,7,3], "#f44336"),
                            _spark_row("Spark Disc",   [6,2,8,4,7,3,9,5,4,8], "#ff9800"),
                            _spark_row("Spark Bullet", [2,5,8,3,7,6,4,9,2,5], "#9c27b0"),
                            _spark_row("Spark Box",    [7,4,9,2,6,8,3,5,7,4], "#00bcd4", last=True),
                        ])
                    ]
                )
            ),

            _card("Doughnut Chart", "doughnut-chart-main", _doughnut_chart()),
            _card("Polar Area Chart", "polar-chart-main", _polar_chart()),
            _card("Radar Chart", "radar-chart-main", _radar_chart()),
            _card("Mixed Chart", "mixed-chart-main", _mixed_chart()),
            _card("Bubble Chart", "bubble-chart-main", _bubble_chart()),

            # Easy Pie Charts
            html.Div(
                className="masonry-item col-md-6",
                children=html.Div(
                    className="bgc-white p-20 bd",
                    children=[
                        html.H6("Donut Charts", className="c-grey-900"),
                        html.Div(
                            className="peers mT-20 fxw-nw jc-sb ta-c gap-10",
                            children=[
                                _donut_mini(75, "#f44336", "New Users"),
                                _donut_mini(50, "#2196f3", "New Purchases"),
                                _donut_mini(90, "#ff9800", "Bounce Rate"),
                            ]
                        )
                    ]
                )
            ),
        ]
    )
