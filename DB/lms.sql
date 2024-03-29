DROP DATABASE IF EXISTS lms;
CREATE DATABASE lms;
USE lms;

-- CREATE TABLES --
CREATE TABLE employee (
    empID INT NOT NULL AUTO_INCREMENT,
    empName VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    username VARCHAR(100) NOT NULL,
    roleType char(1) NOT NULL,

    CONSTRAINT employee_pk PRIMARY KEY (empID)
);

CREATE TABLE course (
    courseID INT NOT NULL AUTO_INCREMENT,
    courseName VARCHAR(100) NOT NULL,
    courseDesc VARCHAR(500) NOT NULL,
    courseDuration VARCHAR(50) NOT NULL,

    CONSTRAINT course_pk PRIMARY KEY (courseID)
);

CREATE TABLE prerequisite (
    courseID INT NOT NULL,
    prerequisiteID INT NOT NULL,

    CONSTRAINT prerequisite_pk PRIMARY KEY (courseID, prerequisiteID),
    CONSTRAINT prerequisite_fk FOREIGN KEY (prerequisiteID) REFERENCES course(courseID)
);

CREATE TABLE classes (
    classID INT NOT NULL AUTO_INCREMENT,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    size INT NOT NULL,
    startTime VARCHAR(20) NOT NULL,
    endTime VARCHAR(20) NOT NULL,
    minSlot INT NOT NULL,
    maxSlot INT NOT NULL,
    regStartDate DATE NOT NULL,
    regEndDate DATE NOT NULL,
    courseID INT NOT NULL,
    trainerID INT,

    CONSTRAINT class_pk PRIMARY KEY (classID),
    CONSTRAINT class_fk1 FOREIGN KEY (courseID) REFERENCES course(courseID),
    CONSTRAINT class_fk2 FOREIGN KEY (trainerID) REFERENCES employee(empID)
);

CREATE TABLE learner (
    empID INT NOT NULL,
    badges VARCHAR(300),

    CONSTRAINT learner_pk PRIMARY KEY (empID),
    CONSTRAINT learner_fk FOREIGN KEY (empID) REFERENCES employee(empID)
);

CREATE TABLE classList (
    learnerID INT NOT NULL,
    classID INT NOT NULL,
    finalQuizGrade VARCHAR(5),

    CONSTRAINT classList_pk PRIMARY KEY (learnerID,classID),
    CONSTRAINT classList_fk1 FOREIGN KEY (learnerID) REFERENCES learner(empID),
    CONSTRAINT classList_fk2 FOREIGN KEY (classID) REFERENCES classes(classID)
);

CREATE TABLE enrolmentList (
    learnerID INT NOT NULL,
    classID INT NOT NULL,
    courseID  INT NOT NULL,
    enrolmentStatus VARCHAR(100) NOT NULL,

    CONSTRAINT enrolmentList_pk PRIMARY KEY (learnerID,classID),
    CONSTRAINT enrolmentList_fk1 FOREIGN KEY (learnerID) REFERENCES learner(empID),
    CONSTRAINT enrolmentList_fk2 FOREIGN KEY (classID) REFERENCES classes(classID),
    CONSTRAINT enrolmentList_fk3 FOREIGN KEY (courseID) REFERENCES course(courseID)
);

CREATE TABLE lesson (
    lessonID INT NOT NULL AUTO_INCREMENT,
    lessonNum INT NOT NULL,
    classID INT NOT NULL,
    courseID INT NOT NULL,
    lessonName VARCHAR(100) NOT NULL,
    lessonDesc VARCHAR(500) NOT NULL,

    CONSTRAINT lesson_pk PRIMARY KEY (lessonID),
    CONSTRAINT lesson_fk FOREIGN KEY (classID) REFERENCES classes(classID),
    CONSTRAINT lesson_fk2 FOREIGN KEY (courseID) REFERENCES classes(courseID)
);

CREATE TABLE lessonMaterials (
    materialID INT NOT NULL AUTO_INCREMENT,
    materialURL varchar(256) NOT NULL,
    content varchar(100) NOT NULL,
    lessonID INT NOT NULL,

    CONSTRAINT lessonMaterials_pk PRIMARY KEY (materialID),
    CONSTRAINT lessonMaterials_fk FOREIGN KEY (lessonID) REFERENCES lesson(lessonID)
);

