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

CREATE TABLE class (
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

CREATE TABLE enrolmentList (
    learnerID INT NOT NULL,
    classID INT NOT NULL,

    CONSTRAINT enrolmentList_pk PRIMARY KEY (learnerID,classID),
    CONSTRAINT enrolmentList_fk1 FOREIGN KEY (learnerID) REFERENCES learner(empID),
    CONSTRAINT enrolmentList_fk2 FOREIGN KEY (classID) REFERENCES class(classID)
);

CREATE TABLE signupList (
    learnerID INT NOT NULL,
    classID INT NOT NULL,
    courseStatus VARCHAR(100),

    CONSTRAINT signupList_pk PRIMARY KEY (learnerID,classID),
    CONSTRAINT signupList_fk1 FOREIGN KEY (learnerID) REFERENCES learner(empID),
    CONSTRAINT signupList_fk2 FOREIGN KEY (classID) REFERENCES class(classID)
);

CREATE TABLE lesson (
    lessonID INT NOT NULL AUTO_INCREMENT,
    classID INT NOT NULL,
    lessonName VARCHAR(100) NOT NULL,
    lessonDesc VARCHAR(500) NOT NULL,
    lessonMaterials VARCHAR(100) NOT NULL,

    CONSTRAINT lesson_pk PRIMARY KEY (lessonID),
    CONSTRAINT lesson_fk FOREIGN KEY (classID) REFERENCES class(classID)
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
    quizID INT NOT NULL,
    qnNo INT NOT NULL,
    question VARCHAR(300) NOT NULL,
    options VARCHAR(100) NOT NULL,
    answer VARCHAR(50) NOT NULL,

    CONSTRAINT quizQuestions_pk PRIMARY KEY (quizID, qnNo),
    CONSTRAINT quizQuestions_fk FOREIGN KEY (quizID) REFERENCES quiz(quizID)
);

-- INSERT DATA --
INSERT INTO  employee(empName, department, username, roleType) VALUES("Alice Teo", "Production", "alice123", "L");
INSERT INTO  employee(empName, department, username, roleType) VALUES("Amy Tan", "R&D", "amy123", "L");
INSERT INTO  employee(empName, department, username, roleType) VALUES("Lucy Wong", "R&D", "lucy123", "L");
INSERT INTO  employee(empName, department, username, roleType) VALUES("Jeremy Lim", "Production", "jeremy123", "T");
INSERT INTO  employee(empName, department, username, roleType) VALUES("January Chan", "HR", "january123", "A");
INSERT INTO  employee(empName, department, username, roleType) VALUES("James Tho", "Production", "james123", "T");

INSERT INTO course(courseName, courseDesc, courseDuration) VALUES("Repair Words 101", "Learn how to speak repair words", "1h");
INSERT INTO course(courseName, courseDesc, courseDuration) VALUES("Repair 101", "Learn how to repair things", "3h");

INSERT INTO prerequisite VALUES(2, 1);

INSERT INTO class(startDate, endDate, size, startTime, endTime, minSlot, maxSlot, regStartDate, regEndDate, courseID, trainerID)
VALUES("2021-08-01", "2021-11-15", 30, "12:00", "13:00", 10, 30, "2021-07-01", "2021-07-18", 1, NULL);
INSERT INTO class(startDate, endDate, size, startTime, endTime, minSlot, maxSlot, regStartDate, regEndDate, courseID, trainerID)
VALUES("2021-08-01", "2021-11-15", 30, "12:00", "15:00", 10, 30, "2021-07-01", "2021-07-18", 2, 2);

INSERT INTO learner VALUES(1, NULL);
INSERT INTO learner VALUES(2, "1");
INSERT INTO learner VALUES(3, NULL);

INSERT INTO enrolmentList VALUES(3, 1);

INSERT INTO signupList VALUES(1, 1, "Pending");
INSERT INTO signupList VALUES(2, 2) , "Successful";

INSERT INTO lesson(classID, lessonName, lessonDesc, lessonMaterials) VALUES(1, "Basic English", "Basic English words.", "basic.pdf");
INSERT INTO lesson(classID, lessonName, lessonDesc, lessonMaterials) VALUES(1, "Advanced English", "Advanced English words.", "advanced.pdf");
INSERT INTO lesson(classID, lessonName, lessonDesc, lessonMaterials) VALUES(1, "Repair English", "English repair words.", "repair.pdf");
INSERT INTO lesson(classID, lessonName, lessonDesc, lessonMaterials) VALUES(2, "Using Hands", "How to use your hands to repair things.", "hands.pptx");
INSERT INTO lesson(classID, lessonName, lessonDesc, lessonMaterials) VALUES(2, "Using Tools", "How to use tools to repair things.", "tools.pdf");

INSERT INTO quiz(quizDuration, passingCriteria, quizType, lessonID) VALUES("10min", "3", "UG", 1);
INSERT INTO quiz(quizDuration, passingCriteria, quizType, lessonID) VALUES("10min", "3", "UG", 2);
INSERT INTO quiz(quizDuration, passingCriteria, quizType, lessonID) VALUES("10min", "3", "UG", 4);

INSERT INTO quizQuestions VALUES(1, 1, "What is the number that is shown when facing printing error?", "21,23,24,25", "21");
INSERT INTO quizQuestions VALUES(1, 2, "Which of the following options states the main purpose of HP Printer?", "Printing,Copying,Scanning,Faxing", "Copying");
INSERT INTO quizQuestions VALUES(1, 3,  "How long does it take for the machine to reboot?", "5 minutes,15 minutes,45 minutes,1 hour", "15 minutes");
INSERT INTO quizQuestions VALUES(1, 4, "True or False: The HP Printer can copy 500 pages at one go.", "True,False", "False");
INSERT INTO quizQuestions VALUES(1, 5, "True or False: The HP Printer have a lifetime warranty.", "True,False", "True");

INSERT INTO quizQuestions VALUES(2, 1, "What is the number that is shown when facing printing error?", "21,23,24,25", "21");
INSERT INTO quizQuestions VALUES(2, 2, "Which of the following options states the main purpose of Xerox Printer?", "Printing,Copying,Scanning,Faxing", "Copying");
INSERT INTO quizQuestions VALUES(2, 3,  "How long does it take for the machine to reboot?", "5 minutes,15 minutes,45 minutes,1 hour", "15 minutes");

INSERT INTO quizQuestions VALUES(3, 1, "True or False: The Canon Printer can copy 500 pages at one go.", "True,False", "False");
INSERT INTO quizQuestions VALUES(3, 2, "True or False: The Canon Printer have a lifetime warranty.", "True,False", "True");