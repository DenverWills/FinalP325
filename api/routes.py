from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__)

@api_bp.route("/dinosaurs", methods=["GET"])
def get_dinosaurs():
    dinos = [
        {"name": "T-Rex", "image": "/static/images/trex.jpg"},
        {"name": "Stegosaurus", "image": "/static/images/stego.jpg"},
        {"name": "Velociraptor", "image": "/static/images/veloc.jpg"},
        {"name": "Triceratops", "image": "/static/images/tri.jpg"},
        {"name": "Brontosaurus", "image": "/static/images/bronto.jpg"},
        {"name": "Pteranodon", "image": "/static/images/ptera.jpg"}
    ]
    return jsonify(dinos)
