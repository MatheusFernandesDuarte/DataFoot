from flask import Flask, jsonify
from src.repositories.db import db
from src.utils.config import Config

from src.modules.team.team_model import Team
from src.modules.championship.championship_model import Championship
from src.modules.player.player_model import Player

from src.modules.models.associations import championship_team_association

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.metadata.clear()
        db.create_all()

    @app.route("/")
    def home() -> dict[str, str]:
        return jsonify({"message": "Hello World"}), 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
