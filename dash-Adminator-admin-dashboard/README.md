# Adminator Admin Dashboard - Dash Version

A complete modern admin dashboard built with Dash and Dash Bootstrap Components, based on the open-source Adminator template.

## Features

✨ **Complete Pages & Components**
- Dashboard with statistics and charts
- Email, Compose, and Chat pages
- Calendar functionality
- Forms with validation
- UI Elements showcase (buttons, badges, alerts, etc.)
- Tables (Basic and Data Tables with DataTable component)
- Maps (Google Maps and Vector Maps placeholders)
- Authentication pages (Sign In, Sign Up)
- Error pages (404, 500)
- Blank page template

📊 **Dashboard Features**
- Interactive charts using Plotly
- Responsive layout
- Sidebar navigation with dropdowns
- Top navigation bar
- Real-time data displays
- Beautiful color scheme matching original design

🎨 **Design**
- Bootstrap 5 styling
- Themify Icons integration
- Font Awesome icons
- Custom CSS with dark mode support (via prefers-color-scheme)
- Professional color palette
- Fully responsive design

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Navigate to the project directory:**
   ```bash
   cd dash-admin
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Start the development server:
```bash
python app.py
```

The application will be available at `http://localhost:8050`

### Production Deployment:
```bash
python app.py
# Or use Gunicorn for production:
gunicorn --workers 4 index:app.server
```

## Project Structure

```
dash-admin/
├── app/
│   ├── __init__.py
│   ├── app.py                 # Main Dash app with routing
│   ├── components/
│   │   ├── __init__.py
│   │   └── layout.py          # Header and sidebar components
│   └── pages/
│       ├── __init__.py
│       ├── dashboard.py       # Dashboard page
│       ├── tables.py          # Data tables pages
│       ├── charts.py          # Charts page
│       ├── forms.py           # Forms page
│       ├── ui_elements.py     # UI elements showcase
│       ├── email_chat.py      # Email, compose, and chat pages
│       ├── other_pages.py     # Calendar, blank, error, and auth pages
│       └── maps.py            # Google Maps and Vector Maps pages
├── assets/
│   └── style.css              # Custom styling
├── index.py                   # Application entry point
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Pages & Routes

| Page | Route | Features |
|------|-------|----------|
| Dashboard | `/` | Statistics, charts, activity feed |
| Email | `/email` | Inbox list and email viewer |
| Compose | `/compose` | Email composition form |
| Chat | `/chat` | Real-time messaging interface |
| Calendar | `/calendar` | Event calendar and date picker |
| Charts | `/charts` | Multiple chart types (line, bar, pie, area) |
| Forms | `/forms` | Form elements and validation states |
| UI Elements | `/ui` | Component showcase (buttons, badges, alerts, etc.) |
| Basic Table | `/tables/basic` | HTML table with Bootstrap styling |
| Data Table | `/tables/data` | Interactive Dash DataTable with 10 rows per page |
| Google Maps | `/maps/google` | Google Maps integration placeholder |
| Vector Maps | `/maps/vector` | Vector maps integration placeholder |
| Blank | `/pages/blank` | Blank template for custom content |
| 404 Error | `/pages/404` | Page not found error page |
| 500 Error | `/pages/500` | Server error page |
| Sign In | `/pages/signin` | Login form |
| Sign Up | `/pages/signup` | Registration form |

## Customization

### Changing Colors & Theme
Edit the CSS variables in `assets/style.css`:

```css
:root {
  --bs-primary: #2196F3;
  --bs-secondary: #757575;
  --bs-success: #4CAF50;
  /* ... other colors ... */
}
```

### Adding Dark Mode
The CSS is pre-configured with dark mode support via `prefers-color-scheme: dark`. Browser will automatically switch based on system settings.

### Modifying Sidebar Menu
Edit the `menu_items` and `dropdown_items` lists in `app/app.py` in the `update_sidebar_menu` callback.

### Adding New Pages
1. Create a new function in `app/pages/` folder
2. Import it in `app/app.py`
3. Add a route in the `display_page` callback
4. Add menu item to `update_sidebar_menu` callback

Example:
```python
# In app/pages/new_page.py
def create_new_page():
    return dbc.Container([
        html.H2("New Page", className="mb-4 mt-4"),
        # Add your content here
    ], fluid=True)

# In app/app.py
elif pathname == "/new-page":
    return create_new_page()
```

## Dependencies

- **dash**: Web application framework
- **dash-bootstrap-components**: Bootstrap 5 components for Dash
- **plotly**: Interactive charting library
- **pandas**: Data manipulation and analysis
- **python-dateutil**: Date utilities

See `requirements.txt` for complete list with versions.

## Screenshots & Features

### Dashboard
- Statistics cards with KPIs
- Interactive charts
- Recent activity feed
- Top pages list

### Tables
- Basic HTML-based tables
- Interactive DataTable with sorting and pagination
- Responsive design

### Forms
- Text inputs
- Dropdowns
- Textareas
- Checkboxes and radio buttons
- Form validation states

### UI Elements
- Buttons (all colors and sizes)
- Badges
- Alerts
- Progress bars
- Accordions
- Cards
- Tooltips

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance Tips

1. Use production mode for deployment (set `debug=False`)
2. Consider using Gunicorn or similar WSGI server
3. Enable caching for static assets
4. Consider using a CDN for external libraries

## Troubleshooting

### Port Already in Use
```bash
# Change port in index.py
python -c "import index; index.app.run_server(port=8051)"
```

### Module Import Errors
```bash
# Ensure you're in the correct directory and virtual environment is activated
cd dash-admin
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Styling Issues
- Clear browser cache (Ctrl+Shift+Delete or Cmd+Shift+Delete)
- Restart the development server
- Check that assets/style.css is being loaded

## Future Enhancements

- [ ] Database integration
- [ ] User authentication
- [ ] Real email and chat functionality
- [ ] Advanced analytics
- [ ] Export to PDF/Excel
- [ ] Real-time notifications
- [ ] Mobile app version
- [ ] API integration examples

## License

This project replicates the structure and design of the open-source Adminator dashboard template by puikinsh. The Dash implementation is provided as-is for educational and development purposes.

Original Adminator: https://github.com/puikinsh/Adminator-admin-dashboard

## Contributing

Feel free to fork, modify, and improve this dashboard. Suggestions and improvements are welcome!

## Support

For issues, questions, or suggestions:
1. Check the troubleshooting section
2. Review the Dash documentation: https://dash.plotly.com/
3. Review Dash Bootstrap Components: https://dash-bootstrap-components.opensource.faculty.ai/

---

**Built with ❤️ using Dash and Dash Bootstrap Components**
