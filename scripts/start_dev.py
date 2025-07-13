"""Development server startup script."""

import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


def start_fastapi() -> None:
    """Start the FastAPI server."""
    print("🚀 Starting FastAPI server...")
    subprocess.run(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "app.main:app",
            "--host",
            "localhost",
            "--port",
            "8000",
            "--reload",
            "--reload-dir",
            "app",
        ]
    )


def start_streamlit() -> None:
    """Start the Streamlit server."""
    print("🎨 Starting Streamlit server...")
    subprocess.run(
        [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            "frontend/main.py",
            "--server.port",
            "8501",
            "--server.address",
            "localhost",
            "--server.headless",
            "false",
        ]
    )


def main() -> None:
    """Start both servers in parallel."""
    print("🔧 Starting development servers...")
    print("📍 FastAPI will be available at: http://localhost:8000")
    print("📍 Streamlit will be available at: http://localhost:8501")
    print("📍 API docs will be available at: http://localhost:8000/docs")
    print("=" * 60)

    # Ensure we're in the project root
    project_root = Path(__file__).parent.parent
    if not (project_root / "app").exists() or not (project_root / "frontend").exists():
        print("❌ Error: Please run this script from the project root directory")
        sys.exit(1)

    # Start both servers in parallel
    with ThreadPoolExecutor(max_workers=2) as executor:
        try:
            # Submit both servers to the thread pool
            fastapi_future = executor.submit(start_fastapi)
            streamlit_future = executor.submit(start_streamlit)

            # Wait for both to complete (they won't unless interrupted)
            fastapi_future.result()
            streamlit_future.result()

        except KeyboardInterrupt:
            print("\n⏹️  Shutting down servers...")
            sys.exit(0)


if __name__ == "__main__":
    main()
