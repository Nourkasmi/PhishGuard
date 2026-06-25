from flask import Flask
from config import Config
from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Connect the database to the app
    db.init_app(app)

    # Create all tables inside the app context
    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        return 'PhishGuard is running.'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)