// Retrieve list of all students of a class
async function retrieveStudents() {
    "http://127.0.0.1:5012/classList/" + sessionStorage.classid;

    try {
        const response =
         await fetch(
           serviceURL, { method: 'GET' }
        );

        const data = await response.json();
        if (response.ok) { 
            console.log(data);
            return data["data"];
        }
    }
    catch (error) {
        // Errors when calling the service; such as network error, 
        // service offline, etc
        alert('There is a problem fetching list of engineers, please try again later.');
    } // error

};

// Assign learner and add record in classList
async function assignLearner(learnerID, classID) {
    var serviceURL = "http://127.0.0.1:5012/classList";
   
    return fetch (serviceURL,
    {
        method: "POST",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify({learnerID: learnerID, classID: classID})
    })
    .then(data => {
        return data.json();
    })
};