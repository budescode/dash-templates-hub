# Quick Start Guide - Adminator Dash Dashboard

Get the admin dashboard up and running in 5 minutes!

## Prerequisites
- Python 3.8+
- pip (comes with Python)

## Installation & Startup

### Step 1: Navigate to Project
```bash
cd dash-admin
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate
# On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the App
```bash
python index.py
```

### Step 5: Open Browser
Visit: **http://localhost:8050**

---

## 🎯 What's Included

| Feature | Location |
|---------|----------|
| Dashboard with Charts | Home page `/` |
| Data Tables | `/tables/basic` `/tables/data` |
| Email Interface | `/email` `/compose` |
| Chat | `/chat` |
| Calendar | `/calendar` |
| Form Examples | `/forms` |
| UI Components | `/ui` |
| Authentication Pages | `/pages/signin` `/pages/signup` |
| Error Pages | `/pages/404` `/pages/500` |

---

## 📁 Project Structure

```
dash-admin/
├── app/
│   ├── app.py              # Main application with routing
│   ├── components/
│   │   └── layout.py       # Header component
│   └── pages/
│       ├── dashboard.py    # Home page
│       ├── tables.py       # Table pages
│       ├── charts.py       # Charts
│       ├── forms.py        # Forms
│       ├── ui_elements.py  # UI Components
│       ├── email_chat.py   # Email, chat pages
│       ├── other_pages.py  # Calendar, errors, etc
│       └── maps.py         # Maps pages
├── assets/
│   └── style.css           # Custom styling
├── index.py                # Entry point
├── requirements.txt        # Dependencies
└── README.md               # Full documentation
```

---

## 🎨 Customization

### Change Colors
Edit `assets/style.css`:
```css
:root {
  --bs-primary: #2196F3;      /* Change this */
  --bs-success: #4CAF50;
  --bs-danger: #F44336;
}
```

### Add New Page
1. Create function in `app/pages/new_page.py`
2. Import in `app/app.py`
3. Add to routing in `display_page()` function
4. Add menu item to `update_sidebar_menu()` function

### Change Navigation
Edit menu in `app/app.py` (line ~120):
```python
menu_items = [
    {"href": "/", "label": "Dashboard", "icon": "ti-home", ...},
    # Add more items here
]
```

---

## 🚀 Deployment

### Local Server
```bash
python index.py
```

### Production with Gunicorn
```bash
# Install
pip install gunicorn

# Run
gunicorn --workers 4 wsgi:app.server
```

### Docker
```bash
docker build -t adminator .
docker run -p 8050:8050 adminator
```

### Heroku
```bash
heroku create your-app-name
git push heroku main
heroku open
```

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change port in index.py or use:
python -c "from app.app import app; app.run_server(port=8051)"
```

### Import Errors
```bash
# Reinstall packages
pip install -r requirements.txt --force-reinstall
```

### No Styling
```bash
# Clear cache and restart
# Ctrl+Shift+Delete to clear browser cache
# Then restart: python index.py
```

---

## 📚 Learn More

- **Dash Tutorial**: https://dash.plotly.com/
- **Bootstrap Components**: https://dash-bootstrap-components.opensource.faculty.ai/
- **Plotly Charts**: https://plotly.com/python/
- **Themify Icons**: https://themify.me/themify-icons

---

## 💡 Tips

✅ Use `debug=True` (default) for development  
✅ Use `debug=False` for production  
✅ Modify sample data in page functions  
✅ Bootstrap CSS classes work out of the box  
✅ Check browser console for JavaScript errors  

---

## 🤝 Contributing

Want to improve the dashboard? 
1. Make your changes
2. Test thoroughly
3. Submit a pull request

---

## 📝 License

Open source - use and modify as needed!

---

**Happy Coding! 🎉**

For more help, check the full [README.md](README.md)
