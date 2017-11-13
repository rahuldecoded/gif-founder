# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import requests
import json
 

from engine import search_endpoint_engine, translate_endpoint_engine, trending_endpoint_engine, random_endpoint_engine


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'GET':
		return render_template("index.html")
	elif request.method == "POST":
		api_key = request.form['api_key']
		r = requests.get("http://api.giphy.com/v1/gifs/search?q=cat&api_key={}&limit=1".format(api_key))
		
		if r.status_code != 200 and r.status_code !=403:
		    return render_template("index.html", message=r.status_code)
		elif r.status_code == 403:
			data = r.json()
			return render_template("index.html", message=data['message'])
		else:
			data = r.json()
			return render_template("index.html", message="https://gif-loader.herokuapp.com/" + api_key)


	

@app.route('/<api_key>/search_endpoint', methods=["GET"])
def search_endpoint(api_key):
    locale = request.args.get("lang")
    title = request.args.get("query").replace(" ", "+")
    result = search_endpoint_engine(api_key, title, locale)
    if result != 'fail':
    	send = {
	        "messages": [
	            {
	      		"attachment": {
	        		"type": "image",
	        		"payload": {
	          			"url": "{}".format(result)
	        		}
	      		}
	    	}
	        ]
    	}
    	return jsonify(send)
    elif result == 'fail':
	    send = {
	        "messages": [
	            {
	      		"text": "Couldn't found anything related to that."
	    	}
	        ]
	    }
	    return jsonify(send)


@app.route("/<api_key>/translate_endpoint")
def translate_endpoint(api_key):
    title = request.args.get("query").replace(" ", "+")
    result = translate_endpoint_engine(api_key, title)
    if result != 'fail':
    	send = {
	        "messages": [
	            {
	      		"attachment": {
	        		"type": "image",
	        		"payload": {
	          			"url": "{}".format(result)
	        		}
	      		}
	    	}
	        ]
    	}
    	return jsonify(send)

    elif result == 'fail':
	    send = {
	        "messages": [
	            {
	      		"text": "Couldn't found anything related to that."
	    	}
	        ]
	    }
	    return jsonify(send)


@app.route("/<api_key>/trending_endpoint")
def trending_endpoint(api_key):
    limit = request.args.get("limit", "")

    send = {
    	"messages":[
	    {
	      	"attachment":{
	        	"type":"template",
	        	"payload":{
	          		"template_type":"generic",
			        "elements": trending_endpoint_engine(api_key, limit)
	        }
	      }
	    }
	  ]
    }
    return jsonify(send)


@app.route("/<api_key>/random_endpoint")
def random_endpoint(api_key):
    tag = request.args.get("tag", "")

    result = random_endpoint_engine(api_key, tag)
    send = {
    	"messages":[
	    	{
	     	"attachment": {
	        	"type": "image",
	        	"payload": {
	          		"url": "{}".format(result)
	        	}
	      	} 	
	    }
	  ]
    }
    print(send)
    return jsonify(send)


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RV'
if __name__ == "__main__":
    app.run()

