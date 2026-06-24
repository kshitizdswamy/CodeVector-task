# Product Browser Backend

Backend task built using FastAPI and PostgreSQL.

## Features

* 200,000 generated products
* Category filtering
* Cursor-based pagination
* PostgreSQL (Neon)
* FastAPI
* Hosted on Render

## Live URL

https://codevector-task-q7i5.onrender.com

## API Endpoints

* GET /products
* GET /docs

## Running Locally

pip install -r requirements.txt

uvicorn app:app --reload

## Data Generation

The seed.sql file generates the dataset using PostgreSQL generate_series.
