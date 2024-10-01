import os
import pyodbc
import pandas as pd
import numpy as np
from dotenv import load_dotenv

load_dotenv()

def execute_sql_query():
    pd.set_option('display.max_columns', None)

    server = os.getenv('SERVER')
    database = os.getenv('DATABASE')
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    connection = pyodbc.connect(connection_string)

    total_query = """
        SELECT SUM(totord) AS total_sales, COUNT(invnum) AS total_invoices
        FROM dbo.fa_ventas_cabecera
        WHERE CAST(invfec AS DATE) = CAST(GETDATE() AS DATE)  -- Filter records for the current day
        AND siscod = 1;  -- Filter records for siscod value of 1
    """

    total_result = pd.read_sql_query(total_query, connection)

    connection.close()

    if total_result.empty:
        total_result = pd.DataFrame([np.nan], columns=['total_sales'])

    return total_result
