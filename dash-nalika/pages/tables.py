from dash import html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

# Sample data
data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'Webcam', 'Speaker', 'Microphone'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Audio', 'Video', 'Audio', 'Audio'],
    'Price': ['$999', '$29', '$79', '$399', '$149', '$89', '$199', '$129'],
    'Stock': [45, 120, 85, 32, 67, 54, 43, 78],
    'Status': ['In Stock', 'In Stock', 'In Stock', 'Low Stock', 'In Stock', 'In Stock', 'Low Stock', 'In Stock']
}

df = pd.DataFrame(data)

CARD_STYLE = {'backgroundColor': '#1b2a47', 'border': '1px solid #1e3a5f'}
HEADER_STYLE = {'backgroundColor': '#152036', 'color': 'white', 'borderBottom': '1px solid #1e3a5f'}

# Static Table
static_table = dbc.Card([
    dbc.CardHeader(html.H5('Static Table', style={'color': 'white'}), style=HEADER_STYLE),
    dbc.CardBody([
        dbc.Table([
            html.Thead([
                html.Tr([
                    html.Th('ID'),
                    html.Th('Product'),
                    html.Th('Category'),
                    html.Th('Price'),
                    html.Th('Stock'),
                    html.Th('Status'),
                    html.Th('Actions'),
                ])
            ]),
            html.Tbody([
                html.Tr([
                    html.Td('1'),
                    html.Td('Laptop'),
                    html.Td('Electronics'),
                    html.Td('$999'),
                    html.Td('45'),
                    html.Td(dbc.Badge('In Stock', color='success')),
                    html.Td([
                        dbc.Button('Edit', color='primary', size='sm', className='me-1'),
                        dbc.Button('Delete', color='danger', size='sm'),
                    ]),
                ]),
                html.Tr([
                    html.Td('2'),
                    html.Td('Mouse'),
                    html.Td('Accessories'),
                    html.Td('$29'),
                    html.Td('120'),
                    html.Td(dbc.Badge('In Stock', color='success')),
                    html.Td([
                        dbc.Button('Edit', color='primary', size='sm', className='me-1'),
                        dbc.Button('Delete', color='danger', size='sm'),
                    ]),
                ]),
                html.Tr([
                    html.Td('3'),
                    html.Td('Keyboard'),
                    html.Td('Accessories'),
                    html.Td('$79'),
                    html.Td('85'),
                    html.Td(dbc.Badge('In Stock', color='success')),
                    html.Td([
                        dbc.Button('Edit', color='primary', size='sm', className='me-1'),
                        dbc.Button('Delete', color='danger', size='sm'),
                    ]),
                ]),
                html.Tr([
                    html.Td('4'),
                    html.Td('Monitor'),
                    html.Td('Electronics'),
                    html.Td('$399'),
                    html.Td('32'),
                    html.Td(dbc.Badge('Low Stock', color='warning')),
                    html.Td([
                        dbc.Button('Edit', color='primary', size='sm', className='me-1'),
                        dbc.Button('Delete', color='danger', size='sm'),
                    ]),
                ]),
            ])
        ], bordered=True, hover=True, responsive=True, striped=True, className='table-dark')
    ])
], className='mb-4', style=CARD_STYLE)

# Data Table
data_table = dbc.Card([
    dbc.CardHeader(html.H5('Interactive Data Table', style={'color': 'white'}), style=HEADER_STYLE),
    dbc.CardBody([
        dash_table.DataTable(
            id='product-table',
            columns=[{'name': col, 'id': col} for col in df.columns],
            data=df.to_dict('records'),
            style_table={'overflowX': 'auto'},
            style_cell={
                'backgroundColor': '#1b2a47',
                'color': '#ffffff',
                'border': '1px solid #152036',
                'textAlign': 'left',
                'padding': '10px'
            },
            style_header={
                'backgroundColor': '#152036',
                'fontWeight': 'bold',
                'border': '1px solid #152036'
            },
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': '#152036'
                }
            ],
            page_size=10,
            sort_action='native',
            filter_action='native',
        )
    ])
], className='mb-4', style=CARD_STYLE)

# Bordered Table
bordered_table = dbc.Card([
    dbc.CardHeader(html.H5('Bordered Table', style={'color': 'white'}), style=HEADER_STYLE),
    dbc.CardBody([
        dbc.Table([
            html.Thead([
                html.Tr([
                    html.Th('#'),
                    html.Th('First Name'),
                    html.Th('Last Name'),
                    html.Th('Email'),
                    html.Th('Role'),
                ])
            ]),
            html.Tbody([
                html.Tr([
                    html.Td('1'),
                    html.Td('John'),
                    html.Td('Doe'),
                    html.Td('john@example.com'),
                    html.Td(dbc.Badge('Admin', color='primary')),
                ]),
                html.Tr([
                    html.Td('2'),
                    html.Td('Jane'),
                    html.Td('Smith'),
                    html.Td('jane@example.com'),
                    html.Td(dbc.Badge('User', color='secondary')),
                ]),
                html.Tr([
                    html.Td('3'),
                    html.Td('Bob'),
                    html.Td('Johnson'),
                    html.Td('bob@example.com'),
                    html.Td(dbc.Badge('Manager', color='info')),
                ]),
            ])
        ], bordered=True, hover=True, responsive=True, className='table-dark')
    ])
], className='mb-4', style=CARD_STYLE)

layout = html.Div([
    dbc.Breadcrumb(items=[
        {'label': 'Home', 'href': '/', 'active': False},
        {'label': 'Tables', 'active': True},
    ], className='breadcrumb'),
    
    static_table,
    data_table,
    bordered_table,
])
