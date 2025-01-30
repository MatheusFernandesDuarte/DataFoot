from src.repositories.db import db

"""
Many-to-Many relationship between Championships and Teams.
A team can participate in multiple championships and a championship can have multiple teams.
"""
championship_team_association = db.Table(
    "championship_team",
    db.Column("championship_id", db.Integer, db.ForeignKey("championships.id"), primary_key=True),
    db.Column("team_id", db.Integer, db.ForeignKey("teams.id"), primary_key=True),
    __table_args__ = {"sqlite_autoincrement": True, "info": {"bind_key": "championships"}}
)

"""
Many-to-Many relationship between Players and Teams according to the season.
A player can play for different teams in different seasons.
"""
player_team_season_association = db.Table(
    "player_team_season",
    db.Column("player_id", db.Integer, db.ForeignKey("players.id"), primary_key=True),
    db.Column("team_id", db.Integer, db.ForeignKey("teams.id"), primary_key=True),
    db.Column("season", db.String(20), nullable=False),
    __table_args__ = {"sqlite_autoincrement": True, "info": {"bind_key": "players"}}
)

"""
Many-to-Many relationship between Players and Games.
A player can play multiple games and a game can have multiple players.
"""
player_game_association = db.Table(
    "player_game",
    db.Column("player_id", db.Integer, db.ForeignKey("players.id"), primary_key=True),
    db.Column("game_id", db.Integer, db.ForeignKey("games.id"), primary_key=True),
    __table_args__ = {"sqlite_autoincrement": True, "info": {"bind_key": "games"}}
)
