# Talha Ijaz — Portfolio Website
**Student ID:** F2023266104 | **Course:** Web Technologies (Spring 2026)

A fully dynamic personal portfolio website built with **Django (MVT Architecture)**.

## 🏗️ Project Structure

```
portfolio/
├── bio/           # App: Bio model (name, title, description, image)
├── education/     # App: Education model (degree, institution, years)
├── skills/        # App: Skill model (name, category, proficiency %)
├── experience/    # App: Experience + Project models
├── templates/     # Base HTML template (index.html)
├── static/        # CSS, JS, Images
└── portfolio/     # Django project settings & URLs
```

## ⚙️ Setup & Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run migrations
python manage.py migrate

# 3. Seed data
python manage.py seed_portfolio

# 4. Run server
python manage.py runserver
```
Visit: http://localhost:8000

## 🚀 Deployment (Netlify)

```bash
# Export static site
python export_static.py

# Upload the dist/ folder to Netlify
# Set site name to: F2023266104
# Live URL: https://F2023266104.netlify.app
```

## 📋 Assessment Coverage

| Component | Implementation |
|---|---|
| Bio App | `bio/models.py` → `Bio` model |
| Education App | `education/models.py` → `Education` model |
| Skills App | `skills/models.py` → `Skill` model |
| Experience/Projects App | `experience/models.py` → `Experience`, `Project` models |
| UI | Classic Professional, responsive, animated skill bars |
| Deployment | Netlify static export via `export_static.py` |
