function getOTP(emailFieldID,otpURLFieldID) {
  swal({
    icon: "warning",
    button: false,
    title: "Please Wait!",
    text: "We are sending an OTP to your email...",
    showLoaderOnConfirm: true,
  });
    var emailInitial = document.getElementById(emailFieldID).value;    
    var otpURL = document.getElementById(otpURLFieldID).innerHTML;
    console.log(otpURL);
    let csrf_token = document.querySelector("[name=csrfmiddlewaretoken]").value;
    var mydata = {email_initial : emailInitial, csrfmiddlewaretoken: csrf_token};
    $.ajax({
        method: 'POST',
        url: otpURL,
        data: mydata,
        success: function (response) {
          if(response.status == "success"){

            swal({
              icon: "success",
              button: false,
              title: "OTP Sent!",
              text: "Check your email and enter the OTP",
              timer: 3000,
            });

          }
          else{
            swal({
              icon: "error",
              button: false,
              title: "Invalid Email",
              text: response.message,
              // timer: 2000,
            });
          }
        },
        error: function (response) {
          swal({
              icon: "error",
              button: false,
              title: "Error!",
              // text: "Something went wrong! Please Check the email you entered or try again",
              text: error,
              // timer: 2000,
            });
        }
        
       
      });
}


