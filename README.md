# 🚀 Streamlit + FastAPI Production Template

A production-ready, scalable template for building modern web applications with Streamlit frontend and FastAPI backend. This template follows industry best practices, clean architecture principles, and provides a solid foundation for your next project.

## 🌟 Features

- **Modern Stack**: Streamlit + FastAPI + UV package manager
- **Clean Architecture**: Domain-driven design with clear separation of concerns
- **Type Safety**: Full type annotations with Pydantic models
- **Testing**: Comprehensive test suite with pytest
- **Code Quality**: Pre-commit hooks, linting, and formatting
- **Documentation**: Auto-generated API docs and comprehensive guides
- **Containerization**: Docker support with multi-stage builds
- **CI/CD Ready**: GitHub Actions workflows
- **Monitoring**: Health checks and logging
- **Security**: Authentication, CORS, and security headers

## 📁 Project Structure

```
streamlit-fastapi-template/
├── README.md                   # This file
├── pyproject.toml             # Project configuration and dependencies
├── uv.lock                    # Lock file for reproducible builds
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
├── .pre-commit-config.yaml    # Pre-commit hooks configuration
├── docker-compose.yml         # Docker compose for local development
├── Dockerfile                 # Multi-stage Docker build
├── Makefile                   # Common development tasks
│
├── app/                       # Main application package
│   ├── __init__.py
│   ├── main.py               # FastAPI application entry point
│   ├── config.py             # Application configuration
│   ├── dependencies.py       # FastAPI dependencies
│   │
│   ├── api/                  # API layer
│   │   ├── __init__.py
│   │   ├── routes/           # API routes
│   │   │   ├── __init__.py
│   │   │   ├── health.py
│   │   │   ├── users.py
│   │   │   └── items.py
│   │   └── middleware.py     # Custom middleware
│   │
│   ├── core/                 # Core business logic
│   │   ├── __init__.py
│   │   ├── models/           # Pydantic models
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── user.py
│   │   │   └── item.py
│   │   ├── services/         # Business logic services
│   │   │   ├── __init__.py
│   │   │   ├── user_service.py
│   │   │   └── item_service.py
│   │   └── exceptions.py     # Custom exceptions
│   │
│   ├── database/             # Database layer
│   │   ├── __init__.py
│   │   ├── connection.py     # Database connection
│   │   ├── repositories/     # Data access layer
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── user_repository.py
│   │   │   └── item_repository.py
│   │   └── migrations/       # Database migrations
│   │       └── __init__.py
│   │
│   └── utils/                # Utility functions
│       ├── __init__.py
│       ├── logger.py         # Logging configuration
│       ├── security.py       # Security utilities
│       └── helpers.py        # General helpers
│
├── frontend/                 # Streamlit frontend
│   ├── __init__.py
│   ├── main.py              # Streamlit app entry point
│   ├── config.py            # Frontend configuration
│   │
│   ├── components/          # Reusable UI components
│   │   ├── __init__.py
│   │   ├── sidebar.py
│   │   ├── header.py
│   │   └── charts.py
│   │
│   ├── pages/               # Streamlit pages
│   │   ├── __init__.py
│   │   ├── 1_📊_Dashboard.py
│   │   ├── 2_👤_Users.py
│   │   └── 3_📦_Items.py
│   │
│   ├── services/            # Frontend services (API clients)
│   │   ├── __init__.py
│   │   ├── api_client.py
│   │   └── auth_service.py
│   │
│   └── utils/               # Frontend utilities
│       ├── __init__.py
│       ├── session.py       # Session management
│       └── validators.py    # Input validation
│
├── tests/                   # Test suite
│   ├── __init__.py
│   ├── conftest.py         # Pytest configuration
│   ├── test_api/           # API tests
│   │   ├── __init__.py
│   │   ├── test_health.py
│   │   ├── test_users.py
│   │   └── test_items.py
│   ├── test_core/          # Core logic tests
│   │   ├── __init__.py
│   │   ├── test_services.py
│   │   └── test_models.py
│   └── test_frontend/      # Frontend tests
│       ├── __init__.py
│       └── test_components.py
│
├── scripts/                # Utility scripts
│   ├── start_dev.py       # Development server startup
│   ├── setup_db.py        # Database setup
│   └── generate_docs.py   # Documentation generation
│
└── docs/                   # Documentation
    ├── api.md             # API documentation
    ├── deployment.md      # Deployment guide
    ├── development.md     # Development guide
    └── architecture.md    # Architecture overview
```

