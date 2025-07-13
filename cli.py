#!/usr/bin/env python3
"""
Project management CLI tool for Streamlit FastAPI Template.

This script provides convenient commands for common development tasks.
"""

import subprocess
import typer
from pathlib import Path
from rich.console import Console
from rich.table import Table

app = typer.Typer(help="🚀 Streamlit FastAPI Template CLI")
console = Console()


@app.command()
def install() -> None:
    """Install project dependencies using UV."""
    console.print("📦 Installing dependencies...", style="bold blue")

    try:
        subprocess.run(["uv", "sync"], check=True)
        subprocess.run(["uv", "run", "pre-commit", "install"], check=True)
        console.print("✅ Dependencies installed successfully!", style="bold green")
    except subprocess.CalledProcessError as e:
        console.print(f"❌ Installation failed: {e}", style="bold red")
        raise typer.Exit(1)


@app.command()
def dev() -> None:
    """Start development servers (FastAPI + Streamlit)."""
    console.print("🚀 Starting development servers...", style="bold blue")
    console.print("📍 FastAPI: http://localhost:8000", style="dim")
    console.print("📍 Streamlit: http://localhost:8501", style="dim")
    console.print("📍 API Docs: http://localhost:8000/docs", style="dim")

    try:
        subprocess.run(["uv", "run", "python", "scripts/start_dev.py"], check=True)
    except KeyboardInterrupt:
        console.print("\n⏹️ Servers stopped.", style="bold yellow")
    except subprocess.CalledProcessError as e:
        console.print(f"❌ Failed to start servers: {e}", style="bold red")
        raise typer.Exit(1)


@app.command()
def test(
    coverage: bool = typer.Option(False, "--coverage", "-c", help="Run with coverage"),
    file: str | None = typer.Option(None, "--file", "-f", help="Run specific test file"),
) -> None:
    """Run tests with optional coverage."""
    console.print("🧪 Running tests...", style="bold blue")

    cmd = ["uv", "run", "pytest"]

    if coverage:
        cmd.extend(["--cov=app", "--cov=frontend", "--cov-report=html", "--cov-report=term-missing"])

    if file:
        cmd.append(file)

    try:
        subprocess.run(cmd, check=True)
        console.print("✅ Tests completed!", style="bold green")

        if coverage:
            console.print("📊 Coverage report generated in htmlcov/", style="dim")
    except subprocess.CalledProcessError as e:
        console.print(f"❌ Tests failed: {e}", style="bold red")
        raise typer.Exit(1)


@app.command()
def lint() -> None:
    """Run code linting."""
    console.print("🔍 Running linter...", style="bold blue")

    try:
        subprocess.run(["uv", "run", "ruff", "check", "."], check=True)
        console.print("✅ Linting passed!", style="bold green")
    except subprocess.CalledProcessError:
        console.print("❌ Linting failed!", style="bold red")
        raise typer.Exit(1)


@app.command()
def format() -> None:
    """Format code with ruff."""
    console.print("🎨 Formatting code...", style="bold blue")

    try:
        subprocess.run(["uv", "run", "ruff", "format", "."], check=True)
        subprocess.run(["uv", "run", "ruff", "check", "--fix", "."], check=True)
        console.print("✅ Code formatted!", style="bold green")
    except subprocess.CalledProcessError as e:
        console.print(f"❌ Formatting failed: {e}", style="bold red")
        raise typer.Exit(1)


@app.command()
def typecheck() -> None:
    """Run type checking with mypy."""
    console.print("🔍 Running type checker...", style="bold blue")

    try:
        subprocess.run(["uv", "run", "mypy", "app/", "frontend/", "--ignore-missing-imports"], check=True)
        console.print("✅ Type checking passed!", style="bold green")
    except subprocess.CalledProcessError:
        console.print("❌ Type checking failed!", style="bold red")
        raise typer.Exit(1)


@app.command()
def quality() -> None:
    """Run all quality checks (lint, typecheck, test)."""
    console.print("🔍 Running quality checks...", style="bold blue")

    try:
        # Linting
        console.print("1/3 Running linter...", style="dim")
        subprocess.run(["uv", "run", "ruff", "check", "."], check=True)

        # Type checking
        console.print("2/3 Running type checker...", style="dim")
        subprocess.run(["uv", "run", "mypy", "app/", "frontend/", "--ignore-missing-imports"], check=True)

        # Tests
        console.print("3/3 Running tests...", style="dim")
        subprocess.run(["uv", "run", "pytest"], check=True)

        console.print("✅ All quality checks passed!", style="bold green")
    except subprocess.CalledProcessError:
        console.print("❌ Quality checks failed!", style="bold red")
        raise typer.Exit(1)


@app.command()
def clean() -> None:
    """Clean cache and temporary files."""
    console.print("🧹 Cleaning cache files...", style="bold blue")

    patterns = [
        "__pycache__",
        "*.pyc",
        "*.pyo",
        "*.pyd",
        ".coverage",
        "*.egg-info",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache",
        "htmlcov",
        "dist",
        "build",
    ]

    for pattern in patterns:
        subprocess.run(["find", ".", "-name", pattern, "-exec", "rm", "-rf", "{}", "+"], capture_output=True)

    console.print("✅ Cleanup completed!", style="bold green")


@app.command()
def docker() -> None:
    """Build and run with Docker Compose."""
    console.print("🐳 Starting Docker containers...", style="bold blue")

    try:
        subprocess.run(["docker-compose", "up", "--build"], check=True)
    except KeyboardInterrupt:
        console.print("\n⏹️ Containers stopped.", style="bold yellow")
    except subprocess.CalledProcessError as e:
        console.print(f"❌ Docker failed: {e}", style="bold red")
        raise typer.Exit(1)


@app.command()
def status() -> None:
    """Show project status and information."""
    console.print("📊 Project Status", style="bold blue")

    # Create status table
    table = Table(title="Streamlit FastAPI Template")
    table.add_column("Component", style="cyan")
    table.add_column("Status", style="magenta")
    table.add_column("Details", style="green")

    # Check if key files exist
    files_to_check = [
        ("pyproject.toml", "Configuration"),
        (".env", "Environment"),
        ("app/main.py", "FastAPI Backend"),
        ("frontend/main.py", "Streamlit Frontend"),
        ("tests/", "Test Suite"),
    ]

    for file_path, description in files_to_check:
        if Path(file_path).exists():
            status = "✅ Ready"
            details = "File exists"
        else:
            status = "❌ Missing"
            details = "File not found"

        table.add_row(description, status, details)

    console.print(table)

    # Show available commands
    console.print("\n🛠️  Available Commands:", style="bold")
    commands = [
        ("cli.py install", "Install dependencies"),
        ("cli.py dev", "Start development servers"),
        ("cli.py test", "Run tests"),
        ("cli.py quality", "Run all quality checks"),
        ("cli.py docker", "Run with Docker"),
    ]

    for cmd, desc in commands:
        console.print(f"  {cmd:<20} {desc}", style="dim")


if __name__ == "__main__":
    app()
