# Portfolio — Johan Simonneau

Site vitrine one-page, HTML/CSS/JS natif (aucune dépendance, aucun build).

## Arborescence

```
.
├── index.html
├── style.css
├── script.js
├── README.md
└── assets/
    ├── icons/
    │   ├── paid-media.svg
    │   ├── mobile-growth.svg
    │   └── analytics.svg
    └── img/
        ├── johan-portrait.svg      → à remplacer par une vraie photo
        ├── project-tiime.svg       → à remplacer par une capture du projet
        ├── project-swapn.svg
        ├── project-pentalog.svg
        ├── project-skillvalue.svg
        ├── avatar-vincent.svg      → à remplacer par une photo de profil
        ├── avatar-sebastien.svg
        └── avatar-alizee.svg
```

Les fichiers `.svg` dans `assets/img/` sont des placeholders flat design
respectant la charte (fond `#f6f4f0`, accent `#4ce6b9`, navy `#001b48`).
Pour les remplacer par de vraies photos : ajoutez vos fichiers `.jpg` ou
`.webp` dans le même dossier, avec le même nom (ex. `johan-portrait.jpg`),
puis mettez à jour l'attribut `src` correspondant dans `index.html`.

## Aucune installation nécessaire

Le site fonctionne en ouvrant simplement `index.html` dans un navigateur.
Aucun `npm install`, aucun serveur requis pour le développement local.

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
   "Output Directory" vides).
5. Cliquez sur **Deploy**.

Votre site est en ligne en moins d'une minute, à une adresse du type
`portfolio-johan-simonneau.vercel.app`.

### 3. Mises à jour futures

Chaque `git push` sur la branche `main` redéploie automatiquement le site
sur Vercel — aucune action manuelle supplémentaire.

### 4. Nom de domaine personnalisé (optionnel)

Dans le tableau de bord Vercel du projet : **Settings → Domains**, ajoutez
votre domaine (ex. `johansimonneau.com`) et suivez les instructions DNS
affichées (ajout d'un enregistrement chez votre registrar).
