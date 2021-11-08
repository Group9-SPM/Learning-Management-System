// Assigns list of learners and add records in classList
async function assignLearner(assignmentList) {
    var serviceURL = "http://127.0.0.1:5012/classList";
    return fetch (serviceURL,
    {
        method: "POST",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(assignmentList)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        window.location.href = "classList.html"
    })
};