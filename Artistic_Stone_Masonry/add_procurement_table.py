import sqlite3

def add_procurement_table():
    db_path = 'Artistic_Stone_Masonry/Masonry_Projects.db'
    conn = sqlite3.connect(db_path)
    
    # 1. Create the Procurement_Log table
    conn.execute("""
    CREATE TABLE IF NOT EXISTS Procurement_Log (
        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER NOT NULL,
        line_id INTEGER, -- Links back to the original Contract Line Item
        material_name TEXT NOT NULL,
        quantity_ordered REAL,
        unit TEXT,
        order_date TEXT,
        status TEXT DEFAULT 'Not Ordered', -- Not Ordered, Ordered, Received, On-Site, Installed
        notes TEXT,
        FOREIGN KEY (project_id) REFERENCES Projects(project_id),
        FOREIGN KEY (line_id) REFERENCES Contract_Lines(line_id)
    )
    """)
    
    print("\nSUCCESS: Procurement_Log table added to Database.")
    conn.close()

if __name__ == "__main__":
    add_procurement_table()
