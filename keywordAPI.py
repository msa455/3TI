# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, abort, make_response
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

import jieba.analyse

app = Flask(__name__)


# @auth.get_password
# def get_password(username):
#     if username == "tester":
#         return "pass"
#     else:
#         return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({"error":"Unauthorized access:"}),403)

@app.route("/keywords",methods=["GET","POST"])
#@auth.login_required
def keywords():
    if(request.method=="GET"):
        text = request.args.get("text")
        numResults = request.args.get("numResults")
        withWeight = request.args.get("withWeight")

        if(numResults == None):
            numResults = 5
        else:
            numResults = int(numResults)

        if(withWeight=="True"):
            withWeight=True
        else:
            withWeight=False


        jieba_important = jieba.analyse.textrank(text,topK=numResults,withWeight=withWeight)

        return jsonify(jieba_important)
    else:

        req_data = request.get_json()
        text=req_data["text"]
        numResults = 5
        withWeight = False
        if(len(req_data) != 1):
            try:
                numResults = int(req_data["numResults"])
            except KeyError,e:
                print(e)
            try:
                withWeight = req_data["withWeight"]
                if(withWeight == "True" or withWeight=="true"):
                    withWeight = True
            except KeyError,e:
                print(e)



        #test string for checking keyword extraction functionality
        #doc = "今年是马克思诞辰200周年。作为人类最伟大的政治家、思想家和理论家，马克思的理论创造和思想成果涉及方方面面。在新闻领域，他也有独特的经历与特殊的贡献"
        jieba_important = jieba.analyse.textrank(text,topK=numResults,withWeight=withWeight)

        #if jieba_important == []:
        #    abort(404)
        #else:

        return jsonify(jieba_important)



# @app.errorhandler(404)
# def no_keywords(error):
#     return make_response(jsonify({"error":"no keywords"}),404)

if __name__ ==  "__main__":
    app.run(debug=True)
