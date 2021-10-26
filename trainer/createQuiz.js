
var optionCount = 3;
var questionCount = 2;

function addOption(current) {
    var optionElement = current.parentNode;
    var length = optionElement.childNodes.length;
    var newNode = document.createElement("div");
    newNode.classList.add("form-check");

    var newOption = `<input class="form-check-input" type="radio" value="option${optionCount}">
                    <input type="text" class="form-control" id="option${optionCount}" placeholder="Option ${optionCount}" style="display: inline; width: 625px;">
                    <button class="btn btn-secondary" type="button"><i class="ri-delete-bin-fill"></i></button>
                    `;
    newNode.innerHTML = newOption;

    console.log(optionElement.parentNode.parentNode.childNodes);
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
                    <!-- Options -->
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
                        <button type="button" class="btn btn-primary" style="margin-top: 10px; float: right;" onclick="addOption(this)">Add New Option</button>
                      </div>
                    </div>
                    <!-- Correct Answer -->
                    <div class="row mb-3">
                      <label for="correctAns" class="col-sm-2 col-form-label">Correct Answer</label>
                      <div class="col-sm-10">
                        <input type="text" class="form-control" id="correctAns">
                      </div>
                    </div>`;
    newNode.innerHTML = newQuestion;

    var buttonElement = document.getElementById("questionBtn").parentNode;
    var length = buttonElement.childNodes.length
    buttonElement.insertBefore(newNode, buttonElement.childNodes[length - 7]);
    questionCount++;
}

function create() {
    const form = document.getElementById("quizForm");
    formArr = form.elements;

    var lessonNum = formArr["inputNum"].value
    var quizType = "UG"
    var quizDuration = formArr["inputDur"].value
    var passingCriteria = formArr["inputPass"].value
    var questions = []
    var answers = []

    console.log(formArr);
    console.log(formArr[1].checked, formArr[2].checked);

    if (formArr[1].checked) {
      quizType = "G"
    } 
    // formArr["inputQn"].forEach(qns => {
    //     questions.push(qns.value);
    // });
    // formArr["correctAns"].forEach(ans => {
    //     answers.push(ans.value);
    // });
    const quiz_data = {lessonNum, quizType, quizDuration, passingCriteria }
    console.log(quiz_data);
    // $.ajax({
    //   type: "POST",
    //   url: "/quiz-create",
    //   data: JSON.stringify(quiz_data),
    //   contentType: "application/json",
    //   dataType: 'json',
    //   success: function(result) {
    //     test.innerHTML = result.rows; 
    //   } 
    // });
    fetch('http://localhost:5014/quiz-create', {
      method: 'POST', // or 'PUT'
      // mode: 'cors',
      // credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(quiz_data),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

function deleteBtn(ele) {
    var parent = ele.parentNode;
}