# Dash Admin Dashboards

A growing collection of open-source admin dashboard templates, reimagined and rebuilt in **Plotly Dash** with Python. New dashboards are added **weekly**.

## What This Is

Popular HTML/Bootstrap admin templates from across the web — rebuilt as fully interactive, production-ready **Dash applications**. Each dashboard preserves the original design while replacing static HTML with dynamic Python/Dash components, Plotly charts, and real callback interactivity.

---

## Dashboards

| Dashboard | Theme | Specialty | Port | View |
|-----------|-------|-----------|------|------|
| [Adminator](dash-admin-dashboard/) | Light / Modern | General admin | 8051 | [Live](https://09143eb7-503a-475d-8ca4-a2477c8cdce0.plotly.app/) |
| [Nalika](#nalika) | Dark / Professional | Analytics-focused | 8050 | — |
| [Bootstrap Admin Template](#bootstrap-admin-template) | Light / Clean | E-commerce management | 8000 | — |
| [Kiaalap](#kiaalap) | Light / Indigo | Education management | 8050 | — |

## Screenshots

### Adminator
![Adminator Dashboard](screenshots/adminator.png)

### Nalika
![Nalika Dashboard](screenshots/nalika.png)

### Bootstrap Admin Template
![Bootstrap Admin Template](screenshots/bootstrap-admin-template.png)

### Kiaalap
![Kiaalap Dashboard](screenshots/kiaalap.png)

---

## Dashboards in Detail

### Adminator
> Based on the [Adminator](https://github.com/puikinsh/Adminator-admin-dashboard) HTML template

A clean, modern general-purpose admin dashboard with 18 fully built pages.

**Live Demo:** https://09143eb7-503a-475d-8ca4-a2477c8cdce0.plotly.app/

**Pages:** Dashboard · Email · Compose · Chat · Calendar · Charts · Basic Tables · Data Tables · Forms · UI Elements · Google Maps · Vector Maps · Sign In · Sign Up · 404 · 500 · Blank

```bash
cd dash-admin-dashboard
pip install -r requirements.txt
python app.py
# → http://localhost:8051
```

---

### Nalika
> Based on the Nalika Bootstrap admin template

A dark-themed dashboard with a teal accent palette, suited for professional or corporate environments.

**Pages:** Dashboard · Analytics · Charts · Tables · Forms · Widgets · Mailbox · Cards · Profile · Buttons · Modals · Progress · Notifications · Calendar · Tabs & Accordions · Maps · Login

**Color palette:** `#152036` background · `#24caa1` accent · `#eb4b4b` danger

```bash
cd nalika-dash
pip install -r requirements.txt
python app.py
# → http://localhost:8050
```

---

### Bootstrap Admin Template
> Based on the Colorlib Bootstrap admin template

An e-commerce-focused admin dashboard with modules for managing the full lifecycle of an online store.

**Pages:** Dashboard · Orders · Products · Users · Sellers · Payments · Reviews · Messages · Files · Calendar · Geo Location · Security · Settings · Help & Support

```bash
cd Dash-Bootstrap-Admin-Template
pip install -r requirements.txt
python app.py
# → http://localhost:8000
```

---

### Kiaalap
> Based on the Kiaalap Bootstrap admin template

The most comprehensive dashboard in the collection — an education management system with 50+ pages covering academic, administrative, and developer tooling needs.

**Page categories:**
- **Academic** — Students, Professors, Courses, Library, Departments (full CRUD: list · add · edit · profile/info)
- **Communication** — Mailbox, Compose, View
- **UI Components** — Buttons, Alerts, Modals, Accordion, Forms (basic & advanced), Password Meter, Image Cropper, Multi-upload
- **Charts** — Line, Area, Bar (via Plotly)
- **Tables** — Static & interactive data tables
- **Maps** — Google Maps, Data Maps
- **Auth** — Login, Register, Lock, Password Recovery, 404, 500
- **Developer Tools** — Code Editor, PDF Viewer, Tree View, Preloader, Notifications

**Color palette:** `#6366f1` primary (indigo) · `#1e293b` sidebar · `#f5f7fa` background

```bash
cd dash-kiaalap
pip install -r requirements.txt
python app.py
# → http://localhost:8050
```

---

## Tech Stack

All dashboards are built on the same core stack:

| Package | Purpose |
|---------|---------|
| `dash` | Web framework & routing |
| `dash-bootstrap-components` | Bootstrap 5 UI components |
| `plotly` | Interactive charts |
| `pandas` | Data handling |

Some dashboards use additional packages (e.g. `dash-ag-grid` for advanced data tables).

---

## Getting Started

**Prerequisites:** Python 3.8+

```bash
# Clone the repo
git clone https://github.com/your-username/dash-admin-dashboards.git
cd dash-admin-dashboards

# Pick a dashboard, install its dependencies, and run it
cd dash-kiaalap
pip install -r requirements.txt
python app.py
```

Each dashboard is self-contained with its own `requirements.txt` and can be run independently.

---

## Roadmap

- [x] Adminator Admin Dashboard
- [x] Nalika Dark Admin Dashboard
- [x] Bootstrap Admin Template (E-commerce)
- [x] Kiaalap Education Management Dashboard
- [ ] New dashboard — coming this week

Dashboards are added weekly. Watch or star the repo to get notified.

---

## Contributing

Contributions are welcome. If you've rebuilt an admin template in Dash and want it included:

1. Fork the repo.
2. Add your dashboard in its own directory with a `requirements.txt` and basic `README.md` for the repo.
3. Open a pull request.

Please keep each dashboard self-contained and runnable with `python app.py`.

---

## Support

If this project has been useful to you, consider buying me a coffee — it helps keep new dashboards coming every week!

[![Donate via PayPal](https://img.shields.io/badge/Donate-PayPal-0070ba?logo=paypal&logoColor=white)](https://www.paypal.com/paypalme/omonbudeemma)

---

## License

Each dashboard is a reimplementation of an open-source template. Original template licenses apply to the design assets. The Dash Python code in this repo is released under the [MIT License](LICENSE).
