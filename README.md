# Collabo - Full-Stack Project

Collabo is a collaborative platform designed to streamline project management and team communication. It provides tools for managing user profiles, projects, notifications, and messaging, all within an integrated and user-friendly environment. The project consists of a frontend built with React and a backend powered by Python. The application follows best practices for single-page applications (SPA) and RESTful APIs.

## Table of Contents

-   Frontend
    
-   Backend
    
-   File Structure
    
-   Features
    
-   Contributing
    

## Frontend

### Installation

1.  Navigate to the frontend folder:
    
    ```
    cd frontend
    ```
    
2.  Install dependencies:
    
    ```
    npm install
    ```
    

### Usage

1.  Start the development server:
    
    ```
    npm start
    ```
    
2.  Open your browser and navigate to:
    
    ```
    http://localhost:3000
    ```
    

## Backend

### Installation

1.  Navigate to the backend folder:
    
    ```
    cd backend
    ```
    
2.  Install Python dependencies:
    
    ```
    pip install -r requirements.txt
    ```
    
3.  Set up environment variables:
    
    -   Create a `.env` file in the `backend/backend/` directory.
        
    -   Add the required variables (refer to `config.py` for expected values).
        

### Usage

1.  Start the backend server:
    
    ```
    python backend/app/main.py
    ```
    

## File Structure

### Frontend

```
frontend/
├── public/
│   ├── index.html
│   ├── favicon.ico
│   └── assets/
├── src/
│   ├── components/
│   │   ├── Layout/
│   │   ├── Navbar/
│   │   └── Footer/
│   ├── pages/
│   │   ├── home/
│   │   ├── login/
│   │   ├── profile/
│   │   └── projectdetails/
│   ├── assets/
│   │   ├── styles/
│   │   └── images/
│   ├── App.js
│   ├── index.js
│   └── utilities/
│       ├── api.js
│       └── constants.js
└── package.json
```

### Backend

```
backend/
    backend/
        .env
        install_py_req.sh
        requirements.txt
        app/
            config.py
            db.py
            main.py
            __init__.py
            auth/
                jwt_handler.py
                password_utils.py
            models/
                messages.py
                notifications.py
                project.py
                user.py
                __init__.py
            routes/
                auth.py
                messages.py
                notifications.py
                projects.py
                users.py
                __init__.py
            schemas/
                messages.py
                notifications.py
                project.py
                user.py
                __init__.py
            services/
                auth_service.py
                messaging_service.py
                notification_servce.py
                project_service.py
                __init__.py
            utils/
                __init__.py
        tests/
            test_auth.py
            test_projects.py
```

## Features

-   **Frontend**:
    
    -   React Router for SPA navigation.
        
    -   Shared layout with Navbar and Footer.
        
    -   Modular design with reusable components.
        
-   **Backend**:
    
    -   RESTful API built with Python.
        
    -   Modular architecture with clearly defined models, routes, and services.
        
    -   JWT-based authentication.
        

## Contributing

1.  Fork the repository.
    
2.  Create a new branch for your feature or fix:
    
    ```
    git checkout -b feature/your-feature-name
    ```
    
3.  Commit your changes:
    
    ```
    git commit -m "Add your message here"
    ```
    
4.  Push to your branch:
    
    ```
    git push origin feature/your-feature-name
    ```
    
5.  Open a pull request.
