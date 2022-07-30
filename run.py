# absolute imports
import os

# relative imports
from app import create_app

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run(host='192.168.0.6')
