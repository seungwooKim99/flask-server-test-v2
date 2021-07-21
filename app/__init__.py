from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as users_ns
# 각 controller에서 만든 api 함수를 가져와서 아래 blueprint에 등록해서 사용가능하도록

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS(RESTX) API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus (restx) web service'
          )

api.add_namespace(users_ns, path='/user')