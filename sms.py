import os
from twilio.rest import Client
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')


client = Client(account_sid, auth_token)

def send_sms(recipient_number, total_sales, total_invoices):
    try:
       
        average_transaction = total_sales / total_invoices

        message_body = f"REPORTE MATRIZ {datetime.today().strftime('%Y-%m-%d')}\n"
        message_body += f"Ventas: ${total_sales}\n"
        message_body += f"Facturas: {total_invoices}\n"
        message_body += f"TP: {average_transaction:.2f}"

        
        message = client.messages.create(
            body=message_body,
            from_='+19316832098',  
            to=recipient_number  
        )
        print(f"SMS sent successfully! SID: {message.sid}")
        return True
    except Exception as e:
        print(f"Failed to send SMS: {e}")
        return False
