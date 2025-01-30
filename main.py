from flask import Flask

from src.modules.championship.championship_routes import championship_bp
from src.repositories.db import db
from src.utils.config import Config

def create_app() -> Flask:
    """
    Create and configure the Flask application.

    This function initializes the Flask application, loads configuration 
    settings, connects to the database, and registers application blueprints.

    Steps:
    1. Create a Flask instance.
    2. Load configuration settings from the `Config` class.
    3. Initialize the SQLAlchemy database extension with the app.
    4. Register application blueprints (e.g., championship routes).
    5. Create all database tables within the application context.

    Returns:
        Flask: The configured Flask application instance.
    """

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(championship_bp)

    with app.app_context():
        db.create_all()
        print("✅ Database initialized successfully!")

    return app

if __name__ == "__main__":
    """
    Entry point for running the Flask application.

    - Calls `create_app()` to initialize the Flask app.
    - Runs the app in debug mode on `0.0.0.0:5000`.
    - Includes a safety check to ensure the app was initialized before starting.

    If the application fails to initialize, an error message is printed.
    """
    app = create_app()
    if app:
        print("🚀 Starting Flask application...")
        app.run(debug=True, host="0.0.0.0", port=5000)
    else:
        print("🚨 ERROR: Flask app failed to initialize.")
