/* ==========================================================================
   Johan Simonneau — Portfolio
   diagnostic.js — logique du quiz "Score de maturité Growth Marketing"
   Chargé uniquement sur diagnostic.html. Aucun backend : tout se calcule
   côté visiteur, la transmission des résultats se fait via un lien mailto
   pré-rempli (cohérent avec le reste du site, aucune donnée stockée).
   ========================================================================== */

(function () {
  "use strict";

  var root = document.getElementById("diagnosticApp");
  if (!root) return;

  var QUESTIONS = [
    {
      axis: "tracking",
      axisLabel: "Tracking & mesure",
      question: "Comment est configuré votre tracking (GA4 / GTM) aujourd'hui ?",
      pillarUrl: "/analytics",
      pillarLabel: "Analytics",
      options: [
        "Pas de GA4 installé, ou configuration jamais vérifiée",
        "GA4 installé mais peu d'événements de conversion configurés",
        "GA4 et conversions configurés, pas de Conversion API ni de Consent Mode",
        "GA4, Conversion API et Consent Mode bien configurés"
      ]
    },
    {
      axis: "acquisition",
      axisLabel: "Acquisition payante",
      question: "Où en sont vos campagnes publicitaires (Google Ads, Meta Ads...) ?",
      pillarUrl: "/sea",
      pillarLabel: "SEA",
      options: [
        "Aucune campagne active actuellement",
        "Campagnes actives, jamais auditées depuis plus de 6 mois",
        "Campagnes optimisées régulièrement, CPA et ROAS suivis",
        "Stratégie multi-plateformes pilotée avec des objectifs ROAS clairs"
      ]
    },
    {
      axis: "seo",
      axisLabel: "SEO",
      question: "Où en est votre visibilité sur les moteurs de recherche classiques ?",
      pillarUrl: "/seo",
      pillarLabel: "SEO",
      options: [
        "Pas de stratégie SEO définie",
        "Quelques optimisations ponctuelles, sans suivi régulier",
        "Stratégie de contenu en place, suivi de positions",
        "Stratégie mature : cocons sémantiques, netlinking actif"
      ]
    },
    {
      axis: "geo",
      axisLabel: "Visibilité IA (GEO)",
      question: "Savez-vous si votre marque apparaît dans les réponses de ChatGPT, Claude ou Perplexity sur votre secteur ?",
      pillarUrl: "/geo",
      pillarLabel: "GEO",
      options: [
        "Jamais vérifié",
        "Vérifié une fois manuellement, sans plan d'action",
        "Un début d'optimisation de contenu pour le GEO",
        "Suivi régulier et contenu spécifiquement optimisé"
      ]
    },
    {
      axis: "cro",
      axisLabel: "CRO / conversion",
      question: "Testez-vous et optimisez-vous vos pages de destination ?",
      pillarUrl: "/cro",
      pillarLabel: "CRO",
      options: [
        "Jamais d'A/B test ni d'optimisation",
        "Modifications ponctuelles, sans mesure rigoureuse",
        "A/B tests occasionnels sur les pages clés",
        "Programme de test continu, avec méthodologie"
      ]
    },
    {
      axis: "pilotage",
      axisLabel: "Pilotage global",
      question: "À quelle fréquence analysez-vous vos indicateurs de croissance (CAC, ROAS, LTV...) ?",
      pillarUrl: "/comment-je-travaille",
      pillarLabel: "Comment je travaille",
      options: [
        "Jamais, ou pas d'indicateurs définis",
        "Occasionnellement, sans tableau de bord",
        "Mensuellement, via un tableau de bord",
        "En continu, avec objectifs et alertes"
      ]
    }
  ];

  var MAX_POINTS_PER_QUESTION = 3;
  var MAX_TOTAL = QUESTIONS.length * MAX_POINTS_PER_QUESTION;

  var answers = new Array(QUESTIONS.length).fill(null);
  var currentIndex = 0;

  var quizEl = root.querySelector("[data-quiz]");
  var resultsEl = root.querySelector("[data-results]");
  var progressBarEl = root.querySelector("[data-progress-bar]");
  var progressLabelEl = root.querySelector("[data-progress-label]");
  var questionCardEl = root.querySelector("[data-question-card]");
  var backBtn = root.querySelector("[data-back-btn]");

  function renderQuestion() {
    var q = QUESTIONS[currentIndex];
    progressLabelEl.textContent = "Question " + (currentIndex + 1) + " / " + QUESTIONS.length;
    progressBarEl.style.width = Math.round((currentIndex / QUESTIONS.length) * 100) + "%";
    backBtn.style.visibility = currentIndex === 0 ? "hidden" : "visible";

    var optionsHtml = "";
    for (var i = 0; i < q.options.length; i++) {
      var isSelected = answers[currentIndex] === i;
      optionsHtml +=
        '<button type="button" class="diag-option' + (isSelected ? " is-selected" : "") + '" data-option-index="' + i + '">' +
        '<span class="diag-option-radio" aria-hidden="true"></span>' +
        '<span>' + q.options[i] + "</span>" +
        "</button>";
    }

    questionCardEl.innerHTML =
      '<p class="diag-axis">' + q.axisLabel + "</p>" +
      "<h2>" + q.question + "</h2>" +
      '<div class="diag-options">' + optionsHtml + "</div>";

    var optionButtons = questionCardEl.querySelectorAll("[data-option-index]");
    optionButtons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var idx = parseInt(btn.getAttribute("data-option-index"), 10);
        answers[currentIndex] = idx;
        if (currentIndex < QUESTIONS.length - 1) {
          currentIndex++;
          renderQuestion();
        } else {
          progressBarEl.style.width = "100%";
          progressLabelEl.textContent = "Terminé";
          showResults();
        }
      });
    });
  }

  backBtn.addEventListener("click", function () {
    if (currentIndex > 0) {
      currentIndex--;
      renderQuestion();
    }
  });

  function verdictFor(percent) {
    if (percent < 34) {
      return "Les fondations sont à poser. C'est le meilleur moment pour structurer les choses proprement plutôt que d'accumuler les correctifs plus tard.";
    }
    if (percent < 67) {
      return "De bonnes bases sont posées, avec une vraie marge de progression sur au moins un des piliers.";
    }
    return "Une maturité growth avancée. Le potentiel de gain se trouve maintenant dans le détail plus que dans les fondations.";
  }

  function showResults() {
    var totalPoints = 0;
    var axisRows = "";
    var weakest = null;

    for (var i = 0; i < QUESTIONS.length; i++) {
      var points = answers[i] === null ? 0 : answers[i];
      totalPoints += points;
      if (weakest === null || points < weakest.points) {
        weakest = { points: points, question: QUESTIONS[i] };
      }
    }

    var percent = Math.round((totalPoints / MAX_TOTAL) * 100);

    for (var j = 0; j < QUESTIONS.length; j++) {
      var p = answers[j] === null ? 0 : answers[j];
      var barPercent = Math.round((p / MAX_POINTS_PER_QUESTION) * 100);
      axisRows +=
        '<div class="diag-axis-row">' +
        '<span class="diag-axis-row-label">' + QUESTIONS[j].axisLabel + "</span>" +
        '<span class="diag-axis-row-bar"><span data-bar-fill="' + barPercent + '"></span></span>' +
        '<span class="diag-axis-row-score">' + p + "/" + MAX_POINTS_PER_QUESTION + "</span>" +
        "</div>";
    }

    var bodyLines = [
      "Bonjour Johan,",
      "",
      "J'ai fait le diagnostic Growth Marketing sur johansimonneau.fr, voici mon score : " + percent + "% (" + totalPoints + "/" + MAX_TOTAL + ").",
      "",
      "Détail par pilier :"
    ];
    for (var k = 0; k < QUESTIONS.length; k++) {
      var pk = answers[k] === null ? 0 : answers[k];
      bodyLines.push("- " + QUESTIONS[k].axisLabel + " : " + pk + "/" + MAX_POINTS_PER_QUESTION);
    }
    bodyLines.push("");
    bodyLines.push("J'aimerais échanger sur mon pilier le plus faible (" + weakest.question.axisLabel + ").");

    var mailtoLink =
      "mailto:johansimonneau.pro@gmail.com?subject=" +
      encodeURIComponent("Mon diagnostic Growth Marketing (" + percent + "%)") +
      "&body=" + encodeURIComponent(bodyLines.join("\n"));

    resultsEl.innerHTML =
      '<p class="diag-axis">Votre résultat</p>' +
      '<div class="diag-score">' + percent + "%</div>" +
      '<p class="diag-verdict">' + verdictFor(percent) + "</p>" +
      '<div class="diag-axis-rows">' + axisRows + "</div>" +
      '<div class="diag-recommendation">' +
      "<p>Le pilier avec le plus de potentiel d'amélioration&nbsp;: <strong>" + weakest.question.axisLabel + "</strong>.</p>" +
      '<a href="' + weakest.question.pillarUrl + '" class="btn btn-ghost">Voir la page ' + weakest.question.pillarLabel + "</a>" +
      "</div>" +
      '<div class="sub-cta-actions diag-actions">' +
      '<a href="' + mailtoLink + '" class="btn btn-primary">Recevoir mon diagnostic par email</a>' +
      '<a href="https://calendly.com/johan-simonneau/30min" class="btn btn-ghost" target="_blank" rel="noopener">Prendre RDV</a>' +
      "</div>" +
      '<button type="button" class="diag-restart" data-restart>Refaire le diagnostic</button>';

    resultsEl.querySelectorAll("[data-bar-fill]").forEach(function (fill) {
      fill.style.width = fill.getAttribute("data-bar-fill") + "%";
    });

    resultsEl.querySelector("[data-restart]").addEventListener("click", function () {
      answers = new Array(QUESTIONS.length).fill(null);
      currentIndex = 0;
      resultsEl.style.display = "none";
      quizEl.style.display = "block";
      renderQuestion();
    });

    quizEl.style.display = "none";
    resultsEl.style.display = "block";
  }

  renderQuestion();
})();
