import boto3
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

ses = boto3.client('ses')

message = MIMEMultipart()
message['Subject'] = 'Incoming Service Request'
message['From'] = 'CCE-Service <service@cce-service.ca>'
message['To'] = ', '.join(['sbrukson@gmail.com', 'alex@ccemedical.com'])
# message body
body_string = 'Submitted By: <br/> Requested Engineer: <br/><br/>'
body_string += 'Date: <br/> Client: <br/> Address: <br/> Systems: <br/> Description: <br/>'

part = MIMEText(body_string, 'html')
message.attach(part)
# attachment
filename = 'attachment_file.docx'
part = MIMEApplication(open(filename, 'rb').read())

part.add_header('Content-Disposition', 'attachment', filename=filename)
message.attach(part)
response = ses.send_raw_email(
    Source=message['From'],
    Destinations=['sbrukson@gmail.com', 'alex@ccemedical.com'],
    RawMessage={
        'Data': message.as_string()
    }
)

print(response)
