Source: [[PocketBase_Official_Intro.md]]

## Summary
- **PocketBase** is an open-source, all-in-one Go backend built on an embedded **[[SQLite]]** database.
- Features real-time subscriptions, built-in authentication, and a file storage system.
- Distributed as a **single portable binary**, making it ideal for rapid development and "Indie" projects.

## Main Features
- **Realtime Database**: High-performance embedded **[[SQLite]]** with automated migrations and real-time updates.
- **Auth Management**: Out-of-the-box support for Email/Password and OAuth2 (Google, GitHub, etc.).
- **File Storage**: Locally stored or S3-compatible (AWS, B2, MinIO) with automatic image thumbnail generation.
- **Admin Dashboard**: Built-in Svelte-powered UI for managing collections, users, and files without code.

## 2026 Implementation Strategy
- **[[RV Park Digital Strategy]]**: Recommended as the primary backend for the 2026 website implementation due to its "one-file" simplicity and low resource usage.
- **Hosting**: Can be deployed on a minimal $5/month VPS with zero database server overhead.

---
**See also:** [[SQLite]], [[RV Park Digital Strategy]].
