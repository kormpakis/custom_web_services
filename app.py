from flask import Flask, jsonify

from utilities import select_interest_array

app = Flask(__name__)


@app.route('/interests/', methods=['GET'])
def get_interest():
    results = select_interest_array()
    items = []
    for result in results:
        result_json = {"user_id": result[0], "tags_id": result[1], "count_tags": result[2]}
        items.append(result_json)
    return jsonify(items=items)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
