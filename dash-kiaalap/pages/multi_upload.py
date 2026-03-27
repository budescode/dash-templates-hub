from dash import html, dcc
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5('File Upload', className='mb-0')),
            dbc.CardBody([
                dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        html.I(className='bi bi-cloud-upload', style={'fontSize': '48px', 'color': '#6366f1'}),
                        html.P('Drag and Drop or', className='mb-1 mt-2'),
                        html.A('Browse Files', className='text-primary fw-semibold'),
                        html.P('Supports: PDF, DOC, XLS, PNG, JPG (Max 10MB)', className='text-muted small mt-1'),
                    ], className='text-center py-4'),
                    style={
                        'border': '2px dashed #d1d5db',
                        'borderRadius': '8px',
                        'cursor': 'pointer',
                        'background': '#f9fafb',
                    },
                    multiple=True,
                    className='mb-3',
                ),
                html.Div(id='upload-output'),
            ]),
        ]), md=8, className='mb-3'),

        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5('Upload Guidelines', className='mb-0')),
            dbc.CardBody([
                dbc.ListGroup([
                    dbc.ListGroupItem([html.I(className='bi bi-check-circle text-success me-2'), 'PDF documents']),
                    dbc.ListGroupItem([html.I(className='bi bi-check-circle text-success me-2'), 'Word documents (.doc, .docx)']),
                    dbc.ListGroupItem([html.I(className='bi bi-check-circle text-success me-2'), 'Excel spreadsheets']),
                    dbc.ListGroupItem([html.I(className='bi bi-check-circle text-success me-2'), 'Images (PNG, JPG, GIF)']),
                    dbc.ListGroupItem([html.I(className='bi bi-x-circle text-danger me-2'), 'Executable files (.exe, .sh)']),
                    dbc.ListGroupItem([html.I(className='bi bi-x-circle text-danger me-2'), 'Files larger than 10MB']),
                ], flush=True),
            ]),
        ]), md=4, className='mb-3'),
    ]),
], fluid=True)
