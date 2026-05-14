############################################################
#
# ETL example start
#
############################################################

import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")

try:
    ### SETUP THE DATABASE CONNECTION
    print('Opening connection...')
    conn_string = f'host={host_name} dbname={database_name} user={user_name} password={user_password}'
    # Establish a database connection
    with psycopg2.connect(conn_string) as connection:

        print('Opening cursor...')
        cursor = connection.cursor()

    # Create tables including staging_table 
    cursor.execute("""
        CREATE TEMP TABLE staging_sales (
            customer_id text,
            purchase_date text,
            purchase_amount text,
            product_id text
        );
        
        CREATE TABLE IF NOT EXISTS sales_data (
            customer_id int NOT NULL,
            purchase_date date,
            purchase_amount decimal(19,2),
            product_id varchar(10)
        );

        CREATE TABLE IF NOT EXISTS customer_spend (
            customer_id int NOT NULL,
            average_spend decimal(19,2),
            total_spend decimal(19,2)
        );

        CREATE TABLE IF NOT EXISTS customer_products (
            customer_id int NOT NULL,
            product_id varchar(10),
            quantity int
        );
    """)
    
    ### Task 1.1 - EXTRACT
    # 1. Read the sales_data.csv 
    # Load CSV into staging
    with open('sales_data.csv', 'r') as f:
        next(f)  # Skip header
        cursor.copy_from(f, 'staging_sales', sep=',', null='')
    
    # 2. Clean that data (minimum requirement is to remove any rows that contain null cells).
    cursor.execute("""
        DELETE FROM staging_sales 
        WHERE customer_id IS NULL 
        OR customer_id = ''
        OR purchase_amount IS NULL 
        OR purchase_amount = '';
    """)
    
    # 3. Filter data for the period 1 December 2020 - 5 December 2020
    cursor.execute("""
        DELETE FROM staging_sales 
        WHERE TO_DATE(purchase_date, 'YYYY-MM-DD') 
            NOT BETWEEN '2020-12-01' AND '2020-12-05';
    """)

    # 7. Load the transformed data to the created tables
    cursor.execute("""
        INSERT INTO sales_data (customer_id, purchase_date, purchase_amount, product_id)
        SELECT 
            customer_id::int,
            TO_DATE(purchase_date, 'YYYY-MM-DD'),
            purchase_amount::decimal(19,2),
            NULLIF(product_id, '')
        FROM staging_sales
        WHERE product_id IS NOT NULL AND product_id != '';
    """)

    # 4. Calculate each customer's total spend
    # 5. Calculate each customer's average spend
    cursor.execute("""
        INSERT INTO customer_spend (customer_id, average_spend, total_spend)
        SELECT 
            customer_id,
            ROUND(AVG(purchase_amount), 2) as average_spend,
            ROUND(SUM(purchase_amount), 2) as total_spend
        FROM sales_data
        GROUP BY customer_id
        ORDER BY customer_id;
    """)
    
    # 6. Calculate how many times each customer has purchased a specific item
    cursor.execute("""
        INSERT INTO customer_products (customer_id, product_id, quantity)
        SELECT 
            customer_id,
            product_id,
            COUNT(*) as quantity
        FROM sales_data
        WHERE product_id IS NOT NULL
        GROUP BY customer_id, product_id
        ORDER BY customer_id, product_id;
    """)

    connection.commit()

    print('Closing cursor...')
    # Closes the cursor so will be unusable from this point
    cursor.close()
    
    print('Closing connection...')
    
    # The connection will automatically close here 
except Exception as ex:
    print('Failed to:', ex)

# Leave this line here!
print('All done!')
