from dash import html, dcc, register_page, Input, Output, callback, ctx
import dash_bootstrap_components as dbc

register_page(
    __name__,
    path='/security',
    name='Security'
)

# =============================================================================
# 1. DEFINE CONTENT FOR EACH TAB
# =============================================================================

def render_account_security():
    return html.Div([
        html.H5("Account Security", className="fw-bold"),
        html.P("Manage your account security settings and password requirements", className="text-muted mb-5"),

        # --- Section 1: Password ---
        html.Div([
            html.Label("Password", className="fw-bold mb-1"),
            html.Div("Last changed 45 days ago", className="text-muted small mb-2"),
            dbc.Button("Change Password", color="outline-primary", size="sm", className="mb-4")
        ]),

        # --- Section 2: Recovery Email ---
        html.Div([
            html.Label("Account Recovery Email", className="fw-bold mb-1"),
            html.Div("john.doe@example.com", className="text-muted mb-2"), # Replaced input with text per screenshot design
            dbc.Button("Update", color="secondary", size="sm", className="mb-4")
        ]),

        html.Hr(className="my-4 text-muted"),

        # --- Section 3: Lockout Protection ---
        dbc.Row([
            dbc.Col([
                html.Label("Account Lockout Protection", className="fw-bold mb-0"),
                html.Small("Automatically lock account after failed login attempts", className="text-muted"),
            ], width=8),
            dbc.Col([
                dbc.Switch(value=True, className="fs-4 float-end")
            ], width=4)
        ], className="mb-2 align-items-center"),

    ], className="p-4")


def render_2fa():
    return html.Div([
        html.H5("Two-Factor Authentication", className="fw-bold"),
        html.P("Add an extra layer of security to your account", className="text-muted mb-5"),

        # Status Card
        dbc.Card([
            dbc.CardBody([
                html.Div([
                    html.I(className="bi bi-shield-check fs-1 text-success me-3"),
                    html.Div([
                        html.H6("2FA is currently ENABLED", className="fw-bold text-success mb-1"),
                        html.Small("Your account is protected with an authenticator app.", className="text-muted")
                    ])
                ], className="d-flex align-items-center")
            ])
        ], className="bg-light border-success mb-4"),

        dbc.Button("Configure 2FA Methods", color="primary"),
    ], className="p-4")


def render_active_sessions():
    return html.Div([
        html.H5("Active Sessions", className="fw-bold"),
        html.P("Manage devices currently logged into your account", className="text-muted mb-4"),

        # Session Item 1
        dbc.ListGroup([
            dbc.ListGroupItem([
                html.Div([
                    html.I(className="bi bi-laptop fs-4 me-3 text-primary"),
                    html.Div([
                        html.H6("MacBook Pro - Chrome", className="fw-bold mb-0"),
                        html.Small("Kingston, UK • Active Now", className="text-success")
                    ], className="flex-grow-1"),
                    dbc.Button("Revoke", color="outline-danger", size="sm")
                ], className="d-flex align-items-center py-2")
            ]),
            
            # Session Item 2
            dbc.ListGroupItem([
                html.Div([
                    html.I(className="bi bi-phone fs-4 me-3 text-secondary"),
                    html.Div([
                        html.H6("iPhone 13 - Safari", className="fw-bold mb-0"),
                        html.Small("London, UK • 2 hours ago", className="text-muted")
                    ], className="flex-grow-1"),
                    dbc.Button("Revoke", color="outline-danger", size="sm")
                ], className="d-flex align-items-center py-2")
            ]),
        ], flush=True)

    ], className="p-4")


def render_security_log():
    return html.Div([
        html.H5("Security Activity", className="fw-bold"),
        html.P("Recent security events and login attempts", className="text-muted mb-4"),
        
        # Simple Table
        dbc.Table([
            html.Thead(html.Tr([html.Th("Event"), html.Th("Date"), html.Th("IP Address"), html.Th("Status")])),
            html.Tbody([
                html.Tr([html.Td("Login Attempt"), html.Td("2025-01-01 10:00"), html.Td("192.168.1.1"), html.Td(html.Span("Success", className="badge bg-success"))]),
                html.Tr([html.Td("Password Change"), html.Td("2024-12-28 14:30"), html.Td("192.168.1.1"), html.Td(html.Span("Success", className="badge bg-success"))]),
                html.Tr([html.Td("Failed Login"), html.Td("2024-12-25 09:15"), html.Td("45.22.19.11"), html.Td(html.Span("Blocked", className="badge bg-danger"))]),
            ])
        ], bordered=False, hover=True, responsive=True)
    ], className="p-4")