CREATE TABLE lessonMaterialsViewed (
    materialID INT NOT NULL,
    learnerID INT NOT NULL,
    lessonID INT NOT NULL,
    completed TINYINT NOT NULL,

    CONSTRAINT lessonMaterialsViewed_pk PRIMARY KEY (materialID, learnerID),
    CONSTRAINT lessonMaterialsViewed_fk1 FOREIGN KEY (learnerID) REFERENCES learner(empID),
    CONSTRAINT lessonMaterialsViewed_fk2 FOREIGN KEY (materialID) REFERENCES lessonMaterials(materialID),
    CONSTRAINT lessonMaterialsViewed_fk3 FOREIGN KEY (lessonID) REFERENCES lesson(lessonID)
);

CREATE TABLE quiz (
    quizID INT NOT NULL AUTO_INCREMENT,
    quizDuration VARCHAR(20) NOT NULL,
    passingCriteria VARCHAR(5) NOT NULL,
    quizType VARCHAR(2) NOT NULL,
    lessonID INT NOT NULL,

    CONSTRAINT quiz_pk PRIMARY KEY (quizID),
    CONSTRAINT quiz_fk FOREIGN KEY (lessonID) REFERENCES lesson(lessonID)
);

CREATE TABLE quizQuestions (
    questionsID INT NOT NULL AUTO_INCREMENT,
    quizID INT NOT NULL,
    qnNo INT NOT NULL,
    question VARCHAR(300) NOT NULL,
    options VARCHAR(100) NOT NULL,
    answer VARCHAR(50) NOT NULL,

    CONSTRAINT quizQuestions_pk PRIMARY KEY (questionsID),
    CONSTRAINT quizQuestions_fk FOREIGN KEY (quizID) REFERENCES quiz(quizID)
);

CREATE TABLE quizAttempt (
    quizAttemptID INT NOT NULL AUTO_INCREMENT,
    quizID INT NOT NULL,
    learnerID INT NOT NULL,
    score INT NOT NULL,
    max_score INT NOT NULL,

    CONSTRAINT quizAttempt_pk PRIMARY KEY (quizAttemptID),
    CONSTRAINT quizAttempt_fk FOREIGN KEY (quizID) REFERENCES quiz(quizID),
    CONSTRAINT quizAttempt_fk1 FOREIGN KEY (learnerID) REFERENCES learner(empID)
);

-- INSERT DATA --
INSERT INTO  employee(empName, department, username, roleType) VALUES("Alice Teo", "Production", "alice123", "L");
INSERT INTO  employee(empName, department, username, roleType) VALUES("Amy Tan", "R&D", "amy123", "L");
INSERT INTO  employee(empName, department, username, roleType) VALUES("Lucy Wong", "R&D", "lucy123", "L");
INSERT INTO  employee(empName, department, username, roleType) VALUES("Jeremy Lim", "Production", "jeremy123", "T");
INSERT INTO  employee(empName, department, username, roleType) VALUES("January Chan", "HR", "january123", "A");
INSERT INTO  employee(empName, department, username, roleType) VALUES("James Tho", "Production", "james123", "T");
INSERT INTO  employee(empName, department, username, roleType) VALUES("Layla Chan", "Production", "layla123", "T");


INSERT INTO course(courseName, courseDesc, courseDuration) VALUES("Repair Words 101", "Learn how to speak repair words", "1h");
INSERT INTO course(courseName, courseDesc, courseDuration) VALUES("Repair 101", "Learn how to repair things", "3h");
INSERT INTO course(courseName, courseDesc, courseDuration) VALUES("Repair testing", "Learn how to repair things testing ", "3h");

INSERT INTO prerequisite VALUES(2, 1);
INSERT INTO prerequisite VALUES(3, 2);

