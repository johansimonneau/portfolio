/* ==========================================================================
   Johan Simonneau — Portfolio
   experiment-hero-cta.js — SIM Lab, Test n°1 : intitulé du CTA principal
   du hero (page d'accueil). Répartition 50/50 par visiteur, mémorisée en
   localStorage. Les événements sont poussés dans dataLayer via gtag ;
   ils ne remontent à Google Analytics que si les cookies de mesure ont
   été acceptés (cf. cookie-consent.js, qui charge GTM sous condition).
   ========================================================================== */

(function () {
  "use strict";

  var cta = document.querySelector('[data-sim-lab="hero-cta"]');
  if (!cta) return;

  var KEY = "simlab_exp_hero_cta";
  var VARIANT_B_TEXT = "Réserver un appel gratuit (30 min)";
  var variant;

  try {
    variant = localStorage.getItem(KEY);
    if (variant !== "A" && variant !== "B") {
      variant = Math.random() < 0.5 ? "A" : "B";
      localStorage.setItem(KEY, variant);
    }
  } catch (e) {
    variant = "A";
  }

  if (variant === "B") {
    cta.textContent = VARIANT_B_TEXT;
  }

  function track(eventName) {
    if (typeof window.gtag === "function") {
      window.gtag("event", eventName, {
        experiment: "hero_cta_copy",
        variant: variant
      });
    }
  }

  track("sim_lab_experiment_view");
  cta.addEventListener("click", function () {
    track("sim_lab_experiment_click");
  });
})();
