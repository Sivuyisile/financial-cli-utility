import sqlite3
from contextlib import contextmanager
from pathlib import Path

DB_PATH = Path(__file__).parent/"fin_database.db"

class DatabaseManager:

    def __init__(self, db_path=DB_PATH):

        self.db_path = db_path


    @contextmanager
    def get_connection(self):

        is_uri = str(self.db_path).startswith("file:")
        conn = sqlite3.connect(self.db_path, uri=is_uri)
        conn.row_factory = sqlite3.Row

        conn.execute("PRAGMA foreign_keys = ON;")   #positioning --> for/following DRY principle

        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()


    def execute_query(self, query, params):

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)


    def executemany_query(self, query, params_list):

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.executemany(query, params_list)


    def fetch_all(self, query, params):

        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)

            rows = cursor.fetchall()

            return [dict(row) for row in rows]


    def fetch_one(self, query, params):

        with self.get_connection() as conn:
            cursor = conn.cursor()  
            cursor.execute(query, params)

            row = cursor.fetchone()

            return dict(row) if row else None


    def create_tables(self):

        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
    
                script = """
                    CREATE TABLE IF NOT EXISTS monthly_budgets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    month_year TEXT NOT NULL UNIQUE, --e.g. '10-2026'
                    net_income TEXT NOT NULL, --still text for decimal precision
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);    
    
    
                    CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    budget_id INTEGER NOT NULL,
                    category TEXT NOT NULL,
                    item_name TEXT NOT NULL,
                    amount TEXT NOT NULL,   --again, as text for decimal precision
                    quantity INTEGER DEFAULT 1,
                    FOREIGN KEY (budget_id) REFERENCES monthly_budgets (id) ON DELETE CASCADE)
                """
    
                cursor.executescript(script)
    
                print('Database script executed successfully')
                
    
        except sqlite3.Error as e:
            print(f"Transaction failed, rolled back changes: {e}")
        