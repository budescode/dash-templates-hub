from dash import html, dcc, register_page, Input, Output, callback, ctx
import dash_bootstrap_components as dbc

register_page(
    __name__,
    path='/help',
    name='Help & Support'
)

# =============================================================================
# 1. HELPER: ARTICLE CARD COMPONENT
# =============================================================================
def build_article_card(title, description, read_time, rating=5):
    """Creates a standard Help Article card with stars and a button."""
    stars = [html.I(className="bi bi-star-fill text-warning fs-6 me-1") for _ in range(rating)]
    
    return dbc.Card([
        dbc.CardBody([
            html.H6(title, className="fw-bold mb-2"),
            html.P(description, className="text-muted small mb-3"),
            
            # Rating and Time Row
            html.Div([
                html.Div(stars, className="d-flex align-items-center me-3"),
                html.Small(f"{read_time} min read", className="text-muted")
            ], className="d-flex align-items-center mb-3"),
            
            dbc.Button("Read Article", color="outline-primary", size="sm")
        ])
    ], className="h-100 shadow-sm border-light")

# =============================================================================
# 2. DEFINE CONTENT FOR EACH TAB
# =============================================================================

def render_getting_started():
    return html.Div([
        html.H5("Getting Started", className="fw-bold"),
        
        # --- Row 1: Two Article Cards ---
        dbc.Row([
            dbc.Col([
                build_article_card(
                    "Quick Start Guide", 
                    "Learn the basics of navigating and using the admin dashboard effectively.", 
                    5
                )
            ], width=6),
            
            dbc.Col([
                build_article_card(
                    "Dashboard Overview", 
                    "Understand the main dashboard features, widgets, and data visualization tools.", 
                    3
                )
            ], width=6),
        ], className="g-4 mb-4"), # g-4 adds gap between columns

        # --- Row 2: Article + Video ---
        dbc.Row([
            dbc.Col([
                build_article_card(
                    "User Management", 
                    "How to add, edit, and manage user accounts and permissions.", 
                    8
                )
            ], width=6),
            
            # Video Placeholder Card
            dbc.Col([
                html.Div([
                    html.Div([
                        html.I(className="bi bi-play-circle-fill text-primary display-4"),
                    ], className="bg-light rounded p-4 text-center mb-2 d-flex justify-content-center align-items-center", style={"height": "120px"}),
                    
                    html.H6("Platform Introduction", className="fw-bold mb-1"),
                    html.Small("5-minute video walkthrough of the platform", className="text-muted")
                ])
            ], width=6),
        ], className="g-4"),

    ], className="p-4")


def render_faq():
    return html.Div([
        html.H5("Frequently Asked Questions", className="fw-bold mb-4"),
        dbc.Accordion([
            dbc.AccordionItem(
                "Yes, you can export data to CSV, Excel, or PDF formats from the Reports page.",
                title="Can I export my data?"
            ),
            dbc.AccordionItem(
                "Admins can invite new users via the User Management settings. An email invitation will be sent.",
                title="How do I add a new team member?"
            ),
            dbc.AccordionItem(
                "We support all major credit cards, PayPal, and bank transfers for enterprise accounts.",
                title="What payment methods do you support?"
            ),
        ], start_collapsed=True)
    ], className="p-4")


def render_documentation():
    return html.Div([
        html.H5("Documentation", className="fw-bold mb-4"),
        dbc.ListGroup([
            dbc.ListGroupItem([
                html.Div([
                    html.H6("API Reference", className="fw-bold mb-0"),
                    html.Small("Complete documentation for our REST API endpoints.", className="text-muted")
                ], className="py-2"),
                html.I(className="bi bi-box-arrow-up-right text-muted")
            ], className="d-flex justify-content-between align-items-center action-hover"),
            
            dbc.ListGroupItem([
                html.Div([
                    html.H6("Integration Guide", className="fw-bold mb-0"),
                    html.Small("Connect our platform with third-party tools like Slack and Jira.", className="text-muted")
                ], className="py-2"),
                html.I(className="bi bi-box-arrow-up-right text-muted")
            ], className="d-flex justify-content-between align-items-center action-hover"),
        ], flush=True)
    ], className="p-4")


