import pandas as pd
import sqlite3
import os

db_path = 'Artistic_Stone_Masonry/Masonry_Projects.db'
schema_path = 'Artistic_Stone_Masonry/Masonry_Schema.sql'

def init_db():
    conn = sqlite3.connect(db_path)
    with open(schema_path, 'r') as f:
        conn.executescript(f.read())
    
    # 1. Populate 2025-2026 Jobs
    for year in ['2025', '2026']:
        try:
            df_jobs = pd.read_excel('Artistic_Stone_Masonry/Job Number List.xlsx', sheet_name=year)
            # Handle potential header issues
            df_jobs.columns = [str(c).strip() for c in df_jobs.columns]
            df_jobs = df_jobs.rename(columns={'Job #': 'job_number', 'Builder': 'contractor', "Client's Name": 'job_name'})
            
            for _, row in df_jobs.iterrows():
                j_num = str(row.get('job_number', '')).strip()
                j_name = str(row.get('job_name', '')).strip()
                j_contractor = str(row.get('contractor', '')).strip()
                
                if j_num and j_name and j_num != 'nan' and j_name != 'nan':
                    conn.execute('INSERT OR IGNORE INTO Projects (job_number, job_name, contractor) VALUES (?, ?, ?)', 
                                 (j_num, j_name, j_contractor))
        except Exception as e:
            print(f"Error processing year {year}: {e}")

    conn.commit()

    # 2. Populate Mecham Detailed Data (#25064)
    # Search for Mecham (using the specific job number)
    cursor = conn.execute("SELECT project_id FROM Projects WHERE job_number LIKE '%25064%'")
    row = cursor.fetchone()
    if not row:
        print("Mecham project not found in Job List.")
        return
    
    project_id = row[0]
    
    # Update Mecham project with specific details from its spreadsheet
    df_mecham = pd.read_excel('Artistic_Stone_Masonry/Mecham.xlsx')
    
    # Extract Address and Estimate #
    address = str(df_mecham.iloc[0, 1])
    stone = str(df_mecham.iloc[4, 1])
    
    conn.execute("UPDATE Projects SET address = ?, stone_selection = ? WHERE project_id = ?", 
                 (address, stone, project_id))

    # Extract sections and components
    # Based on the spreadsheet structure: Section/Room is in Col 0, SF is in Col 2
    for index, row in df_mecham.iterrows():
        section_name = str(row.iloc[0]).strip()
        # Skip metadata and headers
        if section_name in ['nan', 'Section/Room', 'Job Name & Number:', 'Job Address:', 'Stone Selections:']:
            continue
            
        try:
            sf_val = float(row.iloc[2])
            if sf_val > 0:
                # Create Section
                conn.execute('INSERT INTO Sections (project_id, section_name) VALUES (?, ?)', (project_id, section_name))
                section_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
                
                # Add Component (Veneer)
                conn.execute('INSERT INTO Components (section_id, category, description, quantity, unit) VALUES (?, ?, ?, ?, ?)',
                             (section_id, 'Veneer', 'Stone or Brick Veneer', sf_val, 'SF'))
        except (ValueError, TypeError):
            continue

    conn.commit()
    print(f"Database Initialized. Mecham Project (#{project_id}) populated with details.")
    conn.close()

if __name__ == "__main__":
    init_db()
