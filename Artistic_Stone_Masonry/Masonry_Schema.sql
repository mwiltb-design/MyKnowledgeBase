-- 1. Projects: The master list of all jobs.
CREATE TABLE IF NOT EXISTS Projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_number TEXT UNIQUE NOT NULL,
    job_name TEXT NOT NULL,
    contractor TEXT,
    address TEXT,
    stone_selection TEXT,
    total_contract_value REAL DEFAULT 0.0,
    status TEXT DEFAULT 'Active' -- Active, Complete, Bid
);

-- 2. Sections: Breaks the house down into areas (like your spreadsheet).
CREATE TABLE IF NOT EXISTS Sections (
    section_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    section_name TEXT NOT NULL, -- e.g., 'Four Car Garage', 'Entry Surround'
    FOREIGN KEY (project_id) REFERENCES Projects(project_id)
);

-- 3. Components: The actual items to track (Veneer, Caps, etc.).
CREATE TABLE IF NOT EXISTS Components (
    component_id INTEGER PRIMARY KEY AUTOINCREMENT,
    section_id INTEGER NOT NULL,
    category TEXT, -- e.g., 'Veneer', 'Accents', 'Sills'
    description TEXT,
    quantity REAL,
    unit TEXT, -- e.g., 'SF', 'LF', 'Each'
    progress_status TEXT DEFAULT 'Not Started', -- Not Started, Shop, Site, Installed
    FOREIGN KEY (section_id) REFERENCES Sections(section_id)
);

-- 4. Labor_Logs: Tracking the Fabrication vs. Installation time.
CREATE TABLE IF NOT EXISTS Labor_Logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    cost_center TEXT NOT NULL, -- 'Fabrication' or 'Installation'
    date TEXT NOT NULL,
    hours REAL NOT NULL,
    description TEXT,
    FOREIGN KEY (project_id) REFERENCES Projects(project_id)
);

-- 5. Draws: Tracking the "Progress Billing" and payments.
CREATE TABLE IF NOT EXISTS Draws (
    draw_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    description TEXT,
    amount_billed REAL NOT NULL,
    date_billed TEXT,
    amount_paid REAL DEFAULT 0.0,
    date_paid TEXT,
    status TEXT DEFAULT 'Unpaid',
    FOREIGN KEY (project_id) REFERENCES Projects(project_id)
);
