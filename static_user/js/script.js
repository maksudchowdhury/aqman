
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
const tooltipList = [...tooltipTriggerList].map((tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl));
  

$(document).ready(function(){
    $("#toggle-btn").click(function(){
      $("#toggle-example").collapse('toggle'); // toggle collapse
    });
});


$(document).ready(function(){

    $("#printBtn").click(function(){
      $("#page").printThis({
        debug:true,
        importCSS: true,
        importStyle: true,
        loadCSS: "https://raw.githubusercontent.com/maksudchowdhury/cdn/main/printThisCustomStyle.css",
      });
    });

});

function hideBullets(typeName){
  typeName= "."+typeName;
  [].forEach.call(document.querySelectorAll(typeName), function (el) {
    el.style.display = 'none';
  });
}


function approveQuestion(id){
  $(document).ready(function(){
    id = id.split("_")[0];
    id="#"+id+"_container";
    console.log(id);
    $(id).fadeToggle(250);
    toastr.success("question added to database","Successful", toasterOptions);
  });
}

function denyQuestion(id){
  $(document).ready(function(){
    id = id.split("_")[0];
    id="#"+id+"_container";
    console.log(id);
    $(id).fadeToggle(250);
  });
}

