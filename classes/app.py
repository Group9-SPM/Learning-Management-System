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

#EMPLOYEE
class Employee(db.Model): 

    __tablename__ = 'employee'

    empID = db.Column(db.Integer, primary_key=True)
    empName = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    roleType = db.Column(db.String(1), nullable=False)

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

#LEARNER
class Learner(Employee): 

    __tablename__ = 'learner'

    badges = db.Column(db.String(300))
    empID = db.Column(db.Integer, db.ForeignKey(Employee.empID), primary_key=True)
    
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

#course
class Course(db.Model): 

    __tablename__ = 'course'

    courseID = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String(100), nullable=False)
    courseDesc = db.Column(db.String(500), nullable=False)
    courseDuration = db.Column(db.String(50), nullable=False)

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

#CLASSES
class Classes(db.Model): 
    
    __tablename__ = 'classes'

    classID = db.Column(db.Integer, primary_key=True)
    startDate = db.Column(db.DateTime, nullable=False)
    endDate = db.Column(db.DateTime, nullable=False)
    size = db.Column(db.Integer, nullable=False)
    startTime = db.Column(db.String(20), nullable=False)
    endTime = db.Column(db.String(20), nullable=False)
    minSlot = db.Column(db.Integer, nullable=False)
    maxSlot = db.Column(db.Integer, nullable=False)
    regStartDate = db.Column(db.DateTime, nullable=False)
    regEndDate = db.Column(db.DateTime, nullable=False)
    courseID = db.Column(db.Integer, db.ForeignKey(Course.courseID))
    trainerID = db.Column(db.Integer, db.ForeignKey(Employee.empID))
    
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

#classlist
class ClassList(db.Model): 

    __tablename__ = 'classList'

    classID = db.Column(db.Integer, db.ForeignKey(Classes.classID), primary_key=True)
    learnerID = db.Column(db.Integer, db.ForeignKey(Learner.empID), nullable=False)
    progressPercentage = db.Column(db.Integer, nullable=False)
    finalQuizGrade = db.Column(db.String(5))

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

#ENROLMENTLIST
class EnrolmentList(db.Model): 

    __tablename__ = 'enrolmentList'

    classID = db.Column(db.Integer, db.ForeignKey(Classes.classID), primary_key=True)
    learnerID = db.Column(db.Integer, db.ForeignKey(Learner.empID), nullable=False)
    courseID = db.Column(db.Integer, db.ForeignKey(Course.courseID), nullable=False)
    enrolmentStatus = db.Column(db.String(100), nullable=False)

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


#PREREQ
class Prerequisite(db.Model):
    __tablename__ = 'prerequisite'

    courseID = db.Column(db.Integer, db.ForeignKey(Course.courseID) ,primary_key=True)
    prerequisiteID = db.Column(db.Integer, primary_key=True)

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


#LESSON CLASS
class Lesson(db.Model):
    __tablename__ = 'lesson'

    lessonID = db.Column(db.Integer, primary_key=True)
    lessonNum = db.Column(db.Integer, nullable=False)
    classID = db.Column(db.Integer, db.ForeignKey(Classes.classID), nullable=False)
    courseID = db.Column(db.Integer, db.ForeignKey(Course.courseID), nullable=False)
    lessonName = db.Column(db.String(100), nullable=False)
    lessonDesc = db.Column(db.String(500), nullable=False)

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


#LESSON MATERIAL CLASS
class LessonMaterials(db.Model): 
    
    __tablename__ = 'lessonMaterials'

    materialID = db.Column(db.Integer, primary_key=True)
    materialURL = db.Column(db.String(500), nullable=False)
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

#LESSON MATERIAL VIEWED CLASS
class LessonMaterialsViewed(db.Model):
    __tablename__ = 'lessonMaterialsViewed'

    materialID = db.Column(db.Integer, db.ForeignKey(LessonMaterials.materialID), primary_key=True)
    learnerID = db.Column(db.Integer, db.ForeignKey(Learner.empID), nullable=False)
    lessonID = db.Column(db.Integer, db.ForeignKey(Lesson.lessonID), nullable=False)
    completed = db.Column(db.Boolean, default=False)

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

