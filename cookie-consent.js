/* ==========================================================================
   Johan Simonneau — Portfolio
   cookie-consent.js — bandeau de consentement cookies (RGPD / CNIL)
   Fonctionne avec le Consent Mode Google initialisé dans le <head> de
   chaque page (gtag('consent', 'default', {...denied...})).
   ========================================================================== */

(function () {
  "use strict";

  var STORAGE_KEY = "cookie_consent";
  var existing = null;

  try {
    existing = localStorage.getItem(STORAGE_KEY);
  } catch (e) {
    // localStorage indisponible (navigation privée stricte, etc.) : on
    // affichera le bandeau à chaque visite plutôt que de bloquer le site.
  }

  function updateConsent(granted) {
    if (typeof window.gtag !== "function") return;
    window.gtag("consent", "update", {
      analytics_storage: granted ? "granted" : "denied",
    });
  }

  function storeChoice(value) {
    try {
      localStorage.setItem(STORAGE_KEY, value);
    } catch (e) {
      /* pas de stockage possible, le choix ne sera pas mémorisé */
    }
  }

  function buildBanner() {
    var wrapper = document.createElement("div");
    wrapper.id = "cookieConsent";
    wrapper.setAttribute("role", "dialog");
    wrapper.setAttribute("aria-label", "Gestion des cookies");
    wrapper.innerHTML =
      '<div class="cookie-consent-card">' +
      '<p class="cookie-consent-text">' +
      "Ce site utilise des cookies de mesure d'audience (<strong>Google Analytics</strong>) pour comprendre comment il est consulté. " +
      'Ces cookies ne sont déposés qu\'avec votre accord. En savoir plus dans notre <a href="/politique-de-confidentialite">politique de confidentialité</a>.' +
      "</p>" +
      '<div class="cookie-consent-actions">' +
      '<button type="button" id="cookieDecline">Refuser</button>' +
      '<button type="button" id="cookieAccept">Accepter</button>' +
      "</div>" +
      "</div>";
    document.body.appendChild(wrapper);
    return wrapper;
  }

  function init() {
    if (existing === "accepted" || existing === "declined") {
      // Choix déjà fait : rien à afficher au chargement. Le consentement
      // "accepted" a déjà été appliqué au Consent Mode par le script
      // inline du <head>. Le lien "Gérer mes cookies" du footer permet
      // de rouvrir le bandeau à tout moment (voir bindReopenLink).
      bindReopenLink();
      return;
    }

    showBanner();
    bindReopenLink();
  }

  function showBanner() {
    var banner = document.getElementById("cookieConsent") || buildBanner();

    window.requestAnimationFrame(function () {
      window.requestAnimationFrame(function () {
        banner.classList.add("is-visible");
      });
    });

    document.getElementById("cookieAccept").addEventListener("click", function () {
      storeChoice("accepted");
      updateConsent(true);
      hideBanner(banner);
    });

    document.getElementById("cookieDecline").addEventListener("click", function () {
      storeChoice("declined");
      updateConsent(false);
      hideBanner(banner);
    });
  }

  function hideBanner(banner) {
    banner.classList.remove("is-visible");
    window.setTimeout(function () {
      banner.remove();
    }, 320);
  }

  function bindReopenLink() {
    var reopenLink = document.getElementById("cookieManage");
    if (!reopenLink) return;
    reopenLink.addEventListener("click", function (e) {
      e.preventDefault();
      if (document.getElementById("cookieConsent")) return;
      showBanner();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
