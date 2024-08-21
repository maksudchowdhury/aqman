// ++++++++++++++++++++++++ email input validation ++++++++++++++++++++++++
$(".emailInitial").on("input", function () {
  var c = this.selectionStart,
    r = /[^a-z0-9.\-+_]/gi,
    v = $(this).val();  
  if (r.test(v)) {
    $(this).val(v.replace(r, ""));
    c--;
  }
  this.setSelectionRange(c, c);
});

// ++++++++++++++++++++++++ OTP input validation ++++++++++++++++++++++++
$("#otpInputField").on("input", function () {
  var c = this.selectionStart,
    r = /[^a-z0-9]/gi,
    v = $(this).val();
  if (r.test(v)) {
    $(this).val(v.replace(r, ""));
    c--;
  }
  this.setSelectionRange(c, c);
});

// ++++++++++++++++++++++++ password input validation ++++++++++++++++++++++++
var pass1isValid = false;
$("#pass1").on("input", function () {
  var v = $(this).val();
  var r = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*]).{8,}$/;
  if (r.test(v)) {
    pass1isValid = true;
  } else {
    pass1isValid = false;
  }
});

// ++++++++++++++++++++++++ password confirmation validation ++++++++++++++++++++++++

$("#pass1").on("input", function () {
  if ($("#pass1").val() == $("#pass2").val() && $("#pass1").val().length > 0) {
    $("#pass1").addClass("correctInsertion");
    $("#pass2").addClass("correctInsertion");
  } else {
    $("#pass1").removeClass("correctInsertion");
    $("#pass2").removeClass("correctInsertion");
  }
});

$("#pass2").on("input", function () {
  if ($("#pass1").val() == $("#pass2").val() && $("#pass1").val().length > 0) {
    $("#pass1").addClass("correctInsertion");
    $("#pass2").addClass("correctInsertion");
  } else {
    $("#pass1").removeClass("correctInsertion");
    $("#pass2").removeClass("correctInsertion");
  }
});

// ++++++++++++++++++++++++ enable signup button ++++++++++++++++++++++++

$("input").on("input", function () {
  if( $("#fname").length){
    var fname = Boolean($("#fname").val().length > 0);
  
  }
  if( $("#lname").length){
    var lname = Boolean($("#lname").val().length > 0);
  }

  if( $("#emailInitial").length){
    var email = Boolean($("#emailInitial").val().length > 0);
  }
  if( $("#pass1").length){
    var passMatch = Boolean($("#pass1").val() == $("#pass2").val());
  }
  if (fname && lname && email && passMatch && pass1isValid) {
    $("#signUpBtn").removeClass("disabled");
  } else {
    $("#signUpBtn").addClass("disabled");
  }
});
