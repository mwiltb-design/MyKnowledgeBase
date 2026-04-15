import sqlite3
import pandas as pd

def show_data():
    conn = sqlite3.connect('Artistic_Stone_Masonry/Masonry_Projects.db')
    
    # This SQL query "Joins" three separate tables to show one unified view
    query = """
    SELECT 
        p.job_name AS 'Project', 
        s.section_name AS 'Section', 
        c.description AS 'Component', 
        c.quantity AS 'Qty', 
        c.unit AS 'Unit'
    FROM Projects p
    JOIN Sections s ON p.project_id = s.project_id
    JOIN Components c ON s.section_id = c.section_id
    WHERE p.job_number LIKE '%25064%'
    LIMIT 15;
    """
    
    df = pd.read_sql_query(query, conn)
    print("\n--- MECHAM (#25064) PROJECT BREAKDOWN ---")
    print(df.to_string(index=False))
    
    # Let's also count the total 2025/2026 jobs we imported
    total_jobs = conn.execute("SELECT COUNT(*) FROM Projects").fetchone()[0]
    print(f"\nTotal Projects in Database: {total_jobs}")
    
    conn.close()

if __name__ == "__main__":
    show_data()
