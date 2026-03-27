from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5('Basic Accordion', className='mb-0')),
            dbc.CardBody(dbc.Accordion([
                dbc.AccordionItem('Computer Science covers algorithms, data structures, software engineering, and computing theory.', title='Computer Science'),
                dbc.AccordionItem('Mathematics covers calculus, linear algebra, statistics, and discrete mathematics.', title='Mathematics'),
                dbc.AccordionItem('Engineering covers mechanical, electrical, civil, and chemical engineering disciplines.', title='Engineering'),
                dbc.AccordionItem('Biology covers cell biology, genetics, ecology, and human anatomy.', title='Biology'),
            ], start_collapsed=True)),
        ]), md=6, className='mb-3'),

        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5('Always Open Accordion', className='mb-0')),
            dbc.CardBody(dbc.Accordion([
                dbc.AccordionItem([
                    html.P('Semester 1: Introduction to Programming, Calculus I, Physics I'),
                    html.P('Semester 2: Data Structures, Calculus II, Physics II'),
                ], title='First Year Curriculum'),
                dbc.AccordionItem([
                    html.P('Semester 3: Algorithms, Linear Algebra, Statistics'),
                    html.P('Semester 4: Database Systems, Operating Systems, Discrete Math'),
                ], title='Second Year Curriculum'),
                dbc.AccordionItem([
                    html.P('Semester 5: Software Engineering, Computer Networks, AI'),
                    html.P('Semester 6: Machine Learning, Cloud Computing, Electives'),
                ], title='Third Year Curriculum'),
            ], always_open=True)),
        ]), md=6, className='mb-3'),
    ]),
], fluid=True)
