import sqlite3

def check_db():
    db_path = 'Artistic_Stone_Masonry/Masonry_Projects.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    
    print("--- TABLES IN DATABASE ---")
    for table in tables:
        table_name = table[0]
        print(f"\nTable: {table_name}")
        
        # Get columns for each table
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        for col in columns:
            print(f"  - {col[1]} ({col[2]})")

    conn.close()

if __name__ == "__main__":
    check_db()
