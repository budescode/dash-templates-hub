from dash import html, dcc, register_page, Input, Output, callback, ctx
import dash_bootstrap_components as dbc

register_page(
    __name__,
    path='/settings',
    name='Settings'
)

# =============================================================================
# 1. DEFINE CONTENT FOR EACH TAB
# =============================================================================

def render_general():
    return html.Div([
        html.H5("General Settings", className="fw-bold"),
        html.P("Configure basic application preferences and behavior", className="text-muted mb-5"),

        # --- Field 1: Language ---
        dbc.Row([
            dbc.Col([
                html.Label("Application Language", className="fw-bold mb-0"),
                html.Small("Choose your preferred language for the interface", className="text-muted"),
            ], width=8),
            dbc.Col([
                dbc.Select(
                    options=[
                        {"label": "English", "value": "en"},
                        {"label": "Spanish", "value": "es"},
                        {"label": "Portuguese", "value": "pt"},
                    ],
                    value="en",
                )
            ], width=4)
        ], className="mb-4 align-items-center"),

        # --- Field 2: Timezone ---
        dbc.Row([
            dbc.Col([
                html.Label("Timezone", className="fw-bold mb-0"),
                html.Small("Set your local timezone for accurate timestamps", className="text-muted"),
            ], width=8),
            dbc.Col([
                dbc.Select(
                    options=[{"label": "Eastern Time (ET)", "value": "ET"}],
                    value="ET",
                )
            ], width=4)
        ], className="mb-4 align-items-center"),

        # --- Field 3: Date Format ---
        dbc.Row([
            dbc.Col([
                html.Label("Date Format", className="fw-bold mb-0"),
                html.Small("Choose how dates are displayed throughout the application", className="text-muted"),
            ], width=8),
            dbc.Col([
                dbc.Select(
                    options=[{"label": "MM/DD/YYYY (US)", "value": "US"}],
                    value="US",
                )
            ], width=4)
        ], className="mb-4 align-items-center"),

        html.Hr(className="my-4 text-muted"),

        # --- Field 4: Auto Save (Switch) ---
        dbc.Row([
            dbc.Col([
                html.Label("Auto-save", className="fw-bold mb-0"),
                html.Small("Automatically save changes as you work", className="text-muted"),
            ], width=8),
            dbc.Col([
                dbc.Switch(id="autosave-switch", value=True, className="fs-4 float-end")
            ], width=4)
        ], className="mb-2 align-items-center"),

    ], className="p-4")

def render_appearance():
    return html.Div([
        html.H5("Appearance", className="fw-bold"),
        html.P("Customize how the dashboard looks on your device", className="text-muted mb-5"),

        dbc.Row([
            dbc.Col([
                html.Label("Interface Theme", className="fw-bold mb-0"),
                html.Small("Select your preferred UI theme", className="text-muted"),
            ], width=8),
            dbc.Col([
                dbc.RadioItems(
                    options=[
                        {"label": "Light Mode", "value": "light"},
                        {"label": "Dark Mode", "value": "dark"},
                        {"label": "System", "value": "system"},
                    ],
                    value="light",
                    inline=True
                )
            ], width=4)
        ], className="mb-4 align-items-center"),

        html.Hr(className="my-4 text-muted"),

        dbc.Row([
            dbc.Col([
                html.Label("Compact Density", className="fw-bold mb-0"),
                html.Small("Reduce whitespace to show more data on screen", className="text-muted"),
            ], width=8),
            dbc.Col([
                dbc.Switch(value=False, className="fs-4 float-end")
            ], width=4)
        ], className="mb-2 align-items-center"),
    ], className="p-4")

def render_notifications():
    return html.Div([
        html.H5("Notifications", className="fw-bold"),
        html.P("Manage how we communicate with you", className="text-muted mb-5"),

        html.H6("Email Alerts", className="fw-bold text-uppercase text-muted mb-3 fs-7"),
        
        dbc.Row([
            dbc.Col(html.Label("Weekly Performance Digest", className="fw-bold"), width=8),
            dbc.Col(dbc.Switch(value=True, className="fs-5 float-end"), width=4)
        ], className="mb-3 align-items-center"),

        dbc.Row([
            dbc.Col(html.Label("New Order Alerts", className="fw-bold"), width=8),
            dbc.Col(dbc.Switch(value=True, className="fs-5 float-end"), width=4)
        ], className="mb-3 align-items-center"),

        html.Hr(className="my-4 text-muted"),

        html.H6("Push Notifications", className="fw-bold text-uppercase text-muted mb-3 fs-7"),
        
        dbc.Row([
            dbc.Col(html.Label("Browser Popups", className="fw-bold"), width=8),
            dbc.Col(dbc.Switch(value=False, className="fs-5 float-end"), width=4)
        ], className="mb-3 align-items-center"),
    ], className="p-4")

