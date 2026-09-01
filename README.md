# Portfolio — Johan Simonneau

Site HTML/CSS/JS natif (aucune dépendance, aucun build, aucun backend) —
31 pages statiques déployées sur Vercel, partageant la même identité
visuelle et les mêmes composants CSS.

## Arborescence

```
.
├── index.html                    → Home page
├── 404.html                      → Page d'erreur personnalisée
├── comment-je-travaille.html     → Méthode de travail (sans tarifs)
├── diagnostic.html               → Quiz interactif "Score de maturité Growth Marketing"
├── blog.html                     → Index du blog (/blog)
├── seo-geo-ce-qui-change-vraiment.html  → 1er article de blog
│
├── sea.html, sma.html, seo.html, geo.html,
│   mobile-marketing.html, analytics.html, cro.html
│                                  → 7 pages piliers (une par service)
│
├── ab-testing-faible-trafic.html, amplitude-mixpanel.html,
│   analyse-comportementale.html, apple-search-ads.html,
│   audit-visibilite-ia.html, bing-ads-freelance.html,
│   consultant-ga4.html, conversion-api-tracking-server-side.html,
│   donnees-structurees.html, google-ads-petit-budget.html,
│   google-shopping.html, optimisation-landing-page.html,
│   tiktok-ads.html, tracking-mobile.html, youtube-ads.html
│                                  → 15 sous-pages (niveau 2 du maillage interne)
│
├── mentions-legales.html, politique-de-confidentialite.html, cgp.html
│                                  → Pages légales (noindex)
│
├── style.css        → Feuille de style principale (variables, composants
│                       partagés : header, footer, boutons, hero, cartes…)
├── pillar.css        → Composants des pages piliers (méthodologie, FAQ,
│                       grille de définition). Charge après style.css.
├── subpage.css        → Composants des sous-pages/articles de blog (fil
│                        d'Ariane, en-tête d'article, byline, FAQ). Charge
│                        après style.css.
├── legal.css           → Composants des pages légales et de la 404.
├── blog.css              → Grille de cartes de l'index du blog.
├── diagnostic.css         → Composants du quiz interactif.
├── cookie-consent.css      → Bandeau de consentement cookies.
│
├── script.js          → Animations au scroll, menu mobile, mega-menu,
│                        lien actif dans la nav.
├── cookie-consent.js   → Bandeau de consentement + Consent Mode Google.
├── diagnostic.js        → Logique du quiz (calcul du score, résultats,
│                          lien mailto pré-rempli — 100% côté client).
│
├── vercel.json         → URLs propres, en-têtes de sécurité (dont la CSP)
├── robots.txt / sitemap.xml
├── .well-known/security.txt   → Contact pour signalement de faille (RFC 9116)
├── favicon.ico, favicon-*.png, apple-touch-icon.png
└── assets/
    ├── fonts/            → Poppins + Inter auto-hébergées (sous-ensemble latin)
    ├── icons/            → Icônes SVG des blocs de services
    └── img/
        ├── logo-js.png / logo-js-white.png   → Logo (header / footer)
        ├── og-default.png                     → Image de partage par défaut (og:image /
        │                                         twitter:image sitewide), générée à partir
        │                                         du logo — voir section Blog
        ├── johan-portrait-photo.jpg           → Photo "À propos"
        ├── avatar-*.jpg                       → Photos des témoignages
        ├── project-*.jpg                      → Captures des études de cas
        ├── blog-*.png                         → Illustrations des articles de blog
        └── clients/                            → Logos clients (carrousel)
```

## Structure des pages

Toutes les pages partagent le même header (logo, mega-menu Services,
CTA Contact), le même footer, et le même bloc de scripts Consent Mode/GTM en
tête de `<head>`. Trois gabarits couvrent l'ensemble du site :

