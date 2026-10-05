(function () {
  "use strict";
  document.querySelectorAll("[data-bar-fill]").forEach(function (bar) {
    bar.style.width = bar.getAttribute("data-bar-fill") + "%";
  });

  var sections = document.querySelectorAll(".baro-section[id]");
  var links = document.querySelectorAll(".baro-subnav a[href^='#']");
  if (!sections.length || !links.length || !("IntersectionObserver" in window)) return;

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      var id = entry.target.getAttribute("id");
      links.forEach(function (link) {
        link.classList.toggle("is-active", link.getAttribute("href") === "#" + id);
      });
    });
  }, { rootMargin: "-45% 0px -50% 0px", threshold: 0 });

  sections.forEach(function (section) {
    observer.observe(section);
  });
})();
