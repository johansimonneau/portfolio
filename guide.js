/* ==========================================================================
   Johan Simonneau — Portfolio
   guide.js — formulaire de la page ressource "20 prompts Claude pour le
   SEO". Aucun backend : les coordonnées sont transmises via un lien mailto
   pré-rempli (même mécanisme que le reste du site), puis le lien de
   téléchargement du PDF est révélé.
   ========================================================================== */

(function () {
  "use strict";

  var form = document.getElementById("guideForm");
  if (!form) return;

  var prenomInput = document.getElementById("guidePrenom");
  var nomInput = document.getElementById("guideNom");
  var emailInput = document.getElementById("guideEmail");
  var submitBtn = document.getElementById("guideSubmit");
  var errorEl = document.getElementById("guideError");
  var successEl = document.getElementById("guideSuccess");

  var EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  function showError(message) {
    errorEl.textContent = message;
    errorEl.hidden = false;
  }

  function clearError() {
    errorEl.hidden = true;
    errorEl.textContent = "";
    prenomInput.classList.remove("has-error");
    emailInput.classList.remove("has-error");
  }

  submitBtn.addEventListener("click", function () {
    clearError();

    var prenom = prenomInput.value.trim();
    var nom = nomInput.value.trim();
    var email = emailInput.value.trim();

    if (!prenom) {
      prenomInput.classList.add("has-error");
      showError("Merci de renseigner votre prénom.");
      prenomInput.focus();
      return;
    }

    if (!email || !EMAIL_PATTERN.test(email)) {
      emailInput.classList.add("has-error");
      showError("Merci de renseigner une adresse email valide.");
      emailInput.focus();
      return;
    }

    var bodyLines = [
      "Prénom : " + prenom,
      "Nom : " + nom,
      "Email : " + email,
      "",
      "A demandé le guide \"20 prompts Claude pour structurer votre SEO\".",
      "URL de la demande : " + window.location.href
    ].join("\n");

    var mailtoLink =
      "mailto:johansimonneau.pro@gmail.com?subject=" +
      encodeURIComponent("Téléchargement du guide Claude SEO") +
      "&body=" + encodeURIComponent(bodyLines);

    window.location.href = mailtoLink;

    form.hidden = true;
    successEl.hidden = false;
  });
})();
