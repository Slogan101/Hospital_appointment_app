# 🏥 Hospital Appointment Booking App

A simple backend system for managing hospital appointments. It features user registration, doctor and patient profiles, appointment scheduling, and role-based access control — all powered by FastAPI, PostgreSQL, and JWT authentication.

---

## 🔧 Tech Stack

- **Backend:** FastAPI
- **Database:** PostgreSQL
- **Authentication:** JWT (JSON Web Tokens)
- **ORM:** SQLAlchemy

---

## 📌 Features

### 1. User Registration & Role Assignment

- A new user can register using just **email** and **password**.
- After registration, a user must choose a role to continue:
  - **Doctor**
  - **Patient**

Once a role is selected, they are automatically assigned the correct permissions and categorized accordingly.

---

### 2. Doctor & Patient Management

Each role has full CRUD access to manage their profile:

- **GET** - Retrieve your profile.
- **POST** - Create a profile.
- **PUT/PATCH** - Update your profile.
- **DELETE** - Delete your profile.

---

### 3. Appointment Booking System

- **POST /appointments**:  
  - Accessible only by patients.
  - Automatically finds and assigns the **next available doctor**.
  - Updates the doctor's availability to `false`.
  - Ensures appointments **don’t fall on weekends or outside work hours**.

- **GET /appointments**:  
  - Retrieve all booked appointments for both **patients** and **doctors**.

- **GET /appointments/available-dates**:  
  - View available appointment slots based on doctor availability.

---

### 4. Security

- JWT is used for secure authentication and authorization.
- Endpoints are protected based on user roles (doctor or patient).

---

## 🗄️ Database Schema Overview

- **Users**: Stores basic user credentials and login info.
- **Doctors**: Extended profile including availability.
- **Patients**: Patient profile and personal info.
- **Appointments**: Handles scheduling, timestamps, and doctor-patient assignments.

---

## 🚀 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/slogan101/Hospital_appointment_app.git
   cd Hospital_Appointment

2. **Create and activate virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Configure environment variables (.env):**
    ```bash
    DATABASE_URL=postgresql://user:password@localhost/db_name
    SECRET_KEY=your_jwt_secret
    ALGORITHM=HS256

5. **Start the app:**
    ```bash
    uvicorn main:app --reload

📫 **API Documentation**
Visit http://localhost:8000/docs to access the interactive Swagger UI for testing all available endpoints.



✍️ **Author**
Built with ❤️ by Slogan_codes.