**Pages piliers** (`pillar.css`) — une par service (SEA, SMA, SEO, GEO,
Mobile Marketing, Analytics, CRO). Structure "landing page" : hero, grille de
définition, étapes de méthodologie numérotées, FAQ en accordéon. JSON-LD
`Service` + `FAQPage`.

**Sous-pages et articles de blog** (`subpage.css`) — format "article dense"
volontairement distinct des pages piliers pour éviter la cannibalisation SEO :
fil d'Ariane, pas de hero plein écran, corps en `<h2>`/listes/FAQ. JSON-LD
`Article` (sous-pages) ou `BlogPosting` (articles de blog).

**Pages légales** (`legal.css`) — mentions légales, politique de
confidentialité, CGP, 404. Pas de JSON-LD (sauf 404, en `noindex`).

Pour créer une nouvelle page pilier ou sous-page : dupliquez la page
existante la plus proche, adaptez le contenu et le JSON-LD, ajoutez le lien
dans la nav/mega-menu et le footer des autres pages si pertinent, et
ajoutez l'URL dans `sitemap.xml`.

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
  (`.sub-hook`), puis `.sub-byline` (auteur · date · temps de lecture).
- Image de couverture `.sub-cover` juste après l'en-tête (voir "Images des
  articles de blog" ci-dessous).
- Corps en `.sub-article` : `<h2>`, `.sub-points` pour les listes à puces
  avec amorce en gras, `.sub-faq` pour les questions/réponses.
- CTA de fin (`.sub-cta`) + bandeau de liens connexes (`.sub-pillar-band`).

Pour publier un nouvel article : dupliquez le fichier, changez le contenu et
le JSON-LD, ajoutez une entrée dans `.blog-list` sur `blog.html`, ajoutez le
lien `/blog` dans le footer si absent (déjà fait sur toutes les pages
existantes), et ajoutez l'URL dans `sitemap.xml`.

### Images des articles de blog

