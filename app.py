from flask import Flask, render_template

from api.routes import api_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp, url_prefix="/api")
    
    @app.route("/gallery")
    def gallery():
        return render_template("gallery.html")
    
    return app
