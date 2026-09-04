/* ==========================================================================
   Johan Simonneau — Portfolio
   audit-budget-ads.js — auto-diagnostic "10 questions" et boutons copier
   des prompts, pour la page /audit-budget-ads. Aucun backend : le score
   se calcule côté visiteur, la transmission se fait via un lien mailto
   pré-rempli (même mécanisme que /diagnostic).
   ========================================================================== */

(function () {
  "use strict";

  // ---------- Barres des benchmarks ----------
  document.querySelectorAll("[data-bar-chart]").forEach(function (chart) {
    var max = parseFloat(chart.getAttribute("data-bar-max")) || 100;
    chart.querySelectorAll("[data-bar-value]").forEach(function (row) {
      var value = parseFloat(row.getAttribute("data-bar-value"));
      var fill = row.querySelector(".bm-bar-fill");
      if (fill && !isNaN(value)) {
        var percent = Math.min(100, Math.round((value / max) * 100));
        fill.style.width = percent + "%";
      }
    });
  });

  var quiz = document.getElementById("auditQuiz");
  if (quiz) {
    var QUESTIONS = [
      "Vous n'avez pas ajouté de mots-clés négatifs depuis plus de 30 jours",
      "Vous ne savez pas quel % de votre budget PMAX part en Display/YouTube",
      "Vous n'avez pas vérifié votre tracking depuis plus de 3 mois",
      "Tout votre budget pub est sur un seul canal (Google OU Meta, pas les deux)",
      "Votre taux de conversion landing page est inférieur à 5%",
      "Vous n'avez pas uploadé de liste clients dans PMAX (Customer Match)",
      "Vous regardez votre ROAS global sans segmenter par produit/client",
      "Vos CPC ont augmenté de plus de 15% en 1 an sans que votre ROAS suive",
      "Vous ne savez pas combien vous coûte un nouveau client vs un client existant",
      "Vous n'avez jamais audité vos termes de recherche Google Ads"
    ];

    var BANDS = [
      {
        max: 2,
        key: "ok",
        label: "Compte plutôt sain",
        verdict: "Votre compte est probablement bien géré.",
        detail: "Mais un audit externe par un œil neuf ne fait jamais de mal — même les comptes bien gérés ont des angles morts."
      },
      {
        max: 5,
        key: "fuites",
        label: "Des fuites à colmater",
        verdict: "Vous avez des fuites de budget identifiables.",
        detail: "Chaque point ci-dessus correspond à du budget gaspillé chaque mois. Avec des CPC en hausse constante, chaque fuite coûte de plus en plus cher avec le temps."
      },
      {
        max: 8,
        key: "serieux",
        label: "Fuite sérieuse",
        verdict: "Votre compte perd sérieusement de l'argent.",
        detail: "En moyenne, les comptes dans cette zone gaspillent plus de 1 000€ par mois (WordStream, 2026). Un audit est urgent."
      },
      {
        max: 10,
        key: "urgent",
        label: "Reprise à zéro nécessaire",
        verdict: "Il faut tout reprendre.",
        detail: "Chaque jour qui passe coûte de l'argent. 29% des comptes Google Ads ne génèrent aucune conversion malgré des dépenses actives — ne faites pas partie de cette statistique."
      }
    ];

    var listEl = quiz.querySelector("[data-quiz-list]");
    var submitBtn = quiz.querySelector("[data-quiz-submit]");
    var hintEl = quiz.querySelector("[data-quiz-hint]");
    var resultEl = document.getElementById("auditResult");

    var answers = new Array(QUESTIONS.length).fill(null);

    var itemsHtml = "";
    for (var i = 0; i < QUESTIONS.length; i++) {
      itemsHtml +=
        '<div class="audit-quiz-item">' +
        '<span class="audit-quiz-question">' + QUESTIONS[i] + "</span>" +
        '<span class="audit-quiz-toggle" data-question-index="' + i + '">' +
        '<button type="button" data-value="oui">Oui</button>' +
        '<button type="button" data-value="non">Non</button>' +
        "</span>" +
        "</div>";
    }
    listEl.innerHTML = itemsHtml;

    function updateSubmitState() {
      var answeredCount = answers.filter(function (a) { return a !== null; }).length;
      var allAnswered = answeredCount === QUESTIONS.length;
      submitBtn.disabled = !allAnswered;
      hintEl.textContent = allAnswered
        ? "Toutes les questions sont répondues."
        : (QUESTIONS.length - answeredCount) + " question(s) restante(s).";
    }

    listEl.querySelectorAll("[data-question-index]").forEach(function (toggle) {
      var qIndex = parseInt(toggle.getAttribute("data-question-index"), 10);
      toggle.querySelectorAll("button").forEach(function (btn) {
        btn.addEventListener("click", function () {
          answers[qIndex] = btn.getAttribute("data-value") === "oui";
          toggle.querySelectorAll("button").forEach(function (b) { b.classList.remove("is-selected"); });
          btn.classList.add("is-selected");
          updateSubmitState();
        });
      });
    });

    function bandFor(score) {
      for (var i = 0; i < BANDS.length; i++) {
        if (score <= BANDS[i].max) return BANDS[i];
      }
      return BANDS[BANDS.length - 1];
    }

    submitBtn.addEventListener("click", function () {
      var score = answers.filter(function (a) { return a === true; }).length;
      var band = bandFor(score);

      var bodyLines = [
        "Bonjour Johan,",
        "",
        "J'ai fait l'auto-diagnostic \"Fuites de budget Ads\" sur johansimonneau.fr : " + score + "/10 OUI (" + band.label + ").",
        "",
        "J'aimerais échanger sur mon compte Google Ads / Meta Ads."
      ];
      var mailtoLink =
        "mailto:johansimonneau.pro@gmail.com?subject=" +
        encodeURIComponent("Mon auto-diagnostic budget Ads (" + score + "/10)") +
        "&body=" + encodeURIComponent(bodyLines.join("\n"));

      resultEl.setAttribute("data-band", band.key);
      resultEl.innerHTML =
        '<div class="audit-result-score">' + score + "/10</div>" +
        '<p class="audit-result-score-label">réponses "Oui"</p>' +
        '<span class="audit-result-band">' + band.label + "</span>" +
        '<p class="audit-result-verdict">' + band.verdict + "</p>" +
        '<p class="audit-result-detail">' + band.detail + "</p>" +
        '<div class="sub-cta-actions audit-result-actions">' +
        '<a href="' + mailtoLink + '" class="btn btn-primary">Demander un audit Ads</a>' +
        '<a href="/sea" class="btn btn-ghost">Voir la page SEA</a>' +
        "</div>" +
        '<button type="button" class="audit-restart" data-audit-restart>Refaire le diagnostic</button>';

      resultEl.classList.add("is-visible");
      quiz.hidden = true;
      resultEl.scrollIntoView({ behavior: "smooth", block: "start" });

      resultEl.querySelector("[data-audit-restart]").addEventListener("click", function () {
        answers = new Array(QUESTIONS.length).fill(null);
        listEl.querySelectorAll("button").forEach(function (b) { b.classList.remove("is-selected"); });
        updateSubmitState();
        resultEl.classList.remove("is-visible");
        quiz.hidden = false;
        quiz.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });

    updateSubmitState();
  }

  // ---------- Copier les prompts ----------
  document.querySelectorAll("[data-copy-prompt]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var targetId = btn.getAttribute("data-copy-prompt");
      var block = document.getElementById(targetId);
      if (!block) return;

      var text = block.textContent;
      var defaultLabel = btn.textContent;

      function showCopied() {
        btn.textContent = "Copié !";
        btn.classList.add("is-copied");
        setTimeout(function () {
          btn.textContent = defaultLabel;
          btn.classList.remove("is-copied");
        }, 2000);
      }

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(showCopied).catch(function () {
          btn.textContent = "Sélectionnez et copiez";
        });
      } else {
        btn.textContent = "Sélectionnez et copiez";
      }
    });
  });
})();
