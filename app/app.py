from flask import Flask, g, render_template, jsonify, Response
from flask_cors import CORS
from flask_restful import Api

import random
from flask import request, jsonify
from flask_restful import Resource, reqparse, inputs
import requests
import logging
from sentiment import Model

logger = logging.getLogger(__name__)



class localFlask(Flask):
    def process_response(self, response):
        #Every response will be processed here first
        response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
        response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'

        return(response)

def create_app():


    logger = logging.getLogger(__name__)
    logger.info('app starts...')

    app = localFlask(__name__,
                template_folder="./static")



    CORS(app)
    api = Api(app)
    model = Model()
    # print(model.predict('hello'))

    @app.route('/')
    def home_page():
        example_embed = 'This string is from python'
        return render_template('index.html', embed=example_embed)

    @app.route('/api', methods=["GET"])
    def get_sendiment():
        print(model.predict('hello'))

        user_text = request.args['text']

        jsonObj = {"msg": "{0}".format('hello')}

        return jsonObj

    return app
