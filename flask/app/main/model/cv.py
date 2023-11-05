from .. import db
import datetime


class CV(db.Model):
    """
    CV Model for storing CV related details
    """
    
    __tablename__ = 'cv_table'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(500), unique=False, nullable=False)
    contents = db.Column(db.String(4096), unique=False, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, category, contents):
        self.category = category
        self.contents = contents
        self.created_on = datetime.datetime.now()

    def __repr__(self):
        return '<id: category: {}'.format(self.category)