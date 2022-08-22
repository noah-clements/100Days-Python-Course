import toml
from twilio.rest import Client
from flight_data import FlightData
import smtplib
from email.message import EmailMessage



class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    pass
    def __init__(self) -> None:
        config = toml.load(".project_config")
        self.client = Client(config['Twilio']['account_sid'], config['Twilio']['auth_token'])
        self.from_num = config['Twilio']['from_']
        self.to_num = config['Twilio']['to_']
        self.email = config['EMail']['address']
        self.email_pwd = config['EMail']['pwd']
        self.smtp = config['EMail']['smtp']
        self.port = config['EMail']['port']

    def send_flight_alert(self, flight: FlightData):
        message = self.client.messages \
                .create(
                    body=f"Low Price Alert! {flight}",
                    from_=self.from_num,
                    to=self.to_num
                )
        print(message.status)

    def send_flight_email(self, flight: FlightData, first_name, last_name, email):
        with smtplib.SMTP(self.smtp, port=self.port) as connection:
            connection.starttls()
            connection.login(self.email, password=self.email_pwd)
            connection.sendmail(from_addr=self.email, to_addrs=email,
                                msg=f"Subject:Low Price Alert!\n\n{flight}")

    def send_emails(self, flight: FlightData, users: list):
       
        msg = EmailMessage()
        msg['Subject'] = "New Low Price Flight!"
        msg['From'] = self.email
        msg['Bcc'] = [user['email'] for user in users]
        msg.set_content(f"Low Price Alert!\n\n{flight}") 
        
        with smtplib.SMTP(self.smtp, port=self.port) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.email_pwd)
            connection.send_message(msg)        

