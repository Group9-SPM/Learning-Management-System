
var optionCount = 3;
var questionCount = 2;

function cancel() {
  window.history.back();
}

function addOption(current) {
    var optionElement = current.parentNode;
    var length = optionElement.childNodes.length;
    var newNode = document.createElement("div");
    newNode.classList.add("form-check");

    var newOption = `<input class="form-check-input" type="radio" value="option${optionCount}">
                    <input type="text" class="form-control" id="option${optionCount}" value="${optionCount}" placeholder="Option ${optionCount}" style="display: inline; width: 625px;">
                    <button class="btn btn-secondary" type="button"><i class="ri-delete-bin-fill"></i></button>
                    `;
    newNode.innerHTML = newOption;
    curr = optionElement.parentNode;
    curQnNode = curr.parentNode.childNodes;
    console.log(curr.childNodes[3].childNodes);
    console.log(curr.childNodes[3].childNodes[length - 3].childNodes[2].childNodes);
    
    if (curQnNode.length == 11) {
      console.log(curQnNode[1].innerText);
    } else {
      console.log(curQnNode[0].innerText);
    }
    optionElement.insertBefore(newNode, optionElement.childNodes[length - 2]);

    optionCount++;
}

function addQuestion() {
    var newNode = document.createElement("div");
    newNode.classList.add("mb-3");

    var newQuestion = `<div class="row mb-3">
                      <label for="inputQn" class="col-sm-2 col-form-label">Question ${questionCount}</label>
                      <div class="col-sm-10">
                        <textarea class="form-control" id="inputQn" rows="1"></textarea>
                      </div>
                    </div>
                    <div class="row mb-3">
                      <label class="col-sm-2 col-form-label">Options</label>
                      <div class="col-sm-10">
                        <div class="form-check">
                          <input class="form-check-input" type="radio" value="option1">
                          <input type="text" class="form-control" id="option1" placeholder="True/Option 1">
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="radio" value="option2">
                          <input type="text" class="form-control" id="option2" placeholder="False/Option 2">
                        </div>
                      </div>
                    </div>
                    <div class="row mb-3">
                      <label for="correctAns" class="col-sm-2 col-form-label">Correct Answer</label>
                      <div class="col-sm-10">
                        <input type="text" class="form-control" id="correctAns">
                      </div>
                    </div>`;
    newNode.innerHTML = newQuestion;

    var buttonElement = document.getElementById("questionBtn").parentNode;
    var length = buttonElement.childNodes.length;
    buttonElement.insertBefore(newNode, buttonElement.childNodes[length - 7]);
    questionCount++;
}

function create() {
    const form = document.getElementById("quizForm");
    var formArr = form.elements;
    var lessonID = sessionStorage.lessonID;
    var quizType = "UG";
    var quizDuration = String(formArr["inputDur"].value) + "min";
    var passingCriteria = formArr["inputPass"].value;
    var question_data = []
    var qnNo = 1
    var options = ""
    var question = ""
    var answer = ""
    var questions = []
    var answers = []

    if (formArr[0].checked) {
      quizType = "G";
    } 
    var quiz_data = { lessonID, quizType, quizDuration, passingCriteria };
    
    if (formArr["inputQn"].length) {
      formArr["inputQn"].forEach(qns => {
        questions.push(qns.value);
      });
      formArr["correctAns"].forEach(ans => {
        answers.push(ans.value);
      });
      for (let i = 0; i < questions.length; i++) {
        qnNo = i+1;
        question = questions[i];
        answer = answers[i];
        options = formArr["option1"][i].value + "," + formArr["option2"][i].value;
        data = { qnNo, question, options, answer };
        question_data.push(data);
        sessionStorage.multiple = true;
      }
    } else {
      question = formArr["inputQn"].value;
      answer = formArr["correctAns"].value;
      options = formArr["option1"].value + "," + formArr["option2"].value;
      question_data = [ qnNo, question, options, answer ];
      sessionStorage.multiple = false;
    }
    sessionStorage.quizData = JSON.stringify(quiz_data);
    sessionStorage.qnsData = JSON.stringify(question_data);
    window.location.assign("./quizConfirm.html");
}

function allOption(formArr) {
  formArr = form.elements;
  
}

function createQuiz(quizData, questionData) {
  console.log(quizData);
  quizData = JSON.parse(quizData);
  lessonID = Number(quizData.lessonID);
  passingCriteria = quizData.passingCriteria;
  quizType = quizData.quizType
  quizDuration = quizData.quizDuration

  const quiz_data = { lessonID, quizType, quizDuration, passingCriteria };
  console.log(quiz_data);
  fetch('http://localhost:5000/quiz-create', { //5014
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(quiz_data),
  })
  .then(response => response.json())
  .then(data => {
    var quizID = data.quizID;
    var question_data = {};
    questionData = JSON.parse(questionData);

    if (sessionStorage.multiple == "true") {
      for (let i = 0; i < questionData.length; i++) {
        console.log(questionData[i]);
        qnNo = questionData[i].qnNo;
        question = questionData[i].question;
        options = questionData[i].options;
        answer = questionData[i].answer;
        question_data = { quizID, qnNo, question, options, answer };
        createQns(question_data);
      }
    } else {
      qnNo = questionData[0];
      question = questionData[1];
      options = questionData[2];
      answer = questionData[3];
      question_data = { quizID, qnNo, question, options, answer };
      createQns(question_data);
    }
  })
  .catch((error) => {
    alert('There is a problem, please try again later.');
    console.error('Error:', error);
  });
}

function createQns(question_data) {
  fetch('http://localhost:5000/question-create', { //5013
    method: 'POST', 
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(question_data),
  })
  .then(response => response.json())
  .then((data) => {
    window.location.replace("./content.html")
  })
  .catch((error) => {
    alert('There is a problem, please try again later.');
    console.error('Error:', error);
  });
}
