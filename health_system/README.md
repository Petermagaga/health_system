# Health Information System 🚑

A simple Django-based health information system to manage clients and their enrollment into health programs.

## Features

- 📋 Create Health Programs (e.g., TB, Malaria, HIV)
- 👤 Register new Clients
- ➡️ Enroll Clients into one or more Programs
- 🔎 Search for Clients
- 📄 View a Client's Profile with enrolled Programs
- 🌍 Expose Client Profile via RESTful API
- 🔒 (Optional) Secure APIs with Token Authentication

## API Endpoints

| Endpoint | Method | Description |
|:---|:---|:---|
| `/api/programs/` | POST, GET | Create or list health programs |
| `/api/clients/` | POST, GET | Register or search clients |
| `/api/enrollments/` | POST, GET | Enroll clients into programs |
| `/api/clients/<id>/profile/` | GET | Retrieve client profile with programs |

## Installation

1. Clone the repository:

```bash
git clone https://github.com/petermagaga/health_system.git
cd health_system
