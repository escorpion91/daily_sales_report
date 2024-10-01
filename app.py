import os
from query import execute_sql_query
from sms import send_sms
from dotenv import load_dotenv

load_dotenv()

recipient_number = os.getenv('RECIPIENT_NUMBER')

total_sales_df = execute_sql_query()

total_sales = total_sales_df.at[0, 'total_sales']
total_invoices = total_sales_df.at[0, 'total_invoices']

send_sms(recipient_number, total_sales, total_invoices)
