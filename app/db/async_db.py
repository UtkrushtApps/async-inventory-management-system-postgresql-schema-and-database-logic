import asyncpg
import asyncio

class AsyncDBConnection:
    def __init__(self):
        self.pool = None

    async def init_pool(self):
        if not self.pool:
            self.pool = await asyncpg.create_pool(
                host='db',
                port=5432,
                user='inventory_user',
                password='Inv3nt0ryPwd',
                database='inventory',
                min_size=1,
                max_size=10
            )

    async def fetch_products(self):
        async with self.pool.acquire() as conn:
            rows = await conn.fetch('SELECT id, name, category, quantity, price, created_at FROM products ORDER BY id;')
            return [dict(row) for row in rows]

    async def add_product(self, name:str, category:str, quantity:int, price:float):
        async with self.pool.acquire() as conn:
            try:
                product_id = await conn.fetchval(
                    'INSERT INTO products (name, category, quantity, price) VALUES ($1, $2, $3, $4) RETURNING id;',
                    name, category, quantity, price
                )
                return product_id
            except asyncpg.UniqueViolationError:
                return None

db = AsyncDBConnection()
