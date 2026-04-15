Source: [[DuckDB_Official_Why.md]]

## Summary
- **DuckDB** is an in-process, columnar-vectorized SQL database designed for **Analytical Processing (OLAP)**.
- "The SQLite for Analytics": Embedded, no external dependencies, and extremely fast for data aggregation.
- Supports querying data directly from **Parquet**, **CSV**, and **JSON** without a separate import step.

## Key Benefits
- **Speed**: Uses a vectorized query engine that processes data in large batches (columnar), making it 100x faster than traditional row-based DBs for math-heavy queries.
- **Flexibility**: Can query data directly from existing **[[PostgreSQL]]** and **[[SQLite]]** databases.
- **In-Process**: Runs inside the host application (e.g., a Python research script), eliminating network latency.

## Applications in PKM
- **[[Metric Definition]]**: Analyzing research logs to calculate project-specific scalar metrics.
- **Data Analysis**: Fast processing of health, wealth, and inventory logs directly within the Wiki structure.

---
**See also:** [[SQLite]], [[PostgreSQL]], [[Metric Definition]].
