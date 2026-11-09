# Instructions permanentes — johansimonneau/portfolio

Ce fichier est lu automatiquement par Claude Code au début de chaque session sur ce repo, y compris les Routines automatisées planifiées (publication du blog, veille actu, sourcing Baromètre IA, etc.). Les instructions ci-dessous s'appliquent à toutes, en plus de ce que précise chaque Routine individuellement.

## Garde-fou QA transversal

L'élargissement des permissions (pas de prompt de confirmation pour Notion, les outils PR GitHub, le suivi de PR/Routines Claude Code Remote) sert uniquement à retirer la friction sur des actions déjà non destructrices et déjà couvertes par les contrôles qualité existants. Il ne change rien aux exigences suivantes, qui restent systématiques et ne doivent jamais être sautées pour aller plus vite :

- **Sweep de validation avant tout push de contenu** : CSP, JSON-LD valide, liens internes non cassés, images chargées. 0 problème avant de committer.
- **Vérification fast-forward avant tout push sur une branche partagée** (`git merge-base --is-ancestor`), jamais de `--force` sauf cas explicitement justifié et vérifié juste avant.
- **Jamais de chiffre, citation ou statistique inventés.** Sourcer à une source primaire nommée et datée, ou signaler explicitement dans le texte que la donnée n'est pas vérifiable plutôt que de l'omettre silencieusement ou de la présenter comme un fait.
- **Si quelque chose est cassé, incohérent, ou qu'une action potentiellement destructrice semble nécessaire** (lien mort, image corrompue, échec de sweep, conflit git non trivial, commande irréversible) : s'arrêter et alerter Johan clairement, plutôt que de forcer la publication, de contourner silencieusement le problème, ou de deviner. Ce signalement prime toujours sur la cadence ou la vitesse d'exécution — en cas de doute, le silence (ne rien publier ce cycle-ci) est toujours l'option sûre par défaut.
- **Ne jamais abaisser le niveau d'exigence qualité pour tenir un rythme ou une deadline.** Mieux vaut un cycle sans publication qu'un contenu faible, incohérent ou non vérifié mis en ligne.

En résumé : moins de friction sur les actions sûres, zéro relâchement sur la vérification et l'alerte en cas de problème réel.
