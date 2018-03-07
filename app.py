import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps({'data': 'from the data layer'})

if __name__ == '__main__':
    main()
