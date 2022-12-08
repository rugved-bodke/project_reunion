import os 
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
JWT_SECRET_KEY = "c9972c6b-ade0-44e9-8bf2-e729818b18ac"
FERNET_SECRET_KEY = "Kb6LLOs1RjwESyGIq51qEcqyNpfH4Y5AIMcbZxAK6tQ="