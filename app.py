from flask import Flask
from config import Config
from models import db
from routes.tracking import tracking_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Connect the database
    db.init_app(app)

    # Register blueprints (route groups)
    app.register_blueprint(tracking_bp)

    # Create tables
    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        return 'PhishGuard is running.'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)