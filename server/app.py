from flask import Flask, jsonify, request
from flask_cors import CORS
from mechanize import Browser
import sys
import meaningcloud

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def summarizeArticle(articleURL):
    br = Browser()
    br.open(articleURL)
    article_title = br.title()

    model = 'IAB_en' #basically specifies that the language is english
    key = '9cb4dbf4b67056958232d52630d21988' #to access any API you need to pass your personal key into the request. This is our key
    summary = ''

    summarization_response = meaningcloud.SummarizationResponse(meaningcloud.SummarizationRequest(key, sentences=3, url=articleURL).sendReq())
    if summarization_response.isSuccessful():
        summary = summarization_response.getSummary()
        print(summary)
    else:
        print("\tOops! Request to Summarization was not succesful: (" + summarization_response.getStatusCode() + ') ' + summarization_response.getStatusMsg())


#READING IN THE URL PASSED IN FROM THE FRONT
link = '' #using this page as a placeholder for now

@app.route('/', methods=['GET','POST'])
def test():
    if request.method == 'POST':
        requestData = request.get_json()
        link = requestData['URL']
        summarizeArticle(link)
        return jsonify('IT WORKS')
    else:
        return jsonify('not yet')

if __name__ == '__main__':
    app.run(host="localhost", port=8081, debug=True)