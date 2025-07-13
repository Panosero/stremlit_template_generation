"""GitHub Actions CI/CD workflow configuration generator."""

import yaml
from pathlib import Path


def generate_github_workflow() -> dict:
    """Generate GitHub Actions workflow configuration."""
    return {
        "name": "CI/CD Pipeline",
        "on": {"push": {"branches": ["main", "develop"]}, "pull_request": {"branches": ["main"]}},
        "jobs": {
            "test": {
                "runs-on": "ubuntu-latest",
                "strategy": {"matrix": {"python-version": ["3.11", "3.12"]}},
                "steps": [
                    {"uses": "actions/checkout@v4"},
                    {"name": "Install UV", "uses": "astral-sh/setup-uv@v2"},
                    {
                        "name": "Set up Python ${{ matrix.python-version }}",
                        "run": "uv python install ${{ matrix.python-version }}",
                    },
                    {"name": "Install dependencies", "run": "uv sync"},
                    {"name": "Run linting", "run": "uv run ruff check ."},
                    {"name": "Run type checking", "run": "uv run mypy app/ frontend/"},
                    {"name": "Run tests", "run": "uv run pytest --cov=app --cov=frontend --cov-report=xml"},
                    {
                        "name": "Upload coverage",
                        "uses": "codecov/codecov-action@v3",
                        "with": {"file": "./coverage.xml"},
                    },
                ],
            },
            "docker": {
                "runs-on": "ubuntu-latest",
                "needs": "test",
                "if": "github.ref == 'refs/heads/main'",
                "steps": [
                    {"uses": "actions/checkout@v4"},
                    {"name": "Set up Docker Buildx", "uses": "docker/setup-buildx-action@v3"},
                    {
                        "name": "Login to Docker Hub",
                        "uses": "docker/login-action@v3",
                        "with": {
                            "username": "${{ secrets.DOCKER_USERNAME }}",
                            "password": "${{ secrets.DOCKER_PASSWORD }}",
                        },
                    },
                    {
                        "name": "Build and push",
                        "uses": "docker/build-push-action@v5",
                        "with": {
                            "context": ".",
                            "push": True,
                            "tags": "yourusername/streamlit-fastapi-template:latest",
                        },
                    },
                ],
            },
        },
    }


def main() -> None:
    """Generate and save GitHub Actions workflow."""
    workflow = generate_github_workflow()

    # Create .github/workflows directory
    workflows_dir = Path(".github/workflows")
    workflows_dir.mkdir(parents=True, exist_ok=True)

    # Write workflow file
    workflow_file = workflows_dir / "ci.yml"
    with open(workflow_file, "w") as f:
        yaml.dump(workflow, f, default_flow_style=False, sort_keys=False)

    print(f"✅ Generated GitHub Actions workflow: {workflow_file}")


if __name__ == "__main__":
    main()
