document.addEventListener("DOMContentLoaded", function () {
  var clockEl = document.getElementById("app-clock");
  if (!clockEl) {
    return;
  }

  function pad(value) {
    return String(value).padStart(2, "0");
  }

  function renderClock() {
    var now = new Date();
    var fecha =
      pad(now.getDate()) +
      "/" +
      pad(now.getMonth() + 1) +
      "/" +
      now.getFullYear();
    var hora =
      pad(now.getHours()) +
      ":" +
      pad(now.getMinutes()) +
      ":" +
      pad(now.getSeconds());
    clockEl.textContent = fecha + " · " + hora;
  }

  renderClock();
  setInterval(renderClock, 1000);
});
