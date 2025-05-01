document.addEventListener("DOMContentLoaded", function () {
    const addStudentButton = document.getElementById("add-student-btn");
    const addTeacherButton = document.getElementById("add-teacher-btn");
    const addSubjectButton = document.getElementById("add-subject-btn");
    const addClassButton = document.getElementById("add-class-btn");
      
    if (addStudentButton) {
        addStudentButton.addEventListener("click", function () {
            alert("New student was added!");
        });
        }
    if (addTeacherButton) {
        addTeacherButton.addEventListener("click", function () {
            alert("New teacher was added!");
        });
        }
    if (addSubjectButton) {
        addSubjectButton.addEventListener("click", function () {
            alert("New subject was added!");
        });
        }
    if (addClassButton) {
        addClassButton.addEventListener("click", function () {
            alert("New class was added!");
        });
        }
    
});