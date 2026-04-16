import sqlite3
import pandas as pd
from datetime import datetime

def generate_pick_list(job_num):
    db_path = 'Artistic_Stone_Masonry/Masonry_Projects.db'
    conn = sqlite3.connect(db_path)
    
    # 1. Get Project Details
    project_query = f"SELECT project_id, job_number, job_name, stone_selection FROM Projects WHERE job_number LIKE '%{job_num}%'"
    project = conn.execute(project_query).fetchone()
    
    if not project:
        print(f"Error: Job number {job_num} not found.")
        return
        
    project_id, job_num, job_name, stone_type = project
    
    # 2. Fetch Contract Lines to generate procurement items
    lines_query = f"SELECT line_id, description, quantity, unit FROM Contract_Lines WHERE project_id = {project_id}"
    df_lines = pd.read_sql_query(lines_query, conn)
    
    # 3. Categorize items (improved logic)
    def categorize(desc):
        desc = desc.lower()
        # Strictly exclude labor first
        if 'labor' in desc or 'installation' in desc or 'delivery' in desc or 'crane' in desc:
            return 'SKIP'
        
        # Then categorize materials
        if 'stone' in desc or 'veneer' in desc: 
            return 'A. Primary Stone'
        if 'sill' in desc or 'cap' in desc or 'header' in desc or 'eave' in desc: 
            return 'B. Limestone Accents'
        if 'fabrication' in desc or 'custom' in desc or 'surround' in desc: 
            return 'C. Custom Fabrication/Shop'
        return 'D. Other Materials'

    df_lines['Category'] = df_lines['description'].apply(categorize)
    df_order = df_lines[df_lines['Category'] != 'SKIP'].copy()
    
    # 4. Generate Output Path
    report_date = datetime.now().strftime("%Y-%m-%d")
    output_path = f"Artistic_Stone_Masonry/PickList_{job_num}.md"
    
    with open(output_path, 'w') as f:
        f.write(f"# PROCUREMENT PICK LIST: {job_name} (#{job_num})\n")
        f.write(f"**Generated**: {report_date}\n")
        f.write(f"**Primary Stone**: {stone_type or 'See Below'}\n\n")
        
        # Section Header
        categories = sorted(df_order['Category'].unique())
        for cat in categories:
            f.write(f"## {cat}\n")
            f.write("| [ ] | Description | Qty | Unit | Notes |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- |\n")
            
            items = df_order[df_order['Category'] == cat]
            for _, row in items.iterrows():
                f.write(f"| [ ] | {row['description']} | {row['quantity']} | {row['unit']} | |\n")
            f.write("\n")
            
        f.write("---\n")
        f.write("**Instructions**: Use this list to verify against supplier quotes. Check off items once ordered.\n")

    print(f"\nSUCCESS: Pick List generated for {job_name} at {output_path}")
    conn.close()

if __name__ == "__main__":
    # Test with Meachm #25064
    generate_pick_list('25064')
