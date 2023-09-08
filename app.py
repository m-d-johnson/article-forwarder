from flask import Flask, request

app = Flask(__name__)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    request_data = request.get_json()
    article_author = request_data['items'][0]['author']
    publication = request_data['items'][0]['origin']['title']
    article_title = request_data['items'][0]['title']
    response = article_title + " (" + article_author + " for " + publication + ")"
    print(request.method)
    return response


if __name__ == '__main__':
    app.run()
