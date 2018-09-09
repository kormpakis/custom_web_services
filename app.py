from flask import Flask, jsonify

from request_utilities import get_wordpress_post_info
from utilities import select_interest_array, select_interest_by_user, select_interest_by_tags, \
    select_interest_by_user_tag

app = Flask(__name__)

## WORDPRESS INFO ###
protocol = "http"
host = "localhost/wordpress"
base_url = "{}://{}/wp-json/wp/v2/posts/".format(protocol, host)
media_url = "{}://{}/wp-json/wp/v2/media/".format(protocol, host)


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


@app.route('/post/<post_id>/info/', methods=['GET'])
def get_post_info(post_id):
    results = get_wordpress_post_info(post_id, base_url, media_url)
    if results:
        result_json = {"title": results[0], "post_url": results[1], "image_url": results[2]}
        return jsonify(items=result_json)
    else:
        return jsonify(items={"response": "Not found"})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
