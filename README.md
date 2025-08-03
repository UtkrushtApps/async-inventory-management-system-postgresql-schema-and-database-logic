# Async Inventory Management System: PostgreSQL Schema and Logic

## Task Overview
You will work with an inventory management FastAPI application where fully functional API routes for adding and listing products are already defined. The business requires a robust, normalized PostgreSQL schema and async database connectivity, so products can be stored, queried, and managed efficiently in real-time.

## Guidance
- The FastAPI app and API routing are already implemented and should not be altered.
- Begin by inspecting the `/root/task/app/db/` and `/root/task/app/routes/` directories to understand what database methods you must implement and where.
- Focus only on the following files: `schema.sql` (for schema design), `app/db/async_db.py` (for async DB logic), and `data/sample_data.sql` (for inserting sample product data).
- All SQL queries in your logic must be async/non-blocking using asyncpg.
- Ensure your schema supports future extension (for example, new categories) and prevents data duplication with proper constraints.
- Sample data should enable realistic product listings through API endpoints.

## Database Access
- Host: `<DROPLET_IP>`
- Port: 5432
- Database: inventory
- Username: inventory_user
- Password: Inv3nt0ryPwd
- You may use any PostgreSQL-compatible client (psql, pgAdmin, DBeaver) for direct DB access and validation.

## Objectives
- Design the `products` table (plus any supporting tables like categories if you deem necessary) with primary keys, appropriate constraints, and indices for efficient lookups.
- Implement async-compatible (non-blocking) PostgreSQL data access logic for creating and fetching product records in the provided `app/db/async_db.py` file.
- Ensure sample data in `sample_data.sql` allows both insertion and query testing.
- Allow only valid, non-duplicate products to be inserted.
- API endpoints for creating and listing inventory items must work seamlessly using your async DB code and schema.

## How to Verify
- After starting the stack and adding schema and sample data, use the `/products/` API endpoint to view the product list; new items added via `/products/` should appear instantly.
- Duplicate product names (within the same category) should be rejected per schema constraints.
- Listing products should display all relevant fields (name, category, quantity, price, creation timestamp).
- Check index efficiency for product listing (check via EXPLAIN in psql if interested).
- Ensure API does not block—multiple concurrent requests should be handled smoothly.
