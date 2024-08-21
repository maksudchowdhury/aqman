function signUp() {

  let csrf_token = document.querySelector("[name=csrfmiddlewaretoken]").value;
  var signup_url = document.getElementById("accountRegisterForm").dataset.signup_url;
  var mydata = { csrfmiddlewaretoken: csrf_token };
  console.log("catching the ajax soon");
  $.ajax({
    method: "POST",
    url: signup_url,
    data: mydata,
    success: function (response) {
      if (response.status == "success") {
        // swal({
        //   icon: "success",
        //   button: false,
        //   title: "OTP Sent!",
        //   text: "Check your email and enter the OTP",
        //   timer: 3000,
        // });
      } 
      else {
        console.log(response.message);
        // swal({
        //   icon: "error",
        //   button: false,
        //   title: "Invalid Request",
        //   text: response.message,
        //   // timer: 2000,
        // });
      }
    },
    error: function (response) {
    //   swal({
    //     icon: "error",
    //     button: false,
    //     title: "Error!",
    //     text: "Something went wrong! Please Check the email you entered or try again",
    //     // timer: 2000,
    //   });
    },
  });
}
