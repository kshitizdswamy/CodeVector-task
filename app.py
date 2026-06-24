from fastapi import FastAPI
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Product API is running",
        "docs": "/docs",
        "products": "/products"
    }


@app.get("/products")
def get_products(
    category: str = None,
    cursor: int = None,
    limit: int = 20
):

    with engine.connect() as connection:

        if category:

            if cursor:

                result = connection.execute(
                    text("""
                    SELECT *
                    FROM products
                    WHERE category = :category
                    AND id < :cursor
                    ORDER BY id DESC
                    LIMIT :limit
                    """),
                    {
                        "category": category,
                        "cursor": cursor,
                        "limit": limit
                    }
                )

            else:

                result = connection.execute(
                    text("""
                    SELECT *
                    FROM products
                    WHERE category = :category
                    ORDER BY id DESC
                    LIMIT :limit
                    """),
                    {
                        "category": category,
                        "limit": limit
                    }
                )

        else:

            if cursor:

                result = connection.execute(
                    text("""
                    SELECT *
                    FROM products
                    WHERE id < :cursor
                    ORDER BY id DESC
                    LIMIT :limit
                    """),
                    {
                        "cursor": cursor,
                        "limit": limit
                    }
                )

            else:

                result = connection.execute(
                    text("""
                    SELECT *
                    FROM products
                    ORDER BY id DESC
                    LIMIT :limit
                    """),
                    {
                        "limit": limit
                    }
                )

        products = []

        for row in result:

            products.append({
                "id": row.id,
                "name": row.name,
                "category": row.category,
                "price": float(row.price)
            })

        return products