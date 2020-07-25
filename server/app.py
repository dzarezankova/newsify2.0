from flask import Flask, jsonify
from flask_cors import CORS
import sys
import meaningcloud

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

#API stuff
model = 'IAB_en' #basically specifies that the language is english
key = '9cb4dbf4b67056958232d52630d21988' #to access any API you need to pass your personal key into the request. This is our key
link = 'https://en.wikipedia.org/wiki/Bee_Movie' #yes i am using the plot of the bee movie for the sample text lmao
summary = ''

summarization_response = meaningcloud.SummarizationResponse(meaningcloud.SummarizationRequest(key, sentences=3, url=link).sendReq())
if summarization_response.isSuccessful():
    summary = summarization_response.getSummary()
    print(summary)
else:
    print("\tOops! Request to Summarization was not succesful: (" + summarization_response.getStatusCode() + ') ' + summarization_response.getStatusMsg())

# OPEN http://localhost:5000/ ON YOUR DEVICE AND IT SHOULD DISPLAY THE STRING
@app.route('/', methods=['GET'])
def ping_pong():
    return jsonify(summary)


if __name__ == '__main__':
    app.run()