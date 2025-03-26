from app import create_app
from db.connect import connect 
app = create_app()

if __name__ == "__main__":
    connect()
    app.run(host="0.0.0.0", port=5000)