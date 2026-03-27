# Quick Start Guide

## Installation Steps

1. Navigate to the project directory:
```bash
cd /Users/osakpolor.omonbude/Documents/DASH\ -\ COLORIB/kiaalap/dash-kiaalap
```

2. Create and activate a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

Or use the startup script:
```bash
./start.sh
```

5. Open your browser and navigate to:
```
http://localhost:8050
```

## Project Overview

This Dash application replicates all pages and design from the original Kiaalap template:

### ✅ Completed Features:
- **Main Dashboard** with charts and statistics
- **Sidebar Navigation** with all menu sections
- **Header** with search, notifications, and user menu
- **Footer** component
- **50+ Pages** including:
  - Dashboard variants
  - Student management (list, add, edit, profile)
  - Professor management (list, add, edit, profile)
  - Course management (list, add, edit, info, payment)
  - Library assets management
  - Departments management
  - Mailbox system
  - UI Components (buttons, alerts, modals, accordion)
  - Forms (basic, advanced)
  - Charts (line, area, bar)
  - Tables (static, data tables)
  - Authentication pages (login, register, lock, password recovery)
  - Error pages (404, 500)

### Design Replication:
- ✅ Same color scheme (#1e293b sidebar, #6366f1 primary)
- ✅ Same layout structure (260px sidebar, 60px header)
- ✅ Same typography and spacing
- ✅ Same card styles and shadows
- ✅ Responsive design (mobile-friendly)
- ✅ Bootstrap Icons integration
- ✅ Interactive charts with Plotly

## Customization

### Change Colors:
Edit `assets/dashboard.css` and modify the CSS variables:
```css
:root {
    --sidebar-bg: #1e293b;
    --body-bg: #f5f7fa;
    --border-color: #e5e7eb;
}
```

### Add New Pages:
1. Create a new file in `pages/` directory
2. Define the layout using Dash components
3. Add the route in `app.py`

### Modify Sidebar:
Edit `layouts/sidebar.py` to add/remove menu items

## Troubleshooting

**Port already in use:**
```bash
python app.py --port 8051
```

**Dependencies not installing:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Module not found errors:**
Make sure you're in the correct directory and virtual environment is activated.