## 🛠️ Technology Stack

- **Backend**: FastAPI (async Python web framework)
- **Frontend**: Streamlit (data app framework)
- **Package Manager**: UV (ultra-fast Python package installer)
- **Database**: SQLAlchemy with async support
- **Validation**: Pydantic v2 with type annotations
- **Testing**: Pytest with async support
- **Code Quality**: Ruff (linting), Black (formatting), mypy (type checking)
- **Pre-commit**: Automated code quality checks
- **Containerization**: Docker with multi-stage builds
- **Documentation**: FastAPI auto-docs + Sphinx

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- UV package manager
- Docker (optional)

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd streamlit-fastapi-template

# Install UV if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv sync

# Copy environment variables
cp .env.example .env
```

### 2. Development Setup

```bash
# Install pre-commit hooks
uv run pre-commit install

# Setup database (if using)
uv run python scripts/setup_db.py

# Start development servers
make dev
```

### 3. Access Your Application

- **Streamlit Frontend**: http://localhost:8501
- **FastAPI Backend**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 📝 Development Commands

```bash
# Start development servers
make dev

# Run tests
make test

# Run tests with coverage
make test-cov

# Format code
make format

# Lint code
make lint

# Type check
make typecheck

# Run all quality checks
make quality

# Build Docker image
make docker-build

# Start with Docker
make docker-up
```

## 🏗️ Architecture Overview

This template follows **Clean Architecture** principles:

### Layers

1. **API Layer** (`app/api/`): HTTP request handling, routing, and serialization
2. **Core Layer** (`app/core/`): Business logic, domain models, and services
3. **Database Layer** (`app/database/`): Data persistence and repositories
4. **Frontend Layer** (`frontend/`): User interface and user experience

### Key Principles

- **Dependency Inversion**: Core business logic doesn't depend on external frameworks
- **Single Responsibility**: Each module has a single, well-defined purpose
- **Open/Closed**: Open for extension, closed for modification
- **Interface Segregation**: Clients depend only on interfaces they use
- **DRY**: Don't Repeat Yourself
- **KISS**: Keep It Simple, Stupid
- **YAGNI**: You Aren't Gonna Need It

## 🔧 Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

```bash
# Application
APP_NAME=StreamlitFastAPITemplate
APP_VERSION=1.0.0
DEBUG=True

# API
API_HOST=localhost
API_PORT=8000

# Frontend
FRONTEND_HOST=localhost
FRONTEND_PORT=8501

# Database
DATABASE_URL=sqlite+aiosqlite:///./app.db

# Security
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 🧪 Testing

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=app --cov=frontend

# Run specific test file
uv run pytest tests/test_api/test_users.py

# Run with verbose output
uv run pytest -v
```

## 🐳 Docker Deployment

### Local Development

```bash
docker-compose up --build
```

### Production

```bash
# Build production image
docker build -t streamlit-fastapi-app .

# Run production container
docker run -p 8000:8000 -p 8501:8501 streamlit-fastapi-app
```

## 📚 API Documentation

The FastAPI backend automatically generates interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## 🔒 Security Features

- **CORS**: Configurable cross-origin resource sharing
- **Authentication**: JWT-based authentication system
- **Input Validation**: Pydantic models for request/response validation
- **Security Headers**: Helmet-style security headers
- **Rate Limiting**: Built-in rate limiting for API endpoints

## 📊 Monitoring and Logging

- **Health Checks**: Comprehensive health check endpoints
- **Structured Logging**: JSON-formatted logs with correlation IDs
- **Metrics**: Built-in metrics collection
- **Error Tracking**: Centralized error handling and reporting

## 🚀 Deployment

### Vercel (Recommended for Streamlit)

1. Fork this repository
2. Connect to Vercel
3. Deploy with one click

### Railway

1. Connect your GitHub repository
2. Deploy backend and frontend as separate services

### AWS/GCP/Azure

See `docs/deployment.md` for detailed cloud deployment guides.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the amazing async web framework
- [Streamlit](https://streamlit.io/) for the intuitive data app framework
- [UV](https://github.com/astral-sh/uv) for ultra-fast Python package management
- [Pydantic](https://pydantic-docs.helpmanual.io/) for data validation

## 📞 Support

If you have any questions or need help with this template:

- 📧 Email: support@yourproject.com
- 💬 Discord: [Your Discord Server](https://discord.gg/yourserver)
- 📖 Documentation: [Full Documentation](https://your-docs-site.com)

---

**Happy Coding! 🎉**
