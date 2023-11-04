from flask import request
from flask_restplus import Resource
from ..util.dto import CommonQuestionDto
from app.main.util.decorator import token_required, admin_token_required
from ..service.comm_service import save_question, get_a_question

api = CommonQuestionDto.api
cq = CommonQuestionDto.common_question


@api.route('/<q_id>')
@api.param('q_id', 'The common question identifier')
@api.response(404, 'Question not found.')
class GetACommonQuestion(Resource):
    @api.doc('get a common question')
    @api.marshal_with(cq)
    def get(self, q_id):
        """get a common question given its identifier"""
        q = get_a_question(q_id)
        if not q:
            api.abort(404)
        else:
            return q


@api.route('/')
class SaveCommonQuestion(Resource):
    @api.response(201, 'Question successfully created.')
    @api.doc('create a new question')
    @api.expect(cq, validate=True)
    def post(self):
        """Creates a new Question """
        data = request.json
        return save_question(data=data)

