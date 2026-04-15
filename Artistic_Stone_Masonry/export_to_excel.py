import sqlite3
import pandas as pd

def export_all():
    db_path = 'Artistic_Stone_Masonry/Masonry_Projects.db'
    output_path = 'Artistic_Stone_Masonry/DATABASE_EXPORT.xlsx'
    
    conn = sqlite3.connect(db_path)
    
    # Get all table names
    tables = ['Projects', 'Contract_Lines', 'Sections', 'Components', 'Labor_Logs', 'Draws']
    
    # Create an Excel writer
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        for table in tables:
            df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
            df.to_excel(writer, sheet_name=table, index=False)
            print(f"Exported {len(df)} rows from table '{table}'")
            
    conn.close()
    print(f"\nSUCCESS: Full database exported to {output_path}")

if __name__ == "__main__":
    export_all()
