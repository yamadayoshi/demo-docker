import mysql.connector
from mysql.connector import errorcode

DATABASE = 'data_py'

name = 'Poty'
age = 34

try:
    db = mysql.connector.connect(
        host='mysql',
        user='root',
        password='123'
    )
    
    print(f"DB ====> {db}")
    
    cursor = db.cursor()

    add_user = (f"INSERT INTO {DATABASE}.users "
                "(name, age) "
                f"VALUES ('{name}', {age})")
    
    cursor.execute(add_user)

    db.commit()
    
    cursor.close()
    db.close()
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print(f"Database {DATABASE} does not exist")
  else:
    print(err)