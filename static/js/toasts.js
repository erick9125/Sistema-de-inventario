document.addEventListener("DOMContentLoaded", function () {
  var toastEls = document.querySelectorAll(".toast");
  toastEls.forEach(function (toastEl) {
    var toast = bootstrap.Toast.getOrCreateInstance(toastEl, {
      delay: 4500,
      autohide: true,
    });
    toast.show();
  });
});
