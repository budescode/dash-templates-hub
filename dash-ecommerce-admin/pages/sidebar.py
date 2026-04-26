
import dash_bootstrap_components as dbc
from dash import html

# Define the style that sets the position and width of the sidebar

SIDEBAR_STYLE = {

    "top": "60px", # Start below the horizontal navbar (which is 60px high)
    "left": 0,
    "bottom": 0,

    "padding": "1rem 0.5rem",
    "background-color": "#ffffff",
    "box-shadow": "2px 0 5px rgba(0,0,0,0.1)",
    "z-index": 1, # Ensure it sits above other content
    "height":"100%"
}

def create_sidebar():
    return html.Div(
        [
   
            
            # The actual Navigation Links
            dbc.Nav(
                [
                    dbc.NavLink(
                        html.Div([
                            html.I(className="bi bi-speedometer2 me-2"),
                            html.Span("Dashboard")
                            ],className="ms-2"),
                        href="/",
                        className="nav-link mb-2",
                        active="exact",
                    ),



                    dbc.NavLink(
                        html.Div([
                            html.I(className="bi bi-people me-2"),
                            html.Span("Users")
                            ],className="ms-2"),
                        href="/users",
                        className="nav-link mb-2",
                        active="exact",
                    ),

                    dbc.NavLink(
                        html.Div([
                            html.I(className="bi bi-box me-2"),
                            html.Span("Products")
                            ],className="ms-2"),
                        href="/products",
                        className="nav-link mb-2",
                        active="exact",
                    ),
 
                    dbc.NavLink(
                        html.Div([
                            html.I(className="bi bi-gift me-2"),
                            html.Span("Orders")
                            ],className="ms-2"),
                        href="/orders",
                        className="nav-link mb-2",
                        active="exact",
                    ),

                    dbc.NavLink(
                        html.Div([
                            html.I(className="bi bi-ui-checks me-2"),
                            html.Span("Sellers")
                            ],className="ms-2"),
                        href="/sellers",
                        className="nav-link mb-2",
                        active="exact",
                    ),

                    dbc.NavLink(
                        html.Div([
                            html.I(className="bi bi-file-earmark-x me-2"),
                            html.Span("Reviews")
                            ],className="ms-2"),
                        href="/reviews",
                        className="nav-link mb-2",
                        active="exact",
                    ),

                    dbc.NavLink(
                        html.Div([
                            html.I(className="bi bi-file-earmark-diff me-2"),
                            html.Span("Payments")
                            ],className="ms-2"),
                        href="/payments",
                        className="nav-link mb-2",
                        active="exact",
                    ),


                    html.H6("ADMIN", className="text-uppercase ps-3 pt-4 pb-2", style={"color": "#666666"}),
                    dbc.NavLink(
                        html.Div([
                            html.I(className="bi bi-gear me-2"),
                            html.Span("Settings")
                            ],className="ms-2"),
                        href="/settings",
                        className="nav-link mb-2",
                        active="exact",
                    ),

                    dbc.NavLink(
                        html.Div([
                            html.I(className="bi bi-shield-check me-2"),
                            html.Span("Security")
                            ],className="ms-2"),
                        href="/security",
                        className="nav-link mb-2",
                        active="exact",
                    ),

                    dbc.NavLink(
                        html.Div([
                            html.I(className="bi bi-question-circle me-2"),
                            html.Span("Help & Support")
                            ],className="ms-2"),
                        href="/help",
                        active="exact",
                        className="nav-link mb-2",
                        
                    ),
                ],
                vertical=True, # Make the links stack vertically
                pills=True,     # Use pill style for selection highlights
                className="py-2"
            ),
        ],
        style=SIDEBAR_STYLE,
        className="w-30",
        id="sidebar", # ID for the toggler callback
    )