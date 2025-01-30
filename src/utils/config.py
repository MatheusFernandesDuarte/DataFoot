import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application's global configurations."""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_BINDS = {
        #'cards': os.getenv('BIND_CARD'),
        'championships': os.getenv('BIND_CHAMPIONSHIP'),
        #'games': os.getenv('BIND_GAME'),
        #'games_stats': os.getenv('BIND_GAME_STATS'),
        #'goals': os.getenv('BIND_GOAL'),
        #'players': os.getenv('BIND_PLAYER'),
        #'rankings': os.getenv('BIND_RANKING'),
        #'teams': os.getenv('BIND_TEAM'),
    }
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

print("DATABASE_URI:", Config.SQLALCHEMY_DATABASE_URI)
print("BINDS:", Config.SQLALCHEMY_BINDS)