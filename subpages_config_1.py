# -*- coding: utf-8 -*-
"""Configuration des sous-pages — batch 1/3"""

PAGES_BATCH_1 = [

# ============================================================
# 1. A/B Testing Faible Trafic
# ============================================================
{
    'slug': 'ab-testing-faible-trafic',
    'pillar_label': 'CRO',
    'pillar_slug': '/cro',
    'active_service_path': '/cro',
    'h1_short': 'A/B Testing à faible trafic',
    'h1': "A/B testing à faible trafic : la méthode change, pas l'ambition",
    'hook': "La plupart des guides d'A/B testing sont écrits pour des sites avec des dizaines de milliers de visiteurs par mois. Sur un trafic plus modeste, appliquer la même méthode mène souvent à de fausses conclusions — un test arrêté trop tôt peut désigner un « gagnant » qui n'en est pas un.",
    'title_seo': "A/B Testing à Faible Trafic | Méthode pour PME",
    'meta_description': "Comment faire de l'A/B testing fiable avec un trafic modéré ? Une méthode adaptée aux PME, sans faux positifs statistiques. Cas client SkillValue.",
    'canonical': 'https://johansimonneau.fr/ab-testing-faible-trafic',
    'service_name': 'A/B Testing à faible trafic',
    'schema_type': 'Service',
    'blocks': [
        {'type': 'case', 'label': 'Le cas SkillValue', 'paragraphs': [
            "SkillValue cherchait à accélérer sa croissance en scalant l'acquisition de leads qualifiés et en optimisant les performances du funnel de conversion. Le dispositif mis en place a intégré un A/B testing structuré et un pilotage data-driven, avec un écosystème de tracking connecté pour fiabiliser chaque décision.",
            "Résultat obtenu en priorisant les tests à plus fort impact plutôt qu'en multipliant les micro-optimisations peu concluantes sur un volume de trafic limité :",
        ], 'stats': [('x10', 'des conversions'), ('78%', 'transformation rate'), ('4,7', 'en ROI')]},
        {'type': 'h2', 'text': 'Ce qui change vraiment à faible trafic'},
        {'type': 'points', 'items': [
            ("Moins de tests simultanés, plus de profondeur par test.", " Diviser le trafic entre 4 variantes quand le volume est déjà limité rend chaque variante impossible à évaluer sérieusement."),
            ("Une durée de test plus longue.", " Un résultat qui semble significatif après 3 jours peut s'inverser après 3 semaines — la patience compte davantage que sur un gros compte."),
            ("Prioriser les changements à fort impact.", " Un test sur la couleur d'un bouton apporte rarement un signal exploitable à faible volume ; un test sur la proposition de valeur ou le formulaire a plus de chances de produire un effet mesurable."),
            ("Compléter par de l'analyse qualitative.", " Heatmaps, retours utilisateurs, enregistrements de session — des sources d'information qui ne dépendent pas du volume de trafic pour être exploitables."),
        ]},
        {'type': 'h2', 'text': 'Pour quels types d\'entreprises'},
        {'type': 'list', 'items': [
            "PME et startups avec un trafic mensuel modéré, mais qui veulent tout de même piloter leurs décisions par la donnée",
            "Sites B2B à cycle de vente long, où le volume de conversions reste naturellement limité",
            "Toute entreprise lassée des recommandations génériques pensées pour de gros volumes",
        ]},
        {'type': 'faq', 'items': [
            ("Combien de trafic faut-il vraiment pour faire de l'A/B testing ?", "Il n'y a pas de seuil universel — l'important est le nombre de conversions par variante, pas seulement le trafic brut. En dessous de quelques dizaines de conversions par variante, la significativité devient difficile à atteindre rapidement."),
            ("Comment éviter les faux positifs sur un petit volume ?", "En laissant tourner le test plus longtemps, et en évitant de l'arrêter dès qu'un résultat semble favorable dans les premiers jours."),
            ("Faut-il abandonner l'A/B testing si le trafic est trop faible ?", "Non, mais la méthode doit s'adapter — privilégier des changements à fort impact et compléter par de l'analyse qualitative."),
            ("Combien de temps dure un test à faible trafic ?", "Généralement plus long qu'à fort trafic — comptez plusieurs semaines plutôt que quelques jours pour un résultat fiable."),
        ]},
    ],
    'faq_items': [
        ("Combien de trafic faut-il vraiment pour faire de l'A/B testing ?", "Il n'y a pas de seuil universel — l'important est le nombre de conversions par variante, pas seulement le trafic brut."),
        ("Comment éviter les faux positifs sur un petit volume ?", "En laissant tourner le test plus longtemps, et en évitant de l'arrêter dès qu'un résultat semble favorable dans les premiers jours."),
        ("Faut-il abandonner l'A/B testing si le trafic est trop faible ?", "Non, mais la méthode doit s'adapter — privilégier des changements à fort impact et compléter par de l'analyse qualitative."),
        ("Combien de temps dure un test à faible trafic ?", "Généralement plus long qu'à fort trafic — comptez plusieurs semaines plutôt que quelques jours."),
    ],
    'cta_title': "Discutons d'une méthode de test adaptée à votre volume",
    'cta_primary_label': 'Réserver un audit gratuit',
    'cta_footer_html': 'Pour une vue complète de mon expertise CRO, voir la page <a href="/cro">CRO</a>.',
    'band_text': "Cette page fait partie de l'expertise CRO.",
    'related_links': [('/cro', 'CRO'), ('/analyse-comportementale', 'Analyse comportementale')],
},

# ============================================================
# 2. Amplitude & Mixpanel
# ============================================================
{
    'slug': 'amplitude-mixpanel',
    'pillar_label': 'Analytics',
    'pillar_slug': '/analytics',
    'active_service_path': '/analytics',
    'h1_short': 'Amplitude & Mixpanel',
    'h1': 'Quand GA4 ne suffit plus : comprendre le comportement produit',
    'hook': "GA4 répond bien aux questions marketing (d'où vient le trafic, quel canal convertit). Pour un produit SaaS ou une application avec des parcours utilisateurs complexes, des outils comme Amplitude ou Mixpanel apportent une granularité différente — centrée sur le comportement à l'intérieur du produit lui-même.",
    'title_seo': 'Consultant Amplitude & Mixpanel | Product Analytics',
    'meta_description': "Mise en place d'Amplitude ou Mixpanel pour analyser le comportement produit de votre application ou SaaS, au-delà du tracking marketing classique.",
    'canonical': 'https://johansimonneau.fr/amplitude-mixpanel',
    'service_name': 'Consultant Amplitude & Mixpanel',
    'schema_type': 'Article',
    'blocks': [
        {'type': 'h2', 'text': 'Pourquoi ces outils sont différents de GA4'},
        {'type': 'p', 'text': "GA4 reste orienté acquisition et conversion. Amplitude et Mixpanel sont pensés pour l'analyse de parcours produit : quelles fonctionnalités sont utilisées, où les utilisateurs décrochent dans un onboarding, quels comportements précèdent la rétention ou le churn. C'est une couche d'analyse complémentaire, pas un remplacement du tracking marketing."},
        {'type': 'h2', 'text': 'Ce que couvre la mise en place'},
        {'type': 'points', 'items': [
            ("Définition des événements produit clés.", " Ce qui compte réellement pour votre business (activation, usage récurrent d'une fonctionnalité), pas seulement les pages vues."),
            ("Construction de funnels d'onboarding.", " Identifier précisément où les utilisateurs abandonnent dans leur premier parcours."),
            ("Cohortes de rétention.", " Comprendre quels segments d'utilisateurs reviennent, et pourquoi."),
            ("Connexion avec les autres outils.", " CRM, outils de marketing automation, pour relier comportement produit et cycle commercial."),
        ]},
        {'type': 'h2', 'text': "Pour quels types d'entreprises"},
        {'type': 'list', 'items': [
            "SaaS avec un produit self-service et un parcours d'onboarding à optimiser",
            "Applications avec des fonctionnalités multiples dont l'usage réel reste mal connu",
            "Équipes produit qui veulent des données indépendantes de l'équipe marketing",
        ]},
        {'type': 'faq', 'items': [
            ("Amplitude ou Mixpanel, comment choisir ?", "Les deux se ressemblent fonctionnellement — le choix dépend souvent des intégrations déjà en place et des préférences d'interface de l'équipe produit."),
            ("Faut-il ces outils en plus de GA4, ou à la place ?", "En plus généralement — GA4 reste pertinent pour la mesure marketing globale, ces outils apportent une couche produit complémentaire."),
            ("Ces outils conviennent-ils à un site e-commerce classique ?", "Ils sont surtout pertinents pour des produits avec des parcours utilisateurs complexes (SaaS, applications) — moins déterminants pour un site e-commerce simple."),
            ("Combien de temps pour une mise en place complète ?", "Selon la complexité du produit, généralement 3 à 6 semaines pour un plan d'événements complet et exploitable."),
        ]},
    ],
    'faq_items': [
        ("Amplitude ou Mixpanel, comment choisir ?", "Les deux se ressemblent fonctionnellement — le choix dépend souvent des intégrations déjà en place."),
        ("Faut-il ces outils en plus de GA4, ou à la place ?", "En plus généralement — GA4 reste pertinent pour la mesure marketing globale."),
        ("Ces outils conviennent-ils à un site e-commerce classique ?", "Ils sont surtout pertinents pour des produits avec des parcours utilisateurs complexes."),
        ("Combien de temps pour une mise en place complète ?", "Généralement 3 à 6 semaines pour un plan d'événements complet et exploitable."),
    ],
    'cta_title': 'Envie de savoir si votre produit a besoin de ce niveau d\'analyse ?',
    'cta_primary_label': 'Échanger sur votre analytics produit',
    'cta_footer_html': 'Pour une vue complète de mon expertise Analytics, voir la page <a href="/analytics">Analytics</a>.',
    'band_text': "Cette page fait partie de l'expertise Analytics.",
    'related_links': [('/analytics', 'Analytics'), ('/consultant-ga4', 'Consultant GA4'), ('/tracking-mobile', 'Tracking mobile')],
},

# ============================================================
# 3. Analyse Comportementale
# ============================================================
{
    'slug': 'analyse-comportementale',
    'pillar_label': 'CRO',
    'pillar_slug': '/cro',
    'active_service_path': '/cro',
    'h1_short': 'Analyse comportementale',
    'h1': 'Voir ce que les chiffres ne racontent pas',
    'hook': "Un taux de conversion bas indique qu'un problème existe — pas où il se trouve. L'analyse comportementale (heatmaps, enregistrements de session) permet d'observer concrètement comment les visiteurs interagissent avec une page, et d'identifier ce qui bloque avant même de lancer un test A/B.",
    'title_seo': 'Analyse Comportementale & Heatmaps | Consultant CRO',
    'meta_description': "Heatmaps et enregistrements de session pour comprendre comment vos visiteurs interagissent réellement avec votre site, au-delà des chiffres bruts.",
    'canonical': 'https://johansimonneau.fr/analyse-comportementale',
    'service_name': 'Analyse comportementale & Heatmaps',
    'schema_type': 'Article',
    'blocks': [
        {'type': 'h2', 'text': "Où ça s'intègre dans une démarche CRO"},
        {'type': 'p', 'text': "L'analyse comportementale est un outil de diagnostic, généralement mobilisé avant de formuler des hypothèses de test — elle aide à prioriser les optimisations sur les points de friction réellement observés, plutôt que sur des suppositions."},
        {'type': 'h2', 'text': 'Ce que ça permet de voir'},
        {'type': 'points', 'items': [
            ("Heatmaps de clic.", " Où les visiteurs cliquent réellement — parfois sur des éléments qui ne sont pas cliquables, révélant une attente non satisfaite."),
            ("Heatmaps de scroll.", " Jusqu'où les visiteurs descendent réellement sur la page — utile pour savoir si le contenu en bas de page est même vu."),
            ("Enregistrements de session.", " Rejouer le parcours d'un visiteur pour observer les hésitations, les retours en arrière, les points d'abandon."),
            ("Analyse de formulaire.", " Identifier quels champs génèrent le plus d'abandons dans un formulaire multi-étapes."),
        ]},
        {'type': 'h2', 'text': 'Pour quels types de sites'},
        {'type': 'list', 'items': [
            "Sites avec un taux de conversion stagnant sans explication évidente dans les données classiques",
            "Pages complexes (formulaires longs, tunnels multi-étapes) où le point de friction n'est pas identifiable autrement",
            "Toute entreprise voulant prioriser ses hypothèses de test avant de se lancer dans l'A/B testing",
        ]},
        {'type': 'faq', 'items': [
            ("Les heatmaps remplacent-elles l'A/B testing ?", "Non, elles servent à formuler de meilleures hypothèses de test, pas à les valider statistiquement."),
            ("Est-ce compatible avec le RGPD ?", "Oui, à condition d'anonymiser les données sensibles et d'obtenir le consentement nécessaire, comme pour tout outil de tracking."),
            ("Faut-il beaucoup de trafic pour que ce soit utile ?", "Moins que pour l'A/B testing — quelques dizaines de sessions suffisent déjà à révéler des patterns de comportement exploitables."),
            ("Combien de temps pour obtenir des données exploitables ?", "Généralement 1 à 2 semaines de collecte, selon le volume de trafic de la page analysée."),
        ]},
    ],
    'faq_items': [
        ("Les heatmaps remplacent-elles l'A/B testing ?", "Non, elles servent à formuler de meilleures hypothèses de test, pas à les valider statistiquement."),
        ("Est-ce compatible avec le RGPD ?", "Oui, à condition d'anonymiser les données sensibles et d'obtenir le consentement nécessaire."),
        ("Faut-il beaucoup de trafic pour que ce soit utile ?", "Moins que pour l'A/B testing — quelques dizaines de sessions suffisent déjà."),
        ("Combien de temps pour obtenir des données exploitables ?", "Généralement 1 à 2 semaines de collecte."),
    ],
    'cta_title': 'Envie de voir concrètement comment vos visiteurs interagissent avec votre site ?',
    'cta_primary_label': 'Échanger sur votre analyse comportementale',
    'cta_footer_html': 'Pour une vue complète de mon expertise CRO, voir la page <a href="/cro">CRO</a>.',
    'band_text': "Cette page fait partie de l'expertise CRO.",
    'related_links': [('/cro', 'CRO'), ('/ab-testing-faible-trafic', 'A/B Testing faible trafic'), ('/optimisation-landing-page', 'Optimisation landing page')],
},

# ============================================================
# 4. Apple Search Ads
# ============================================================
{
    'slug': 'apple-search-ads',
    'pillar_label': 'Mobile Marketing',
    'pillar_slug': '/mobile-marketing',
    'active_service_path': '/mobile-marketing',
    'h1_short': 'Apple Search Ads',
    'h1': "Apple Search Ads : capter l'intention au moment exact de la recherche",
    'hook': "Contrairement à la plupart des formats publicitaires mobiles, Apple Search Ads cible des utilisateurs en train de chercher activement une application — l'intention est déjà là, ce qui en fait un levier à fort taux de conversion quand il est bien structuré.",
    'title_seo': 'Apple Search Ads Freelance | Publicité App Store',
    'meta_description': "Consultant Apple Search Ads freelance : campagnes ciblées sur les recherches App Store, en complément d'une stratégie ASO structurée.",
    'canonical': 'https://johansimonneau.fr/apple-search-ads',
    'service_name': 'Apple Search Ads',
    'schema_type': 'Service',
    'blocks': [
        {'type': 'h2', 'text': "Où ça s'intègre dans une stratégie mobile"},
        {'type': 'p', 'text': "Le déploiement d'Apple Search Ads accompagne généralement un travail ASO déjà engagé — les deux leviers se renforcent : un bon classement organique améliore la performance des campagnes payantes, et inversement, une présence payante bien ciblée peut accélérer la visibilité organique. C'est dans cette logique que s'inscrivait le travail mené chez Tiime, dont l'application a atteint le <strong>TOP 5 sur l'ASO</strong> avec plus de <strong>100 000 téléchargements</strong>."},
        {'type': 'h2', 'text': 'Ce qui fait la différence sur Apple Search Ads'},
        {'type': 'points', 'items': [
            ("Un ciblage par mots-clés de recherche réelle.", " Contrairement au Display, l'utilisateur exprime déjà une intention — la structuration des mots-clés est donc déterminante."),
            ("Deux niveaux de campagne.", " Basic (automatisé, simple à démarrer) et Advanced (contrôle fin des enchères et des mots-clés) — le choix dépend du niveau de maturité souhaité."),
            ("Un lien direct avec la fiche store.", " La qualité de la fiche (visuels, description) influence directement le taux de conversion du clic publicitaire."),
            ("Une consolidation avec le tracking d'attribution.", " Indispensable pour mesurer la performance au-delà de l'installation (rétention, valeur générée)."),
        ]},
        {'type': 'h2', 'text': "Pour quels types d'applications"},
        {'type': 'list', 'items': [
            "Applications avec une fiche store déjà optimisée, cherchant à accélérer l'acquisition",
            "Éditeurs en phase de lancement voulant capter la recherche de leur catégorie dès le départ",
            "Applications avec des concurrents directs bien positionnés sur les mots-clés génériques du secteur",
        ]},
        {'type': 'faq', 'items': [
            ("Quelle différence avec une campagne Search classique sur Google Ads ?", "Le principe (cibler une intention de recherche) est similaire, mais l'inventaire est propre à l'App Store, avec un format et des règles spécifiques à Apple."),
            ("Faut-il avoir déjà travaillé son ASO avant de lancer Apple Search Ads ?", "Ce n'est pas obligatoire, mais fortement recommandé — une fiche store optimisée améliore directement le rendement des campagnes."),
            ("Basic ou Advanced, comment choisir ?", "Basic convient pour démarrer simplement. Advanced devient pertinent dès que le volume justifie un pilotage plus fin des enchères et des mots-clés."),
            ("Combien de temps avant de voir des résultats ?", "Les premiers signaux sont visibles rapidement, la phase d'apprentissage des enchères prend généralement quelques semaines."),
        ]},
    ],
    'faq_items': [
        ("Quelle différence avec une campagne Search classique sur Google Ads ?", "Le principe est similaire, mais l'inventaire est propre à l'App Store, avec un format et des règles spécifiques à Apple."),
        ("Faut-il avoir déjà travaillé son ASO avant de lancer Apple Search Ads ?", "Ce n'est pas obligatoire, mais fortement recommandé."),
        ("Basic ou Advanced, comment choisir ?", "Basic convient pour démarrer simplement. Advanced devient pertinent dès que le volume le justifie."),
        ("Combien de temps avant de voir des résultats ?", "Les premiers signaux sont visibles rapidement, la phase d'apprentissage prend quelques semaines."),
    ],
    'cta_title': "Discutons de votre stratégie d'acquisition App Store",
    'cta_primary_label': 'Réserver un audit gratuit',
    'cta_footer_html': 'Pour une vue complète de mon expertise mobile, voir la page <a href="/mobile-marketing">Mobile Marketing</a>.',
    'band_text': "Cette page fait partie de l'expertise Mobile Marketing.",
    'related_links': [('/mobile-marketing', 'Mobile Marketing'), ('/tracking-mobile', 'Tracking mobile')],
},

# ============================================================
# 5. Audit Visibilité IA
# ============================================================
{
    'slug': 'audit-visibilite-ia',
    'pillar_label': 'GEO',
    'pillar_slug': '/geo',
    'active_service_path': '/geo',
    'h1_short': 'Audit de visibilité IA',
    'h1': "Où en êtes-vous déjà dans les réponses de l'IA générative ?",
    'hook': "Avant de parler stratégie, la première question est simple : votre marque apparaît-elle déjà quand un utilisateur pose une question liée à votre secteur sur ChatGPT, Claude ou Perplexity ? La réponse est souvent surprenante — parfois vous êtes déjà cité sans le savoir, parfois un concurrent occupe toute la place.",
    'title_seo': 'Audit de Visibilité IA Générative | ChatGPT & Claude',
    'meta_description': "Découvrez si votre marque apparaît déjà dans les réponses de ChatGPT, Claude et Perplexity. Un audit de visibilité pour anticiper le virage GEO.",
    'canonical': 'https://johansimonneau.fr/audit-visibilite-ia',
    'service_name': 'Audit de visibilité IA générative',
    'schema_type': 'Service',
    'blocks': [
        {'type': 'h2', 'text': 'En quoi consiste cet audit'},
        {'type': 'p', 'text': "Contrairement à un audit SEO classique, il n'existe pas encore d'outil de mesure automatisée fiable pour le GEO. L'audit repose donc sur une méthode manuelle et rigoureuse : une série de requêtes réelles, représentatives de ce que vos clients potentiels pourraient poser à une IA, testées sur plusieurs moteurs génératifs."},
        {'type': 'points', 'items': [
            ("Test de requêtes ciblées", " sur ChatGPT, Claude et Perplexity, construites à partir des intentions de recherche réelles de votre audience."),
            ("Analyse de la présence actuelle", " — êtes-vous cité, ignoré, ou est-ce un concurrent qui apparaît à votre place ?"),
            ("Évaluation de la cohérence des informations de marque", " sur le web (site, réseaux, annuaires) — un facteur clé de la confiance accordée par les modèles."),
            ("Identification des contenus à structurer en priorité", " pour améliorer les chances d'être cité."),
        ]},
        {'type': 'h2', 'text': 'Ce que vous recevez'},
        {'type': 'p', 'text': "Un rapport présentant les résultats des tests de requêtes, une évaluation de votre positionnement actuel face à vos concurrents directs sur ce nouveau terrain, et des recommandations concrètes pour structurer votre contenu en conséquence."},
        {'type': 'h2', 'text': "Pour quels types d'entreprises"},
        {'type': 'list', 'items': [
            "Entreprises B2B avec un contenu d'expertise déjà développé, qui veulent savoir s'il est exploité par les IA",
            "Marques qui commencent à recevoir des questions sur leur présence dans les réponses IA",
            "Toute entreprise qui veut prendre une longueur d'avance avant que ses concurrents s'y intéressent",
        ]},
        {'type': 'faq', 'items': [
            ("Cet audit est-il gratuit ?", "Oui, un premier diagnostic de visibilité est offert."),
            ("Combien de temps prend cet audit ?", "Généralement une semaine, le temps de construire et tester un panel de requêtes représentatif."),
            ("Que faire si je ne suis pas du tout cité aujourd'hui ?", "Ce n'est pas rare pour une discipline aussi jeune — l'audit sert justement à identifier par où commencer."),
            ("Cet audit remplace-t-il un audit SEO classique ?", "Non, les deux sont complémentaires. Le SEO reste la priorité pour la majorité du trafic aujourd'hui — le GEO anticipe un usage en croissance."),
        ]},
    ],
    'faq_items': [
        ("Cet audit est-il gratuit ?", "Oui, un premier diagnostic de visibilité est offert."),
        ("Combien de temps prend cet audit ?", "Généralement une semaine, le temps de construire et tester un panel de requêtes représentatif."),
        ("Que faire si je ne suis pas du tout cité aujourd'hui ?", "Ce n'est pas rare pour une discipline aussi jeune — l'audit sert justement à identifier par où commencer."),
        ("Cet audit remplace-t-il un audit SEO classique ?", "Non, les deux sont complémentaires."),
    ],
    'cta_title': 'Découvrez votre visibilité actuelle dans les réponses IA',
    'cta_primary_label': 'Réserver mon audit gratuit',
    'cta_footer_html': 'Pour comprendre la logique du GEO plus en détail, voir la page <a href="/geo">GEO</a>.',
    'band_text': "Cette page fait partie de l'expertise GEO.",
    'related_links': [('/geo', 'GEO'), ('/donnees-structurees', 'Données structurées')],
},

]
