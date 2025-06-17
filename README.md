# Pizza Restaurant API

A modern RESTful API for a Pizza Restaurant application built with Flask and SQLAlchemy, following best practices with the application factory pattern and proper project structure.

##  Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [API Endpoints](#api-endpoints)
- [Usage Examples](#usage-examples)
- [Development](#development)
- [Contributing](#contributing)

##  Project Overview

This Pizza Restaurant API provides a complete backend solution for managing restaurants, pizzas, and their relationships. Built with modern Python web development practices, it offers a scalable and maintainable codebase perfect for production deployment.

### Features

- RESTful API design
- SQLAlchemy ORM with Flask-Migrate
- Application factory pattern
- Database seeding functionality
- Input validation and error handling
- Clean project structure

##  Project Structure

```
Pizza-Restaurants/
├── Server/                 # Main application package
│   ├── models/            # SQLAlchemy data models
│   ├── app.py            # Flask application factory and routes
│   └── seed.py           # Database seeding script
├── migrations/           # Database migration scripts
├── Pipfile              # Project dependencies (pipenv)
├── Pipfile.lock         # Locked dependency versions
└── README.md           # Project documentation
```

##  Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8+
- pipenv (for dependency management)
- Git (for version control)

##  Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/DedanKIarie/Pizza-Restaurants
cd Pizza-Restaurants
```

### 2. Create Virtual Environment and Install Dependencies

This project uses `pipenv` for clean dependency management:

```bash
# Install all required packages from Pipfile
pipenv install

# Activate the virtual environment
pipenv shell
```

### 3. Database Setup

Run these commands from the root directory (`Pizza-Restaurants/`) to set up your database:

> **Important:** Your application directory is named `Server` (with a capital 'S'). Commands are case-sensitive.

```bash
# Set the FLASK_APP environment variable
export FLASK_APP="Server.app:create_app"

# Initialize migrations (run only once)
flask db init

# Generate initial migration script
flask db migrate -m "Create initial tables"

# Apply migrations to create database tables
flask db upgrade
```

### 4. Seed the Database

Populate your database with sample data:

```bash
python -m Server.seed
```

### 5. Start the Development Server

```bash
flask run
```

 **Your API is now running at:** `http://127.0.0.1:5000`

## API Endpoints

### Restaurants

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/restaurants` | Get all restaurants |
| `GET` | `/restaurants/<id>` | Get restaurant details with pizzas |
| `DELETE` | `/restaurants/<id>` | Delete a restaurant |

### Pizzas

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/pizzas` | Get all available pizzas |

### Restaurant Pizzas

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/restaurant_pizzas` | Create restaurant-pizza association |

#### POST `/restaurant_pizzas` Request Body

```json
{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 1
}
```

**Validation Rules:**
- `price`: Integer between 1 and 30
- `pizza_id`: Must reference existing pizza
- `restaurant_id`: Must reference existing restaurant

##  Usage Examples

### Get All Restaurants

```bash
curl -X GET http://127.0.0.1:5000/restaurants
```

### Get Restaurant Details

```bash
curl -X GET http://127.0.0.1:5000/restaurants/1
```

### Create Restaurant-Pizza Association

```bash
curl -X POST http://127.0.0.1:5000/restaurant_pizzas \
  -H "Content-Type: application/json" \
  -d '{
    "price": 12,
    "pizza_id": 1,
    "restaurant_id": 1
  }'
```

### Delete Restaurant

```bash
curl -X DELETE http://127.0.0.1:5000/restaurants/1
```

## Development

### Running Tests

```bash
# Add your test commands here
python -m pytest
```

### Database Migrations

When you make changes to your models:

```bash
# Generate migration
flask db migrate -m "Description of changes"

# Apply migration
flask db upgrade
```

### Code Style

This project follows PEP 8 guidelines. Consider using:

```bash
# Format code
black .

# Lint code
flake8 .
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) page
2. Create a new issue with detailed description
3. Include error messages and steps to reproduce

---

<div align="center">
  <strong>Built with ❤️ using Flask and SQLAlchemy</strong>
</div>