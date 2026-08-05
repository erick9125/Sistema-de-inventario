document.addEventListener("DOMContentLoaded", function () {
  var sidebar = document.getElementById("appSidebar");
  var toggle = document.getElementById("sidebarToggle");
  var backdrop = document.getElementById("sidebarBackdrop");

  function closeSidebar() {
    document.body.classList.remove("sidebar-open");
  }

  function openSidebar() {
    document.body.classList.add("sidebar-open");
  }

  if (toggle) {
    toggle.addEventListener("click", function () {
      if (document.body.classList.contains("sidebar-open")) {
        closeSidebar();
      } else {
        openSidebar();
      }
    });
  }

  if (backdrop) {
    backdrop.addEventListener("click", closeSidebar);
  }
});
