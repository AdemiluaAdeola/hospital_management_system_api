# 🏥 Hospital Management System API

A Django REST Framework–based Hospital Management System for managing doctors, nurses, patients, laboratory tests, and invoices.  
This API is built with scalability in mind, supporting single-hospital setups, but can be extended for multi-hospital use.

---

## 🚀 Features

- **User Groups & Permissions** – Doctors, Nurses, Lab Technicians, and Admins with role-based access.
- **Patient Management** – Register, update, and view patient records.
- **Doctor Management** – Add doctors and assign them to patients.
- **Lab Requests** – Doctors can request lab tests for patients.
- **Test Results** – Lab staff can upload and update test results.
- **Invoices & Billing** – Create and manage invoices with itemized billing.
- **Authentication** – JWT-based authentication for secure API access.

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL (recommended), SQLite (for development)
- **Auth:** JWT via `djangorestframework-simplejwt`
- **Serialization:** DRF Serializers
- **Permissions:** Custom role-based permissions

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/hospital-management-system.git
   cd hospital-management-system
