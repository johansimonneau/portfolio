# Portfolio — Johan Simonneau

Site HTML/CSS/JS natif (aucune dépendance, aucun build) — une home page et
deux pages piliers SEO (SEA, SMA) partageant la même identité visuelle.

## Arborescence

```
.
├── index.html          → Home page
├── sea.html             → Page pilier "Consultant SEA"
├── sma.html              → Page pilier "Consultant SMA"
├── style.css             → Feuille de style principale (variables, composants)
├── pillar.css             → Composants additionnels pour les pages piliers
│                            (étapes de méthodologie, FAQ, grille définition…)
│                            Se charge après style.css et réutilise ses variables.
├── script.js              → Animations au scroll, menu mobile, compteurs
├── vercel.json             → Configuration des URLs propres (/sea, /sma)
├── favicon.ico, favicon-*.png, apple-touch-icon.png
└── assets/
    ├── icons/               → Icônes SVG des blocs de services
    ├── img/
    │   ├── logo-js.png        → Logo (fond clair, header)
    │   ├── logo-js-white.png   → Logo (fond sombre, footer)
    │   ├── johan-portrait-photo.jpg  → Photo utilisée dans "À propos"
    │   ├── johan-portrait.svg         → Ancienne illustration (non utilisée)
    │   ├── avatar-*.jpg        → Photos des témoignages
    │   ├── project-*.jpg        → Captures des études de cas
    │   └── clients/               → Logos clients (carrousel, niveaux de gris)
```

## Pages piliers (SEA / SMA)

`sea.html` et `sma.html` reprennent exactement les composants visuels de la
home (`.hero`, `.hero-pills`, `.card`, `.project-card`, header/footer) définis
dans `style.css`, complétés par `pillar.css` pour les blocs propres aux pages
piliers : grille de définition à 2 colonnes, étapes de méthodologie
numérotées, FAQ en accordéon. Toute modification de couleur, typo ou espacement
dans `style.css` (variables `:root`) se répercute donc automatiquement sur les
trois pages.

Chaque page pilier embarque un bloc JSON-LD (`schema.org/Service` +
`schema.org/FAQPage`) pour le référencement. Pensez à mettre à jour ce bloc
si le contenu de la page change.

Pour créer une nouvelle page pilier (SEO, GEO, Mobile, Analytics, CRO…) :
dupliquez `sea.html`, adaptez le contenu et le JSON-LD, ajoutez le lien dans
la nav de toutes les pages et dans le bloc `.card-links` de la home si
pertinent.

## Blog

`blog.html` (page d'index, `/blog`) liste les articles ; chaque article est un
fichier à la racine (ex. `seo-geo-ce-qui-change-vraiment.html`), au même
niveau que les autres pages — pas de sous-dossier, pour rester cohérent avec
le reste du site et éviter de casser les chemins relatifs vers `style.css`,
`assets/`, etc.

Template d'article (à dupliquer depuis `seo-geo-ce-qui-change-vraiment.html`) :
- `<head>` : identique aux sous-pages (`subpage.css`), JSON-LD `BlogPosting`
  (+ `FAQPage` si pertinent) au lieu de `Service`.
- Fil d'Ariane `.sub-breadcrumb` : Accueil / Blog / [Titre].
- En-tête `.sub-header` avec tag `Blog` (`.sub-pillar-tag`), `<h1>`, accroche
  (`.sub-hook`), puis `.sub-byline` (auteur · date · temps de lecture) et le
  module `.sub-audio` ("Écouter cet article", synthèse vocale du navigateur,
  gratuite — voir plus bas).
- Corps en `.sub-article` : le contenu à lire à voix haute doit être dans un
  conteneur avec un `id` (ex. `<div id="articleBody">`), qui doit englober
  `<h2>`, `.sub-points`, `.sub-faq` mais **pas** `.sub-cta` (pour ne pas lire
  l'appel à l'action). Le `data-audio-target` du bouton doit référencer cet
  `id`.
- CTA de fin (`.sub-cta`) + bandeau de liens connexes (`.sub-pillar-band`).

### Module audio ("Écouter cet article")

Utilise l'API native `speechSynthesis` du navigateur (gratuite, aucune clé
API, aucun compte) — voix moins naturelle qu'un service payant type
ElevenLabs, mais suffisante et sans coût récurrent. Logique dans `script.js`
(section "Lecture audio de l'article"), activée automatiquement si un
`[data-audio-btn]` est présent sur la page ; masquée automatiquement si le
navigateur ne supporte pas `speechSynthesis` ou si la cible `data-audio-target`
est introuvable. Attention : les icônes play/pause sont basculées via
`element.style.display` en JS plutôt que l'attribut HTML `hidden`, qui ne se
masque pas de façon fiable sur les éléments `<svg>` dans tous les moteurs.

