from dash import html, dcc
import plotly.graph_objects as go


def create_google_maps_page():
    fig = go.Figure(go.Scattergeo(
        lat=[26.8206],
        lon=[30.8025],
        mode="markers",
        marker=dict(size=12, color="#4b7cf3", symbol="circle"),
        name="Egypt"
    ))
    fig.update_geos(
        projection_type="natural earth",
        showland=True, landcolor="#f0f0f0",
        showocean=True, oceancolor="#cce5ff",
        showlakes=True, lakecolor="#cce5ff",
        showrivers=True, rivercolor="#cce5ff",
        showcountries=True, countrycolor="#cccccc",
        showcoastlines=True, coastlinecolor="#aaaaaa",
        center=dict(lat=26.8206, lon=30.8025),
        projection_scale=3,
    )
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        height=500,
        paper_bgcolor="rgba(0,0,0,0)",
        geo_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
    )

    return html.Div(
        className="container-fluid",
        children=[
            html.H4("Google Maps", className="c-grey-900 mT-10 mB-30"),
            html.Div(className="row", children=[
                html.Div(className="col-md-12", children=html.Div(
                    className="bgc-white bd bdrs-3 p-20 mB-20",
                    children=[
                        html.H6("Google Maps", className="c-grey-900 mB-20"),
                        dcc.Graph(figure=fig, config={"displayModeBar": False})
                    ]
                ))
            ])
        ]
    )


def create_vector_maps_page():
    markers = [
        ("India",     21.00,   78.00,  350),
        ("Australia", -33.00, 151.00,  250),
        ("USA",        36.77, -119.41, 250),
        ("UK",         55.37,   -3.41, 250),
        ("UAE",        25.20,   55.27,  250),
    ]

    fig = go.Figure(go.Scattergeo(
        lat=[m[1] for m in markers],
        lon=[m[2] for m in markers],
        text=[f"{m[0]}: {m[3]}" for m in markers],
        mode="markers",
        marker=dict(
            size=12,
            color="#7774e7",
            line=dict(color="#0f9aee", width=2),
            opacity=0.85,
        ),
        hovertemplate="%{text}<extra></extra>",
    ))
    fig.update_geos(
        projection_type="natural earth",
        showland=True,     landcolor="#e6eaf0",
        showocean=True,    oceancolor="#d0e8f5",
        showlakes=True,    lakecolor="#d0e8f5",
        showcountries=True, countrycolor="#d3d9e3",
        showcoastlines=True, coastlinecolor="#aab4c4",
        showframe=False,
    )
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        height=500,
        paper_bgcolor="rgba(0,0,0,0)",
        geo_bgcolor="#f9fafb",
        showlegend=False,
    )

    return html.Div(
        className="container-fluid",
        children=[
            html.H4("Vector Maps", className="c-grey-900 mT-10 mB-30"),
            html.Div(className="row", children=[
                html.Div(className="col-md-12", children=html.Div(
                    className="bgc-white bd bdrs-3 p-20 mB-20",
                    children=[
                        html.H6("Interactive Vector Maps", className="c-grey-900 mB-20"),
                        dcc.Graph(figure=fig, config={"displayModeBar": False})
                    ]
                ))
            ])
        ]
    )