#QUIZ CLASS
class Quiz(db.Model):
    __tablename__ = 'quiz'

    quizID = db.Column(db.Integer, primary_key=True)
    quizDuration = db.Column(db.String(20), nullable=False)
    passingCriteria = db.Column(db.String(5), nullable=False)
    quizType = db.Column(db.String(2), nullable=False)
    lessonID = db.Column(db.Integer, db.ForeignKey(Lesson.lessonID), nullable=False)


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

#QUESTION CLASS
class Questions(db.Model):
    __tablename__ = 'quizQuestions'

    quizID = db.Column(db.Integer, db.ForeignKey(Quiz.quizID), primary_key=True)
    qnNo = db.Column(db.Integer, nullable=False)
    question = db.Column(db.String(300), nullable=False)
    options = db.Column(db.String(100), nullable=False)
    answer = db.Column(db.String(50), nullable=False)

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


#EMPLOYEE
@app.route("/employee")
def employee():
    employee_list = Employee.query.all()
    return jsonify(
        {
            "data": [employee.to_dict()
                     for employee in employee_list]
        }
    ), 200


@app.route("/employee/<int:empID>")
def employee_by_id(empID):
    employee = Employee.query.filter_by(empID=empID).first()
    if employee:
        return jsonify({
            "data": employee.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Employee not found."
        }), 404

#LEARNER

@app.route("/learner")
def learner():
    learner_list = Learner.query.all()
    return jsonify(
        {
            "data": [learner.to_dict()
                     for learner in learner_list]
        }
    ), 200
    

@app.route("/learner/<int:empID>")
def learner_by_empID(empID):
    learner = Learner.query.filter_by(empID=empID).first()
    if learner:
        return jsonify({
            "data": learner.to_dict() 
        }), 200
    else:
        return jsonify({
            "message": "No learner with that empID."
        }), 404



#COURSE
@app.route("/courses")
def courses():
    course_list = Course.query.all()
    return jsonify(
        {
            "data": [course.to_dict()
                     for course in course_list]
        }
    ), 200

@app.route("/course/<string:courseName>")
def course_by_name(courseName):
    course = Course.query.filter_by(courseName=courseName).first()
    if course:
        return jsonify({
            "data": course.to_dict() 
        }), 200
    else:
        return jsonify({
            "message": "Course not found."
        }), 404

@app.route("/course/<int:courseID>")
def course_by_id(courseID):
    course = Course.query.filter_by(courseID=courseID).first()
    if course:
        return jsonify({
            "data": course.to_dict() 
        }), 200
    else:
        return jsonify({
            "message": "Course not found."
        }), 404

#CLASSLIST
@app.route("/classList/<int:classID>")
def classList_by_class(classID):
    classlist = ClassList.query.filter_by(classID=classID)
    if classlist:
        return jsonify({
            "data": [learner.to_dict()
                     for learner in classlist]
        }), 200
    else:
        return jsonify({
            "message": "No learners assigned."
        }), 404

@app.route("/classList/learner/<int:learnerID>")
def classList_by_learner(learnerID):
    assignedClasses = ClassList.query.filter_by(learnerID=learnerID)
    if assignedClasses:
        return jsonify({
            "data": [classes.to_dict()
                     for classes in assignedClasses]
        }), 200
    else:
        return jsonify({
            "message": "No assigned classes."
        }), 404


@app.route("/classList", methods=['POST'])
def assign_learner():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('learnerID', 'classID')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate class
    classes = Classes.query.filter_by(classID=data['classID']).first()
    if not classes:
        return jsonify({
            "message": "Class is not valid."
        }), 500

    # (2): Validate learner
    learner = Learner.query.filter_by(empID=data['learnerID']).first()
    if not learner:
        return jsonify({
            "message": "Learner is not valid."
        }), 500

    # (4): Create assignment record in ClassList
    assignment = ClassList(
        classID=data['classID'], learnerID=data['learnerID'],
        progressPercentage=0
    )

    # (5): Commit to DB
    try:
        db.session.add(assignment)
        db.session.commit()
        return jsonify({
            "code": 201,
            "message": "Learner assigned successfully"
        }), 201
    except Exception as e:
        return jsonify({
            "data": assignment.to_dict(),
            "message": "Unable to commit to database. " + str(e)
        }), 500



