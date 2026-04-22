# 📘 Logbook360

Logbook360 is a multi-school SIWES (Student Industrial Work Experience Scheme) management system that digitizes student logbooks, supervisor reviews, and institutional tracking of industrial training activities.

It replaces traditional paper logbooks with a structured digital system for students, supervisors, and school administrators.

---

## 🚀 Project Overview

Logbook360 enables institutions to:

- Register and manage SIWES programs
- Assign students to supervisors
- Track daily student activities
- Provide structured weekly and monthly reviews
- Generate final SIWES reports

---

## 🧠 Key Features (MVP)

### 🏫 Multi-School Support
Each school operates independently within the system.

### 👨‍💼 Admin Features
- Register school
- Create students and supervisors
- Assign students to supervisors
- Manage SIWES sessions

### 👨‍🎓 Student Features
- Submit daily log entries (Mon–Sat)
- View supervisor feedback
- Submit monthly summaries
- Download final reports

### 👨‍🏫 Supervisor Features
- Review student logs
- Approve/reject entries
- Provide weekly feedback
- Evaluate monthly performance

---

## 🏗️ System Architecture

Logbook360 follows a structured SIWES workflow:

School
  ↓
SIWESSession
  ↓
LogBook
  ↓
DailyLog
  ↓
WeeklyReview
  ↓
MonthlyReview

---

## 🧱 Core Models

- User (role-based authentication)
- School
- Department
- StudentProfile
- SupervisorProfile
- SIWESSession
- LogBook
- DailyLog
- WeeklyReview
- MonthlyReview

---

## ⚙️ Tech Stack

- Backend: Django
- API Layer: Django Ninja
- Database: PostgreSQL (production) / SQLite (development)
- Authentication: JWT
- Deployment: Render (free tier)

---

## 📦 Installation (Development Setup)

git clone [Logbook360](https://github.com/NUCCASJNR/logbook360.git)
cd logbook360
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

---

## 🔐 Authentication

- ADMIN → Manages school system
- SUPERVISOR → Reviews student logs
- STUDENT → Submits daily logs

---

## 📊 Workflow Summary

1. School registers on platform  
2. Admin creates users  
3. Students assigned to supervisors  
4. Students submit daily logs  
5. Supervisors review logs  
6. Weekly/monthly reports generated  
7. Final SIWES report exported  

---

## 🚧 Project Status

- Core models: Completed  
- Authentication: In progress  
- API endpoints: Pending  
- Frontend: Not started  
- Deployment: Pending  

---

## 🔮 Future Improvements

- AI-assisted log generation  
- Voice-to-text logging  
- Notifications  
- Analytics dashboard  
- Mobile app  

---

## 👨‍💻 Author

Al-Areef — Backend Developer (Django & APIs)

---

## 📄 License

Educational / Portfolio Project
