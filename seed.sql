TRUNCATE TABLE products RESTART IDENTITY;

INSERT INTO products
(name, category, price, created_at, updated_at)
SELECT
    'Product ' || number,
    CASE
        WHEN number % 4 = 0 THEN 'Electronics'
        WHEN number % 4 = 1 THEN 'Fashion'
        WHEN number % 4 = 2 THEN 'Books'
        ELSE 'Sports'
    END,
    ROUND((random() * 1000)::numeric, 2),
    NOW() - (number || ' seconds')::interval,
    NOW() - (number || ' seconds')::interval
FROM generate_series(1, 200000) AS number;