# =============================================================================
# 2. MAIN LAYOUT
# =============================================================================

layout = dbc.Container([
        
    # --- Page Header Section ---
    dbc.Row([
        dbc.Col([
            html.H3("Security & Authentication", className="fw-bold text-dark"),
            html.P("Manage your account security and access controls", className="text-muted")
        ]),
        dbc.Col([
            dbc.Button(
                [html.I(className="bi bi-shield-exclamation me-2"), "Security Log"], 
                color="outline-danger", 
                className="me-2 fw-bold"
            ),
            dbc.Button(
                [html.I(className="bi bi-lock-fill me-2"), "Emergency Lockdown"], 
                color="danger", 
                className="fw-bold px-3"
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
                        dbc.NavLink([html.I(className="bi bi-shield-check me-3"), "Account Security"], id="sec-tab-account", n_clicks=0, active=True, href="#", className="fw-bold mb-1 text-start"),
                        dbc.NavLink([html.I(className="bi bi-key me-3"), "Two-Factor Auth"], id="sec-tab-2fa", n_clicks=0, href="#", className="mb-1 text-dark text-start"),
                        dbc.NavLink([html.I(className="bi bi-laptop me-3"), "Active Sessions"], id="sec-tab-sessions", n_clicks=0, href="#", className="mb-1 text-dark text-start"),
                        dbc.NavLink([html.I(className="bi bi-eye-slash me-3"), "Privacy Settings"], id="sec-tab-privacy", n_clicks=0, href="#", className="mb-1 text-dark text-start"),
                        dbc.NavLink([html.I(className="bi bi-activity me-3"), "Security Activity"], id="sec-tab-activity", n_clicks=0, href="#", className="text-dark text-start"),
                    ], vertical=True, pills=True, className="settings-nav p-2")
                ], width=3, className="border-end pe-0 bg-light rounded-start"), 

                # --- RIGHT COLUMN: Dynamic Content Area ---
                dbc.Col([
                    html.Div(id="security-content-area", children=render_account_security())
                ], width=9)
            ], className="g-0") 
        ], className="p-0") 
    ], className="shadow-sm border-0 overflow-hidden") 

], fluid=True, className="py-4")


# =============================================================================
# 3. CALLBACK LOGIC
# =============================================================================

@callback(
    Output("security-content-area", "children"),
    Output("sec-tab-account", "active"),
    Output("sec-tab-2fa", "active"),
    Output("sec-tab-sessions", "active"),
    Output("sec-tab-privacy", "active"),
    Output("sec-tab-activity", "active"),
    [
        Input("sec-tab-account", "n_clicks"),
        Input("sec-tab-2fa", "n_clicks"),
        Input("sec-tab-sessions", "n_clicks"),
        Input("sec-tab-privacy", "n_clicks"),
        Input("sec-tab-activity", "n_clicks"),
    ]
)
def switch_security_tab(c1, c2, c3, c4, c5):
    button_id = ctx.triggered_id if ctx.triggered_id else "sec-tab-account"

    # Default View
    content = render_account_security()
    
    # Switch Logic
    if button_id == "sec-tab-2fa":
        content = render_2fa()
    elif button_id == "sec-tab-sessions":
        content = render_active_sessions()
    elif button_id == "sec-tab-activity":
        content = render_security_log()
    elif button_id == "sec-tab-privacy":
        # Re-using the privacy render from Settings, or you can create a new one
        content = html.Div([html.H5("Privacy Settings"), html.P("Manage data visibility...", className="text-muted")])

    return content, \
           (button_id == "sec-tab-account"), \
           (button_id == "sec-tab-2fa"), \
           (button_id == "sec-tab-sessions"), \
           (button_id == "sec-tab-privacy"), \
           (button_id == "sec-tab-activity")