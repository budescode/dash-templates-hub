from dash import html, dcc
import dash_bootstrap_components as dbc

tools = [
    {
        "label": "Alerts",
        "href": "/alerts",
        "icon": "bi bi-exclamation-triangle",
        "color": "#f59e0b",
        "bg": "rgba(245,158,11,0.1)",
        "desc": "Alert components and notifications"
    },
    {
        "label": "Modals",
        "href": "/modals",
        "icon": "bi bi-window-stack",
        "color": "#6366f1",
        "bg": "rgba(99,102,241,0.1)",
        "desc": "Modal dialogs and overlays"
    },
    {
        "label": "Accordion",
        "href": "/accordion",
        "icon": "bi bi-layout-accordion-collapsed",
        "color": "#10b981",
        "bg": "rgba(16,185,129,0.1)",
        "desc": "Collapsible accordion sections"
    },
    {
        "label": "Code Editor",
        "href": "/code-editor",
        "icon": "bi bi-code-slash",
        "color": "#3b82f6",
        "bg": "rgba(59,130,246,0.1)",
        "desc": "Syntax-highlighted code editor"
    },
    {
        "label": "Preloaders",
        "href": "/preloader",
        "icon": "bi bi-arrow-repeat",
        "color": "#8b5cf6",
        "bg": "rgba(139,92,246,0.1)",
        "desc": "Loading spinners and preloaders"
    },
    {
        "label": "Notifications",
        "href": "/notifications",
        "icon": "bi bi-bell",
        "color": "#ef4444",
        "bg": "rgba(239,68,68,0.1)",
        "desc": "Notification styles and patterns"
    },
    {
        "label": "Tree View",
        "href": "/tree-view",
        "icon": "bi bi-diagram-3",
        "color": "#14b8a6",
        "bg": "rgba(20,184,166,0.1)",
        "desc": "Hierarchical tree structure"
    },
    {
        "label": "PDF Viewer",
        "href": "/pdf-viewer",
        "icon": "bi bi-file-earmark-pdf",
        "color": "#dc2626",
        "bg": "rgba(220,38,38,0.1)",
        "desc": "Embedded PDF document viewer"
    },
    {
        "label": "Interactive Maps",
        "href": "/google-map",
        "icon": "bi bi-geo-alt",
        "color": "#0ea5e9",
        "bg": "rgba(14,165,233,0.1)",
        "desc": "Interactive map component"
    },
    {
        "label": "Data Maps",
        "href": "/data-maps",
        "icon": "bi bi-map",
        "color": "#f97316",
        "bg": "rgba(249,115,22,0.1)",
        "desc": "Data-driven choropleth maps"
    },
]

layout = dbc.Container([
    html.Div([
        html.H5("Tools & Components", className="text-dark"),
        html.P("Developer tools, UI components, and extras.", className="text-muted"),
    ], className="mt-4 mb-4"),

    dbc.Row([
        dbc.Col(
            dcc.Link(
                dbc.Card(
                    dbc.CardBody([
                        html.Div(
                            html.I(className=t["icon"], style={"fontSize": "28px", "color": t["color"]}),
                            className="rounded-circle d-flex align-items-center justify-content-center mb-3",
                            style={"width": "56px", "height": "56px", "background": t["bg"]}
                        ),
                        html.H6(t["label"], className="fw-semibold mb-1"),
                        html.P(t["desc"], className="text-muted small mb-0"),
                    ]),
                    className="h-100 tool-card",
                    style={"cursor": "pointer", "transition": "box-shadow 0.2s"},
                ),
                href=t["href"],
                style={"textDecoration": "none"},
            ),
            md=3, className="mb-4"
        )
        for t in tools
    ]),
], fluid=True)
