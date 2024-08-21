
function navMenuItemActivator(itemID) {
  const navItems = document.querySelectorAll(".nav-item");
  navItems.forEach((navItem) => {
    navItem.classList.remove("active");
  });
  document.getElementById(itemID).classList.add("active");
}



function markAnswer(id) {
  const choices = document.getElementsByClassName("op")
  for (let i = 0; i < choices.length; i++) {
    choices[i].classList.remove("selected");
  }
  let selectedChoice = document.getElementById(id);
  selectedChoice.classList.add("selected");
  

}

function submitQuestion() {

  var qTitle = document.getElementById("qTitle").value.trim();
  var module = document.getElementById("module").value;
  var chapter = document.getElementById("chapter").value;
  var topic = document.getElementById("topic").value;
  var subTopic = document.getElementById("subTopic").value;

  var editor = quill;
  var delta = editor.getContents().ops;
  var question = JSON.stringify(delta);


  var choice1 = document.getElementById("c1").value.trim();
  var choice2 = document.getElementById("c2").value.trim();
  var choice3 = document.getElementById("c3").value.trim();
  var choice4 = document.getElementById("c4").value.trim();

  var answerExist = document.getElementsByClassName("selected");
  
  
  

  let emptyEditor = (question===('[{"insert":"\\n"}]'));
  let emptyInputs = (qTitle==="" || module==="" || chapter==="" || topic==="" || subTopic==="" || choice1==="" || choice2==="" || choice3==="" || choice4==="" || answer==="")


  if (!emptyEditor && !emptyInputs) {


    if(answerExist.length==0 ){
      swal("Error", "Please select the correct answer", "error");
      return;
    }
    else{
      var answerID = document.getElementsByClassName("selected")[0].dataset.answerid;
      var answer = document.getElementById(answerID).value.trim();
    }
    
    var data = {
      qTitle: qTitle,
      module: module,
      chapter: chapter,
      topic: topic,
      subTopic: subTopic,
      question: question,
      choice1: choice1,
      choice2: choice2,
      choice3: choice3,
      choice4: choice4,
      answer: answer,
      csrfmiddlewaretoken: document.querySelector("[name=csrfmiddlewaretoken]").value,
    };

    $.ajax({
      method: "POST",
      url: "/submitQuestion/",
      data: data,
      success: function (response) {
        swal(
          "Question Submitted",
          "Question has been submitted successfully",
          "success"
        );
        console.log(data);
      },
      error: function (response) {
        swal(
          "Error",
          "Error occured while submitting question, Please Try Again",
          "error"
        );
      },
    });

    return;

  } 
  
  else {
    swal("Error", "Please Fill all the fields", "error");
    return;
  }

 
}

function questionList_display(){

    var questions = document.getElementsByClassName("questionList_item")
    for (let i = 0; i < questions.length; i++) {
      console.log(questions[i].id);
      questionQuill="#".concat(questions[i].id);
      var qBody = (document.getElementById(questions[i].id)).dataset.qbody;
      (new Quill(questionQuill, {})).setContents(JSON.parse(qBody));
    }


}

// (new Quill("#cda93d59-edc8-426c-a996-b9d0a6b136da", {})).setContents(JSON.parse('[{"insert":"is this the equation of relativity?\nEquation: "},{"insert":{"formula":"e=mc^2"}},{"insert":" \n"}]'))


// questionQuill="#".concat("2c62e673-0874-4827-94e2-10a7a9e31b1f");
// var qBody = (document.getElementById("2c62e673-0874-4827-94e2-10a7a9e31b1f")).dataset.qbody;

// (new Quill("#2c62e673-0874-4827-94e2-10a7a9e31b1f", {})).setContents(JSON.parse("[{&quot;attributes&quot;:{&quot;background&quot;:&quot;#ffffff&quot;,&quot;color&quot;:&quot;#000000&quot;},&quot;insert&quot;:&quot;Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of \&quot;de Finibus Bonorum et Malorum\&quot; (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, \&quot;Lorem ipsum dolor sit amet..\&quot;, comes from a line in section 1.10.32.&quot;},{&quot;insert&quot;:&quot;\n&quot;},{&quot;insert&quot;:{&quot;formula&quot;:&quot;\\log_a(B)&quot;}},{&quot;insert&quot;:&quot; &quot;},{&quot;attributes&quot;:{&quot;align&quot;:&quot;center&quot;},&quot;insert&quot;:&quot;\n&quot;},{&quot;insert&quot;:{&quot;image&quot;:&quot;/media/images/68b5b84a-867b-4a00-bb6d-f6167a408b42.png&quot;}},{&quot;insert&quot;:&quot;\n&quot;}]"));


