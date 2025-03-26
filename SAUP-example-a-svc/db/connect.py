import time
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

uri = "mysql+pymysql://root:saup123@db:3306/mysql"

def connect():
    for i in range(10):
        try:
            engine = create_engine(uri)
            with engine.connect() as conn:
                result = conn.execute(text("SELECT NOW()"))
                for row in result:
                    print("DB Connected:", row[0])
            break
        except OperationalError as e:
            print(f"Connection failed (attempt {i+1}/10): {e}")
            time.sleep(5)
    else:
        print("Failed to connect to DB after 10 attempts.")