/* ==========================================================================
   Johan Simonneau — Portfolio
   utm-tracking.js — Attribution persistante (UTM + click IDs).

   - Capture à l'arrivée : utm_source/medium/campaign/term/content, click IDs
     (gclid, gbraid, wbraid, fbclid, msclkid, ttclid, li_fat_id), page
     d'atterrissage et référent. Sans paramètre, la source est déduite du
     référent (moteur de recherche → organic, assistant IA → ai, autre
     site → referral), sinon "(direct)".
   - Conserve deux touches : la première (jamais écrasée) et la dernière
     non directe (une visite directe n'écrase pas une source connue).
   - Stockage : sessionStorage pour la visite en cours ; localStorage
     (90 jours) uniquement si les cookies de mesure ont été acceptés
     (cf. cookie-consent.js). Un refus purge la copie persistante.
   - Restitution : ajoutée au corps des emails (liens mailto, statiques ou
     générés par diagnostic/audits), aux liens Calendly (paramètres utm_*
     natifs) et exposée via window.simAttribution (formulaire guide.js).
     Un événement "attribution_ready" est poussé dans dataLayer pour GTM.
   ========================================================================== */

(function () {
  "use strict";

  var KEY = "sim_attribution";
  var TTL = 90 * 24 * 60 * 60 * 1000;
  var UTM = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content"];
  var CLICK_IDS = ["gclid", "gbraid", "wbraid", "fbclid", "msclkid", "ttclid", "li_fat_id"];
  var SEARCH = /(^|\.)(google|bing|duckduckgo|qwant|ecosia|yahoo|yandex|baidu|startpage|brave)\./;
  var AI = /(^|\.)(chatgpt\.com|chat\.openai\.com|perplexity\.ai|claude\.ai|gemini\.google\.com|copilot\.microsoft\.com|mistral\.ai|you\.com)$/;

  function consented() {
    try { return localStorage.getItem("cookie_consent") === "accepted"; } catch (e) { return false; }
  }

  function read(store) {
    try {
      var data = JSON.parse(store.getItem(KEY));
      if (data && data.first && (!data.expires || data.expires > Date.now())) return data;
    } catch (e) {}
    return null;
  }

  function save(data) {
    try { sessionStorage.setItem(KEY, JSON.stringify(data)); } catch (e) {}
    try {
      if (consented()) {
        data.expires = Date.now() + TTL;
        localStorage.setItem(KEY, JSON.stringify(data));
      } else {
        localStorage.removeItem(KEY);
      }
    } catch (e) {}
  }

  function referrerHost() {
    if (!document.referrer) return "";
    try {
      var host = new URL(document.referrer).hostname.replace(/^www\./, "");
      return host === window.location.hostname.replace(/^www\./, "") ? "" : host;
    } catch (e) { return ""; }
  }

  function currentTouch() {
    var params = new URLSearchParams(window.location.search);
    var touch = {};
    var tagged = false;
    UTM.concat(CLICK_IDS).forEach(function (k) {
      var v = params.get(k);
      if (v) { touch[k] = v.slice(0, 200); tagged = true; }
    });

    var ref = referrerHost();
    if (!tagged) {
      if (!ref) return null;
      touch.utm_source = ref;
      touch.utm_medium = SEARCH.test(ref) ? "organic" : AI.test(ref) ? "ai" : "referral";
    } else if (!touch.utm_source) {
      // Click ID sans UTM (auto-tagging) : on déduit la plateforme.
      touch.utm_source = touch.gclid || touch.gbraid || touch.wbraid ? "google"
        : touch.msclkid ? "bing" : touch.fbclid ? "meta"
        : touch.ttclid ? "tiktok" : touch.li_fat_id ? "linkedin" : ref || "(unknown)";
      touch.utm_medium = touch.fbclid && !touch.gclid ? "paid_social" : "cpc";
    }
    touch.landing_page = window.location.pathname;
    if (ref) touch.referrer = ref;
    touch.ts = new Date().toISOString();
    return touch;
  }

  var session = read(sessionStorage);
  var data = session || read(localStorage);
  var touch = currentTouch();

  var sameAsLast = session && touch && ["utm_source", "utm_medium", "utm_campaign", "gclid"].every(function (k) {
    return (touch[k] || "") === (session.last[k] || "");
  });

  if (touch && !sameAsLast) {
    data = data ? { first: data.first, last: touch } : { first: touch, last: touch };
  } else if (!data) {
    var direct = { utm_source: "(direct)", utm_medium: "(none)", landing_page: window.location.pathname, ts: new Date().toISOString() };
    data = { first: direct, last: direct };
  }
  save(data);

  function format(t) {
    var parts = [t.utm_source + " / " + t.utm_medium];
    if (t.utm_campaign) parts.push("campagne : " + t.utm_campaign);
    if (t.utm_content) parts.push("contenu : " + t.utm_content);
    if (t.utm_term) parts.push("mot-clé : " + t.utm_term);
    parts.push("arrivée sur " + t.landing_page + " le " + t.ts.slice(0, 10));
    return parts.join(" — ");
  }

  function clickIds() {
    var out = [];
    CLICK_IDS.forEach(function (k) {
      var v = data.last[k] || data.first[k];
      if (v) out.push(k + " : " + v);
    });
    return out;
  }

  function summary() {
    var lines = ["", "", "— Provenance (merci de ne pas supprimer) —", "Première visite : " + format(data.first)];
    if (data.last.ts !== data.first.ts) lines.push("Dernière source : " + format(data.last));
    return lines.concat(clickIds()).join("\n");
  }

  function fields() {
    var out = {
      "Source (1re visite)": format(data.first),
      "Source (dernière)": format(data.last)
    };
    CLICK_IDS.forEach(function (k) {
      var v = data.last[k] || data.first[k];
      if (v) out[k] = v;
    });
    return out;
  }

  window.simAttribution = {
    get: function () { return JSON.parse(JSON.stringify(data)); },
    summary: summary,
    fields: fields
  };

  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({
    event: "attribution_ready",
    first_source: data.first.utm_source,
    first_medium: data.first.utm_medium,
    first_campaign: data.first.utm_campaign || "(not set)",
    last_source: data.last.utm_source,
    last_medium: data.last.utm_medium,
    last_campaign: data.last.utm_campaign || "(not set)"
  });

  // Enrichit les liens au moment du clic : couvre aussi les mailto générés
  // dynamiquement (diagnostic, audits) après le chargement de la page.
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href]");
    if (!a) return;
    var href = a.getAttribute("href");

    if (href.indexOf("mailto:") === 0) {
      if (href.indexOf(encodeURIComponent("— Provenance")) !== -1) return;
      var hasQuery = href.indexOf("?") !== -1;
      var m = href.match(/([?&])body=([^&]*)/);
      if (m) {
        a.setAttribute("href", href.replace(m[0], m[1] + "body=" + m[2] + encodeURIComponent(summary())));
      } else {
        a.setAttribute("href", href + (hasQuery ? "&" : "?") + "body=" + encodeURIComponent(summary().replace(/^\n+/, "")));
      }
      return;
    }

    if (/^https:\/\/calendly\.com\/johan-simonneau\//.test(href)) {
      try {
        var url = new URL(href);
        UTM.forEach(function (k) {
          var v = data.last[k];
          if (v && !url.searchParams.has(k)) url.searchParams.set(k, v);
        });
        a.setAttribute("href", url.toString());
      } catch (err) {}
    }
  }, true);

  // Bascule immédiate selon le choix fait dans le bandeau de consentement.
  document.addEventListener("click", function (e) {
    var id = e.target && e.target.id;
    if (id === "cookieAccept" || id === "cookieDecline") {
      window.setTimeout(function () { save(data); }, 0);
    }
  });
})();
