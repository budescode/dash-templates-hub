import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, callback
import os

# Import all page components
from app.components.layout import create_header, create_sidebar
from app.pages.dashboard import create_dashboard_page
from app.pages.tables import create_basic_table_page, create_datatable_page
from app.pages.charts import create_charts_page
from app.pages.forms import create_forms_page
from app.pages.ui_elements import create_ui_elements_page
from app.pages.email_chat import create_email_page, create_compose_page, create_chat_page
from app.pages.other_pages import (
    create_calendar_page, create_blank_page, 
    create_error_404_page, create_error_500_page,
    create_signin_page, create_signup_page
)
from app.pages.maps import create_google_maps_page, create_vector_maps_page

# Initialize the Dash app
app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/themify-icons/0.1.2/themify-icons.min.css"
    ],
    suppress_callback_exceptions=True,
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1"
        }
    ]
)

# Set app title
app.title = "Adminator - Admin Dashboard"

# Get the absolute path to assets folder
app.config.assets_folder = os.path.join(os.path.dirname(__file__), 'assets')
app.config.assets_url_base = '/assets/'

# Define the app layout
app.layout = html.Div(
    className="app",
    children=[
        dcc.Location(id="url", refresh=False),
        create_sidebar(),
        html.Div(
            className="page-container",
            children=[
                create_header(),
                html.Main(
                    id="main-content",
                    className="main-content bgc-grey-100",
                    children=html.Div(
                        id="mainContent",
                        children=html.Div(id="page-content")
                    )
                )
            ]
        )
    ]
)

# Callback for page routing
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    """Route to the appropriate page based on URL"""
    
    # Map routes to page functions
    if pathname == "/" or pathname == "/index.html":
        return create_dashboard_page()
    elif pathname == "/email":
        return create_email_page()
    elif pathname == "/compose":
        return create_compose_page()
    elif pathname == "/chat":
        return create_chat_page()
    elif pathname == "/calendar":
        return create_calendar_page()
    elif pathname == "/charts":
        return create_charts_page()
    elif pathname == "/forms":
        return create_forms_page()
    elif pathname == "/ui":
        return create_ui_elements_page()
    elif pathname == "/tables/basic":
        return create_basic_table_page()
    elif pathname == "/tables/data":
        return create_datatable_page()
    elif pathname == "/maps/google":
        return create_google_maps_page()
    elif pathname == "/maps/vector":
        return create_vector_maps_page()
    elif pathname == "/pages/blank":
        return create_blank_page()
    elif pathname == "/pages/404":
        return create_error_404_page()
    elif pathname == "/pages/500":
        return create_error_500_page()
    elif pathname == "/pages/signin":
        return create_signin_page()
    elif pathname == "/pages/signup":
        return create_signup_page()
    else:
        # Default to dashboard
        return create_dashboard_page()

# Callback for sidebar menu generation
@app.callback(
    Output("sidebar-menu", "children"),
    Input("url", "pathname")
)
def update_sidebar_menu(pathname):
    """Generate sidebar menu that mirrors Adminator navigation"""

    menu_items = [
        {"href": "/", "label": "Dashboard", "icon": "ti-home", "color_class": "c-blue-500", "exact": True, "extra_class": "mT-30"},
        {"href": "/email", "label": "Email", "icon": "ti-email", "color_class": "c-brown-500"},
        {"href": "/compose", "label": "Compose", "icon": "ti-share", "color_class": "c-blue-500"},
        {"href": "/calendar", "label": "Calendar", "icon": "ti-calendar", "color_class": "c-deep-orange-500"},
        {"href": "/chat", "label": "Chat", "icon": "ti-comment-alt", "color_class": "c-deep-purple-500"},
        {"href": "/charts", "label": "Charts", "icon": "ti-bar-chart", "color_class": "c-indigo-500"},
        {"href": "/forms", "label": "Forms", "icon": "ti-pencil", "color_class": "c-light-blue-500"},
        {"href": "/ui", "label": "UI Elements", "icon": "ti-palette", "color_class": "c-pink-500"},
    ]

    dropdown_items = [
        {
            "label": "Tables",
            "icon": "ti-layout-list-thumb",
            "color_class": "c-orange-500",
            "items": [
                {"href": "/tables/basic", "label": "Basic Table"},
                {"href": "/tables/data", "label": "Data Table"},
            ]
        },
        {
            "label": "Maps",
            "icon": "ti-map",
            "color_class": "c-purple-500",
            "items": [
                {"href": "/maps/google", "label": "Google Map"},
                {"href": "/maps/vector", "label": "Vector Map"},
            ]
        },
        {
            "label": "Pages",
            "icon": "ti-files",
            "color_class": "c-red-500",
            "items": [
                {"href": "/pages/blank", "label": "Blank"},
                {"href": "/pages/404", "label": "404"},
                {"href": "/pages/500", "label": "500"},
                {"href": "/pages/signin", "label": "Sign In"},
                {"href": "/pages/signup", "label": "Sign Up"},
            ]
        },
        {
            "label": "Multiple Levels",
            "icon": "ti-view-list-alt",
            "color_class": "c-teal-500",
            "items": [
                {"href": "#", "label": "Menu Item"},
                {"href": "#", "label": "Menu Item"}
            ]
        }
    ]

    nav_items = []

    for item in menu_items:
        is_active = (item.get("exact", False) and pathname == item["href"]) or (not item.get("exact", False) and pathname.startswith(item["href"]))
        link_classes = "sidebar-link" + (" active" if is_active else "")
        li_classes = "nav-item" + (f" {item['extra_class']}" if item.get('extra_class') else "")

        nav_items.append(
            html.Li(
                className=li_classes,
                children=html.A(
                    href=item["href"],
                    className=link_classes,
                    children=[
                        html.Span(html.I(className=f"{item['color_class']} {item['icon']}"), className='icon-holder'),
                        html.Span(item['label'], className='title')
                    ]
                )
            )
        )

    for dropdown in dropdown_items:
        sub_active = any(pathname.startswith(sub['href']) for sub in dropdown['items'] if sub['href'] != '#')
        li_classes = 'nav-item dropdown' + (' open' if sub_active else '')
        dropdown_menu = html.Ul(
            className='dropdown-menu',
            style={"display": "block" if sub_active else "none"},
            children=[
                html.Li(
                    html.A(sub_item['label'], href=sub_item['href'], className='sidebar-link' + (' active' if pathname.startswith(sub_item['href']) else ''))
                )
                for sub_item in dropdown['items']
            ]
        )

        nav_items.append(
            html.Li(
                className=li_classes,
                children=[
                    html.A(
                        className='dropdown-toggle',
                        href='#',
                        children=[
                            html.Span(html.I(className=f"{dropdown['color_class']} {dropdown['icon']}"), className='icon-holder'),
                            html.Span(dropdown['label'], className='title'),
                            html.Span(html.I(className='ti-angle-right'), className='arrow')
                        ]
                    ),
                    dropdown_menu
                ]
            )
        )

    return nav_items

if __name__ == '__main__':
    app.run(debug=True, port=8051)