def render_contact():
    return html.Div([
        html.H5("Contact Support", className="fw-bold mb-4"),
        dbc.Form([
            dbc.Row([
                dbc.Col([dbc.Label("Subject"), dbc.Input(placeholder="Brief summary of issue")], width=12, className="mb-3"),
            ]),
            dbc.Row([
                dbc.Col([dbc.Label("Message"), dbc.Textarea(placeholder="Describe your issue in detail...", style={"height": "150px"})], width=12, className="mb-3"),
            ]),
            dbc.Button("Send Message", color="primary")
        ])
    ], className="p-4")


# =============================================================================
# 3. MAIN LAYOUT
# =============================================================================

layout = dbc.Container([
        
    # --- Page Header Section ---
    dbc.Row([
        dbc.Col([
            html.H3("Help & Support", className="fw-bold text-dark"),
            html.P("Get help, find documentation, and contact support", className="text-muted")
        ]),
        dbc.Col([
            dbc.Button(
                [html.I(className="bi bi-download me-2"), "User Guide"], 
                color="light", 
                className="me-2 bg-white border text-muted fw-bold"
            ),
            dbc.Button(
                [html.I(className="bi bi-headset me-2"), "Contact Support"], 
                color="primary", 
                className="fw-bold px-4"
            )
        ], width="auto", className="d-flex align-items-center")
    ], className="mb-4 align-items-center"),

    # --- Main Content Card ---
    dbc.Card([
        dbc.CardBody([
            dbc.Row([
                
                # --- LEFT COLUMN: Vertical Navigation Tabs ---
                dbc.Col([
                    dbc.Nav([
                        dbc.NavLink([html.I(className="bi bi-play-circle me-3"), "Getting Started"], id="help-tab-start", n_clicks=0, active=True, href="#", className="fw-bold mb-1 text-start"),
                        dbc.NavLink([html.I(className="bi bi-question-circle me-3"), "FAQ"], id="help-tab-faq", n_clicks=0, href="#", className="mb-1 text-dark text-start"),
                        dbc.NavLink([html.I(className="bi bi-book me-3"), "Documentation"], id="help-tab-docs", n_clicks=0, href="#", className="mb-1 text-dark text-start"),
                        dbc.NavLink([html.I(className="bi bi-envelope me-3"), "Contact Support"], id="help-tab-contact", n_clicks=0, href="#", className="mb-1 text-dark text-start"),
                        dbc.NavLink([html.I(className="bi bi-lightbulb me-3"), "Feature Requests"], id="help-tab-requests", n_clicks=0, href="#", className="text-dark text-start"),
                    ], vertical=True, pills=True, className="settings-nav p-2")
                ], width=3, className="border-end pe-0 bg-light rounded-start"), 

                # --- RIGHT COLUMN: Dynamic Content Area ---
                dbc.Col([
                    html.Div(id="help-content-area", children=render_getting_started())
                ], width=9)
            ], className="g-0") 
        ], className="p-0") 
    ], className="shadow-sm border-0 overflow-hidden") 

], fluid=True, className="py-4")


# =============================================================================
# 4. CALLBACK LOGIC
# =============================================================================

@callback(
    Output("help-content-area", "children"),
    Output("help-tab-start", "active"),
    Output("help-tab-faq", "active"),
    Output("help-tab-docs", "active"),
    Output("help-tab-contact", "active"),
    Output("help-tab-requests", "active"),
    [
        Input("help-tab-start", "n_clicks"),
        Input("help-tab-faq", "n_clicks"),
        Input("help-tab-docs", "n_clicks"),
        Input("help-tab-contact", "n_clicks"),
        Input("help-tab-requests", "n_clicks"),
    ]
)
def switch_help_tab(c1, c2, c3, c4, c5):
    button_id = ctx.triggered_id if ctx.triggered_id else "help-tab-start"

    # Default View
    content = render_getting_started()
    
    # Switch Logic
    if button_id == "help-tab-faq":
        content = render_faq()
    elif button_id == "help-tab-docs":
        content = render_documentation()
    elif button_id == "help-tab-contact":
        content = render_contact()
    elif button_id == "help-tab-requests":
        content = html.Div([html.H5("Feature Requests"), html.P("Coming soon...")], className="p-4")

    return content, \
           (button_id == "help-tab-start"), \
           (button_id == "help-tab-faq"), \
           (button_id == "help-tab-docs"), \
           (button_id == "help-tab-contact"), \
           (button_id == "help-tab-requests")