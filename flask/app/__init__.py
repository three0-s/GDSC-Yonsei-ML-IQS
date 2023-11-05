# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.comm_controller import api as common_question_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='GDSC@Yonsei-2023 ML/AI IQS (Interview Question Suggestion) API WITH JWT',
          version='0.1',
          description='A simple REST API service implemented in Flask, for interview question suggestion project from GDSC@Yonsei-2023 ML/AI Team.'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(common_question_ns, path='/common_question')