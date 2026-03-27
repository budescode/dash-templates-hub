# Kiaalap Dashboard - Dash Version

A complete replication of the Kiaalap Education Management Dashboard built with Plotly Dash and Dash Bootstrap Components.

## Features

- 📊 Multiple dashboard views with interactive charts
- 👨‍🎓 Student management system
- 👨‍🏫 Professor management
- 📚 Course management
- 📖 Library asset tracking
- 🏢 Department management
- 📧 Mailbox system
- 🎨 UI components (buttons, forms, tables, charts)
- 🔐 Authentication pages
- 📱 Fully responsive design

## Installation

1. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

The application will be available at `http://localhost:8050`

## Project Structure

```
dash-kiaalap/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── assets/
│   └── dashboard.css     # Custom CSS styles
├── layouts/
│   ├── sidebar.py        # Sidebar navigation
│   ├── header.py         # Top navigation bar
│   └── footer.py         # Footer component
└── pages/
    ├── index.py          # Main dashboard
    ├── analytics.py      # Analytics dashboard
    ├── all_students.py   # Student listing
    ├── all_professors.py # Professor listing
    ├── all_courses.py    # Course listing
    └── ...               # Other pages
```

## Pages Included

### Main
- Dashboard (3 variants)
- Analytics
- Widgets
- Events

### Academic
- Students (List, Add, Edit, Profile)
- Professors (List, Add, Edit, Profile)
- Courses (List, Add, Edit, Info, Payment)
- Library Assets (List, Add, Edit)
- Departments (List, Add, Edit)

### Communication
- Mailbox (Inbox, Compose, View)

### Interface
- Components (Buttons, Alerts, Modals, Accordion)
- Forms (Basic, Advanced, Password Meter, File Upload, Image Cropper)
- Charts (Line, Area, Bar)
- Tables (Static, Data Tables)

### Developer Tools
- Code Editor
- Preloaders
- Notifications
- Tree View
- PDF Viewer
- Maps (Interactive, Data Maps)

### Authentication
- Login
- Register
- Lock Screen
- Password Recovery
- Error Pages (404, 500)

## Customization

### Styling
Edit `assets/dashboard.css` to customize colors, spacing, and other visual elements.

### Adding New Pages
1. Create a new file in `pages/` directory
2. Define the layout using Dash HTML components
3. Import and add the route in `app.py`

## Technologies Used

- **Plotly Dash**: Web application framework
- **Dash Bootstrap Components**: Bootstrap components for Dash
- **Plotly**: Interactive charts and graphs
- **Pandas**: Data manipulation (optional)

## License

This project replicates the design of Kiaalap dashboard template.

## Support

For issues and questions, please refer to the original Kiaalap documentation or Dash documentation.