INSERT INTO classes(startDate, endDate, size, startTime, endTime, minSlot, maxSlot, regStartDate, regEndDate, courseID, trainerID)
VALUES("2021-11-20", "2021-12-31", 30, "12:00", "13:00", 10, 30, "2021-10-25", "2021-11-15", 1, 4);
INSERT INTO classes(startDate, endDate, size, startTime, endTime, minSlot, maxSlot, regStartDate, regEndDate, courseID, trainerID)
VALUES("2021-11-20", "2021-12-31", 20, "15:00", "16:00", 10, 30, "2021-11-05", "2021-11-25", 1, 4);
INSERT INTO classes(startDate, endDate, size, startTime, endTime, minSlot, maxSlot, regStartDate, regEndDate, courseID, trainerID)
VALUES("2021-11-20", "2021-12-31", 15, "09:00", "10:00", 10, 30, "2021-10-25", "2021-11-18", 2, 6);
INSERT INTO classes(startDate, endDate, size, startTime, endTime, minSlot, maxSlot, regStartDate, regEndDate, courseID, trainerID)
VALUES("2021-11-20", "2021-12-31", 10, "11:00", "12:00", 10, 30, "2021-10-25", "2021-11-18", 3, 6);
INSERT INTO classes(startDate, endDate, size, startTime, endTime, minSlot, maxSlot, regStartDate, regEndDate, courseID, trainerID)
VALUES("2021-08-01", "2021-11-15", 15, "12:00", "15:00", 10, 30, "2021-07-01", "2021-07-18", 2, 7);
INSERT INTO classes(startDate, endDate, size, startTime, endTime, minSlot, maxSlot, regStartDate, regEndDate, courseID, trainerID)
VALUES("2021-08-05", "2021-11-19", 30, "15:00", "18:00", 10, 30, "2021-07-01", "2021-07-18", 3, 7);


INSERT INTO learner VALUES(1, NULL);
INSERT INTO learner VALUES(2, "1");
INSERT INTO learner VALUES(3, NULL);

INSERT INTO classList VALUES(1, 4, NULL);
INSERT INTO classList VALUES(1, 2, NULL);

INSERT INTO enrolmentList VALUES(1, 1, 2,"Pending");
INSERT INTO enrolmentList VALUES(2, 2 , 1 ,"Successful");

INSERT INTO lesson(lessonNum, classID, courseID, lessonName, lessonDesc) VALUES(1, 1, 1,"Basic English", "Basic English words.");
INSERT INTO lesson(lessonNum, classID, courseID, lessonName, lessonDesc) VALUES(2, 1, 1,"Advanced English", "Advanced English words.");
INSERT INTO lesson(lessonNum, classID, courseID, lessonName, lessonDesc) VALUES(3, 1, 1,"Repair English", "English repair words.");
INSERT INTO lesson(lessonNum, classID, courseID, lessonName, lessonDesc) VALUES(1, 2, 2,"Using Hands", "How to use your hands to repair things.");
INSERT INTO lesson(lessonNum, classID, courseID, lessonName, lessonDesc) VALUES(2, 2, 2, "Using Tools", "How to use tools to repair things.");
INSERT INTO lesson(lessonNum, classID, courseID, lessonName, lessonDesc) VALUES(1, 2, 1, "Repair Words Lesson 1", "How to repair using words 1.");
INSERT INTO lesson(lessonNum, classID, courseID, lessonName, lessonDesc) VALUES(2, 2, 1, "Repair Words Lesson 2", "How to repair using words 2.");

INSERT INTO lessonMaterials(content, materialURL, lessonID) VALUES("Basic_1.pdf", "https://drive.google.com/file/d/1tbOmz0GipcX-_c2oXj4MnzZNodiN85x-/view?usp=sharing" , 1);
INSERT INTO lessonMaterials(content, materialURL, lessonID) VALUES("Advanced.pdf","https://drive.google.com/file/d/1_ZojoH5my2eVY9ONHXiDQGXVJhGQ88Dq/view?usp=sharing", 2);
INSERT INTO lessonMaterials(content, materialURL, lessonID) VALUES("Repair.docx","https://docs.google.com/document/d/1tbu7DVxYJaXgtcqQnDaGQptpEgdqjQah/edit?usp=sharing&ouid=104361878523867233103&rtpof=true&sd=true", 3);
INSERT INTO lessonMaterials(content, materialURL, lessonID) VALUES("Basic_2.pptx","https://docs.google.com/presentation/d/1Ma2ttgemZqUiNdN51Dw7MvgIiDTtM4ha/edit?usp=sharing&ouid=104361878523867233103&rtpof=true&sd=true", 1);
INSERT INTO lessonMaterials(content, materialURL, lessonID) VALUES("Extra_Materials.docx","https://docs.google.com/document/d/1Ly2bwHkbwFl4-7uHjg8OmaUShsXxat9J/edit?usp=sharing&ouid=104361878523867233103&rtpof=true&sd=true", 2);
INSERT INTO lessonMaterials(content, materialURL, lessonID) VALUES("Solution.pdf","https://drive.google.com/file/d/1eBvoGvbmaM7R_KkhwtY-qbrXYUf9zNN6/view?usp=sharing", 4);
INSERT INTO lessonMaterials(content, materialURL, lessonID) VALUES("Exercises.pdf","https://drive.google.com/file/d/1Lkxv3OCAmBI-Z1G4UXnrYkWmKk5Lcati/view?usp=sharing", 5);
INSERT INTO lessonMaterials(content, materialURL, lessonID) VALUES("Additional_Exercise.pptx","https://docs.google.com/presentation/d/1-ZS61Jq0cqy1UQh9Q15kObhNXuJm7cnR/edit?usp=sharing&ouid=104361878523867233103&rtpof=true&sd=true", 4);
INSERT INTO lessonMaterials(content, materialURL, lessonID) VALUES("Exercises.pdf","https://drive.google.com/file/d/1Lkxv3OCAmBI-Z1G4UXnrYkWmKk5Lcati/view?usp=sharing", 6);
INSERT INTO lessonMaterials(content, materialURL, lessonID) VALUES("Additional_Exercise.pptx","https://docs.google.com/presentation/d/1-ZS61Jq0cqy1UQh9Q15kObhNXuJm7cnR/edit?usp=sharing&ouid=104361878523867233103&rtpof=true&sd=true", 6);
INSERT INTO lessonMaterials(content, materialURL, lessonID) VALUES("Extra_Materials.docx","https://docs.google.com/document/d/1Ly2bwHkbwFl4-7uHjg8OmaUShsXxat9J/edit?usp=sharing&ouid=104361878523867233103&rtpof=true&sd=true", 7);

