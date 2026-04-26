from dash import html
import dash_bootstrap_components as dbc

from app.pages.email_chat import _email_side_nav


def compose_email_page():
    return html.Div(
        className="full-container",
        children=html.Div(
            className="email-app",
            children=[
                _email_side_nav(),
                html.Div(
                    className="email-wrapper row remain-height pos-r scrollable bgc-white",
                    children=html.Div(
                        className="email-content open no-inbox-view",
                        children=html.Div(
                            className="email-compose",
                            children=html.Form(
                                className="email-compose-body",
                                children=[
                                    html.H4("Send Message", className="c-grey-900 mB-20"),
                                    html.Div(
                                        className="send-header",
                                        children=[
                                            html.Div(dbc.Input(type="text", placeholder="To"), className="mb-3"),
                                            html.Div(dbc.Input(type="text", placeholder="CC"), className="mb-3"),
                                            html.Div(dbc.Input(type="text", placeholder="Email Subject"), className="mb-3"),
                                            html.Div(
                                                html.Textarea(placeholder="Say Hi...", className="form-control", rows=10),
                                                className="mb-3"
                                            ),
                                        ]
                                    ),
                                    html.Div(
                                        html.Button("Send", className="btn btn-danger btn-color"),
                                        className="text-end mrg-top-30"
                                    )
                                ]
                            )
                        )
                    )
                )
            ]
        )
    )
