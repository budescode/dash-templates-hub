from config.constants import PRIMARY_COLOR_HEX
import dash_bootstrap_components as dbc
from dash import html


# --- Navbar Layout ---
navbar_layout = dbc.Container(
    html.Div(
        [
            # ---------- LEFT ----------
            html.Div(
                [
                    html.A(
                        [
                            html.Span(
                                "Budescode",
                                className="fw-bold fs-5",
                                style={"color": PRIMARY_COLOR_HEX}
                            ),
                        ],
                        href="/",
                        className="d-flex align-items-center text-decoration-none"
                    ),

                    dbc.Button(
                        html.I(className="bi bi-list fs-6"),
                        id="sidebar-toggler",
                        color="light",
                        className="ms-3 bg-transparent border border-secondary"
                    ),
                ],
                className="d-flex align-items-center flex-grow-1"
            ),

            # ---------- CENTER ----------
            html.Div(
                dbc.InputGroup(
                    [
                        dbc.Input(placeholder="Search... (Ctrl+K)"),
                        dbc.InputGroupText(html.I(className="bi bi-search")),
                    ],
                    className="w-66"
                ),
                className="d-flex justify-content-center flex-grow-1"
            ),

            # ---------- RIGHT ----------
            html.Div(
                dbc.Nav(
                    [

                        dbc.NavItem(
                            dbc.Button(
                                [
                                    html.Img(
                                        src="/assets/images/avatar-placeholder.svg",
                                        height="25px",
                                        className="rounded-circle border me-2"
                                    ),
                                    html.Span("John Doe"),
                                ],
                                color="light",
                                className="bg-transparent border-0 d-flex align-items-center"
                            ),
                            className="ms-3"
                        )
                    ],
                    className="d-flex align-items-center"
                ),
                className="d-flex justify-content-end flex-grow-1"
            ),
        ],
        className="d-flex align-items-center w-100 px-3"
    ),
    fluid=True,
    className="px-0"
)

# --- Final Navbar Component ---
horizontal_navbar = dbc.Navbar(
    navbar_layout,
    color="light", # Background color
    className="border-bottom sticky-top shadow-sm ",
    
)