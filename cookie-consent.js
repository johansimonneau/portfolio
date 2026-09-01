/* ==========================================================================
   Johan Simonneau — Portfolio
   cookie-consent.js — bandeau de consentement cookies (RGPD / CNIL)
   Fonctionne avec le Consent Mode Google initialisé dans le <head> de
   chaque page (gtag('consent', 'default', {...denied...})).
   Charge aussi Google Tag Manager, mais seulement une fois le consentement
   déjà donné (visite précédente) ou au moment où il est donné — jamais
   avant, pour ne pas télécharger ce script pour rien tant que le
   visiteur n'a pas encore choisi (ou a refusé).
   ========================================================================== */

(function () {
  "use strict";

  var GTM_ID = "GTM-PTBVL88D";
  var gtmLoaded = false;

  function loadGTM() {
    if (gtmLoaded) return;
    gtmLoaded = true;
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({ "gtm.start": new Date().getTime(), event: "gtm.js" });
    var script = document.createElement("script");
    script.async = true;
    script.src = "https://www.googletagmanager.com/gtm.js?id=" + GTM_ID;
    document.head.appendChild(script);
  }

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
    if (existing === "accepted") {
      // Consentement déjà donné lors d'une visite précédente : on charge
      // GTM, mais après l'événement "load" pour ne pas retarder le rendu
      // initial de la page.
      if (document.readyState === "complete") {
        loadGTM();
      } else {
        window.addEventListener("load", loadGTM);
      }
      bindReopenLink();
      return;
    }

    if (existing === "declined") {
      // Choix déjà fait, refusé : rien à afficher ni à charger au
      // chargement. Le lien "Gérer mes cookies" du footer permet de
      // rouvrir le bandeau à tout moment (voir bindReopenLink).
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
      loadGTM();
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
