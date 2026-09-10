/* ==========================================================================
   Johan Simonneau — Portfolio
   audit-geo.js — auto-diagnostic "10 questions" GEO pour la page
   /audit-geo. Aucun backend : le score se calcule côté visiteur, la
   transmission se fait via un lien mailto pré-rempli (même mécanisme que
   /diagnostic et /audit-budget-ads). Réutilise les classes .audit-quiz /
   .audit-result définies dans audit-budget-ads.css.
   ========================================================================== */

(function () {
  "use strict";

  var quiz = document.getElementById("auditGeoQuiz");
  if (!quiz) return;

  var QUESTIONS = [
    "Votre site n'a pas de données structurées JSON-LD (FAQPage, Organization, Service...).",
    "Vos pages n'ont pas de section questions-réponses clairement identifiable.",
    "L'essentiel de vos informations clés n'est pas énoncé dès le début de vos pages (il faut chercher pour le trouver).",
    "Le nom de votre entreprise, votre activité ou vos coordonnées varient d'un endroit à l'autre du web (site, réseaux, annuaires).",
    "Vous n'avez jamais testé si votre marque ou votre expertise apparaît dans les réponses de ChatGPT, Claude ou Perplexity.",
    "Vos pages n'ont pas de hiérarchie de titres claire et cohérente (H1, H2, H3...).",
    "Vos contenus existants ne sont jamais mis à jour (certaines pages n'ont pas bougé depuis plus d'un an).",
    "Vos pages n'affichent pas de signaux de fiabilité identifiables (auteur, expertise démontrée, page à propos).",
    "Vous n'avez pas de page FAQ ou de contenu structuré en question/réponse sur votre site.",
    "Vous ne savez pas si vos concurrents apparaissent, eux, dans les réponses IA sur vos sujets clés."
  ];

  var BANDS = [
    {
      max: 2,
      key: "ok",
      label: "Fondations solides",
      verdict: "Vos bases GEO sont plutôt bien posées.",
      detail: "La structuration et les données structurées sont en place. La suite consiste à tester régulièrement votre visibilité réelle sur ChatGPT, Claude et Perplexity, et à ajuster au fil de l'eau."
    },
    {
      max: 5,
      key: "fuites",
      label: "Des fondations à renforcer",
      verdict: "Quelques manques identifiables freinent votre visibilité IA.",
      detail: "Chaque point ci-dessus correspond à un frein connu à l'extraction et à la citation par les moteurs génératifs. Ce sont aussi, pour la plupart, des bonnes pratiques SEO classiques — les corriger sert les deux."
    },
    {
      max: 8,
      key: "serieux",
      label: "Visibilité IA à construire",
      verdict: "Votre contenu est aujourd'hui difficile à extraire et à citer pour une IA générative.",
      detail: "Les moteurs génératifs croisent plusieurs sources pour évaluer la fiabilité d'une information — sans structure claire ni cohérence de marque, ils ont peu de chances de vous choisir plutôt qu'un concurrent mieux structuré."
    },
    {
      max: 10,
      key: "urgent",
      label: "Quasiment invisible pour les IA génératives",
      verdict: "Sur la base de ces critères, votre site est aujourd'hui mal préparé pour être cité par une IA.",
      detail: "Le GEO est un champ récent où les mécaniques évoluent vite : plus tôt les fondations sont posées, plus tôt elles portent leurs fruits — comme pour le SEO à ses débuts."
    }
  ];

  var list = quiz.querySelector("[data-quiz-list]");
  var submit = quiz.querySelector("[data-quiz-submit]");
  var hint = quiz.querySelector("[data-quiz-hint]");
  var result = document.getElementById("auditGeoResult");
  var answers = new Array(QUESTIONS.length).fill(null);

  var html = "";
  for (var i = 0; i < QUESTIONS.length; i++) {
    html +=
      '<div class="audit-quiz-item"><span class="audit-quiz-question">' +
      QUESTIONS[i] +
      '</span><span class="audit-quiz-toggle" data-question-index="' +
      i +
      '"><button type="button" data-value="oui">Oui</button><button type="button" data-value="non">Non</button></span></div>';
  }
  list.innerHTML = html;

  function updateHint() {
    var answered = answers.filter(function (a) { return a !== null; }).length;
    var complete = answered === QUESTIONS.length;
    submit.disabled = !complete;
    hint.textContent = complete
      ? "Toutes les questions sont répondues."
      : (QUESTIONS.length - answered) + " question(s) restante(s).";
  }

  function bandFor(score) {
    for (var i = 0; i < BANDS.length; i++) {
      if (score <= BANDS[i].max) return BANDS[i];
    }
    return BANDS[BANDS.length - 1];
  }

  list.querySelectorAll("[data-question-index]").forEach(function (toggle) {
    var index = parseInt(toggle.getAttribute("data-question-index"), 10);
    toggle.querySelectorAll("button").forEach(function (btn) {
      btn.addEventListener("click", function () {
        answers[index] = btn.getAttribute("data-value") === "oui";
        toggle.querySelectorAll("button").forEach(function (b) {
          b.classList.remove("is-selected");
        });
        btn.classList.add("is-selected");
        updateHint();
      });
    });
  });

  submit.addEventListener("click", function () {
    var score = answers.filter(function (a) { return a === true; }).length;
    var band = bandFor(score);
    var bodyLines = [
      "Bonjour Johan,",
      "",
      "J'ai fait l'auto-diagnostic GEO sur johansimonneau.fr : " + score + "/10 OUI (" + band.label + ").",
      "",
      "J'aimerais échanger sur la visibilité de mon site dans les IA génératives."
    ];
    var mailto =
      "mailto:johansimonneau.pro@gmail.com?subject=" +
      encodeURIComponent("Mon auto-diagnostic GEO (" + score + "/10)") +
      "&body=" +
      encodeURIComponent(bodyLines.join("\n"));

    result.setAttribute("data-band", band.key);
    result.innerHTML =
      '<div class="audit-result-score">' + score + '/10</div>' +
      '<p class="audit-result-score-label">réponses "Oui"</p>' +
      '<span class="audit-result-band">' + band.label + '</span>' +
      '<p class="audit-result-verdict">' + band.verdict + '</p>' +
      '<p class="audit-result-detail">' + band.detail + '</p>' +
      '<div class="sub-cta-actions audit-result-actions">' +
      '<a href="' + mailto + '" class="btn btn-primary">Échanger sur ma visibilité IA</a>' +
      '<a href="/geo" class="btn btn-ghost">Voir la page GEO</a>' +
      '</div>' +
      '<button type="button" class="audit-restart" data-audit-restart>Refaire le diagnostic</button>';
    result.classList.add("is-visible");
    quiz.hidden = true;
    result.scrollIntoView({ behavior: "smooth", block: "start" });

    result.querySelector("[data-audit-restart]").addEventListener("click", function () {
      answers = new Array(QUESTIONS.length).fill(null);
      list.querySelectorAll("button").forEach(function (b) {
        b.classList.remove("is-selected");
      });
      updateHint();
      result.classList.remove("is-visible");
      quiz.hidden = false;
      quiz.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });

  updateHint();
})();
