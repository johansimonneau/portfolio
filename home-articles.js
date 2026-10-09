!function () {
  "use strict";
  var grid = document.getElementById("homeArticlesGrid");
  if (!grid) return;

  fetch("/blog.html")
    .then(function (res) {
      if (!res.ok) throw new Error("fetch failed");
      return res.text();
    })
    .then(function (html) {
      var doc = new DOMParser().parseFromString(html, "text/html");
      var articles = Array.prototype.map.call(doc.querySelectorAll(".blog-card"), function (el) {
        var tagEl = el.querySelector(".blog-card-tag");
        var titleEl = el.querySelector("h2");
        var excerptEl = el.querySelector("p:not(.sub-byline)");
        return {
          slug: el.getAttribute("href"),
          tag: tagEl ? tagEl.textContent.trim() : "",
          title: titleEl ? titleEl.textContent.trim() : "",
          excerpt: excerptEl ? excerptEl.textContent.trim() : "",
        };
      }).filter(function (a) { return a.slug && a.title; });

      if (!articles.length) return;

      var pool = articles.slice();
      for (var i = pool.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var tmp = pool[i];
        pool[i] = pool[j];
        pool[j] = tmp;
      }

      pool.slice(0, Math.min(3, pool.length)).forEach(function (article) {
        var card = document.createElement("article");
        card.className = "card";

        var tag = document.createElement("p");
        tag.className = "card-tag";
        tag.textContent = article.tag;

        var title = document.createElement("h3");
        title.className = "card-title";
        title.textContent = article.title;

        var text = document.createElement("p");
        text.className = "card-text";
        text.textContent = article.excerpt;

        var links = document.createElement("div");
        links.className = "card-links";
        var link = document.createElement("a");
        link.className = "card-link";
        link.href = article.slug;
        link.textContent = "Lire l'article →";
        links.appendChild(link);

        card.appendChild(tag);
        card.appendChild(title);
        card.appendChild(text);
        card.appendChild(links);
        grid.appendChild(card);
      });
    })
    .catch(function () {
      var section = grid.closest("section");
      if (section) section.hidden = true;
    });
}();
