## ETL Exercise

The ETL Process will be used to carry out the following exercise in Data Analysis.

We have a set of customer sales data that we want to extract information from.

Needs Docker or Podman running a postgres container that we can use to save the data - see also the [Docker](../../docker/) or [databases](../../databases/) or [databases-sot](../../databases-sot/) sessions.

- The [docker-compose.yml](../handouts/docker-compose.yml) used here is the same as for the above mentioned [databases](../../databases/) session.

## Initial setup

1. Setup PostgreSQL database with docker
    1. Change directory to handouts by running `cd handouts`
    1. Spin up a new Postgres and an Adminer container with `docker compose up -d` in the handouts directory
    1. In the browser go to <http://localhost:8080> to open the Adminer UI
        1. Change the database type dropdown to "PostgreSQL"
        1. Enter Server `my-postgres`, Username `postgres`, Database `postgres` and Password(see inside .env file) to log in
        1. You can use this UI to check any SQL you want to run
1. Create a 'test' database in your PostgreSQL by running the sql `CREATE DATABASE test;`

## Using a venv

> You can either re-use an existing venv, or create a new one just for this session. To use an existing one, jump ahead to the `Activate` step below.

1. You can create a virtual environment with python by running:
    - `python3 -m venv .venv` (MacOS / Unix / GitBash)
    - `py -m venv .venv` (Windows)
1. Activate your virtual environment by running:
    - `source .venv/bin/activate` (MacOS / Unix)
    - `.venv\Scripts\activate` (Windows)
    - `source .venv/Scripts/activate` (GitBash)
1. Install the `requirements.txt` file by running:
    - `py -m pip install -r requirements.txt` (Windows)
    - `python3 -m pip install -r requirements.txt` (MacOS / Unix)
    - `python -m pip install -r requirements.txt` (GitBash)

## Task

Write a python script that executes the below steps. 

Make sure work in the file  `solution_start.py` which sets up the database connection.

The SQL of the target tables is in the `handouts/db-scripts/01_sales_schema.sql` file.

### Task 1 - Extract

1. Extract all the data from the `sales_data.csv`. 
    - The columns for the csv are `customer_id`, `purchase_date`, `purchase_amount` and `product_id`.

### Task 2 - Transform

For the transformation you can make SQL queries and run them using the `psycopg` library.

2. Clean that data (minimum requirement is to remove any rows that contain null cells).
3. Filter data for the period 1 December 2020 - 5 December 2020
4. Calculate each customer's total spend
5. Calculate each customer's average spend
6. Calculate how many times each customer has purchased a specific item

### Task 3 - Load

7. Load the results into the database table that is set up by `handouts/db-scripts/01_sales_schema.sql`
    - Have a look at the DB schema file to work out your queries

### Task 4 - Analyse

8. What does the data in the tables tell you about the different customers purchasing habits?