#CLASSES

@app.route("/classes")
def classes():
    class_list = Classes.query.all()
    return jsonify(
        {
            "data": [classes.to_dict()
                     for classes in class_list]
        }
    ), 200

@app.route("/classes/<int:courseID>")
def class_by_courseID(courseID):
    classCourseID = Classes.query.filter_by(courseID=courseID)
    if classCourseID:
        return jsonify({
            "data": [classCourse.to_dict()
                     for classCourse in classCourseID]
        }), 200
    else:
        return jsonify({
            "message": "No available classes."
        }), 404


@app.route("/classes/byClass/<int:classID>")
def class_by_classID(classID):
    classID = Classes.query.join(Course).filter(Classes.classID==classID)
    if classID:
        return jsonify({
            "data": [classs.to_dict()
                     for classs in classID]
        }), 200
    else:
        return jsonify({
            "message": "No available classes."
        }), 404


#ENROLMENTLIST
@app.route("/enrolmentList")
def enrolmentList():
    enrolments_list = EnrolmentList.query.all()
    return jsonify(
        {
            "data": [enrolment.to_dict()
                     for enrolment in enrolments_list]
        }
    ), 200

@app.route("/enrolmentList/<int:learnerID>")
def enrolments_by_learner(learnerID):
    enrolments = EnrolmentList.query.filter_by(learnerID=learnerID)
    if enrolments:
        return jsonify({
            "data": [enrolment.to_dict()
                     for enrolment in enrolments]
        }), 200
    else:
        return jsonify({
            "message": "No enrolments found."
        }), 404

@app.route("/enrolmentList", methods=['POST'])
def create_enrolment():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('learnerID', 'classID', 'courseID')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate class
    classes = Classes.query.filter_by(classID=data['classID']).first()
    if not classes:
        return jsonify({
            "message": "Class is not valid."
        }), 500

    # (2): Validate learner
    learner = Learner.query.filter_by(empID=data['learnerID']).first()
    if not learner:
        return jsonify({
            "message": "Learner is not valid."
        }), 500

    course = Course.query.filter_by(courseID=data['courseID']).first()
    if not course:
        return jsonify({
            "message": "Course is not valid."
        }), 500

    # (4): Create enrolment record
    enrolment = EnrolmentList(
        classID=data['classID'], learnerID=data['learnerID'],
         courseID=data['courseID'], enrolmentStatus="Pending"
    )

    # (5): Commit to DB
    try:
        db.session.add(enrolment)
        db.session.commit()
        return jsonify(enrolment.to_dict()), 201
    except Exception as e:
        return jsonify({
            "message": "Unable to commit to database. " + str(e)
        }), 500        

#LESSON
@app.route("/lesson/<int:classID>/<int:lessonNum>/<int:courseID>")
def lesson_by_num(classID, lessonNum, courseID):
    lessons = Lesson.query.filter_by(classID=classID, lessonID=lessonNum, courseID=courseID).all()
    if lessons:
        return jsonify({
            "data": [lesson.to_dict()
                     for lesson in lessons]
        }), 200
    else:
        return jsonify({
            "message": "No lessons materials available yet."
        }), 201

@app.route("/lesson/<int:classID>/<int:courseID>")
def retrieve_all_lessons_by_class(classID, courseID):
    lessons = Lesson.query.filter_by(classID=classID, courseID=courseID).all()
    if lessons:
        return jsonify({
            "data": [lesson.to_dict()
                     for lesson in lessons]
        }), 200
    else:
        return jsonify({
            "message": "No lessons available yet."
        }), 201

#LESSONMATERIALS
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

