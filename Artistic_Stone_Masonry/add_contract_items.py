import sqlite3
import pandas as pd

def add_contract_items():
    db_path = 'Artistic_Stone_Masonry/Masonry_Projects.db'
    conn = sqlite3.connect(db_path)
    
    # 1. Create the Contract_Lines table to hold the official Estimate details
    conn.execute("""
    CREATE TABLE IF NOT EXISTS Contract_Lines (
        line_id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER NOT NULL,
        description TEXT NOT NULL,
        quantity REAL,
        unit TEXT,
        unit_price REAL,
        total_value REAL,
        FOREIGN KEY (project_id) REFERENCES Projects(project_id)
    )
    """)
    
    # 2. Get the Mecham project_id
    project_id = conn.execute("SELECT project_id FROM Projects WHERE job_number LIKE '%25064%'").fetchone()[0]
    
    # 3. Update the Total Contract Value for Mecham
    conn.execute("UPDATE Projects SET total_contract_value = 472812.00 WHERE project_id = ?", (project_id,))
    
    # 4. Insert the Contract Line Items from the PDF
    # (Description, Qty, Unit, Unit Price, Total)
    contract_data = [
        ("Antique Desert Stone, full bed", 102, "per ton", 590.00, 60180.00),
        ("Antique Desert Stone, thin veneer flats", 2750, "SF", 14.00, 38500.00),
        ("Antique Desert Stone, thin veneer corners", 300, "LF", 17.50, 5250.00),
        ("3\"x6\" sills and thresholds Shadow Beige Limestone", 80, "LF", 30.00, 2400.00),
        ("3\" Shadow Beige Limestone wall caps", 160, "SF", 38.00, 6080.00),
        ("7\" Sloped/profiled Transition sills Shadow Beige Limestone", 590, "LF", 56.00, 33040.00),
        ("Fabrication of 7\" Sloped/profiled Transition sills corner returns", 52, "EA", 60.00, 3120.00),
        ("10\" Shadow Beige Limestone headers for full bed stone", 58, "LF", 70.00, 4060.00),
        ("10\" Shadow Beige Limestone headers for thin stone", 58, "LF", 54.00, 3132.00),
        ("26\" x 10\" profiled Eave Blocks", 12, "EA", 385.00, 4620.00),
        ("5' x 5' x 4\" Shadow Beige chimney caps", 3, "EA", 1350.00, 4050.00),
        ("8' x 5' x 4\" Shadow Beige chimney caps", 1, "EA", 2150.00, 2150.00),
        ("Fabrication of custom profiled front entry limestone surround", 1, "EA", 6800.00, 6800.00),
        ("Delivery of stone and/or materials", 12, "EA", 400.00, 4800.00),
        ("6\" CMU grouted solid for entry parapet walls", 180, "EA", 19.00, 3420.00),
        ("Installation of exterior stone veneer, full bed", 3460, "SF", 25.00, 86500.00),
        ("Installation of exterior stone above the roof areas, full bed", 690, "SF", 35.00, 24150.00),
        ("Installation of exterior stone veneer, thin veneer", 2290, "SF", 23.00, 52670.00),
        ("Installation of exterior stone above the roof areas, thin veneer", 340, "SF", 30.00, 10200.00),
        ("Installation of stone accents: sills, caps and headers", 920, "SF/LF", 25.00, 23000.00),
        ("Installation of stone eave blocks", 12, "EA", 150.00, 1800.00),
        ("Installation of front entry profiled surround", 1, "EA", 2400.00, 2400.00),
        ("Installation of stone chimney caps", 4, "EA", 500.00, 2000.00),
        ("Allowance for crane rental for chimney cap installations", 1, "EA", 1500.00, 1500.00),
        ("4\"x4\" galvanized angle irons", 820, "LF", 26.00, 21320.00),
        ("**Living Room and basement Family Room fireplaces: Antique Desert thin stone veneer", 2, "EA", 8900.00, 17800.00),
        ("Fabrication of custom limestone fireplace surround and hearth", 2, "EA", 7450.00, 14900.00),
        ("Labor to install stone fireplace surround and hearth", 2, "EA", 1800.00, 3600.00),
        ("**Primary Bedroom: Fabrication of Tudor style surround with white marble and carvings", 1, "EA", 16770.00, 16770.00),
        ("Labor to install stone fireplace surround", 1, "EA", 1800.00, 1800.00),
        ("**Upstairs guest loft fireplace: Fabrication of Tudor style surround with limestone", 1, "EA", 8800.00, 8800.00),
        ("Labor to install stone fireplace surround", 1, "EA", 2000.00, 2000.00)
    ]
    
    # Clear existing if any (prevent duplicates if run twice)
    conn.execute("DELETE FROM Contract_Lines WHERE project_id = ?", (project_id,))
    
    for item in contract_data:
        conn.execute('''
            INSERT INTO Contract_Lines (project_id, description, quantity, unit, unit_price, total_value)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (project_id, item[0], item[1], item[2], item[3], item[4]))
        
    conn.commit()
    
    # Verify and display
    query = f"SELECT description, quantity, unit, unit_price, total_value FROM Contract_Lines WHERE project_id = {project_id}"
    df = pd.read_sql_query(query, conn)
    
    print("\n--- MECHAM CONTRACT SUMMARY ---")
    print(f"Total Contract Value: $472,812.00")
    print(f"Total Line Items Added: {len(df)}")
    print("\nTop 5 Highest Value Items:")
    
    # Show the top 5 highest value items
    top_5 = df.sort_values(by='total_value', ascending=False).head(5)
    print(top_5.to_string(index=False))
    
    conn.close()

if __name__ == "__main__":
    add_contract_items()
