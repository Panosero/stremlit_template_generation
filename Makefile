.PHONY: help dev test test-cov format lint typecheck quality clean docker-build docker-up install

# Default target
help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies using UV
	uv sync
	uv run pre-commit install

dev: ## Start development servers (FastAPI + Streamlit)
	@echo "Starting development servers..."
	@echo "FastAPI will be available at: http://localhost:8000"
	@echo "Streamlit will be available at: http://localhost:8501"
	@echo "API docs will be available at: http://localhost:8000/docs"
	@echo ""
	@echo "Starting servers in parallel..."
	uv run python scripts/start_dev.py

test: ## Run tests
	uv run pytest

test-cov: ## Run tests with coverage
	uv run pytest --cov=app --cov=frontend --cov-report=html --cov-report=term-missing

format: ## Format code with black and ruff
	uv run ruff format .
	uv run ruff check --fix .

lint: ## Lint code with ruff
	uv run ruff check .

typecheck: ## Type check with mypy
	uv run mypy app/ frontend/ tests/

quality: lint typecheck test ## Run all quality checks

clean: ## Clean cache and temporary files
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	rm -rf htmlcov/
	rm -rf dist/
	rm -rf build/

setup-db: ## Setup database
	uv run python scripts/setup_db.py

docker-build: ## Build Docker image
	docker build -t streamlit-fastapi-template .

docker-up: ## Start application with Docker Compose
	docker-compose up --build

docker-down: ## Stop Docker Compose
	docker-compose down

docker-logs: ## View Docker logs
	docker-compose logs -f

docs: ## Generate documentation
	uv run python scripts/generate_docs.py

security: ## Run security checks
	uv run bandit -r app/ frontend/ -f json -o bandit-report.json
	uv run safety check

update-deps: ## Update dependencies
	uv sync --upgrade

pre-commit: ## Run pre-commit hooks on all files
	uv run pre-commit run --all-files

# Production commands
prod-build: ## Build for production
	uv build

prod-install: ## Install production dependencies only
	uv sync --no-dev

# Development utilities
shell: ## Open Python shell with app context
	uv run python -c "from app.main import app; import IPython; IPython.embed()"

api-shell: ## Open interactive API shell
	uv run python -c "import httpx; from app.config import settings; client = httpx.Client(base_url=f'http://{settings.API_HOST}:{settings.API_PORT}'); import IPython; IPython.embed()"
