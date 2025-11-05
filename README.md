## ⚙️ Backend

### 📘 Project Description  
**Bookstop** is a **Single Page Application (SPA)** platform designed to help users discover bookstores, explore local events, and share reviews in an engaging and multilingual environment.  

The platform provides a seamless experience by combining a **React frontend** with a **Django REST Framework (DRF) backend**, ensuring fast navigation and real-time interaction between users and bookstores.  

---

### 🗂️ Repository Description  
**Bookstop Backend** serves as the **server-side application** for the Bookstop platform.  
It manages the database, authentication, and core business logic, and exposes **secure RESTful APIs** consumed by the React frontend.  

**Key Features:**  
- Manage bookstores, events, reviews, and users  
- Support multilingual data  
- Enable smooth API communication with the SPA frontend  


---

### ❄️ IceBox Features

- 🧠 **Recommendation System:** Suggest bookstores or events to users based on preferences and reviews.  
- 🌍 **Multi-language API Support:** Return localized content automatically based on user language.   

---

### 🛠️ Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/Django%20REST%20Framework-ff1709?style=for-the-badge&logo=django&logoColor=white" alt="Django REST Framework" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white" alt="Gunicorn" />
  <img src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white" alt="nginx" />
</p>


<h1>Bookstore</h1>
<table border="1" width="100%">
    <thead>
        <tr>
            <th width="15%">Entity</th>
            <th width="25%">HTTP Method</th>
            <th width="50%">Endpoint</th>
            <th width="10%">Payload Required?</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Bookstore</td><td>GET</td><td>/bookstore</td><td>No</td></tr>
        <tr><td>Bookstore</td><td>GET</td><td>/bookstore/:id</td><td>No</td></tr>
        <tr><td>Bookstore</td><td>POST</td><td>/bookstore</td><td>Yes</td></tr>
        <tr><td>Bookstore</td><td>PUT</td><td>/bookstore/:id</td><td>Yes</td></tr>
        <tr><td>Bookstore</td><td>DELETE</td><td>/bookstore/:id</td><td>No</td></tr>
    </tbody>
</table>

<!-- Review -->
<h1>Review</h1>
<table border="1" width="100%">
  <thead>
    <tr>
      <th width="15%">Entity</th>
      <th width="25%">HTTP Method</th>
      <th width="50%">Endpoint</th>
      <th width="10%">Payload Required?</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Review</td><td>GET</td><td>/bookstores/:bookstore_id/reviews/</td><td>No</td></tr>
    <tr><td>Review</td><td>POST</td><td>/bookstores/:bookstore_id/reviews/</td><td>Yes</td></tr>
    <tr><td>Review</td><td>GET</td><td>/reviews/:review_id/</td><td>No</td></tr>
    <tr><td>Review</td><td>PUT</td><td>/reviews/:review_id/</td><td>Yes</td></tr>
    <tr><td>Review</td><td>DELETE</td><td>/reviews/:review_id/</td><td>No</td></tr>
  </tbody>
</table>

<!-- Event -->
<h1>Event</h1>
<table border="1" width="100%">
  <thead>
    <tr>
      <th width="15%">Entity</th>
      <th width="25%">HTTP Method</th>
      <th width="50%">Endpoint</th>
      <th width="10%">Payload Required?</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Event</td><td>GET</td><td>/events/</td><td>No</td></tr>
    <tr><td>Event</td><td>POST</td><td>/events/</td><td>Yes</td></tr>
    <tr><td>Event</td><td>GET</td><td>/events/:event_id/</td><td>No</td></tr>
    <tr><td>Event</td><td>PUT</td><td>/events/:event_id/</td><td>Yes</td></tr>
    <tr><td>Event</td><td>DELETE</td><td>/events/:event_id/</td><td>No</td></tr>
    <tr><td>Event</td><td>GET</td><td>/bookstores/:bookstore_id/events/</td><td>No</td></tr>
  </tbody>
</table>


<!-- Associate Bookstores to Events -->
<h1>Associate Bookstores to Events</h1>
<table border="1" width="100%">
    <thead>
        <tr>
            <th width="15%">Entity</th>
            <th width="25%">HTTP Method</th>
            <th width="50%">Endpoint</th>
            <th width="10%">Payload Required?</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Bookstores</td><td>PUT</td><td>/bookstores/:id/events/:event_id</td><td>Yes</td></tr>
        <tr><td>Bookstores</td><td>DELETE</td><td>/bookstores/:id/events/:event_id</td><td>No</td></tr>


</table>


<!-- Associate Bookstores to Reviews -->
<h1>Associate Bookstores to Reviews</h1>
<table border="1" width="100%">
    <thead>
        <tr>
            <th width="15%">Entity</th>
            <th width="25%">HTTP Method</th>
            <th width="50%">Endpoint</th>
            <th width="10%">Payload Required?</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Bookstores</td><td>PUT</td><td>/bookstores/:id/reviews/:review_id</td><td>Yes</td></tr>
        <tr><td>Bookstores</td><td>DELETE</td><td>/bookstores/:id/reviews/:review_id</td><td>No</td></tr>
    </tbody>
</table>

<!-- User -->
<h1>User</h1>
<table border="1" width="100%">
  <thead>
    <tr>
      <th width="15%">Entity</th>
      <th width="25%">HTTP Method</th>
      <th width="50%">Endpoint</th>
      <th width="10%">Payload Required?</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>User</td><td>POST</td><td>/users/signup/</td><td>Yes</td></tr>
    <tr><td>User</td><td>POST</td><td>/users/login/</td><td>Yes</td></tr>
    <tr><td>User</td><td>POST</td><td>/users/token/refresh/</td><td>Yes</td></tr>
  </tbody>
</table>

  


---

### 🔗 Frontend Repository
👉 [Bookstop Frontend Repository](https://github.com/Worood11/CapstoneProject_frontend)

---

### 🌐 API Base URL
👉 `http://127.0.0.1:8000`  


---

### ⚙️ Installation Instructions

#### 🐳 Option 1 — Run with Docker
```bash
# Clone the repository
git clone https://github.com/Worood11/CapstoneProject_backend.git
cd CapstoneProject_backend

# Build the Docker image
docker build -t bookstop-backend .

# Run the container
docker run -p 8000:8000 bookstop-backend
```

### 💻 Option 2 — Run without Docker
```bash
# Clone the repository
git clone https://github.com/Worood11/CapstoneProject_backend.git
cd CapstoneProject_backend

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```