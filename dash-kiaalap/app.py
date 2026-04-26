import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# Initialize the Dash app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
    suppress_callback_exceptions=True,
    title="Kiaalap Dashboard"
)

# Import layouts
from layouts import sidebar, footer
from layouts.header import create_header
from pages import index, analytics, widgets, events, all_students, add_student, edit_student, student_profile
from pages import all_professors, add_professor, edit_professor, professor_profile
from pages import all_courses, add_course, edit_course, course_info, course_payment
from pages import library_assets, add_library_assets, edit_library_assets
from pages import departments, add_department, edit_department
from pages import mailbox, mailbox_compose, mailbox_view
from pages import buttons, alerts, modals, accordion
from pages import basic_form, advance_form, password_meter, multi_upload, images_cropper
from pages import line_charts, area_charts, bar_charts
from pages import static_table, data_table
from pages import code_editor, preloader, notifications, tree_view, pdf_viewer, tools
from pages import google_map, data_maps
from pages import login, register, lock, password_recovery, error_404, error_500

# App layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Callback for page routing
@app.callback(
    dash.dependencies.Output('page-content', 'children'),
    [dash.dependencies.Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/' or pathname == '/index':
        return create_page_layout(index.layout, 'Dashboard')
    elif pathname == '/analytics':
        return create_page_layout(analytics.layout, 'Analytics')
    elif pathname == '/widgets':
        return create_page_layout(widgets.layout, 'Widgets')
    elif pathname == '/events':
        return create_page_layout(events.layout, 'Events')
    elif pathname == '/all-students':
        return create_page_layout(all_students.layout, 'All Students')
    elif pathname == '/add-student':
        return create_page_layout(add_student.layout, 'Add Student')
    elif pathname == '/edit-student':
        return create_page_layout(edit_student.layout, 'Edit Student')
    elif pathname == '/student-profile':
        return create_page_layout(student_profile.layout, 'Student Profile')
    elif pathname == '/all-professors':
        return create_page_layout(all_professors.layout, 'All Professors')
    elif pathname == '/add-professor':
        return create_page_layout(add_professor.layout, 'Add Professor')
    elif pathname == '/edit-professor':
        return create_page_layout(edit_professor.layout, 'Edit Professor')
    elif pathname == '/professor-profile':
        return create_page_layout(professor_profile.layout, 'Professor Profile')
    elif pathname == '/all-courses':
        return create_page_layout(all_courses.layout, 'All Courses')
    elif pathname == '/add-course':
        return create_page_layout(add_course.layout, 'Add Course')
    elif pathname == '/edit-course':
        return create_page_layout(edit_course.layout, 'Edit Course')
    elif pathname == '/course-info':
        return create_page_layout(course_info.layout, 'Course Info')
    elif pathname == '/course-payment':
        return create_page_layout(course_payment.layout, 'Course Payment')
    elif pathname == '/library-assets':
        return create_page_layout(library_assets.layout, 'Library Assets')
    elif pathname == '/add-library-assets':
        return create_page_layout(add_library_assets.layout, 'Add Library Asset')
    elif pathname == '/edit-library-assets':
        return create_page_layout(edit_library_assets.layout, 'Edit Library Asset')
    elif pathname == '/departments':
        return create_page_layout(departments.layout, 'Departments')
    elif pathname == '/add-department':
        return create_page_layout(add_department.layout, 'Add Department')
    elif pathname == '/edit-department':
        return create_page_layout(edit_department.layout, 'Edit Department')
    elif pathname == '/mailbox':
        return create_page_layout(mailbox.layout, 'Mailbox')
    elif pathname == '/mailbox-compose':
        return create_page_layout(mailbox_compose.layout, 'Compose')
    elif pathname == '/mailbox-view':
        return create_page_layout(mailbox_view.layout, 'View Message')
    elif pathname == '/buttons':
        return create_page_layout(buttons.layout, 'Buttons')
    elif pathname == '/alerts':
        return create_page_layout(alerts.layout, 'Alerts')
    elif pathname == '/modals':
        return create_page_layout(modals.layout, 'Modals')
    elif pathname == '/accordion':
        return create_page_layout(accordion.layout, 'Accordion')
    elif pathname == '/basic-form-element':
        return create_page_layout(basic_form.layout, 'Basic Forms')
    elif pathname == '/advance-form-element':
        return create_page_layout(advance_form.layout, 'Advanced Forms')
    elif pathname == '/password-meter':
        return create_page_layout(password_meter.layout, 'Password Meter')
    elif pathname == '/multi-upload':
        return create_page_layout(multi_upload.layout, 'File Upload')
    elif pathname == '/images-cropper':
        return create_page_layout(images_cropper.layout, 'Image Cropper')
    elif pathname == '/line-charts':
        return create_page_layout(line_charts.layout, 'Line Charts')
    elif pathname == '/area-charts':
        return create_page_layout(area_charts.layout, 'Area Charts')
    elif pathname == '/bar-charts':
        return create_page_layout(bar_charts.layout, 'Bar Charts')
    elif pathname == '/static-table':
        return create_page_layout(static_table.layout, 'Static Tables')
    elif pathname == '/data-table':
        return create_page_layout(data_table.layout, 'Data Tables')
    elif pathname == '/tools':
        return create_page_layout(tools.layout, 'Tools')
    elif pathname == '/code-editor':
        return create_page_layout(code_editor.layout, 'Code Editor')
    elif pathname == '/preloader':
        return create_page_layout(preloader.layout, 'Preloaders')
    elif pathname == '/notifications':
        return create_page_layout(notifications.layout, 'Notifications')
    elif pathname == '/tree-view':
        return create_page_layout(tree_view.layout, 'Tree View')
    elif pathname == '/pdf-viewer':
        return create_page_layout(pdf_viewer.layout, 'PDF Viewer')
    elif pathname == '/google-map':
        return create_page_layout(google_map.layout, 'Interactive Maps')
    elif pathname == '/data-maps':
        return create_page_layout(data_maps.layout, 'Data Maps')
    elif pathname == '/login':
        return login.layout
    elif pathname == '/register':
        return register.layout
    elif pathname == '/lock':
        return lock.layout
    elif pathname == '/password-recovery':
        return password_recovery.layout
    elif pathname == '/404':
        return error_404.layout
    elif pathname == '/500':
        return error_500.layout
    else:
        return error_404.layout

def create_page_layout(content, page_title):
    return html.Div([
        sidebar.layout,
        html.Div([
            create_header(page_title),
            html.Main([
                html.Div([content], className='container-fluid')
            ], className='dashboard-content', id='main-content'),
            footer.layout
        ], className='main-wrapper', id='mainWrapper')
    ])

# Callback to set active nav link
@app.callback(
    [
        dash.dependencies.Output('nav-dashboard', 'className'),
        dash.dependencies.Output('nav-analytics', 'className'),
        dash.dependencies.Output('nav-widgets', 'className'),
        dash.dependencies.Output('nav-events', 'className'),
        dash.dependencies.Output('nav-all-professors', 'className'),
        dash.dependencies.Output('nav-all-students', 'className'),
        dash.dependencies.Output('nav-all-courses', 'className'),
        dash.dependencies.Output('nav-library-assets', 'className'),
        dash.dependencies.Output('nav-departments', 'className'),
        dash.dependencies.Output('nav-mailbox', 'className'),
        dash.dependencies.Output('nav-buttons', 'className'),
        dash.dependencies.Output('nav-forms', 'className'),
        dash.dependencies.Output('nav-charts', 'className'),
        dash.dependencies.Output('nav-tables', 'className'),
        dash.dependencies.Output('nav-login', 'className'),
        dash.dependencies.Output('nav-tools', 'className'),
    ],
    [dash.dependencies.Input('url', 'pathname')]
)
def update_active_nav(pathname):
    nav_links = {
        '/': 'nav-dashboard',
        '/index': 'nav-dashboard',
        '/analytics': 'nav-analytics',
        '/widgets': 'nav-widgets',
        '/events': 'nav-events',
        '/all-professors': 'nav-all-professors',
        '/add-professor': 'nav-all-professors',
        '/edit-professor': 'nav-all-professors',
        '/professor-profile': 'nav-all-professors',
        '/all-students': 'nav-all-students',
        '/add-student': 'nav-all-students',
        '/edit-student': 'nav-all-students',
        '/student-profile': 'nav-all-students',
        '/all-courses': 'nav-all-courses',
        '/add-course': 'nav-all-courses',
        '/edit-course': 'nav-all-courses',
        '/course-info': 'nav-all-courses',
        '/course-payment': 'nav-all-courses',
        '/library-assets': 'nav-library-assets',
        '/add-library-assets': 'nav-library-assets',
        '/edit-library-assets': 'nav-library-assets',
        '/departments': 'nav-departments',
        '/add-department': 'nav-departments',
        '/edit-department': 'nav-departments',
        '/mailbox': 'nav-mailbox',
        '/mailbox-compose': 'nav-mailbox',
        '/mailbox-view': 'nav-mailbox',
        '/buttons': 'nav-buttons',
        '/alerts': 'nav-buttons',
        '/modals': 'nav-buttons',
        '/accordion': 'nav-buttons',
        '/basic-form-element': 'nav-forms',
        '/advance-form-element': 'nav-forms',
        '/password-meter': 'nav-forms',
        '/multi-upload': 'nav-forms',
        '/images-cropper': 'nav-forms',
        '/line-charts': 'nav-charts',
        '/area-charts': 'nav-charts',
        '/bar-charts': 'nav-charts',
        '/static-table': 'nav-tables',
        '/data-table': 'nav-tables',
        '/code-editor': 'nav-tables',
        '/preloader': 'nav-tables',
        '/notifications': 'nav-tables',
        '/tree-view': 'nav-tables',
        '/pdf-viewer': 'nav-tables',
        '/google-map': 'nav-tables',
        '/data-maps': 'nav-tables',
        '/login': 'nav-login',
        '/tools': 'nav-tools',
        '/alerts': 'nav-tools',
        '/modals': 'nav-tools',
        '/accordion': 'nav-tools',
        '/code-editor': 'nav-tools',
        '/preloader': 'nav-tools',
        '/notifications': 'nav-tools',
        '/tree-view': 'nav-tools',
        '/pdf-viewer': 'nav-tools',
        '/google-map': 'nav-tools',
        '/data-maps': 'nav-tools',
    }
    
    active_id = nav_links.get(pathname, None)
    
    return [
        'nav-link active' if active_id == 'nav-dashboard' else 'nav-link',
        'nav-link active' if active_id == 'nav-analytics' else 'nav-link',
        'nav-link active' if active_id == 'nav-widgets' else 'nav-link',
        'nav-link active' if active_id == 'nav-events' else 'nav-link',
        'nav-link active' if active_id == 'nav-all-professors' else 'nav-link',
        'nav-link active' if active_id == 'nav-all-students' else 'nav-link',
        'nav-link active' if active_id == 'nav-all-courses' else 'nav-link',
        'nav-link active' if active_id == 'nav-library-assets' else 'nav-link',
        'nav-link active' if active_id == 'nav-departments' else 'nav-link',
        'nav-link active' if active_id == 'nav-mailbox' else 'nav-link',
        'nav-link active' if active_id == 'nav-buttons' else 'nav-link',
        'nav-link active' if active_id == 'nav-forms' else 'nav-link',
        'nav-link active' if active_id == 'nav-charts' else 'nav-link',
        'nav-link active' if active_id == 'nav-tables' else 'nav-link',
        'nav-link active' if active_id == 'nav-login' else 'nav-link',
        'nav-link active' if active_id == 'nav-tools' else 'nav-link',
    ]

if __name__ == '__main__':
    app.run(debug=True, port=8050)
