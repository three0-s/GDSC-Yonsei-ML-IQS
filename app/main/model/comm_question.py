from .. import db



class CommonQuestions(db.Model):
    """
    Common Questions Model for storing Common Questions related details
    """
    
    __tablename__ = 'common_questions_table'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(1024), unique=False, nullable=False)

    def __repr__(self):
        return '<id: category: {}'.format(self.question)