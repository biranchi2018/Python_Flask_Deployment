
'''
    https://towardsdatascience.com/deploying-keras-deep-learning-models-with-flask-5da4181436a2
'''

# load Flask 
import flask
app = flask.Flask(__name__)

# define a predict function as an endpoint 
@app.route("/", methods=["GET","POST"])
@app.route("/predict", methods=["GET","POST"])
def predict():
    data = {"success": False}

    # get the request parameters
    params = flask.request.json
    print("flask.request.json : ", flask.request.json)
    print("flask.request.args : ", flask.request.args)

    if (params == None):
        params = flask.request.args
    
    # if parameters are found, echo the msg parameter 
    if (params != None):
        data["response"] = params.get("msg")
        data["success"] = True
    
    # return a response in json format 
    return flask.jsonify(data)

# start the flask app, allow remote connections
app.run(host='0.0.0.0')



'''

# Browser 
http://localhost:5000/predict?msg=HelloWorld

# Curl
curl -X POST -H "Content-Type: application/json" -d "{ \"msg\":\"Hello World\" }" http://localhost:5000/predict

# Response 
{
  "response": "Hello World",
  "success": true
}

'''