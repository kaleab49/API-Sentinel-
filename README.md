# API Sentinel

API Sentinel is a full-stack web application designed to scan, analyze, and monitor RESTful APIs. It provides a user-friendly React frontend and a robust Django backend, enabling users to input API endpoints, configure headers, and receive detailed scan results.

---

## Features

- **API Scanning:** Submit API endpoints for automated scanning and analysis.
- **Custom Headers:** Add custom headers to your API requests.
- **Results Dashboard:** View scan results and potential issues in a clear interface.
- **Modern UI:** Built with React and Vite for fast, responsive user experience.
- **Secure Backend:** Django backend with SQLite database for data storage.

---

## Project Structure

```
backend/
  ├── api/                # Django app for API logic
  ├── backend/            # Django project settings
  ├── db.sqlite3          # SQLite database
  ├── manage.py           # Django management script
  └── requirements.txt    # Python dependencies

frontend/
  ├── public/             # Static assets
  ├── src/                # React source code
  ├── index.html          # HTML entry point
  ├── package.json        # Node dependencies and scripts
  └── vite.config.js      # Vite configuration
```

---

## Getting Started

### Backend (Django)

1. **Install dependencies:**

   ```sh
   cd backend
   python -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

2. **Run migrations:**

   ```sh
   python manage.py migrate
   ```

3. **Start the backend server:**
   ```sh
   python manage.py runserver
   ```

### Frontend (React + Vite)

1. **Install dependencies:**

   ```sh
   cd frontend
   npm install
   ```

2. **Start the frontend dev server:**

   ```sh
   npm run dev
   ```

3. **Access the app:**  
   Open [http://localhost:5173](http://localhost:5173) in your browser.

---

## Development Notes

- The frontend communicates with the backend via REST API endpoints.
- Update backend API URLs in the frontend as needed for deployment.
- Use environment variables for sensitive configuration.

---

## License

This project is licensed under the MIT
