
var optionCount = 3;
var questionCount = 2;

function deleteBtn(ele) {
    var parent = ele.parentNode;
}

function addOption(current) {
    var newNode = document.createElement("div");
    newNode.classList.add("form-check");

    var newOption = `<input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios${optionCount}" value="option${optionCount}">
                    <input type="text" class="form-control" placeholder="Option ${optionCount}" style="display: inline; width: 625px;">
                    <button class="btn btn-secondary" type="button"><i class="ri-delete-bin-fill"></i></button>
                    `;
    newNode.innerHTML = newOption;

    var optionElement = current.parentNode;
    var length = optionElement.childNodes.length
    optionElement.insertBefore(newNode, optionElement.childNodes[length - 2]);

    optionCount++;
}

function addQuestion(current) {
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
                          <input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios1" value="option1">
                          <input type="text" class="form-control" placeholder="True/Option 1">
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios2" value="option2">
                          <input type="text" class="form-control" placeholder="False/Option 2">
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

function createQuiz(params) {
    
}