import argparse
from flask import Flask, jsonify, make_response
from flask_httpauth import HTTPBasicAuth
import requests
import conf

app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    """Checking login and password"""
    if username == login:
        return password
    return None


@auth.error_handler
def unauthorized():
    """Handling incorrect credentials"""
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


@app.route('/googler/api/text/<string:search_request>', methods=['GET'])
@auth.login_required
def text_search(search_request):
    """Getting text search results"""
    response = requests.get(
        f"https://customsearch.googleapis.com/customsearch/v1?cx={conf.cse_id}&exactTerms={search_request}\
        &key={conf.api_key}&num=10")
    items = [
        {
            "title": i['title'],
            "info": i['snippet'],
            "link": i['link']
        }
        for i in response.json()['items']
    ]
    return jsonify(results=items)


@app.route('/googler/api/image/<string:search_request>', methods=['GET'])
@auth.login_required
def image_search(search_request):
    """Getting image search results"""
    response = requests.get(
        f"https://customsearch.googleapis.com/customsearch/v1?searchType=image&cx={conf.cse_id}&exactTerms={search_request}\
        &key={conf.api_key} &num=10")
    items = [
        {
            "source": i['displayLink'],
            "info": i['snippet'],
            "size": {
                "height": i['image']['height'],
                "width": i['image']['width']
            },
            "link": i['link'],
            "context": i['image']['contextLink']
        }
        for i in response.json()['items']
    ]
    return jsonify(results=items)


if __name__ == '__main__':
    # Parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', help='Port number', nargs='?', type=int, const=5000, default=5000)
    parser.add_argument('--login', help='Login', nargs='?', type=str, const='admin', default='admin')
    parser.add_argument('--password', help='Password', nargs='?', type=str, const='System1!', default='System1!')
    port = parser.parse_args().port
    login = parser.parse_args().login
    password = parser.parse_args().password
    app.run(port=port)
