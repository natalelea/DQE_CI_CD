import pymssql

SERVER_NAME = 'EPUALVIW08B4\\SQLEXPRESS01'
DATABASE_NAME = 'TRN'
UID = 'TestLogin'
PWD = '123Password!'

conn = pymssql.connect(server=SERVER_NAME, user=UID, password=PWD, database=DATABASE_NAME)
# cursor = conn.cursor(as_dict=True)
#
# cursor.execute('SELECT max([salary]) as max_sal FROM [TRN].[hr].[employees]')
# for row in cursor:
#     print(row['max_sal'])

# conn.close()
