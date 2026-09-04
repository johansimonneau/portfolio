/* ==========================================================================
   Johan Simonneau — Portfolio
   script.js — navigation, animations au scroll, micro-interactions
   ========================================================================== */

(function () {
  "use strict";

  var prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Liens de contact : sujet + corps pré-remplis ---------- */

  var contactLinks = document.querySelectorAll('a[href^="mailto:johansimonneau.pro@gmail.com"]');
  if (contactLinks.length) {
    var contactBody = [
      "Nom : ",
      "Prénom : ",
      "Email : ",
      "N° téléphone : ",
      "Demande : ",
      "URL de la demande : " + window.location.href
    ].join("\n");

    var contactMailto =
      "mailto:johansimonneau.pro@gmail.com?subject=" +
      encodeURIComponent("Demande à partir du Portfolio") +
      "&body=" + encodeURIComponent(contactBody);

    contactLinks.forEach(function (link) {
      link.setAttribute("href", contactMailto);
    });
  }

  /* ---------- Bandeau promo (page d'accueil uniquement) ---------- */

  var isHome = window.location.pathname === "/" || window.location.pathname === "/index.html";
  var siteHeader = document.querySelector(".site-header");

  if (isHome && siteHeader) {
    var BANNER_STORAGE_KEY = "promo_banner_guide_claude_seo";
    var alreadyDismissed = false;
    try {
      alreadyDismissed = localStorage.getItem(BANNER_STORAGE_KEY) === "dismissed";
    } catch (e) {
      // localStorage indisponible : le bandeau s'affichera à chaque visite.
    }

    if (!alreadyDismissed) {
      var banner = document.createElement("div");
      banner.className = "promo-banner";
      banner.id = "promoBanner";
      banner.setAttribute("role", "region");
      banner.setAttribute("aria-label", "Guide gratuit");
      banner.innerHTML =
        '<div class="promo-banner-inner">' +
        '<span><strong>Nouveau —</strong> le guide gratuit « 20 prompts Claude pour structurer votre SEO ».</span>' +
        '<a href="/guide-prompts-claude-seo" class="promo-banner-cta">Voir le guide →</a>' +
        '<button type="button" class="promo-banner-close" id="promoBannerClose" aria-label="Fermer ce message">' +
        '<svg viewBox="0 0 14 14" fill="none"><path d="M1 1L13 13M13 1L1 13" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>' +
        "</button>" +
        "</div>";

      siteHeader.parentNode.insertBefore(banner, siteHeader);

      document.getElementById("promoBannerClose").addEventListener("click", function () {
        banner.remove();
        try {
          localStorage.setItem(BANNER_STORAGE_KEY, "dismissed");
        } catch (e) {
          /* pas de stockage possible, le bandeau réapparaîtra à la prochaine visite */
        }
      });
    }
  }

  /* ---------- Animation d'entrée du titre hero ---------- */

  var heroTitle = document.querySelector(".hero-title");
  if (heroTitle && !prefersReducedMotion) {
    window.requestAnimationFrame(function () {
      window.requestAnimationFrame(function () {
        heroTitle.classList.add("animate-in");
      });
    });
  }

  /* ---------- Menu mobile ---------- */

  var navToggle = document.getElementById("navToggle");
  var mainNav = document.getElementById("main-nav");

  if (navToggle && mainNav) {
    navToggle.addEventListener("click", function () {
      var isOpen = navToggle.getAttribute("aria-expanded") === "true";
      navToggle.setAttribute("aria-expanded", String(!isOpen));
      navToggle.setAttribute("aria-label", isOpen ? "Ouvrir le menu" : "Fermer le menu");
      mainNav.classList.toggle("is-open", !isOpen);
      document.body.style.overflow = isOpen ? "" : "hidden";
    });

    mainNav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        navToggle.setAttribute("aria-expanded", "false");
        navToggle.setAttribute("aria-label", "Ouvrir le menu");
        mainNav.classList.remove("is-open");
        document.body.style.overflow = "";
      });
    });
  }

  /* ---------- Mega-menus (Services, Ressources) ---------- */

  var menuPairs = [];
  document.querySelectorAll(".services-trigger").forEach(function (trigger) {
    var targetId = trigger.getAttribute("aria-controls");
    var menu = targetId ? document.getElementById(targetId) : null;
    if (menu) {
      menuPairs.push({ trigger: trigger, menu: menu });
    }
  });

  if (menuPairs.length) {
    function closeAllMenus() {
      menuPairs.forEach(function (pair) {
        pair.trigger.setAttribute("aria-expanded", "false");
        pair.menu.classList.remove("is-open");
      });
    }

    menuPairs.forEach(function (pair) {
      pair.trigger.addEventListener("click", function (e) {
        e.stopPropagation();
        var isOpen = pair.trigger.getAttribute("aria-expanded") === "true";
        closeAllMenus();
        if (!isOpen) {
          pair.trigger.setAttribute("aria-expanded", "true");
          pair.menu.classList.add("is-open");
        }
      });

      // Un clic sur un lien du mega-menu ferme aussi le menu mobile parent
      pair.menu.querySelectorAll("a").forEach(function (link) {
        link.addEventListener("click", function () {
          closeAllMenus();
          if (navToggle && mainNav) {
            navToggle.setAttribute("aria-expanded", "false");
            navToggle.setAttribute("aria-label", "Ouvrir le menu");
            mainNav.classList.remove("is-open");
            document.body.style.overflow = "";
          }
        });
      });
    });

    // Ferme au clic en dehors de tout menu (desktop)
    document.addEventListener("click", function (e) {
      var clickedInsideAny = false;
      for (var i = 0; i < menuPairs.length; i++) {
        if (menuPairs[i].menu.contains(e.target) || menuPairs[i].trigger.contains(e.target)) {
          clickedInsideAny = true;
          break;
        }
      }
      if (!clickedInsideAny) closeAllMenus();
    });

    // Ferme à l'échappement, rend le focus au déclencheur ouvert
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        var openTrigger = null;
        for (var j = 0; j < menuPairs.length; j++) {
          if (menuPairs[j].trigger.getAttribute("aria-expanded") === "true") {
            openTrigger = menuPairs[j].trigger;
            break;
          }
        }
        closeAllMenus();
        if (openTrigger) openTrigger.focus();
      }
    });
  }

  /* ---------- Barre de progression de scroll ---------- */

  var progressBar = document.getElementById("scrollProgress");

  function updateScrollProgress() {
    if (!progressBar) return;
    var scrollTop = window.scrollY || document.documentElement.scrollTop;
    var docHeight = document.documentElement.scrollHeight - window.innerHeight;
    var pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    progressBar.style.width = pct + "%";
  }

  /* ---------- Header : compact au scroll ---------- */

  var header = document.querySelector(".site-header");

  function updateHeaderState() {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 24);
  }

  /* ---------- Parallax léger du hero ---------- */

  var heroBlob = document.querySelector(".hero-blob");
  var heroInner = document.querySelector(".hero-inner");

  function updateParallax() {
    if (prefersReducedMotion) return;
    var y = window.scrollY;
    if (heroBlob) {
      heroBlob.style.transform = "translate3d(0, " + y * 0.18 + "px, 0)";
    }
    if (heroInner) {
      var fade = Math.max(0, 1 - y / 500);
      heroInner.style.opacity = fade.toFixed(3);
      heroInner.style.transform = "translate3d(0, " + y * 0.08 + "px, 0)";
    }
  }

  var ticking = false;
  function onScroll() {
    if (!ticking) {
      window.requestAnimationFrame(function () {
        updateScrollProgress();
        updateHeaderState();
        updateParallax();
        ticking = false;
      });
      ticking = true;
    }
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- Compteurs animés (hero-stat) ---------- */

  function animateCount(el) {
    var raw = el.getAttribute("data-count-to");
    if (!raw) return;

    var match = raw.match(/^([^\d]*)(\d+(?:[.,]\d+)?)(.*)$/);
    if (!match) return;

    var prefix = match[1];
    var numStr = match[2];
    var suffix = match[3];
    var hasComma = numStr.indexOf(",") !== -1;
    var target = parseFloat(numStr.replace(",", "."));
    var decimals = hasComma ? numStr.split(",")[1].length : 0;

    var duration = 1100;
    var startTime = null;

    function easeOutExpo(t) {
      return t === 1 ? 1 : 1 - Math.pow(2, -10 * t);
    }

    function step(timestamp) {
      if (startTime === null) startTime = timestamp;
      var progress = Math.min((timestamp - startTime) / duration, 1);
      var eased = easeOutExpo(progress);
      var current = target * eased;
      var display = decimals > 0 ? current.toFixed(decimals).replace(".", ",") : Math.round(current).toString();
      el.textContent = prefix + display + suffix;
      if (progress < 1) {
        window.requestAnimationFrame(step);
      } else {
        el.textContent = prefix + numStr + suffix;
      }
    }

    window.requestAnimationFrame(step);
  }

  /* ---------- Reveal au scroll (différencié par type) ---------- */

  var revealEls = document.querySelectorAll("[data-reveal]");
  var statEls = document.querySelectorAll("[data-count-to]");

  if (prefersReducedMotion || !("IntersectionObserver" in window)) {
    revealEls.forEach(function (el) {
      el.classList.add("is-visible");
    });
    statEls.forEach(function (el) {
      var raw = el.getAttribute("data-count-to");
      if (raw) el.textContent = raw;
    });
  } else {
    var revealObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            var group = entry.target.closest("[data-reveal-group]");
            var siblings = group ? Array.prototype.slice.call(group.querySelectorAll("[data-reveal]")) : [entry.target];
            var index = siblings.indexOf(entry.target);
            var delay = Math.max(0, index) * 90;

            setTimeout(function () {
              entry.target.classList.add("is-visible");
            }, delay);

            revealObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.14, rootMargin: "0px 0px -60px 0px" }
    );

    revealEls.forEach(function (el) {
      revealObserver.observe(el);
    });

    var statObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            animateCount(entry.target);
            statObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.6 }
    );

    statEls.forEach(function (el) {
      statObserver.observe(el);
    });
  }

  /* ---------- Tilt discret au survol (project-card, card) ---------- */

  if (!prefersReducedMotion && window.matchMedia("(hover: hover)").matches) {
    var tiltEls = document.querySelectorAll("[data-tilt]");

    tiltEls.forEach(function (el) {
      var bounds;

      el.addEventListener("pointerenter", function () {
        bounds = el.getBoundingClientRect();
      });

      el.addEventListener("pointermove", function (e) {
        if (!bounds) bounds = el.getBoundingClientRect();
        var x = (e.clientX - bounds.left) / bounds.width - 0.5;
        var y = (e.clientY - bounds.top) / bounds.height - 0.5;
        var rotateX = (-y * 4).toFixed(2);
        var rotateY = (x * 4).toFixed(2);
        el.style.transform = "perspective(800px) rotateX(" + rotateX + "deg) rotateY(" + rotateY + "deg) translateY(-4px)";
      });

      el.addEventListener("pointerleave", function () {
        el.style.transform = "";
      });
    });
  }

  /* ---------- Active nav link selon la section visible ---------- */

  var sections = document.querySelectorAll("main section[id]");
  var navLinks = document.querySelectorAll(".main-nav a[href^='#']");

  if (sections.length && navLinks.length && "IntersectionObserver" in window) {
    var navObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            var id = entry.target.getAttribute("id");
            navLinks.forEach(function (link) {
              link.classList.toggle("is-active", link.getAttribute("href") === "#" + id);
            });
          }
        });
      },
      { rootMargin: "-45% 0px -50% 0px", threshold: 0 }
    );

    sections.forEach(function (section) {
      navObserver.observe(section);
    });
  }
})();
