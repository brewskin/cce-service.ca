import boto3
S3 = boto3.resource('s3')
S3.Object('cce-service-request','test.docx').upload_file(Filename='test.docx')

