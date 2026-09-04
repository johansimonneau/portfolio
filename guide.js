/* ==========================================================================
   Johan Simonneau — Portfolio
   guide.js — formulaire de la page ressource "20 prompts Claude pour le
   SEO". Aucun backend propre : les coordonnées sont envoyées via l'API
   AJAX gratuite FormSubmit (https://formsubmit.co), qui relaie directement
   un email à johansimonneau.pro@gmail.com sans dépendre du client mail du
   visiteur. Le lien de téléchargement du PDF est révélé une fois l'envoi
   confirmé.
   ========================================================================== */

(function () {
  "use strict";

  var form = document.getElementById("guideForm");
  if (!form) return;

  var FORMSUBMIT_ENDPOINT = "https://formsubmit.co/ajax/johansimonneau.pro@gmail.com";

  var prenomInput = document.getElementById("guidePrenom");
  var nomInput = document.getElementById("guideNom");
  var emailInput = document.getElementById("guideEmail");
  var honeyInput = document.getElementById("guideHoney");
  var submitBtn = document.getElementById("guideSubmit");
  var errorEl = document.getElementById("guideError");
  var successEl = document.getElementById("guideSuccess");

  var SUBMIT_LABEL_DEFAULT = submitBtn.textContent;
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

  function setLoading(isLoading) {
    submitBtn.disabled = isLoading;
    submitBtn.textContent = isLoading ? "Envoi en cours…" : SUBMIT_LABEL_DEFAULT;
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

    if (honeyInput && honeyInput.value) {
      // Piège anti-spam rempli par un bot : on fait semblant que ça a marché.
      form.hidden = true;
      successEl.hidden = false;
      return;
    }

    setLoading(true);

    fetch(FORMSUBMIT_ENDPOINT, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify({
        Prénom: prenom,
        Nom: nom,
        Email: email,
        Demande: "Téléchargement du guide \"20 prompts Claude pour structurer votre SEO\"",
        "Page": window.location.href,
        _subject: "Téléchargement du guide Claude SEO",
        _captcha: "false",
        _template: "table"
      })
    })
      .then(function (response) {
        return response.text().then(function (raw) {
          // Log brut pour diagnostiquer depuis la console navigateur si besoin.
          console.log("FormSubmit — statut " + response.status + " :", raw);
          var data = null;
          try { data = JSON.parse(raw); } catch (e) { /* réponse non-JSON */ }
          var explicitlyFailed = data && (data.success === false || data.success === "false");
          if (!response.ok || !data || explicitlyFailed) {
            throw new Error("formsubmit-failed");
          }
        });
      })
      .then(function () {
        setLoading(false);
        form.hidden = true;
        successEl.hidden = false;
      })
      .catch(function (err) {
        console.error("Échec de l'envoi du formulaire guide :", err);
        setLoading(false);
        showError("L'envoi a échoué. Réessayez, ou écrivez-moi directement à johansimonneau.pro@gmail.com.");
      });
  });
})();
