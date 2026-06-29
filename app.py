from flask import Flask
from config import Config
from models import db
from routes.tracking import tracking_bp
from routes.landing import landing_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Connect the database
    db.init_app(app)

    # Register blueprints (route groups)
    app.register_blueprint(tracking_bp)
    app.register_blueprint(landing_bp)

    # Create tables
    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        return 'PhishGuard is running.'

    @app.route('/awareness')
    def awareness():
        return 'This was a phishing simulation. Stay alert!'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)