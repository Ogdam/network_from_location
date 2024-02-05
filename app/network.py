from flask import Flask, request, jsonify
from .utils import get_legal_projection_coordinates, search_all_nearest_network, format_network_response

app = Flask(__name__)

@app.route("/", methods=['GET'])
def get_address_network():
    address = request.args.get('q')
    if address is None : 
        return jsonify({"code":400,"message":"q is a required parameter"})

    (x, y) = get_legal_projection_coordinates(address=address)
    network_list = search_all_nearest_network(int(x),int(y))
    resp = format_network_response(network_list)
    return jsonify(resp) 

