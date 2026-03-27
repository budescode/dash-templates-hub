# File: pages/index.py (The second page)

from dash import html, register_page, dcc
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
from config.helpers import loadDataSet
import plotly.express as px
import pandas as pd


# --- 1. Register with a Unique Path ---
register_page(
    __name__,
    path='/reviews', # Set a unique path
    name='Reviews'
)
reviews_df = loadDataSet("order_reviews")
score_counts = reviews_df["review_score"].value_counts().reset_index()
score_counts.columns = ["Score", "Count"]

# 1. Convert Date
reviews_df["review_creation_date"] = pd.to_datetime(reviews_df["review_creation_date"])
# 2. Resample by Month (M) and calculate Mean Score
monthly_scores = reviews_df.set_index("review_creation_date").resample("ME")["review_score"].mean().reset_index()
all_stars =  len(reviews_df["review_score"])
one_star_total = len(reviews_df[reviews_df["review_score"] == 1]) 
two_star_total = len(reviews_df[reviews_df["review_score"] == 2] )
three_star_total = len(reviews_df[reviews_df["review_score"] == 3] )
four_star_total = len(reviews_df[reviews_df["review_score"] == 4]) 
five_star_total = len(reviews_df[reviews_df["review_score"] == 5] )

# --- 2. Define the Page Layout ---
# This is the content specific to this second page.
layout = dbc.Container([
                       html.Div([
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                            html.Div([
                                                html.Div(
                                                    [
                                                    html.H6("All Stars", className="text-muted"),
                                                    html.H3(f"{all_stars:,}", className="text-dark"),
                                                    ]
                                                ),
                                                html.I(className="bi bi-star fs-1 text-primary"),
                                            ],
                                            className="d-flex justify-content-between align-items-center",
                                            )
                                            ]
                                        )
                                    ),
                                    md=2
                                ),
                                                              dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                            html.Div([
                                                html.Div(
                                                    [
                                                    html.H6("One Star", className="text-muted"),
                                                    html.H3(f"{one_star_total:,}", className="text-dark"),
                                                    ]
                                                ),
                                                html.I(className="bi bi-star fs-1 text-primary"),
                                            ],
                                            className="d-flex justify-content-between align-items-center",
                                            )
                                            ]
                                        )
                                    ),
                                    md=2
                                ),
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                            html.Div([
                                                html.Div(
                                                    [
                                                    html.H6("Two Stars", className="text-muted"),
                                                    html.H3(f"{two_star_total:,}", className="text-dark"),
                                                    ]
                                                ),
                                                html.I(className="bi bi-star fs-1 text-primary"),
                                            ],
                                            className="d-flex justify-content-between align-items-center",
                                            )
                                            ]
                                        )
                                    ),
                                    md=2
                                ),
                                  dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                            html.Div([
                                                html.Div(
                                                    [
                                                    html.H6("Three Stars", className="text-muted"),
                                                    html.H3(f"{three_star_total:,}", className="text-dark"),
                                                    ]
                                                ),
                                                html.I(className="bi bi-star fs-1 text-primary"),
                                            ],
                                            className="d-flex justify-content-between align-items-center",
                                            )
                                            ]
                                        )
                                    ),
                                    md=2
                                ),
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                            html.Div([
                                                html.Div(
                                                    [
                                                    html.H6("Four Stars", className="text-muted"),
                                                    html.H3(f"{four_star_total:,}", className="text-dark"),
                                                    ]
                                                ),
                                                html.I(className="bi bi-star fs-1 text-primary"),
                                            ],
                                            className="d-flex justify-content-between align-items-center",
                                            )
                                            ]
                                        )
                                    ),
                                    md=2
                                ),
                                dbc.Col(
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                            html.Div([
                                                html.Div(
                                                    [
                                                    html.H6("Five Stars", className="text-muted"),
                                                    html.H3(f"{five_star_total:,}", className="text-dark"),
                                                    ]
                                                ),
                                                html.I(className="bi bi-star fs-1 text-primary"),
                                            ],
                                            className="d-flex justify-content-between align-items-center",
                                            )
                                            ]
                                        )
                                    ),
                                    md=2
                                ),
                            ], className="mt-4"),]),

   dbc.Row(
       children=[
           dbc.Col(
               md=12, children=[
                        dbc.Card(
                        dbc.CardBody(
                            children = [
                                dcc.Graph(
                                    figure=px.bar(
                                        score_counts,
                                        x="Score",
                                        y="Count",
                                        title="Customer Satisfaction Breakdown",
                                        # Color logic: Red for 1, Green for 5
                                        color="Score",
                                        color_continuous_scale="RdYlGn" # Red-Yellow-Green scale
                                    )
                                )
                            ]
                        )
                    )
               ]
           ),
       ], class_name='mt-4'
   ), 
   dbc.Row(
       children=[
           dbc.Col(
               md=12,
               children=[
                   dbc.Card(
                       dbc.CardBody(
                           children = [   dcc.Graph(
                                figure=px.line(
                                    monthly_scores,
                                    x="review_creation_date",
                                    y="review_score",
                                    title="Average Review Score Over Time",
                                    markers=True
                                )
                            )]
                       )
                   )
                
               ]
           )
       ], class_name='mt-4'
   ),
   dbc.Row(
       children=[
           dbc.Col(md=12, children=[
                  dbc.Card(
                       dbc.CardBody(
                           children = [    
                               html.H6("Reviews"),
                               dag.AgGrid( 
                                    columnDefs = list({"headerName":x, "field":x} for x in reviews_df.columns),
                                    rowData = reviews_df.to_dict("records"),
                                    style={"height":"500px"}
                                    )
                            ]
                       )
                   )
           ]
            )
       ], class_name='mt-4'
   )
  
], fluid=True)