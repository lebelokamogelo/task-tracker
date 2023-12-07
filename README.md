## Task Tracker

### Overview
Is a Django Rest Framework (DRF) API designed for simplifying user authentication and authorization.

### Features
- JWT-based authentication and authorization
- ect

### Getting Started
- Install: `pip install -r requirements.txt`
- Run your local development server: `python manage.py runserver`
- Usage:
  - Home Page: [http://localhost:8000/](http://localhost:8000/)
  - List of Todos: [http://localhost:8000/api/todos/](http://localhost:8000/api/todos/)
  - Individual Todo: [http://localhost:8000/api/todo/1/](http://localhost:8000/api/todo/<str:pk>/)

### Authentication
- Obtain Token: [http://localhost:8000/api/token/](http://localhost:8000/api/token/)
- Refresh Token: [http://localhost:8000/api/token/refresh/](http://localhost:8000/api/token/refresh/)

### Contributing
We welcome contributions.

### License
This project is licensed under the MIT License.