from flask import Flask, jsonify

from utilities import select_interest_array, select_interest_by_user, select_interest_by_tags, \
    select_interest_by_user_tag

app = Flask(__name__)


@app.route('/interests/', methods=['GET'])
def get_interest():
    results = select_interest_array()
    items = []
    for result in results:
        result_json = {"user_id": result[0], "tags_id": result[1], "count_tags": result[2]}
        items.append(result_json)
    return jsonify(items=items)


@app.route('/user/<id>/interests/', methods=['GET'])
def get_user_interest(id):
    results = select_interest_by_user(id)
    items = []
    if results:
        for result in results:
            result_json = {"user_id": result[0], "tags_id": result[1], "count_tags": result[2]}
            items.append(result_json)
        return jsonify(items=items)
    else:
        return jsonify(items={"response": "Not found"})


@app.route('/tag/<id>/interests/', methods=['GET'])
def get_tag_interest(id):
    results = select_interest_by_tags(id)
    items = []
    if results:
        for result in results:
            result_json = {"user_id": result[0], "tags_id": result[1], "count_tags": result[2]}
            items.append(result_json)
        return jsonify(items=items)
    else:
        return jsonify(items={"response": "Not found"})


@app.route('/user/<user_id>/tag/<tags_id>/interests/', methods=['GET'])
def get_user_tag_interest(user_id, tags_id):
    results = select_interest_by_user_tag(user_id, tags_id)
    items = []
    if results:
        for result in results:
            result_json = {"user_id": result[0], "tags_id": result[1], "count_tags": result[2]}
            items.append(result_json)
        return jsonify(items=items)
    else:
        return jsonify(items={"response": "Not found"})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
