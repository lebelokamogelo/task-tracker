## Todo API

### Overview
Is a Django Rest Framework (DRF) API designed for simplifying user authentication and authorization.

### Features
- JWT-based authentication and authorization
- React App for CRUD Demonstration
- Docker containerization
- GraphQL support for Todo operations

### Getting Started
- Install: `pip install -r requirements.txt`
- Run your local development server: `python manage.py runserver`
- Build and run using Docker:
  ```bash
  docker compose up

### Usage

- Home Page: [/](http://localhost:8000/)
- List of Todos: [/api/todos/](http://localhost:8000/api/todos/)
- Individual Todo: [/api/todo/1/](http://localhost:8000/api/todo/<str:pk>)

### Authentication

- Obtain Token: [/api/token/](http://localhost:8000/api/token/)
- Refresh Token: [/api/token/refresh/](http://localhost:8000/api/token/refresh/)

### GraphQL

    GraphQL endpoint: http://localhost:8000/graphql/

#### Query for Todos:

    query {
      todos {
        id
        title
        description
        completed
        priority
      }
    }

#### Mutations:

    Create Todo:

    mutation {
      create(title: "New Todo", description: "Description", completed: false, priority: "High") {
        todo {
          id
          title
          description
          completed
          priority
        }
      }
    }

#### Update Todo:

    mutation {
      update(id: 1, title: "Updated Todo") {
        todo {
          id
          title
          description
          completed
          priority
        }
      }
    }

#### Delete Todo:

    mutation {
      delete(id: 1) {
        success
      }
    }

### Contributing

We welcome contributions.
### License

This project is licensed under the MIT License.