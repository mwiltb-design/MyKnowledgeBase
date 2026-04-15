# Why DuckDB?

DuckDB is an in-process SQL OLAP database management system. It is designed to be fast, reliable, and easy to use.

## Key Benefits
- **Simple Installation**: DuckDB has no external dependencies. It is distributed as a single C++ header/source pair or as pre-compiled binaries for all major platforms.
- **Feature Rich**: It supports a large subset of SQL, including complex joins, window functions, and advanced data types.
- **Speed**: DuckDB contains a columnar-vectorized query execution engine, where queries are not interpreted row-by-row but in large batches. This makes it extremely fast for analytical queries.
- **Flexibility**: DuckDB can query data directly from Parquet, CSV, and JSON files without an explicit import step. It can also query data directly from Postgres and SQLite databases.
- **In-Process**: There is no server to manage. The database runs inside the host process (e.g., your Python script or CLI tool), ensuring no network latency between the app and the data.
