# CareerBridge | جسر المسار

A bilingual Arabic/English Django platform for connecting learners with mentorship and early-career opportunities.

## Run locally

```powershell
.\.venv\Scripts\Activate.ps1
python manage.py runserver
```

Then open http://127.0.0.1:8000/ar/ . Use the language switcher to view English.

## Included

- Arabic RTL and English LTR interface
- Searchable, filterable opportunity catalog with 30 presentation-ready demo roles
- Opportunity detail pages and a guided application flow
- Personal dashboard for tracking submitted applications
- Django language middleware and language selector
- Admin workspace for opportunities, profiles, and applications
- Responsive Bootstrap-based UI with accessible focus states and reduced-motion support

## Demo data

Populate the catalog with realistic demo opportunities:

```powershell
python seed_demo.py
```

## Admin

Create a superuser locally, then open `/ar/admin/`:

```powershell
python manage.py createsuperuser
```

Do not commit local database files, virtual environments, or credentials.
