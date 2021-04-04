####################################################################################
#!/usr/bin/env python
####################################################################################
from flask import  abort, Flask, g, jsonify, redirect, request, send_from_directory, url_for, render_template
from flask_cors import CORS, cross_origin
####################################################################################
DEBUG_FLAG = True
####################################################################################
app = Flask(__name__, static_url_path='/static')
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/": {"origins": '*'}
							})


####################################################################################
###UI will call this URL,
####################################################################################
@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')
####################################################################################
if __name__ == '__main__':
	app.run()
####################################################################################