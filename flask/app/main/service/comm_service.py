from app.main import db
from app.main.model.comm_question import CommonQuestions
from app.main.service import save_changes



def get_a_question(id):
    return CommonQuestions.query.filter_by(id=id).first()



def save_question(data):
    question = CommonQuestions(question=data['question'])
    try:
        # insert the added question
        save_changes(question)
        response_object = {
            'status': 'success',
            'message': 'Common question successfully added.'
        }
        return response_object, 200
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': e
        }
        return response_object, 200