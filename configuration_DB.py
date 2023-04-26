import pymssql

SERVER_NAME = 'EPUALVIW08B4\\SQLEXPRESS01'
DATABASE_NAME = 'TRN'
UID = 'TestLogin'
PWD = '123Password!'

conn = pymssql.connect(server=SERVER_NAME, user=UID, password=PWD, database=DATABASE_NAME)
