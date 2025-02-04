# 📌 DataFoot - API for Football Championship Management

## 📖 About the Project
**DataFoot** is an API developed in Python with Flask and SQLAlchemy to manage football championships. It allows registering teams, players, matches, statistics, goals, and rankings in an organized and efficient manner.

## 🚀 Technologies Used
- **Python 3.12**
- **Flask** (Web framework)
- **Flask-SQLAlchemy** (ORM for database management)
- **SQLite / PostgreSQL** (Database)
- **Dotenv** (Environment variable management)
- **Selenium** (Web scraping for data collection)

## 📂 Project Structure
```bash
DataFoot/
├── main.py          # Main file to run the API
├── requirements.txt # Project dependencies
├── LICENSE          # Project license
├── README.md        # Documentation
├── src/
│   ├── modules/     # Main modules
│   │   ├── card/      # Card management
│   │   ├── championship/ # Championship management
│   │   ├── game/      # Match management
│   │   ├── game_stats/ # Match statistics
│   │   ├── goal/      # Goal management
│   │   ├── models/    # Table associations
│   │   ├── player/    # Player management
│   │   ├── ranking/   # Team rankings
│   │   ├── team/      # Team management
│   ├── repositories/ # Database management
│   ├── utils/        # Utility functions
```

## 🔧 How to Run the Project
### 1️⃣ **Clone the repository**
```bash
git clone https://github.com/MatheusFernandesDuarte/datafoot.git
cd datafoot
```

### 2️⃣ **Create and activate a virtual environment**
```bash
python -m venv venv
# Activate on Windows
venv\Scripts\activate
# Activate on Linux/Mac
source venv/bin/activate
```

### 3️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Configure the database**
Edit the `.env` file to set database connections:
```ini
DATABASE_URL=sqlite:///default_db.sqlite
BIND_CARD=sqlite:///card.db
BIND_CHAMPIONSHIP=sqlite:///championship.db
BIND_GAME=sqlite:///game.db
BIND_GAME_STATS=sqlite:///game_stats.db
BIND_GOAL=sqlite:///goal.db
BIND_PLAYER=sqlite:///player.db
BIND_RANKING=sqlite:///ranking.db
BIND_TEAM=sqlite:///team.db
```

### 5️⃣ **Start the API**
```bash
python main.py
```
The API will be running at `http://localhost:5000`.

## 🎯 Future Improvements
- Implement Main Endpoints
- Develop an admin dashboard
- Improve performance with caching
- Integrate with external football APIs
- **Automated web scraping with Selenium** to populate the database with real-time football data
- **Interactive LLM integration using LangChain** for intelligent queries and insights

## 📝 License
This project is licensed under the [MIT License](LICENSE).
