from dash import html
import dash_bootstrap_components as dbc
import dash_ag_grid as dag


authors = [
    {"name": "Esthera Jackson", "email": "esthera@simmmple.com", "role": "Manager", "dept": "Organization", "status": "Online"},
    {"name": "Alexa Liras", "email": "alexa@simmmple.com", "role": "Programmer", "dept": "Developer", "status": "Offline"},
    {"name": "Laurent Michael", "email": "laurent@simmmple.com", "role": "Executive", "dept": "Projects", "status": "Online"},
    {"name": "Freduardo Hill", "email": "freduardo@simmmple.com", "role": "Manager", "dept": "Organization", "status": "Online"},
    {"name": "Daniel Thomas", "email": "daniel@simmmple.com", "role": "Programmer", "dept": "Developer", "status": "Offline"},
    {"name": "Mark Wilson", "email": "mark@simmmple.com", "role": "Designer", "dept": "UI/UX Design", "status": "Offline"},
]

projects = [
    {"name": "Chakra Soft UI Version", "budget": "$14,000", "status": "Working", "completion": 60},
    {"name": "Add Progress Track", "budget": "$3,000", "status": "Canceled", "completion": 10},
    {"name": "Fix Platform Errors", "budget": "Not set", "status": "Done", "completion": 100},
    {"name": "Launch our Mobile App", "budget": "$32,000", "status": "Done", "completion": 100},
    {"name": "Add the New Pricing Page", "budget": "$400", "status": "Working", "completion": 25},
]


authors_rows = [
    {
        "author": f"{author['name']}\n{author['email']}",
        "function": f"{author['role']}\n{author['dept']}",
        "status": author["status"],
        "employed": "14/06/21",
        "edit": "Edit",
    }
    for author in authors
]

projects_rows = [
    {
        "company": project["name"],
        "budget": project["budget"],
        "status": project["status"],
        "completion": f"{project['completion']}%",
        "menu": "...",
    }
    for project in projects
]

layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row(
            className="g-3",
            children=[
                dbc.Col(
                    html.Div(
                        className="card-surface chart-card",
                        children=[
                            html.Div("Authors Table", className="chart-title"),
                            html.Div(
                                style={"overflowX": "auto"},
                                children=dag.AgGrid(
                                    rowData=authors_rows,
                                    columnDefs=[
                                        {"headerName": "AUTHOR", "field": "author", "flex": 2, "minWidth": 160},
                                        {"headerName": "FUNCTION", "field": "function", "flex": 2, "minWidth": 140},
                                        {"headerName": "STATUS", "field": "status", "flex": 1, "minWidth": 90},
                                        {"headerName": "EMPLOYED", "field": "employed", "flex": 1, "minWidth": 100},
                                        {"headerName": "", "field": "edit", "flex": 0.6, "minWidth": 60},
                                    ],
                                    defaultColDef={
                                        "sortable": False,
                                        "filter": False,
                                        "resizable": True,
                                        "wrapText": True,
                                        "autoHeight": True,
                                    },
                                    dashGridOptions={"domLayout": "autoHeight"},
                                    className="ag-theme-alpine purity-ag",
                                ),
                            ),
                        ],
                    ),
                    xs=12,
                )
            ],
        ),
        dbc.Row(
            className="g-3 row-gap",
            children=[
                dbc.Col(
                    html.Div(
                        className="card-surface chart-card",
                        children=[
                            html.Div("Projects", className="chart-title"),
                            html.Div("30 done this month", className="chart-sub"),
                            html.Div(
                                style={"overflowX": "auto"},
                                children=dag.AgGrid(
                                    rowData=projects_rows,
                                    columnDefs=[
                                        {"headerName": "COMPANIES", "field": "company", "flex": 2, "minWidth": 180},
                                        {"headerName": "BUDGET", "field": "budget", "flex": 1, "minWidth": 90},
                                        {"headerName": "STATUS", "field": "status", "flex": 1, "minWidth": 90},
                                        {"headerName": "COMPLETION", "field": "completion", "flex": 1, "minWidth": 110},
                                        {"headerName": "", "field": "menu", "flex": 0.5, "minWidth": 50},
                                    ],
                                    defaultColDef={
                                        "sortable": False,
                                        "filter": False,
                                        "resizable": True,
                                        "wrapText": True,
                                        "autoHeight": True,
                                    },
                                    dashGridOptions={"domLayout": "autoHeight"},
                                    className="ag-theme-alpine purity-ag",
                                ),
                            ),
                        ],
                    ),
                    xs=12,
                )
            ],
        ),
    ],
)