Chaque article a une image de couverture (`.sub-cover`, 1200×630, juste après
l'en-tête) en lien avec son sujet, et peut inclure une ou deux images
ressource dans le corps du texte (`.sub-figure`, avec `<figcaption>`) —
typiquement un schéma qui illustre un point de l'article. L'image de
couverture sert aussi d'`og:image`/`twitter:image` propre à l'article (au
lieu de `og-default.png`), pour un partage plus parlant sur les réseaux.

Le site n'utilise aucune photo ou image tierce pour ces illustrations : la
CSP (`img-src 'self'`) n'autorise que des images auto-hébergées, donc tout
visuel est une composition HTML/CSS maison (mêmes variables de style que le
reste du site : couleurs `--color-navy`/`--color-mint`, polices Poppins/
Inter, motif "blob + carré arrondi" du hero) exportée en PNG. Pour en
générer une : construisez la page dans un fichier HTML autonome, servez-la
avec un petit serveur local (les polices `@font-face` ne se chargent pas en
`file://`), puis capturez-la avec Playwright à la taille cible
(`page.screenshot()`). Voir `blog-seo-geo-hero.png` et
`blog-seo-geo-flow.png` comme référence.

**Piège CSP à connaître** (utile pour tout élément affiché/masqué
dynamiquement en JS sur ce site) : basculez toujours la visibilité via
l'assignation directe `element.style.xxx = ...`, jamais via un `style=""`
écrit dans du HTML généré (violerait la CSP `style-src`), ni via l'attribut
HTML `hidden` sur un `<svg>` (ne se masque pas de façon fiable dans
Chromium).

## Diagnostic interactif (`/diagnostic`)

Quiz en 6 questions (tracking, acquisition payante, SEO, GEO, CRO, pilotage)
qui calcule un score et une recommandation personnalisée **entièrement côté
client** (`diagnostic.js`) — aucun backend, conformément au choix
architectural du site. La transmission du résultat passe par un lien
`mailto:` pré-rempli avec les réponses (même mécanisme que le formulaire de
contact), jamais par un service tiers.

Point d'attention si vous modifiez `diagnostic.js` : tout texte inséré dans
le corps de l'email doit passer par `encodeURIComponent()` sur l'ensemble du
message (pas de concaténation manuelle de `%0D%0A`) pour éviter qu'un
caractère comme `&` ne casse le lien `mailto:`.

## Sécurité

`vercel.json` définit une **Content-Security-Policy stricte** sans
`'unsafe-inline'` : `script-src` n'autorise que `'self'`, les hashes SHA-256
des deux scripts inline (Consent Mode + boucle de chargement GTM, identiques
sur les 31 pages) et les domaines Google Tag Manager/Analytics ;
`style-src`/`img-src`/`font-src` sont limités à `'self'` ; `object-src` et
`form-action` sont interdits.

**Si vous ajoutez un script inline** (rare — préférez toujours un fichier
`.js` externe) : son hash SHA-256 doit être ajouté à `script-src` dans
`vercel.json`, sinon il sera bloqué silencieusement par la CSP. Pour
calculer un hash : `openssl dgst -sha256 -binary fichier.js | openssl base64`.

Autres en-têtes actifs : `X-Content-Type-Options`, `X-Frame-Options`,
`Referrer-Policy`, `Permissions-Policy`, `Strict-Transport-Security`.
`.well-known/security.txt` (RFC 9116) donne un contact pour le signalement
responsable de failles.

**Pour valider une modification de la CSP avant de pousser** : servez le
site en local avec un petit serveur qui rejoue les en-têtes de `vercel.json`,
et vérifiez l'absence d'événements `securitypolicyviolation` (Chromium via
Playwright, par exemple) sur toutes les pages plutôt que sur un échantillon —
un hash qui ne correspond plus après une modification de script casse la
page silencieusement, sans erreur visible à l'œil nu.

## RGPD & cookies

Consentement recueilli via `cookie-consent.js` + Google Consent Mode (refus
par défaut tant que l'utilisateur n'a pas choisi — voir le script inline en
tête de `<head>` sur chaque page). Polices auto-hébergées (`assets/fonts/`)
pour éviter toute transmission de l'IP du visiteur à Google avant
consentement. Détails complets dans `politique-de-confidentialite.html`.

## URLs propres (`/sea`, `/diagnostic`, etc.)

Le fichier `vercel.json` active `cleanUrls`, qui fait correspondre
automatiquement `sea.html` → `/sea` (et ainsi pour toutes les pages) une fois
déployé sur Vercel (redirection 308 si quelqu'un visite l'URL avec `.html`).
Tous les liens internes du site utilisent déjà ces chemins propres — pas de
configuration supplémentaire nécessaire.

**Important : ce comportement ne fonctionne qu'une fois déployé sur Vercel.**
En ouvrant les fichiers directement dans un navigateur (`file://...`) ou avec
un simple serveur local, les liens propres ne résoudront pas — utilisez les
noms de fichiers `.html` pour un test en local, ou `vercel dev` si la CLI
Vercel est installée.

## Aucune installation nécessaire

Pour prévisualiser en local, ouvrez `index.html` dans un navigateur, ou
servez le dossier avec `python3 -m http.server`. Aucun `npm install`, aucun
serveur applicatif requis.

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
   automatiquement (URLs propres + en-têtes de sécurité).
5. Cliquez sur **Deploy**.

Votre site est en ligne en moins d'une minute, avec toutes les URLs propres
fonctionnelles dès le premier déploiement.

### 3. Mises à jour futures

Chaque `git push` sur la branche `main` redéploie automatiquement le site
sur Vercel — aucune action manuelle supplémentaire.

### 4. Nom de domaine personnalisé

Dans le tableau de bord Vercel du projet : **Settings → Domains**, ajoutez
votre domaine (ex. `johansimonneau.fr`) et suivez les instructions DNS
affichées (ajout d'un enregistrement chez votre registrar).
