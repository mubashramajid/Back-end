from flask import jsonify
from src.app import app


@app.route("/error422")
@app.errorhandler(422)
@app.errorhandler(400)
def handle_validation_error(error):
    headers = error.data.get("headers", None)
    messages = error.data.get("messages", ["Invalid request."])
    if headers:
        return jsonify({"errors": messages}), error.code, headers
    else:
        return jsonify({"errors": messages}), error.code


@app.route("/error404")
@app.errorhandler(404)
def handle_method_error(error):
    return jsonify({"error": error.description}), error.code
