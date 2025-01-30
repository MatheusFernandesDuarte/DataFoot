from flask import Flask
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy

class CustomSQLAlchemy(SQLAlchemy):
    """Custom class to configure SQLAlchemy with additional optimizations."""
    def apply_driver_hacks(self, app: Flask, info: Engine, options: dict) -> None:
        """
        Applies database driver adjustments before establishing the connection.

        If the 'pool_pre_ping' option is not set, it is enabled to prevent
        the use of inactive connections in the pool, reducing connection errors
        in databases like PostgreSQL and MySQL.

        Parameters:
            app (Flask): The Flask application instance.
            info (Engine): Information about the database connection.
            options (dict): Additional SQLAlchemy options.

        Returns:
            None
        """
        if 'pool_pre_ping' not in options:
            options['pool_pre_ping'] = True
        super().apply_driver_hacks(app, info, options)

db = CustomSQLAlchemy()