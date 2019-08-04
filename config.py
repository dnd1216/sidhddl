from sqlalchemy import create_engine, text

db = {
    'user' : 'root',
    'password' : '12345678',
    'host' : 'localhost',
    'port' : 3306,
    'database' : 'miniter'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"

JWT_SECRET_KEY = 'HELLO_MY_SECRET'



## db_url = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}?charset=utf8"
##db = create_engine(db_url, encoding = 'utf-8', max_overflow = 0)


##params = {'name' : '임나연'}
##rows = db.execute(text("SELECT * FROM users WHERE name = :name"),params).fetchall()

##for row in rows:
    ##print(f"name : {row['name']}")
    ##print(f"email : {row['email']}")
    