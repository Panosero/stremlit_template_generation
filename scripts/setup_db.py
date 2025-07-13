"""Database setup script."""

import asyncio
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


async def setup_database() -> None:
    """Set up the database with initial tables."""
    try:
        from app.database.connection import create_tables

        print("🗄️ Setting up database...")
        await create_tables()
        print("✅ Database setup completed successfully!")

    except Exception as e:
        print(f"❌ Database setup failed: {e}")
        sys.exit(1)


def main() -> None:
    """Main function to run database setup."""
    print("🚀 Starting database setup...")
    asyncio.run(setup_database())


if __name__ == "__main__":
    main()
