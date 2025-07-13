# Development Guide

This guide will help you set up and develop with the Streamlit FastAPI template.

## Prerequisites

- Python 3.11 or higher
- UV package manager
- Git
- Docker (optional)

## Quick Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd streamlit-fastapi-template
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

4. **Install pre-commit hooks**
   ```bash
   uv run pre-commit install
   ```

5. **Start development servers**
   ```bash
   make dev
   ```

## Development Workflow

### Code Quality

We use several tools to maintain code quality:

- **Ruff**: Fast Python linter and formatter
- **MyPy**: Static type checking
- **Pre-commit**: Automated checks before commits
- **Pytest**: Testing framework

```bash
# Run all quality checks
make quality

# Individual checks
make lint      # Linting
make typecheck # Type checking
make format    # Code formatting
make test      # Run tests
```

### Project Structure

```
streamlit-fastapi-template/
├── app/                    # FastAPI backend
│   ├── api/               # API routes
│   ├── core/              # Business logic
│   ├── database/          # Database layer
│   └── utils/             # Utilities
├── frontend/              # Streamlit frontend
│   ├── components/        # UI components
│   ├── pages/            # Streamlit pages
│   ├── services/         # API clients
│   └── utils/            # Frontend utilities
└── tests/                # Test suite
```

### Adding New Features

1. **API Endpoints**
   - Add routes in `app/api/routes/`
   - Define models in `app/core/models/`
   - Implement business logic in `app/core/services/`

2. **Frontend Pages**
   - Add pages in `frontend/pages/`
   - Create reusable components in `frontend/components/`
   - Update navigation in sidebar

3. **Database Models**
   - Define SQLAlchemy models in `app/database/models/`
   - Create migrations if needed
   - Update repositories in `app/database/repositories/`

### Testing

```bash
# Run all tests
make test

# Run tests with coverage
make test-cov

# Run specific test file
uv run pytest tests/test_api/test_health.py

# Run tests in watch mode
uv run pytest-watch
```

### Environment Variables

Key environment variables:

- `DEBUG`: Enable debug mode
- `API_HOST`, `API_PORT`: API server configuration
- `DATABASE_URL`: Database connection string
- `SECRET_KEY`: JWT secret key (change in production!)

### Docker Development

```bash
# Build and run with Docker Compose
make docker-up

# View logs
make docker-logs

# Stop containers
make docker-down
```

## Architecture Overview

### Clean Architecture

The project follows Clean Architecture principles:

1. **API Layer**: HTTP handling and serialization
2. **Core Layer**: Business logic and domain models
3. **Database Layer**: Data persistence
4. **Frontend Layer**: User interface

### Dependency Injection

FastAPI's dependency injection system is used for:

- Database sessions
- Configuration settings
- Authentication
- Rate limiting

### Error Handling

- Custom exceptions in `app/core/exceptions.py`
- Global error handlers in FastAPI
- Structured logging with correlation IDs

### Security

- JWT authentication
- CORS configuration
- Input validation with Pydantic
- SQL injection prevention with SQLAlchemy

## Best Practices

### Code Style

- Follow PEP 8 and PEP 20
- Use type hints everywhere
- Write docstrings for all public functions
- Keep functions small and focused

### API Design

- Use RESTful conventions
- Version your APIs (`/api/v1/`)
- Implement proper HTTP status codes
- Use Pydantic models for validation

### Frontend Development

- Create reusable components
- Use session state wisely
- Implement proper error handling
- Cache expensive operations

### Database

- Use migrations for schema changes
- Implement proper indexes
- Use async/await for database operations
- Handle database errors gracefully

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure you're in the virtual environment
2. **Database connection**: Check `DATABASE_URL` in `.env`
3. **Port conflicts**: Change ports in configuration
4. **Permission errors**: Check file permissions

### Debug Mode

Enable debug mode for detailed error messages:

```bash
# In .env file
DEBUG=True
```

### Logging

View application logs:

```bash
# FastAPI logs
tail -f logs/app.log

# Streamlit logs
streamlit run frontend/main.py --logger.level=debug
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run quality checks
5. Submit a pull request

See the main README for detailed contribution guidelines.
