# Introduction to PocketBase

PocketBase is an open-source Go backend, consisting of an embedded database (SQLite) with realtime subscriptions, built-in auth management, a convenient dashboard UI, and a simple REST-ish API.

## Main Features
- **Realtime Database**: High-performance embedded SQLite database with support for realtime subscriptions and automated migrations.
- **Auth Management**: Manage your app users and their logins via Email/Password or OAuth2 (Google, GitHub, GitLab, etc.).
- **File Storage**: Store files locally or in S3-compatible storage (AWS S3, MinIO, Google Cloud Storage, etc.) with built-in image thumb generation.
- **Admin Dashboard**: A simple and powerful UI to manage your collections, users, and files without writing code.
- **Extendable**: Use it as a standalone app or as a Go/Dart framework to add your own custom business logic.

## Architecture
PocketBase is distributed as a single portable binary. It is built with Go and Svelte. It uses SQLite with the WAL mode enabled to handle high-concurrency workloads.