def render_privacy():
    return html.Div([
        html.H5("Privacy & Security", className="fw-bold"),
        html.P("Control who can see your profile and data", className="text-muted mb-5"),

        dbc.Row([
            dbc.Col([
                html.Label("Profile Visibility", className="fw-bold mb-0"),
                html.Small("Who can see your profile details?", className="text-muted"),
            ], width=8),
            dbc.Col([
                dbc.Select(
                    options=[
                        {"label": "Everyone", "value": "public"},
                        {"label": "Team Only", "value": "team"},
                        {"label": "Private", "value": "private"},
                    ],
                    value="team",
                )
            ], width=4)
        ], className="mb-4 align-items-center"),

        html.Hr(className="my-4 text-muted"),

        dbc.Row([
            dbc.Col([
                html.Label("Share Usage Data", className="fw-bold mb-0"),
                html.Small("Allow us to collect anonymous usage stats to improve the app", className="text-muted"),
            ], width=8),
            dbc.Col([
                dbc.Switch(value=False, className="fs-4 float-end")
            ], width=4)
        ], className="mb-2 align-items-center"),
    ], className="p-4")

def render_storage():
    return html.Div([
        html.H5("Storage & Data", className="fw-bold"),
        html.P("Manage your file usage and cache", className="text-muted mb-5"),

        html.Div([
            html.Div([
                html.Span("14.2 GB", className="fw-bold text-dark"),
                html.Span(" used of 20 GB", className="text-muted")
            ], className="d-flex justify-content-between mb-2"),
            dbc.Progress(value=71, color="primary", className="mb-2", style={"height": "8px"}),
            html.Small("71% used - You are running low on space", className="text-warning")
        ], className="bg-light p-3 rounded mb-4 border"),

        dbc.Row([
            dbc.Col([
                html.Label("Cache Management", className="fw-bold mb-0"),
                html.Small("Clear temporary files to free up space", className="text-muted"),
            ], width=8),
            dbc.Col([
                dbc.Button("Clear Cache", color="outline-danger", size="sm", className="float-end")
            ], width=4)
        ], className="mb-4 align-items-center"),
    ], className="p-4")


# =============================================================================
# 2. MAIN LAYOUT
# =============================================================================

layout = dbc.Container([
        
    # --- Page Header Section ---
    dbc.Row([
        dbc.Col([
            html.H3("Settings", className="fw-bold text-dark"),
            html.P("Manage your application preferences and configuration", className="text-muted")
        ]),
        dbc.Col([
            dbc.Button(
                [html.I(className="bi bi-arrow-counterclockwise me-2"), "Reset to Defaults"], 
                color="light", 
                className="me-2 bg-white border text-muted fw-bold"
            ),
            dbc.Button(
                [html.I(className="bi bi-check2 me-2"), "Save Changes"], 
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
                        dbc.NavLink([html.I(className="bi bi-gear-fill me-3"), "General"], id="tab-general", n_clicks=0, active=True, href="#", className="fw-bold mb-1 text-start"),
                        dbc.NavLink([html.I(className="bi bi-palette me-3"), "Appearance"], id="tab-appearance", n_clicks=0, href="#", className="mb-1 text-dark text-start"),
                        dbc.NavLink([html.I(className="bi bi-bell me-3"), "Notifications"], id="tab-notifications", n_clicks=0, href="#", className="mb-1 text-dark text-start"),
                        dbc.NavLink([html.I(className="bi bi-shield-lock me-3"), "Privacy"], id="tab-privacy", n_clicks=0, href="#", className="mb-1 text-dark text-start"),
                        dbc.NavLink([html.I(className="bi bi-hdd me-3"), "Storage"], id="tab-storage", n_clicks=0, href="#", className="text-dark text-start"),
                    ], vertical=True, pills=True, className="settings-nav p-2")
                ], width=3, className="border-end pe-0 bg-light rounded-start"), 

                # --- RIGHT COLUMN: Dynamic Content Area ---
                dbc.Col([
                    # We give this Div an ID so the callback can target it
                    html.Div(id="settings-content-area", children=render_general())
                ], width=9)
            ], className="g-0") 
        ], className="p-0") 
    ], className="shadow-sm border-0 overflow-hidden") 

], fluid=True, className="py-4")


# =============================================================================
# 3. CALLBACK LOGIC
# =============================================================================

@callback(
    Output("settings-content-area", "children"),
    Output("tab-general", "active"),
    Output("tab-appearance", "active"),
    Output("tab-notifications", "active"),
    Output("tab-privacy", "active"),
    Output("tab-storage", "active"),
    [
        Input("tab-general", "n_clicks"),
        Input("tab-appearance", "n_clicks"),
        Input("tab-notifications", "n_clicks"),
        Input("tab-privacy", "n_clicks"),
        Input("tab-storage", "n_clicks"),
    ]
)
def switch_settings_tab(c1, c2, c3, c4, c5):
    # Determine which button was clicked
    button_id = ctx.triggered_id if ctx.triggered_id else "tab-general"

    # Default content
    content = render_general()
    
    # Logic to switch content based on ID
    if button_id == "tab-appearance":
        content = render_appearance()
    elif button_id == "tab-notifications":
        content = render_notifications()
    elif button_id == "tab-privacy":
        content = render_privacy()
    elif button_id == "tab-storage":
        content = render_storage()

    # Return Content + Active State (True/False) for each tab
    return content, \
           (button_id == "tab-general"), \
           (button_id == "tab-appearance"), \
           (button_id == "tab-notifications"), \
           (button_id == "tab-privacy"), \
           (button_id == "tab-storage")