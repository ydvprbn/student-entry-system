# Student Entry System Project

This project includes essential features such as CRUD operations and API development built using Django and DRF, a high-level Python web framework.

## Setup Instructions

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git@github.com:ydvprbn/student-entry-system.git
   cd student_entry_system
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```
3. **Activate the virtual environment:**

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply database migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin):**

   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server:**

   ```bash
   python manage.py runserver
   ```
   
8. **Open your web browser and navigate to following URL adresss to access DRF interactive browsable API**
   ```
   http://127.0.0.1:8000/api/student/
   ```
   **Perform Different HTTP Methods**
    > GET (Retrieve a list of students):
      - GET: /api/student/
      - Click the GET button and retrieve a list of students
       :
    > POST (Create a new student):
      - POST: /api/student/
      - Enter student details in the form, then "POST"
      :
    > PUT (Update an existing student):
      - PUT: /api/student/{id}/
      - Change the values and select "PUT"
      :
    > DELETE (Remove a student):
      - DELETE: /api/student/{id}/
      - Click "DELETE"
       
8. **Open your web browser and navigate to following URL adresss to access Admin Panel:**
   ```
   http://127.0.0.1:8000/admin/
   ```   
