# 🏥 Hospital Management System (HMS)

> A production-ready, learning-friendly Hospital Management System built with **Django REST Framework** (API), **React** (web), **PostgreSQL** (DB), **Celery + Redis** (tasks), and optional **AI/Analytics** modules for insights. Designed to help you learn end‑to‑end development, ship a real product, and showcase your skills.

<p align="center">
  <img alt="HMS" src="https://img.shields.io/badge/Django-4.2-green">
  <img alt="DRF" src="https://img.shields.io/badge/DRF-3.14-red">
  <img alt="React" src="https://img.shields.io/badge/React-18-blue">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-black">
</p>

---

## ✨ Highlights

* **Modular architecture**: Patients, Appointments, EMR, Billing, Pharmacy, Laboratory, Inventory, Staff & Roles, Messaging/Notifications, Reports.
* **Secure authentication**: JWT (access/refresh), role-based permissions, audit trails.
* **API-first**: Auto-generated OpenAPI/Swagger docs.
* **Scalable**: Async background jobs with Celery; containerized with Docker.
* **Analytics-ready**: Event logging, exports, and a `/analytics/` module (Pandas/Notebooks) for data analysis.
* **AI hook**: Optional prediction service (e.g., triage risk, no‑show probability) via a separate microservice.

---

## 🧱 Monorepo Structure

```
HMS/
├─ backend/                 # Django + DRF project
│  ├─ manage.py
│  ├─ core/                 # settings, urls, ASGI/WSGI, utils
│  ├─ apps/
│  │  ├─ accounts/          # users, roles, auth, audit
│  │  ├─ patients/          # demographics, contacts, kin
│  │  ├─ appointments/      # scheduling, calendars
│  │  ├─ emr/               # encounters, vitals, notes, orders
│  │  ├─ billing/           # invoices, payments, insurance claims
│  │  ├─ pharmacy/          # medications, dispensing, rx
│  │  ├─ lab/               # test orders, results   
│  │  └─ core/              # handle doctor, nurse amd labscientist profile
│  ├─ requirements.txt
│  └─ scripts/              # seed, backup, maintenance
│
│
├─ analytics/               # notebooks, datasets, ETL helpers
│  ├─ notebooks/
│  └─ etl/
│
├─ deploy/                  # docker compose, nginx, CI/CD, k8s manifests
│  ├─ docker/
│  └─ k8s/
│
├─ .env.example
├─ docker-compose.yml
├─ Makefile
└─ README.md
```

---

## 🔒 Roles & Permissions (Default)

* **Admin** – full access.
* **Doctor** – EMR + orders + results + limited billing.
* **Nurse** – vitals + notes + scheduling + limited EMR.
* **Cashier** – billing + payments.
* **Pharmacist** – pharmacy operations.
* **LabTech** – lab orders & results.
* **Reception** – patient registration + appointments.

> Permissions are enforced via DRF permissions and per‑object checks.

---

## 🚀 Quickstart

### 1) Prerequisites

* Python **3.10+**
* PostgreSQL **14+**
* Redis **6+** (for Celery)
* Docker (optional but recommended for prod/dev parity)

### 2) Clone & Environment

```bash
git clone https://github.com/yourusername/hms.git
cd hms
cp .env.example .env   # update values
```

### 3) Backend Setup

```bash
cd backend
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata initial_roles  # optional seed
python manage.py runserver
```

### 4) Celery & Redis (tasks)

```bash
# terminal A (Redis)
redis-server

# terminal B (Celery worker)
cd backend && source .venv/bin/activate
celery -A core worker -l info

# terminal C (Celery beat – scheduled jobs)
celery -A core beat -l info
```

### 5) With Docker (one command)

```bash
docker compose up --build
# backend: http://localhost:8000
# docs:    http://localhost:8000/api/docs/
```

---

## ⚙️ Configuration (.env)

| Key                    | Example                                   | Notes                 |
| ---------------------- | ----------------------------------------- | --------------------- |
| `DJANGO_SECRET_KEY`    | change-me-please                          | keep secret in prod   |
| `DJANGO_DEBUG`         | `True`                                    | `False` in prod       |
| `DATABASE_URL`         | `postgres://user:pass@localhost:5432/hms` | or individual DB vars |
| `REDIS_URL`            | `redis://localhost:6379/0`                | Celery broker/result  |
| `ALLOWED_HOSTS`        | `localhost,127.0.0.1`                     | comma‑separated       |
| `CORS_ALLOWED_ORIGINS` | `http://localhost:5173`                   | frontend origin       |
| `JWT_ACCESS_LIFETIME`  | `5`                                       | minutes               |
| `JWT_REFRESH_LIFETIME` | `1440`                                    | minutes (1 day)       |

---

## 🧪 Testing

```bash
cd backend && pytest --maxfail=1 --disable-warnings -q
# coverage
pytest --cov=apps --cov-report=term-missing

# frontend
cd ../frontend && pnpm test
```

---

## 📜 API Docs

* **OpenAPI**: `/api/schema/` (JSON)
* **Swagger UI**: `/api/schema/swagger-ui/`
* **ReDoc**: `/api/schema/redoc/`

> Generated via `drf-spectacular`.

---

## 📦 Backend Dependencies (excerpt)

```
Django==4.2.*
djangorestframework==3.14.*
drf-spectacular
psycopg2-binary
django-filter
djangorestframework-simplejwt
django-cors-headers
celery
redis
Pillow
python-dotenv
gunicorn
```

---

## 🔗 Core Endpoints

> See Swagger UI for the full, always‑up‑to‑date list.

---

---

## 🛡️ Security Checklist

* [x] Use **.env** + strong `DJANGO_SECRET_KEY`.
* [x] `DEBUG=False` in production.
* [x] HTTPS, HSTS, secure cookies, CSRF where applicable.
* [x] RBAC + per‑object permissions.
* [x] Input validation & serializer field whitelisting.
* [x] Rate limiting (e.g., DRF throttling / reverse proxy).
* [x] Audit logs for auth & critical actions.

---

## 📈 Analytics & AI (Optional Modules)

* **Analytics**: ETL scripts to warehouse (CSV/Parquet), notebooks for KPIs (utilization, wait times, revenue, stock levels).
* **AI**: A separate service (FastAPI/Flask) for predictions (e.g., no‑show, triage risk), consumed by the Django API.

---

## 🧰 Developer Experience

* **Makefile** shortcuts:

```Makefile
setup:            # create venv & install deps
	python -m venv .venv && . .venv/bin/activate && pip install -r backend/requirements.txt
run:              # run backend & frontend
	( cd backend && . ../.venv/bin/activate && python manage.py runserver ) & ( cd frontend && pnpm dev )
format:           # ruff/black + prettier
	ruff check --fix backend && black backend && cd frontend && pnpm format
```

* **Pre-commit** hooks (black, ruff, isort, prettier).
* **GitHub Actions**: CI for `lint`, `test`, `build`.

---

---

## 🤝 Contributing

1. Fork the repo & create a feature branch.
2. Write tests and docs.
3. Open a PR with a clear description and screenshots.

---

## 🗺️ Roadmap

* **Phase 1**: Auth, Patients, Appointments, EMR basics, Billing.
* **Phase 2**: Pharmacy, Lab, Inventory, Reports, Notifications.
* **Phase 3**: Multi‑facility support, Analytics, AI microservice, Mobile‑friendly UI.

---

## 📄 License

[MIT](LICENSE)

---

## 🙌 Acknowledgements

Built with ❤️ by learners & professionals who care about practical healthcare software.
