from app import create_app
import os

app = create_app()

if os.environ.get("ENV") == "development" and __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
