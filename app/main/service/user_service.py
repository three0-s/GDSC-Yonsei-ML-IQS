import uuid
import datetime

from app.main.service import save_changes
from app.main.model.user import User
from app.main.model.cv import CV

def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': f'Some error occurred. Please try again. {str(e)}'
        }
        return response_object, 401
    

def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_cv(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    if user:
        cv = CV.query.filter_by(id=user.cv_id).first()
        if cv:
            user.category = cv.category
            user.contents = cv.contents
            save_changes(user)
            return cv, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'CV does not exists. Maybe you shoud try set_cv.',
            }
            return response_object, 409
    else:
        response_object = {
            'status': 'fail',
            'message': 'User does not exist.',
        }
        return response_object, 409



def set_cv(data):
    user = User.query.filter_by(email=data['email']).first()
    if user:
        if user.cv_id and CV.query.filter_by(id=user.cv_id).first():
            response_object = {
                'status': 'fail',
                'message': 'CV already exists. Maybe you shoud try update_cv.',
            }
            return response_object, 409
        else:
            new_cv = CV(
                category=data['category'],
                contents=data['contents'],
            )
            save_changes(new_cv)
            user.cv_id = new_cv.id
            save_changes(user)
            response_object = {
                'status': 'success',
                'message': 'CV successfully added.',
            }
            return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User does not exist.',
        }
        return response_object, 409
    

def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()

