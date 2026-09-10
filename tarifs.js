/* ==========================================================================
   Johan Simonneau — Portfolio
   tarifs.js — simulateur de TJM interactif sur la page /tarifs. Aucun
   backend : le calcul se fait côté visiteur à partir de la grille de
   dégressivité affichée sur la page (durée d'engagement, volume de jours,
   leviers combinés), plafonnée à -25% au total. Résultat indicatif, le
   tarif définitif est confirmé au moment du devis.
   ========================================================================== */

(function () {
  "use strict";

  var root = document.getElementById("tjmSim");
  if (!root) return;

  var BASE = 550;
  var CAP = 25;
  var state = { duree: 0, volume: 0, leviers: 0 };

  var valueEl = document.getElementById("tjmSimValue");
  var detailEl = document.getElementById("tjmSimDetail");

  function update() {
    var total = state.duree + state.volume + state.leviers;
    var applied = Math.min(total, CAP);
    var price = Math.round(BASE * (1 - applied / 100));
    valueEl.textContent = price;

    if (applied === 0) {
      detailEl.textContent = "Tarif de référence — aucune dégressivité appliquée.";
      return;
    }

    var saved = BASE - price;
    var cappedNote = total > CAP ? " (plafonné à -" + CAP + "%)" : "";
    detailEl.textContent = "Dégressivité de -" + applied + "%" + cappedNote + ", soit " + saved + "€ de moins que le tarif de référence.";
  }

  root.querySelectorAll("[data-sim-group]").forEach(function (group) {
    var key = group.getAttribute("data-sim-group");
    group.querySelectorAll("button").forEach(function (btn) {
      btn.addEventListener("click", function () {
        group.querySelectorAll("button").forEach(function (b) {
          b.classList.remove("is-selected");
        });
        btn.classList.add("is-selected");
        state[key] = parseInt(btn.getAttribute("data-value"), 10);
        update();
      });
    });
  });

  update();
})();
