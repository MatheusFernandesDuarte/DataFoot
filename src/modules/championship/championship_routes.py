from flask import Blueprint
from src.modules.championship.championship_controller import ChampionshipController

championship_bp = Blueprint('championship', __name__, url_prefix='/championship')

championship_bp.route('/', methods=['GET'])(ChampionshipController.get_all)
championship_bp.route('/<int:id>', methods=['GET'])(ChampionshipController.get_by_id)
championship_bp.route('/', methods=['POST'])(ChampionshipController.create)
championship_bp.route('/<int:id>', methods=['PUT'])(ChampionshipController.update)
championship_bp.route('/<int:id>', methods=['DELETE'])(ChampionshipController.delete)
