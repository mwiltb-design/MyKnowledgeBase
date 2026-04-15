Source: [[PostgreSQL_Official_About.md]]

## Summary
- **PostgreSQL** is a powerful, open-source object-relational database system with over 35 years of active development.
- Known for its extreme **extensibility**, reliability, and data integrity.
- Supports advanced data types like **JSONB**, **Geospatial (PostGIS)**, and **Vector (pgvector)**.

## Core Characteristics
- **Extensibility**: Allows defining custom data types and functions (including in different programming languages).
- **SQL Compliance**: Conforms closely to the SQL standard while maintaining traditional high-performance features.
- **Data Integrity**: Features multi-version concurrency control (**MVCC**), point-in-time recovery, and write-ahead logging (**WAL**) for fault tolerance.

## Data Types
- **Structured**: Integer, Numeric, String, Boolean, Date/Time, Array, Range, **UUID**.
- **Document**: **JSON/JSONB**, XML, Key-Value.
- **Geospatial**: Point, Line, Circle, Polygon via **PostGIS**.
- **Vector**: High-performance vector similarity search via **pgvector**.

## Use Cases
- High-reliability backend for large-scale web services.
- Analytical workloads and complex data modeling.
- **[[AI Memory]]**: Long-term persistent storage for agent state and embeddings.

---
**See also:** [[SQLite]], [[LanceDB]], [[AI Memory]].
