# Flexible Database Design: Artistic Stone Masonry Job Tracker

## Objective
A local SQLite database designed to track bespoke high-end masonry projects with variable billing, procurement, and progress logic.

## 1. Core Tables (The "Flexible" Approach)

### `Projects` (The Anchor)
- `Project_ID`: Primary Key.
- `Project_Name`: (e.g., "The Smith Residence - Pool Deck").
- `Client_Contractor`: Who the contract is with.
- `Billing_Type`: (e.g., "Progress", "Milestone", "Lump Sum").
- `Status`: (Bid, Contracted, Active, Complete, Archived).

### `Bid_Line_Items` (The Scope)
*This table handles both "1,000 sqft of Veneer" AND "Lump Sum for Portico Carving".*
- `Item_ID`: Primary Key.
- `Project_ID`: Foreign Key.
- `Description`: (e.g., "Main House Veneer", "Custom Carved Sinks").
- `Type`: (Material, Labor, Fabrication, Subtotal).
- `Quantity`: (Optional).
- `Unit`: (sqft, tons, each, hrs).
- `Unit_Price`: (Optional).
- `Total_Value`: The contracted amount for this specific line.

### `Procurement_Log` (The Materials)
- `Log_ID`: Primary Key.
- `Project_ID`: Foreign Key.
- `Material_Name`: What was ordered.
- `Quantity`: Amount ordered/received.
- `Status`: (Ordered, Shipped, On-Site, Installed).

### `Labor_and_Progress` (The Work)
- `Entry_ID`: Primary Key.
- `Project_ID`: Foreign Key.
- `Cost_Center`: (Fabrication-Shop vs. Installation-Site).
- `Description`: (e.g., "Setting coping on North wall").
- `Hours`: Time spent.
- `Percent_Complete`: (0-100%).

### `Billing_Log` (The Cash Flow)
- `Invoice_ID`: Primary Key.
- `Project_ID`: Foreign Key.
- `Amount`: Amount invoiced.
- `Date_Sent`: When you billed.
- `Status`: (Draft, Sent, Paid).

## 2. Iteration Strategy
1. **The Spreadsheet Hook**: Our first "Tool" will be a script that reads your **Bid Spreadsheet** and automatically creates the `Projects` and `Bid_Line_Items` entries.
2. **The "Vibe Check"**: Once a project is loaded, we'll manually enter a week's worth of Shop and Site logs to see if the reports (Progress vs. Billing) actually make sense for your workflow.
3. **Refinement**: If a specific contractor requires a weird billing format, we add a "Custom_Field" column to handle it without breaking the rest of the system.
