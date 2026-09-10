/* ==========================================================================
   Johan Simonneau — Portfolio
   impact-semrush.js — Pixel d'affiliation Semrush (réseau Impact).
   Chargé uniquement après consentement aux cookies de mesure (même
   logique que le chargement de GTM dans cookie-consent.js) : au
   chargement de la page si déjà accepté, ou au clic sur "Accepter" si
   le consentement est donné en cours de visite. Externalisé (au lieu
   du snippet inline fourni par Impact) pour rester compatible avec le
   CSP du site (script-src 'self', pas de script inline).
   ========================================================================== */

(function () {
  "use strict";

  var loaded = false;

  function loadImpact() {
    if (loaded) return;
    loaded = true;
    (function (i, m, p, a, c, t) {
      c.ire_o = p;
      c[p] = c[p] || function () { (c[p].a = c[p].a || []).push(arguments); };
      t = a.createElement(m);
      var z = a.getElementsByTagName(m)[0];
      t.async = 1;
      t.src = i;
      z.parentNode.insertBefore(t, z);
    })("https://utt.impactcdn.com/P-A4109584-b738-4263-b5f7-1730d392c8231.js", "script", "impactStat", document, window);
    window.impactStat("transformLinks");
    window.impactStat("trackImpression");
  }

  var consent;
  try {
    consent = localStorage.getItem("cookie_consent");
  } catch (e) {
    consent = null;
  }

  if (consent === "accepted") {
    loadImpact();
  } else {
    document.addEventListener("click", function (e) {
      if (e.target && e.target.id === "cookieAccept") loadImpact();
    });
  }
})();
