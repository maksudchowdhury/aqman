
var icons = Quill.import('ui/icons');
icons['customButton'] = '<img src="/static_system/images/editor_icons/information.svg" class="fm_editor_icon">'; 
// \static_system\images\editor_icons/information.svg



var myToolbar = [
  [
    { header: [1, 2, 3, 4, 5, 6, false] },
    "bold",
    "italic",
    "underline",
    { list: "ordered" },
    { list: "bullet" },
    { list: "check" },
    { indent: "-1" },
    { indent: "+1" },
    { align: [] },
    { color: [] },
    { background: [] },
    "link",
    "code-block",
    // [" "],
    "image",
    "formula",
    "customButton",
  ],
];

const el = document.createElement('div')
el.innerHTML = "<a target='_blank' href='http://google.com'>Documentation</a>"

const quillOptions = {
  theme: "snow",
  placeholder: "write the question here.",
  modules: {
    imageResize: {
      displaySize: true
    },
    toolbar: {
      container: myToolbar,
      handlers: {
        image: imageHandler,
        customButton: () => {
          // custom functionality
          swal("Check the documention from here", {
            button: false,
            content: el,
            // timer: 3000,
          });
          // end of custom functionality
        },
      },
    },


 
  },
};



function imageHandler() {

  var fileInputTag = document.getElementById("file");

  var range = this.quill.getSelection();
  fileInputTag.click();

  // fileInputTag.click();

  // Listen upload local image and save to server
  fileInputTag.onchange = () => {
    const imageFile = fileInputTag.files[0];
    // file type is only image.
    if (/^image\//.test(imageFile.type)) {
      if (imageFile.size > 200*1024) {// 200KB
        swal("Image Size Exceeded", "Image size should be less than 200KB", "error");
        return;
      }
      var data = new FormData();
      data.append("file", $("input[id^='file']")[0].files[0]);
      data.append("csrfmiddlewaretoken",document.querySelector("[name=csrfmiddlewaretoken]").value);
      $.ajax({
        method: fileInputTag.getAttribute("method"),
        url: fileInputTag.getAttribute("action"),
        processData: false,
        contentType: false,
        mimeType: "multipart/form-data",
        data: data,
        success: function (response) {
          response = JSON.parse(response);
          quill.insertEmbed(range.index, 'image', response.imageLink, "user");
        },
       
      });

    }

    else {
      // alert('You could only upload images.');
      swal("Wrong Filetype", "You are allowed to select images only", "error");
      return;
    }
  };
  return;
}

Quill.register('modules/imageResize', QuillResizeModule);
const options = {};
const quill = new Quill("#editor", quillOptions);
// const vquill = new Quill("#veditor", options);

(function ($, Quill) {
  $(document).ready(() => {
    const enableMathQuillFormulaAuthoring = window.mathquill4quill();
    enableMathQuillFormulaAuthoring(quill, {
      operators: [
        ["x^a", "{x}^{a}"],
        ["x_b", "x_b"],
        ["\\frac{x}{y}", "\\frac"],
        ["\\sqrt[n]{x}", "\\nthroot"],
        ["\\log_a(B)", "\\log_a(B)"],
        ["dx", "dx"],
        ["\\lim_{x\\to b}", "\\lim _{x \\to b }"],
        ["\\int_a^bX", "\\int_a^bX"],
        ["()", "\\left(\\right)"],
        ["[ ]", "\\left[\\right]"],
        ["\\times", "\\times"],
        ["\\div", "\\div"],
        ["\\alpha", "\\alpha"],
        ["\\beta", "\\beta"],
        ["\\delta", "\\delta"],
        ["\\epsilon", "\\epsilon"],
        ["\\eta", "\\eta"],
        ["\\gamma", "\\gamma"],
        ["\\lambda", "\\lambda"],
        ["\\mu", "\\mu"],
        ["\\omega", "\\omega"],
        ["\\phi", "\\phi"],
        ["\\pi", "\\pi"],
        ["\\rho", "\\rho"],
        ["\\sigma", "\\sigma"],
        ["\\theta", "\\theta"],
        ["\\Delta", "\\Delta"],
        ["\\Omega", "\\Omega"],
        ["\\Theta", "\\Theta"],
        ["\\Sigma", "\\Sigma"],
        ["\\pm", "\\pm"],
        ["\\equiv", "\\equiv"],
        ["\\simeq", "\\simeq"],
        ["\\cong", "\\cong"],
        ["\\approx", "\\approx"],
        ["\\propto", "\\propto"],
        ,
      ],
      displayHistory: true,
      displayDeleteButtonOnHistory: true,
    });
  });
})(window.jQuery, window.Quill);

// function submitData() {
//   var editor = quill;
//   var delta = editor.getContents().ops;
//   console.log(delta);
//   var msg = JSON.stringify(delta);
//   vquill.setContents(JSON.parse(msg));
//   console.log(msg); // store this msg variable in the database
//   vquill.disable();
// }

