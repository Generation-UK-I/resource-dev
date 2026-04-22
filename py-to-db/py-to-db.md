# Persisting Data to a Database with Python

## Why Move From CSV to a Database?

CSV files are great for early learning, but they have limitations:

- No concurrency (two users writing at once corrupts data)
- No indexing or fast searching
- No relationships between data
- No data validation
- Hard to scale

A PostgreSQL database solves all of these by providing:
- Structured tables
- Querying with SQL
- Data types (text, numeric, foreign keys)
- ACID guarantees
- Persistence across sessions

## Connecting to a Database

>NOTE: This guide assumes you are using VSCode, if you are working from Jupyter you may need to add `psycopg` to your requirements.txt and restart your environment - *or install it using magics to run bash commands*

### Setup

We have deployed a PostgreSQL database in a Docker container, which is accessible over our network. Now we need a library that let's Python talk to Postgres.

>Optional: Create a virtual environment with python -m venv ./venv then activate it with .venv\Scripts\activate.ps1

Install a PostgreSQL Library for Python with `pip install psycopg
`

### Connecting Python to PostgreSQL

A connection is like opening a communication channel to the database, and when connected a cursor is used to execute SQL commands.

Open a connection to your DB as follows:

```python
import psycopg2

def get_connection():
    return psycopg2.connect(
        host="[DOCKER_VM_IP]",
        port=5432,
        database="postgres",
        user="postgres",
        password="mysecretpassword"
    )
```

- `psycopg2.connect(...)` the connection *method* provided by the `psycopg` library

These values match the Docker container settings, the function can be reused as needed, and if connection fails, Python will raise an exception.

The function returns an object containing all of the connection parameters. Since it's a function it will only execute when called, which could be by a different function which carries out an action against the DB - which we'll do shortly.

### Planning DB Tables

At this point our app has products, couriers, and orders, all as dictionaries. Based on the values and data types, the DB tables might look like this:

```sql
# Products
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price NUMERIC(10,2) NOT NULL
);

# Couriers
CREATE TABLE couriers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
);

# Orders
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name TEXT NOT NULL,
    customer_address TEXT NOT NULL,
    customer_phone TEXT NOT NULL,
    courier_id INTEGER REFERENCES couriers(id),
    status TEXT NOT NULL,
    items TEXT NOT NULL 
);
```

- `serial`: Auto-generates IDs
- `REFERENCES couriers(id)`: creates a foreign key
- `items`: currently includes multiple values (not normalised - fix later)

### Creating SQL DB Tables from Python

We can return a connection object using our `get_connection` function, so to create tables we need to call the function, then execute the above SQL commands, as though we were typing them ourselves through the DBs CLI.

To do so we need to open a `cursor` within our DB, and have Python enter the relevant commands for us.

Below we have a `create_tables()` function, which:

- Calls `get_connection`
- The returned object is stored in the `conn` variable
- We call the `cursor()` method which creates a **cursor object**
- The cursor object has it's own methods it can call.

```py
def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            price NUMERIC(10,2) NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS couriers (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id SERIAL PRIMARY KEY,
            customer_name TEXT NOT NULL,
            customer_address TEXT NOT NULL,
            customer_phone TEXT NOT NULL,
            courier_id INTEGER REFERENCES couriers(id),
            status TEXT NOT NULL,
            items TEXT NOT NULL
        );
    """)

    conn.commit()
    cur.close()
    conn.close()
```

Some of the cursor methods include:

- `.execute()`: Execute SQL Commands - Used to run SQL queries
- `.commit()` Commit Changes: To permanently save the changes following commands that modify data (INSERT/UPDATE/DELETE).
- `.close()`: Close the cursor and connection to free database resources
  - **NOTE**: The `cur` and `conn` objects are both closed.

>Always close cursor + connection

In our case, the cur.execute() lines call the execute method, and pass our `CREATE TABLE...` statements as strings to the database.
