from dash import Dash, html, page_container, callback, Input, Output, State
import dash_bootstrap_components as dbc
# Import global components/constants

from pages.sidebar import create_sidebar # Import the function
from pages.navbar_h import horizontal_navbar

 

BOOTSTRAP_ICONS = "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css"

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, BOOTSTRAP_ICONS],
    use_pages=True,
    suppress_callback_exceptions=True,
    pages_folder="pages",# Use the robust path
    title="Ecommerce Dashboard"

)


# Define the Global Layout ---
app.layout = html.Div(
    [
        horizontal_navbar, # Global Navbar (always visible)
        dbc.Container(
            [
             
                dbc.Row(
                    [
                        dbc.Col(md=2, id="sidebar-col", children=[create_sidebar()]), # Sidebar column (W-30)
                        dbc.Col(md=10, id="content-col", children=[page_container]), # Sidebar column (W-30)
                    ]
                )
              
            ],
            style={"background-color": "#f8f9fa"}, # Use a placeholder color
            className="",
            fluid=True
        )
    ], className="px-0"
)

@callback(
    Output("sidebar-col", "style"),
    Output("sidebar-col", "md"),
    Output("content-col", "md"),
    Input("sidebar-toggler", "n_clicks"),
    State("sidebar-col", "md")
)
def toggle_sidebar(n, current_sidebar_width):
    print(n, current_sidebar_width)
    # If button hasn't been clicked, do nothing (return current state)
    if not n:
        # Default: Visible (display: block, width=2, content=10)
        return {"display": "block", "overflow": "hidden"}, 2, 10

    # If sidebar is currently visible (width=2) -> HIDE IT
    if current_sidebar_width == 2:
        return {"display": "none"}, 0, 12
    
    # If sidebar is currently hidden (width=0) -> SHOW IT
    else:
        return {"display": "block"}, 2, 10
    
# Run the app
if __name__ == "__main__":
    app.run(debug=True, port=8000)