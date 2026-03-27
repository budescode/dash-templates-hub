#!/usr/bin/env python3
"""Generate all page files for the Dash Kiaalap project"""

import os

pages = {
    'analytics': 'Analytics Dashboard',
    'widgets': 'Widgets',
    'events': 'Events Calendar',
    'all_students': 'All Students',
    'add_student': 'Add Student',
    'edit_student': 'Edit Student',
    'student_profile': 'Student Profile',
    'all_professors': 'All Professors',
    'add_professor': 'Add Professor',
    'edit_professor': 'Edit Professor',
    'professor_profile': 'Professor Profile',
    'all_courses': 'All Courses',
    'add_course': 'Add Course',
    'edit_course': 'Edit Course',
    'course_info': 'Course Information',
    'course_payment': 'Course Payment',
    'library_assets': 'Library Assets',
    'add_library_assets': 'Add Library Asset',
    'edit_library_assets': 'Edit Library Asset',
    'departments': 'Departments',
    'add_department': 'Add Department',
    'edit_department': 'Edit Department',
    'mailbox': 'Mailbox',
    'mailbox_compose': 'Compose Message',
    'mailbox_view': 'View Message',
    'buttons': 'Buttons',
    'alerts': 'Alerts',
    'modals': 'Modals',
    'accordion': 'Accordion',
    'basic_form': 'Basic Forms',
    'advance_form': 'Advanced Forms',
    'password_meter': 'Password Meter',
    'multi_upload': 'File Upload',
    'images_cropper': 'Image Cropper',
    'line_charts': 'Line Charts',
    'area_charts': 'Area Charts',
    'bar_charts': 'Bar Charts',
    'static_table': 'Static Tables',
    'data_table': 'Data Tables',
    'code_editor': 'Code Editor',
    'preloader': 'Preloaders',
    'notifications': 'Notifications',
    'tree_view': 'Tree View',
    'pdf_viewer': 'PDF Viewer',
    'google_map': 'Interactive Maps',
    'data_maps': 'Data Maps',
    'login': 'Login',
    'register': 'Register',
    'lock': 'Lock Screen',
    'password_recovery': 'Password Recovery',
    'error_404': '404 Error',
    'error_500': '500 Error',
}

template = """from dash import html

layout = html.Div([
    html.Div([
        html.H1('{title}', className='h3 font-bold'),
        html.P('This is the {title} page.', className='text-muted text-sm')
    ], className='mb-3'),
    
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H5('{title}', className='dashboard-card-title')
                ], className='dashboard-card-header'),
                html.Div([
                    html.P('Content for {title} will be displayed here.')
                ], className='dashboard-card-body')
            ], className='dashboard-card')
        ], className='dashboard-grid grid-cols-1')
    ], className='dashboard-row')
])
"""

auth_template = """from dash import html

layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('{title}', className='text-center mb-4'),
                    html.P('This is the {title} page.', className='text-center text-muted')
                ], className='card-body p-5')
            ], className='card shadow-lg', style={{'max-width': '400px', 'width': '100%'}})
        ], className='d-flex justify-content-center align-items-center', style={{'min-height': '100vh'}})
    ], className='container')
])
"""

# Create pages directory if it doesn't exist
os.makedirs('pages', exist_ok=True)

# Generate all page files
for page_name, page_title in pages.items():
    file_path = f'pages/{page_name}.py'
    
    # Skip if file already exists
    if os.path.exists(file_path):
        print(f'Skipping {file_path} (already exists)')
        continue
    
    # Use auth template for login/register/lock/password_recovery pages
    if page_name in ['login', 'register', 'lock', 'password_recovery', 'error_404', 'error_500']:
        content = auth_template.format(title=page_title)
    else:
        content = template.format(title=page_title)
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f'Created {file_path}')

print('\\nAll page files generated successfully!')
