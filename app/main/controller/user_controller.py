from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto
from app.main.util.decorator import token_required, admin_token_required
from ..service.user_service import save_new_user, get_all_users, get_a_user, set_cv, get_cv

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    @admin_token_required
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/cv/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class UserCV(Resource):
    @api.doc('get cv of a user')
    @api.marshal_with(_user)
    @api.response(201, 'CV successfully retrieved.')
    @admin_token_required
    def get(self, public_id):
        """get cv of a user"""
        return get_cv(public_id)
    
    @api.response(201, 'CV successfully added.')
    @api.doc('Set CV for a user')
    @api.expect(_user, validate=True)
    @token_required
    def post(self):
        """set cv for a user """
        data = request.json
        return set_cv(data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    @admin_token_required
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user
        