INSERT INTO quiz(quizDuration, passingCriteria, quizType, lessonID) VALUES("10min", "3", "UG", 1);
INSERT INTO quiz(quizDuration, passingCriteria, quizType, lessonID) VALUES("10min", "3", "UG", 2);
INSERT INTO quiz(quizDuration, passingCriteria, quizType, lessonID) VALUES("10min", "3", "UG", 4);
INSERT INTO quiz(quizDuration, passingCriteria, quizType, lessonID) VALUES("10min", "3", "UG", 6);
INSERT INTO quiz(quizDuration, passingCriteria, quizType, lessonID) VALUES("10min", "3", "G", 7);


INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(1, 1, "What is the number that is shown when facing printing error?", "21,23,24,25", "21");
INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(1, 2, "Which of the following options states the main purpose of HP Printer?", "Printing,Copying,Scanning,Faxing", "Copying");
INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(1, 3,  "How long does it take for the machine to reboot?", "5 minutes,15 minutes,45 minutes,1 hour", "15 minutes");
INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(1, 4, "True or False: The HP Printer can copy 500 pages at one go.", "True,False", "False");
INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(1, 5, "True or False: The HP Printer have a lifetime warranty.", "True,False", "True");

INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(2, 1, "What is the number that is shown when facing printing error?", "21,23,24,25", "21");
INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(2, 2, "Which of the following options states the main purpose of Xerox Printer?", "Printing,Copying,Scanning,Faxing", "Copying");
INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(2, 3,  "How long does it take for the machine to reboot?", "5 minutes,15 minutes,45 minutes,1 hour", "15 minutes");

INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(3, 1, "True or False: The Canon Printer can copy 500 pages at one go.", "True,False", "False");
INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(3, 2, "True or False: The Canon Printer have a lifetime warranty.", "True,False", "True");

INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(4, 1, "What is the number that is shown when facing printing error?", "21,23,24,25", "21");
INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(4, 2, "Which of the following options states the main purpose of HP Printer?", "Printing,Copying,Scanning,Faxing", "Copying");
INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(4, 3,  "How long does it take for the machine to reboot?", "5 minutes,15 minutes,45 minutes,1 hour", "15 minutes");
INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(4, 4, "True or False: The HP Printer can copy 500 pages at one go.", "True,False", "False");
INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(4, 5, "True or False: The HP Printer have a lifetime warranty.", "True,False", "True");

INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(5, 1, "What is the number that is shown when facing printing error?", "21,23,24,25", "21");
INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(5, 2, "Which of the following options states the main purpose of HP Printer?", "Printing,Copying,Scanning,Faxing", "Copying");
INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(5, 3,  "How long does it take for the machine to reboot?", "5 minutes,15 minutes,45 minutes,1 hour", "15 minutes");
INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(5, 4, "True or False: The HP Printer can copy 500 pages at one go.", "True,False", "False");
INSERT INTO quizQuestions(quizID, qnNo, question, options, answer) VALUES(5, 5, "True or False: The HP Printer have a lifetime warranty.", "True,False", "True");