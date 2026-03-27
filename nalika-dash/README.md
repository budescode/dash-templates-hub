# Nalika Dashboard - Dash Bootstrap Components Version

A complete rewrite of the Nalika Bootstrap admin dashboard template using Dash and Dash Bootstrap Components.

## Features

- **Dark Theme Design** - Matching the original Nalika dark color scheme
- **Responsive Layout** - Works on all devices
- **Multiple Pages**:
  - Dashboard (Main page with stats, charts, products)
  - Login Page
  - Analytics (Progress bars, charts, metrics table)
  - Charts (Line, Bar, Area, Donut charts)
  - Data Tables (Static and interactive tables)
  - Forms (Basic, advanced, input groups)
  - Widgets (Alerts, badges, buttons, progress bars, cards, spinners)

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:8050
```

## Project Structure

```
nalika-dash/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── assets/
│   └── custom.css        # Custom dark theme CSS
├── components/
│   ├── sidebar.py        # Sidebar navigation component
│   └── navbar.py         # Top navbar component
└── pages/
    ├── dashboard.py      # Main dashboard page
    ├── login.py          # Login page
    ├── analytics.py      # Analytics page
    ├── charts.py         # Charts page
    ├── tables.py         # Data tables page
    ├── forms.py          # Forms page
    └── widgets.py        # Widgets page
```

## Pages Overview

### Dashboard (/)
- Statistics cards (Orders, Tax, Revenue, Sales)
- Product sales chart
- Analytics metrics
- Traffic analysis
- Product showcase
- Footer

### Login (/login)
- Clean login form
- Username and password fields
- Remember me checkbox
- Register button

### Analytics (/analytics)
- Progress bars with percentages
- Revenue analytics chart
- Sales distribution pie chart
- Performance metrics table

### Charts (/charts)
- Line chart with multiple series
- Grouped bar chart
- Area chart
- Donut chart

### Tables (/tables)
- Static table with actions
- Interactive data table with sorting and filtering
- Bordered table

### Forms (/forms)
- Basic form elements
- Advanced form elements (dropdowns, sliders, checkboxes, radio buttons)
- Input groups with icons and buttons

### Widgets (/widgets)
- Alerts (success, info, warning, danger)
- Badges
- Buttons (various colors and sizes)
- Progress bars (striped, animated)
- Cards
- Spinners
- Tooltips and popovers

## Color Scheme

- Primary Background: #152036
- Secondary Background: #1b2a47
- Accent Color: #24caa1
- Text Color: #ffffff
- Success: #24caa1
- Danger: #eb4b4b
- Info: #2eb7f3
- Warning: #f8ac59

## Customization

You can customize the theme by editing `assets/custom.css`. The CSS uses CSS variables for easy color customization.

## Technologies Used

- **Dash** - Python framework for building web applications
- **Dash Bootstrap Components** - Bootstrap components for Dash
- **Plotly** - Interactive charts and graphs
- **Pandas** - Data manipulation for tables

## License

MIT License - Based on the original Nalika template by Colorlib

## Credits

Original Nalika template: https://colorlib.com/polygon/nalika/
Converted to Dash Bootstrap Components
