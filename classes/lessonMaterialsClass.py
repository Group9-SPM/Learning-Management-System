from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class LessonMaterials(db.Model): 
    
    __tablename__ = 'lessonMaterials'

    materialID = db.Column(db.Integer, primary_key=True)
    lessonID = db.Column(db.Integer, db.ForeignKey('lesson.lessonID'), nullable=False)
    content = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


@app.route("/lessonMaterials/<int:lessonID>")
def lessonMaterials_by_lesson(lessonID):
    lessonMaterials = LessonMaterials.query.filter_by(lessonID=lessonID).all()
    if lessonMaterials:
        return jsonify({
            "data": [lessonMaterial.to_dict()
                     for lessonMaterial in lessonMaterials]
        }), 200
    else:
        return jsonify({
            "message": "No lesson materials found."
        }), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)