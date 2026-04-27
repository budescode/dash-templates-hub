import dash
from dash import dcc, html, Input, Output, State
import os

# Import all page components
from app.components.layout import create_header, create_sidebar
from app.pages.dashboard import create_dashboard_page
from app.pages.tables import create_basic_table_page, create_datatable_page
from app.pages.charts import create_charts_page
from app.pages.forms import create_forms_page
from app.pages.ui_elements import create_ui_elements_page
from app.pages.email_chat import create_email_page
from app.pages.email_compose import compose_email_page
from app.pages.chat import create_chat_page
from app.pages.calendars import create_calendar_page
from app.pages.other_pages import (
    create_blank_page,
    create_error_404_page, create_error_500_page,
    create_signin_page, create_signup_page
)
from app.pages.maps import create_google_maps_page, create_vector_maps_page

# Get the absolute path to assets folder
assets_folder = os.path.join(os.path.dirname(__file__), 'assets')

# Initialize the Dash app
app = dash.Dash(
    __name__,
    assets_folder=assets_folder,
    external_stylesheets=[],
    suppress_callback_exceptions=True,
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1, shrink-to-fit=no"
        }
    ]
)

app.title = "Dash Administrator Dashboard"

# Define the app layout using the Adminator HTML structure
app.layout = html.Div(
    id='app-container',
    className='app',
    children=[
        dcc.Location(id='url', refresh=False),
        dcc.Store(id='_fc-init-store'),
        dcc.Store(id='_sidebar-store', data=False),
        dcc.Store(id='_theme-store', storage_type='local', data='light'),

        # Left Sidebar
        create_sidebar(),

        # Main page container
        html.Div(
            className='page-container',
            children=[
                # Topbar / Header
                create_header(),

                # App Screen Content
                html.Main(
                    className='main-content bgc-grey-100',
                    children=html.Div(id='page-content')
                ),

                # Footer
                html.Footer(
                    className='bdT ta-c p-30 lh-0 fsz-sm c-grey-600',
                    children=html.Span([
                        "Copyright © 2025 · Inspired by Adminator · Built with Dash by ",
                        html.A(
                            "budescode",
                            href="https://github.com/budescode",
                            target="_blank",
                            rel="noopener noreferrer",
                            title="budescode on GitHub"
                        ),
                        " · ",
                        html.A(
                            "LinkedIn",
                            href="https://www.linkedin.com/in/budescode",
                            target="_blank",
                            rel="noopener noreferrer",
                            title="budescode on LinkedIn"
                        ),
                        ". All rights reserved."
                    ])
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
    if pathname == "/" or pathname == "/index.html":
        return create_dashboard_page()
    elif pathname == "/email":
        return create_email_page()
    elif pathname == "/compose":
        return compose_email_page()
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
        return create_dashboard_page()


# Callback for sidebar menu generation
@app.callback(
    Output("sidebar-menu", "children"),
    Input("url", "pathname")
)
def update_sidebar_menu(pathname):
    """Generate sidebar menu items with active states"""

    def nav_item(href, label, icon_class, color, first=False):
        is_active = pathname == href
        extra_class = " mT-30" if first else ""
        active_class = " actived" if is_active else ""
        return html.Li(
            className=f"nav-item{extra_class}{active_class}",
            children=dcc.Link(
                className="sidebar-link",
                href=href,
                children=[
                    html.Span(
                        html.I(className=f"{color} {icon_class}"),
                        className="icon-holder"
                    ),
                    html.Span(label, className="title")
                ]
            )
        )

    def dropdown_item(label, icon_class, color, sub_items):
        is_open = any(pathname == sub["href"] for sub in sub_items)
        return html.Li(
            className="nav-item dropdown" + (" open has-active-child" if is_open else ""),
            children=[
                html.A(
                    className="dropdown-toggle",
                    href="#",
                    children=[
                        html.Span(
                            html.I(className=f"{color} {icon_class}"),
                            className="icon-holder"
                        ),
                        html.Span(label, className="title"),
                        html.Span(html.I(className="ti-angle-right"), className="arrow")
                    ]
                ),
                html.Ul(
                    className="dropdown-menu",
                    style={"display": "block" if is_open else "none"},
                    children=[
                        html.Li(
                            dcc.Link(sub["label"], className="sidebar-link", href=sub["href"]),
                            className="actived" if pathname == sub["href"] else ""
                        )
                        for sub in sub_items
                    ]
                )
            ]
        )

    menu = [
        nav_item("/", "Dashboard", "ti-home", "c-blue-500", first=True),
        nav_item("/email", "Email", "ti-email", "c-brown-500"),
        nav_item("/compose", "Compose", "ti-share", "c-blue-500"),
        nav_item("/calendar", "Calendar", "ti-calendar", "c-deep-orange-500"),
        nav_item("/chat", "Chat", "ti-comment-alt", "c-deep-purple-500"),
        nav_item("/charts", "Charts", "ti-bar-chart", "c-indigo-500"),
        nav_item("/forms", "Forms", "ti-pencil", "c-light-blue-500"),
        html.Li(
            className="nav-item dropdown" + (" actived" if pathname == "/ui" else ""),
            children=dcc.Link(
                className="sidebar-link",
                href="/ui",
                children=[
                    html.Span(
                        html.I(className="c-pink-500 ti-palette"),
                        className="icon-holder"
                    ),
                    html.Span("UI Elements", className="title")
                ]
            )
        ),
        dropdown_item("Tables", "ti-layout-list-thumb", "c-orange-500", [
            {"href": "/tables/basic", "label": "Basic Table"},
            {"href": "/tables/data", "label": "Data Table"},
        ]),
        dropdown_item("Maps", "ti-map", "c-purple-500", [
            {"href": "/maps/google", "label": "Google Map"},
            {"href": "/maps/vector", "label": "Vector Map"},
        ]),
        dropdown_item("Pages", "ti-files", "c-red-500", [
            {"href": "/pages/blank", "label": "Blank"},
            {"href": "/pages/404", "label": "404"},
            {"href": "/pages/500", "label": "500"},
            {"href": "/pages/signin", "label": "Sign In"},
            {"href": "/pages/signup", "label": "Sign Up"},
        ]),
    ]

    return menu


# Clientside callback: initialize FullCalendar after each page navigation
app.clientside_callback(
    """
    function(pathname) {
        if (pathname !== '/calendar') return null;

        function tryInit() {
            var el = document.getElementById('fullcalendar');
            if (!el || typeof FullCalendar === 'undefined') {
                setTimeout(tryInit, 100);
                return;
            }
            if (el._fcInstance) {
                el._fcInstance.destroy();
                el._fcInstance = null;
            }
            var cal = new FullCalendar.Calendar(el, {
                initialView: 'dayGridMonth',
                headerToolbar: {
                    left: 'prev,next today',
                    center: 'title',
                    right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
                },
                buttonText: {
                    today: 'today', month: 'month', week: 'week', day: 'day', list: 'list'
                },
                editable: true,
                selectable: true,
                events: [
                    { title: 'All Day Event', start: '2026-03-01', allDay: true },
                    { title: 'Long Event', start: '2026-03-22', end: '2026-03-24' },
                    { title: 'Conference', start: '2026-03-24', end: '2026-03-26' },
                    { title: 'Click for Google', url: 'http://google.com/', start: '2026-03-28' }
                ]
            });
            cal.render();
            el._fcInstance = cal;
        }

        setTimeout(tryInit, 50);
        return null;
    }
    """,
    Output('_fc-init-store', 'data'),
    Input('url', 'pathname')
)


# Clientside callback: sidebar toggle (hamburger)
app.clientside_callback(
    """
    function(n_clicks, is_collapsed) {
        if (!n_clicks) return window.dash_clientside.no_update;
        var app = document.getElementById('app-container');
        if (app) {
            app.classList.toggle('is-collapsed');
            setTimeout(function() { window.dispatchEvent(new Event('resize')); }, 300);
        }
        return !is_collapsed;
    }
    """,
    Output('_sidebar-store', 'data'),
    Input('sidebar-toggle', 'n_clicks'),
    Input('_sidebar-store', 'data'),
    prevent_initial_call=True,
)


# Clientside callback: dark mode toggle
app.clientside_callback(
    """
    function(n_clicks, current_theme) {
        var theme = current_theme || 'light';
        if (n_clicks) {
            theme = theme === 'dark' ? 'light' : 'dark';
        }
        document.documentElement.setAttribute('data-theme', theme);
        var icon = document.getElementById('theme-icon');
        if (icon) {
            icon.className = theme === 'dark' ? 'fa fa-sun-o' : 'fa fa-moon-o';
        }
        return theme;
    }
    """,
    Output('_theme-store', 'data'),
    Input('theme-toggle', 'n_clicks'),
    State('_theme-store', 'data'),
    prevent_initial_call=False,
)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8051)
