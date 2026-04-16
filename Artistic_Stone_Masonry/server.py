from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import sqlite3
import os

app = FastAPI(title="StoneLedger A2UI Server")

DB_PATH = 'Artistic_Stone_Masonry/Masonry_Projects.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/api/ui/dashboard")
async def get_dashboard_ui():
    conn = get_db_connection()
    
    # 1. Fetch Aggregated Metrics
    total_contract = conn.execute("SELECT SUM(total_contract_value) FROM Projects").fetchone()[0] or 0
    total_billed = conn.execute("SELECT SUM(amount_billed) FROM Draws").fetchone()[0] or 0
    total_paid = conn.execute("SELECT SUM(amount_paid) FROM Draws").fetchone()[0] or 0
    
    # 2. Fetch Active Projects List
    projects = conn.execute("SELECT job_number, job_name, contractor, total_contract_value, status FROM Projects WHERE status = 'Active' LIMIT 10").fetchall()
    
    conn.close()

    # 3. Construct A2UI Adjacency List (v0.8)
    # The A2UI protocol uses a flat list of components
    ui_payload = {
        "type": "surface",
        "id": "stoneledger-main",
        "components": [
            {
                "id": "page-header",
                "type": "Header",
                "props": {
                    "title": "StoneLedger Dashboard",
                    "subtitle": "Artistic Stone Masonry & Supply, Inc."
                }
            },
            {
                "id": "metrics-row",
                "type": "Row",
                "props": { "spacing": "medium" },
                "children": ["metric-contracted", "metric-billed", "metric-paid"]
            },
            {
                "id": "metric-contracted",
                "type": "MetricCard",
                "props": {
                    "label": "Total Contracted",
                    "value": f"${total_contract:,.2f}",
                    "icon": "handshake"
                }
            },
            {
                "id": "metric-billed",
                "type": "MetricCard",
                "props": {
                    "label": "Total Billed",
                    "value": f"${total_billed:,.2f}",
                    "icon": "invoice"
                }
            },
            {
                "id": "metric-paid",
                "type": "MetricCard",
                "props": {
                    "label": "Total Paid",
                    "value": f"${total_paid:,.2f}",
                    "icon": "payments"
                }
            },
            {
                "id": "projects-section",
                "type": "Section",
                "props": { "title": "Active Projects (Top 10)" }
            },
            {
                "id": "projects-table",
                "type": "DataTable",
                "props": {
                    "columns": [
                        {"key": "job_number", "label": "Job #"},
                        {"key": "job_name", "label": "Project Name"},
                        {"key": "contractor", "label": "Contractor"},
                        {"key": "total_contract_value", "label": "Value"}
                    ],
                    "rows": [dict(p) for p in projects]
                }
            }
        ]
    }
    
    return ui_payload

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("Artistic_Stone_Masonry/dashboard.html", "r") as f:
        return f.read()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
