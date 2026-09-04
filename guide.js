/* ==========================================================================
   Johan Simonneau — Portfolio
   guide.js — formulaire partagé par les pages ressource "guide" (Claude &
   SEO, GEO...). Aucun backend propre : les coordonnées sont envoyées via
   l'API Web3Forms (https://web3forms.com), qui relaie directement un
   email à johansimonneau.pro@gmail.com sans dépendre du client mail du
   visiteur. La clé d'accès est publique par conception (documentation
   Web3Forms) : elle identifie seulement la boîte mail de destination, elle
   ne donne aucun accès en lecture. Le lien de téléchargement du PDF est
   révélé une fois l'envoi confirmé. Le nom du guide est lu depuis
   l'attribut data-guide-name du formulaire pour rester générique d'une
   page à l'autre.
   ========================================================================== */

(function () {
  "use strict";

  var form = document.getElementById("guideForm");
  if (!form) return;

  var WEB3FORMS_ENDPOINT = "https://api.web3forms.com/submit";
  var WEB3FORMS_ACCESS_KEY = "d5498fee-c4ba-4887-aeb1-70ee410fd1a1";
  var GUIDE_NAME = form.getAttribute("data-guide-name") || "un guide";

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

    fetch(WEB3FORMS_ENDPOINT, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify({
        access_key: WEB3FORMS_ACCESS_KEY,
        subject: "Téléchargement du guide \"" + GUIDE_NAME + "\"",
        from_name: prenom + (nom ? " " + nom : ""),
        Guide: GUIDE_NAME,
        Prénom: prenom,
        Nom: nom,
        email: email,
        Page: window.location.href
      })
    })
      .then(function (response) {
        return response.json().then(function (data) {
          console.log("Web3Forms — statut " + response.status + " :", data);
          if (!response.ok || !data || data.success !== true) {
            throw new Error("web3forms-failed");
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