#LESSONMATERIALSVIEWED
@app.route("/lessonMaterialsViewed/check/<int:materialID>/<int:learnerID>/<int:lessonID>")
def lessonMaterialsViewed_by_lesson_material(materialID, learnerID, lessonID):
    lessonMaterialsViewed = LessonMaterialsViewed.query.filter_by(materialID=materialID, learnerID=learnerID, lessonID=lessonID).first()
    if lessonMaterialsViewed:
        return jsonify({
            "data": lessonMaterialsViewed.to_dict(),
            "status": "success"
        }), 200
    else:
        return jsonify({
            "message": "No lesson materials found.",
            "status": "not found"
        }), 201

#ADD TO DB THAT ITS VIEWED
@app.route("/lessonMaterialsViewed/add/<int:materialID>/<int:learnerID>/<int:lessonID>")
def lessonMaterialsViewed_add_by_lesson_material(materialID, learnerID, lessonID):
    lessonMaterialsViewed = LessonMaterialsViewed.query.filter_by(materialID=materialID, learnerID=learnerID, lessonID=lessonID).first()
    if lessonMaterialsViewed:
        return jsonify({
            "message": "Lesson Material already viewed."
        }), 201
    else:
        newMaterial = LessonMaterialsViewed(
            materialID=materialID, 
            learnerID=learnerID,
            lessonID=lessonID,
            completed=False
        )
        try:
            db.session.add(newMaterial)
            db.session.commit()
            return jsonify({
                "message": "Viewed Material."
            }), 200
        except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500

#UPDATE COMPLETED
@app.route("/lessonMaterialsViewed/update/<int:materialID>/<int:learnerID>/<int:lessonID>")
def lessonMaterialsViewed_update_by_lesson_material(materialID, learnerID, lessonID):
    lessonMaterialsViewed = LessonMaterialsViewed.query.filter_by(materialID=materialID, learnerID=learnerID, lessonID=lessonID).first()
    lessonMaterialsViewed.completed = True 
    try:
        db.session.commit()
        return jsonify({
            "message": "Updated Completed."
        }), 200
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500

#PREREQ        
@app.route("/prerequisite")
def prerequisite():
    prerequisite = Prerequisite.query.all()
    return jsonify(
        {
            "data": [prereq.to_dict()
                     for prereq in prerequisite]
        }
    ), 200


@app.route("/prerequisite/<int:courseID>")
def prerequisite_by_courseID(courseID):
    prerequisite = Prerequisite.query.filter_by(courseID=courseID).first()
    if prerequisite:
        return jsonify({
            "data": prerequisite.to_dict() 
        }), 200
    else:
        return jsonify({
            "message": "Error getting prerequisite course."
        }), 404

#QUIZCLASS

@app.route("/quiz")
def quizList():
    quizList = Quiz.query.all()
    return jsonify(
        {
            "data": [item.to_dict()
                     for item in quizList]
        }
    ), 200

@app.route('/quiz-create', methods=['POST'])
def create_quiz():
    data = request.get_json()
    print(data)
    item = Quiz(
        quizDuration=data['quizDuration'], passingCriteria=data['passingCriteria'],
        quizType=data['quizType'], lessonID=data['lessonID']
    )
    if ( request.get_json() is not None ): 
        try:
            db.session.add(item)
            db.session.commit()
            return jsonify(item.to_dict()), 201
        except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500

#QUESTIONCLASS

@app.route("/question/<int:quizID>")
def quizQuestions(quizID):
    quizQuestions = Questions.query.filter_by(quizID=quizID)
    if quizQuestions:
        return jsonify({
            "data": [quizQuestions.to_dict()
                     for quizQuestions in quizQuestions]
        }), 200
    else:
        return jsonify({
            "message": "No questions found."
        }), 404

@app.route('/question-create', methods=['POST'])
def create_question():
    data = request.get_json()
    # quizID = Quiz.query. get latest QuizID
    item = Questions(
        qnNo=data['qnNo'], question=data['question'],
        options=data['options'], answer=data['answer']
    )
    if ( request.get_json() is not None ): 
        try:
            db.session.add(item)
            db.session.commit()
            return jsonify(item.to_dict()), 201
        except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)