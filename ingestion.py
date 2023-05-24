import snowflake.connector
import pandas as pd

# Snowflake connection parameters
snowflake_params = {
    'user': '**********',
    'password': '************',
    'account': '************',
    'warehouse': 'COMPUTE_WH',
    'database': 'AMERIGAS',
    'schema': 'PUBLIC'
}

# CSV file path
csv_path = '/Users/sidharthaannamaneni/Downloads/p3_data.csv'

# Snowflake table name
table_name = 'FEEDBACK'

# Create a Snowflake connection
conn = snowflake.connector.connect(**snowflake_params)

# Create a Snowflake cursor
cur = conn.cursor()
print("connected to snowflake")


try:
    stage_name = 'temp_stage'
    create_stage = f"CREATE TEMPORARY STAGE {stage_name}"
    cur.execute(create_stage)

    put_sql = f"PUT file://{csv_path} @{stage_name}"
    cur.execute(put_sql)
    print("file pushed to stage from local")

    copy_cmd = f"COPY INTO {table_name} FROM @{stage_name}/p3_data.csv FILE_FORMAT=(TYPE=CSV, FIELD_DELIMITER=',', SKIP_HEADER=1)"
    cur.execute(copy_cmd)
    print("file written to table")

    conn.commit()
except snowflake.connector.errors.DatabaseError as e:
    print(f"Error {e}")
finally:
    cur.close()
    conn.close()




