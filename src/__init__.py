from .main import get_app
import json  


data = json.load(open('data.json'))

app = get_app(data)

