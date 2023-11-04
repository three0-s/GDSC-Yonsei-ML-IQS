from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier'),
        'admin': fields.Boolean(description='user admin'),
        'category': fields.String(description='user CV category'),
        'contents': fields.String(description='user CV contents'),
        'specific_question1': fields.String(description='user specific question1'),
        'specific_question2': fields.String(description='user specific question2'),
        'specific_question3': fields.String(description='user specific question3'),
        'specific_question4': fields.String(description='user specific question4')
    })

class CommonQuestionDto:
    api = Namespace('common_question', description='common_question related operations')
    common_question = api.model('common_question', {
        'question': fields.String(required=True, description='common_question question'),
        'id': fields.Integer(description='common_question id'),
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