Pour publier un nouvel article : dupliquez le fichier, changez le contenu et
le JSON-LD, ajoutez une entrée dans `.blog-list` sur `blog.html`, ajoutez le
lien `/blog` dans le footer si absent (déjà fait sur toutes les pages
existantes), et ajoutez l'URL dans `sitemap.xml`.

## URLs propres (`/sea`, `/sma`)

Le fichier `vercel.json` active `cleanUrls`, qui fait correspondre
automatiquement `sea.html` → `/sea` et `sma.html` → `/sma` une fois déployé
sur Vercel (redirection 308 si quelqu'un visite l'URL avec `.html`). Tous les
liens internes du site utilisent déjà ces chemins propres (`/sea`, `/sma`,
`/`, `/#contact`…) — pas de configuration supplémentaire nécessaire.

**Important : ce comportement ne fonctionne qu'une fois déployé sur Vercel.**
En ouvrant les fichiers directement dans un navigateur (`file://...`) ou avec
un simple serveur local, les liens `/sea` et `/sma` ne résoudront pas — utilisez
`sea.html` / `sma.html` pour un test en local, ou `vercel dev` si la CLI
Vercel est installée.

## Aucune installation nécessaire

Pour prévisualiser en local, ouvrez `index.html` dans un navigateur.
Aucun `npm install`, aucun serveur requis.

---

## Déployer sur GitHub + Vercel

### 1. Créer le dépôt GitHub

1. Allez sur [github.com/new](https://github.com/new).
2. Nom du dépôt : `portfolio-johan-simonneau` (ou autre).
3. Laissez-le public ou privé, sans README (vous en avez déjà un).
4. Cliquez sur **Create repository**.

Dans un terminal, à la racine de ce dossier :

```bash
git init
git add .
git commit -m "Initial commit — portfolio Johan Simonneau"
git branch -M main
git remote add origin https://github.com/VOTRE-USER/portfolio-johan-simonneau.git
git push -u origin main
```

### 2. Déployer sur Vercel

1. Allez sur [vercel.com/new](https://vercel.com/new).
2. Connectez votre compte GitHub si ce n'est pas déjà fait.
3. Sélectionnez le dépôt `portfolio-johan-simonneau`.
4. Vercel détecte un site statique : aucune configuration n'est nécessaire
   (laissez "Framework Preset" sur **Other**, "Build Command" et
   "Output Directory" vides). Le fichier `vercel.json` est pris en compte
   automatiquement.
5. Cliquez sur **Deploy**.

Votre site est en ligne en moins d'une minute, avec `/sea` et `/sma`
fonctionnels dès le premier déploiement.

### 3. Mises à jour futures

Chaque `git push` sur la branche `main` redéploie automatiquement le site
sur Vercel — aucune action manuelle supplémentaire.

### 4. Nom de domaine personnalisé

Dans le tableau de bord Vercel du projet : **Settings → Domains**, ajoutez
votre domaine (ex. `johansimonneau.fr`) et suivez les instructions DNS
affichées (ajout d'un enregistrement chez votre registrar). Une fois
configuré, `johansimonneau.fr/sea` et `johansimonneau.fr/sma` fonctionneront
directement.
