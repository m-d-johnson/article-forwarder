import datetime
import json
import uuid

import pytz
import requests
from flask import Flask, request

unique_id = uuid.uuid4()
tz = pytz.timezone('Europe/London')
baserow_url = "https://baserow.transsafety.network/api/database/rows/table/315/?user_field_names=true"
headers = {'Authorization': 'Token YN0cIkp610D7vZqnq94Q2AALbsr76lOs', 'Content-Type': 'application/json'}

app = Flask(__name__)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    request_data = request.get_json()
    now = datetime.datetime.now()

    rq = {
        "rule": request_data['rule']['name'],
        "publication_name": request_data['items'][0]['origin']['title'],
        "article_author": request_data['items'][0]['author'],
        "article_title": request_data['items'][0]['title'],
        "article_href": request_data['items'][0]['canonical'][0]['href'],
        "article_date": datetime.datetime.fromtimestamp(request_data['items'][0]['published'], tz).isoformat(),
        "article_content": "This is a placeholder",
        "date_logged": now.strftime("%Y-%m-%dT%H:%M:%SZ"),  # now()
        "reviewed": False,
        "article_id": str(uuid.uuid4())
    }

    req = requests.post(baserow_url, data=json.dumps(rq), headers=headers)

    if req.status_code != 200:
        print("Error:", req.status_code)
    else:
        return json.dumps(req.json(), indent=4)


if __name__ == '__main__':
    app.run()
