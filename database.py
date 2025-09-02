# database.py
import sqlite3

DATABASE_NAME = 'impact_tool.db'

def get_db_connection():
    """Establishes a connection to the database."""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    return conn

def init_db():
    """Initializes the database table if it doesn't exist."""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            org_name TEXT,
            website TEXT,
            country TEXT,
            mission TEXT,
            problem_addressed TEXT,
            beneficiaries TEXT,
            solution TEXT,
            metrics TEXT,
            impacted_last_year INTEGER,
            sdg TEXT,
            seeking_funding TEXT,
            funding_amount INTEGER,
            funding_use TEXT,
            founder_name TEXT,
            founder_gender TEXT,
            ai_keywords TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

def add_submission(data):
    """Adds a new submission to the database."""
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO submissions (org_name, website, country, mission, problem_addressed, beneficiaries, solution, metrics, impacted_last_year, sdg, seeking_funding, funding_amount, funding_use, founder_name, founder_gender, ai_keywords)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.get('org_name'), data.get('website'), data.get('country'), data.get('mission'),
        data.get('problem_addressed'), data.get('beneficiaries'), data.get('solution'),
        data.get('metrics'), data.get('impacted_last_year'), ", ".join(data.getlist('sdg')), # Handle multiple SDGs
        data.get('seeking_funding'), data.get('funding_amount'), data.get('funding_use'),
        data.get('founder_name'), data.get('founder_gender'), data.get('ai_keywords')
    ))
    conn.commit()
    conn.close()

def get_all_submissions():
    """Retrieves all submissions from the database."""
    conn = get_db_connection()
    submissions = conn.execute('SELECT * FROM submissions ORDER BY timestamp DESC').fetchall()
    conn.close()
    return submissions