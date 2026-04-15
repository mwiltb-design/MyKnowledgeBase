import sqlite3
import pandas as pd
from datetime import datetime

def generate_draw(percentage):
    db_path = 'Artistic_Stone_Masonry/Masonry_Projects.db'
    conn = sqlite3.connect(db_path)
    
    # 1. Get Project Details
    project_query = "SELECT project_id, job_number, job_name, contractor, address, total_contract_value FROM Projects WHERE job_number LIKE '%25064%'"
    project = conn.execute(project_query).fetchone()
    project_id, job_num, job_name, contractor, address, total_value = project
    
    # 2. Get Previous Draws to calculate "Already Billed"
    prev_draws = conn.execute("SELECT SUM(amount_billed) FROM Draws WHERE project_id = ?", (project_id,)).fetchone()[0] or 0
    
    # 3. Calculate Current Draw
    draw_amount = total_value * (percentage / 100)
    draw_date = datetime.now().strftime("%m/%d/%Y")
    
    # 4. Generate Invoice Number (e.g., 25064-01)
    draw_count = conn.execute("SELECT COUNT(*) FROM Draws WHERE project_id = ?", (project_id,)).fetchone()[0] + 1
    invoice_num = f"{job_num}-{draw_count:02d}"
    
    # 5. Record the Draw
    conn.execute('''
        INSERT INTO Draws (project_id, description, amount_billed, date_billed, status)
        VALUES (?, ?, ?, ?, ?)
    ''', (project_id, f"Draw #{draw_count}", draw_amount, draw_date, 'Sent'))
    conn.commit()
    
    # 6. Fetch Contract Lines
    lines_query = f"SELECT description, total_value FROM Contract_Lines WHERE project_id = {project_id}"
    df_lines = pd.read_sql_query(lines_query, conn)
    
    # 7. Generate Professional Layout
    output_path = f"Artistic_Stone_Masonry/Invoice_{invoice_num}.md"
    
    with open(output_path, 'w') as f:
        # Header
        f.write("Artistic Stone Masonry & Supply, Inc.  \n")
        f.write("280 N 2000 W, Lindon, UT 84042  \n")
        f.write("801-796-6681 | www.artisticstonemasonry.com  \n\n")
        
        f.write(f"# INVOICE / DRAW REQUEST  \n")
        f.write(f"**Date**: {draw_date} | **Invoice #**: {invoice_num}  \n\n")
        
        # Bill To & Project Info
        f.write("| BILL TO | PROJECT INFO |\n")
        f.write("| :--- | :--- |\n")
        f.write(f"| {contractor} | **Job**: {job_num} {job_name} |\n")
        f.write(f"| Brandon Bodell | **Address**: {address} |\n")
        f.write(f"| 586 Fine Dr, Salt Lake City, UT 84115 | **Contract Value**: ${total_value:,.2f} |\n\n")
        
        # Financial Summary
        f.write("### **Financial Summary**\n")
        f.write(f"- **Original Contract Amount**: ${total_value:,.2f}\n")
        f.write(f"- **Previous Payments Requested**: ${prev_draws:,.2f}\n")
        f.write(f"- **Current Draw ({percentage}%)**: **${draw_amount:,.2f}**\n")
        f.write(f"- **Remaining Balance**: ${(total_value - prev_draws - draw_amount):,.2f}\n\n")
        
        # Line Item Table
        f.write("### **Line Item Breakdown**\n")
        f.write("| Description | Contract Amount | This Draw ({percentage}%) |\n")
        f.write("| :--- | :---: | :---: |\n")
        
        for _, row in df_lines.iterrows():
            line_val = row['total_value'] * (percentage / 100)
            f.write(f"| {row['description']} | ${row['total_value']:,.2f} | ${line_val:,.2f} |\n")
            
        f.write(f"\n\n**Please make checks payable to**: Artistic Stone Masonry & Supply, Inc.  \n")
        f.write(f"*A Finance Charge will be assessed on all PAST DUE INVOICES.*  \n\n")
        f.write(f"**Authorized Signature**: ________________________  **Date**: __________\n")
    
    print(f"\nSUCCESS: Professional Invoice {invoice_num} generated at {output_path}")
    conn.close()

if __name__ == "__main__":
    # You can change the percentage here
    generate_draw(50)
