# -*- coding: utf-8 -*-
"""Configuration des sous-pages — batch 2/3"""

PAGES_BATCH_2 = [

# ============================================================
# 6. Bing Ads
# ============================================================
{
    'slug': 'bing-ads-freelance',
    'pillar_label': 'SEA',
    'pillar_slug': '/sea',
    'active_service_path': '/sea',
    'h1_short': 'Bing Ads',
    'h1': "Bing Ads freelance : le canal que la plupart des agences n'activent pas",
    'hook': "Microsoft Ads (Bing, Yahoo, DuckDuckGo, Edge) capte une audience B2B et senior souvent sous-représentée sur Google — avec un coût par clic généralement plus bas. Peu d'agences le proposent par défaut, ce qui en fait un levier sous-exploité sur beaucoup de comptes.",
    'title_seo': 'Bing Ads Freelance | Consultant Microsoft Advertising',
    'meta_description': "Consultant Microsoft (Bing) Ads freelance, en complément de Google Ads. Cas client Pentalog : +62% de conversions, -55% de CPA sur une stratégie multicanale.",
    'canonical': 'https://johansimonneau.fr/bing-ads-freelance',
    'service_name': 'Microsoft (Bing) Ads',
    'schema_type': 'Service',
    'blocks': [
        {'type': 'case', 'label': 'Le cas Pentalog', 'paragraphs': [
            "Pentalog souhaitait accélérer sa croissance B2B à l'international via une refonte complète de sa stratégie d'acquisition digitale. La stratégie déployée combinait Google Ads, LinkedIn Ads, Meta Ads <strong>et Bing Ads</strong>, avec une infrastructure de tracking et d'attribution unifiée sur l'ensemble des canaux.",
            "Bing Ads a contribué à élargir la couverture de la demande active sans cannibaliser le budget Google Ads — une audience B2B complémentaire, avec un coût d'entrée plus faible. Résultat global de cette stratégie multicanale :",
        ], 'stats': [('+62%', 'de conversions'), ('-55%', 'de CPA'), ('5,9', 'en ROAS')]},
        {'type': 'h2', 'text': 'Ce qui fait la différence sur Bing Ads'},
        {'type': 'points', 'items': [
            ("Une audience B2B et senior différente de Google.", " Les utilisateurs de Bing (souvent via Windows/Edge par défaut) ont un profil démographique distinct — pertinent pour certaines offres B2B."),
            ("Un coût par clic généralement plus bas.", " Moins de concurrence sur la plateforme, donc des enchères souvent plus accessibles pour un budget équivalent."),
            ("Import direct depuis Google Ads.", " La structure de campagne peut être largement réutilisée, ce qui limite le travail de duplication."),
            ("Un complément, pas un remplacement.", " Bing Ads fonctionne rarement seul — il s'active en parallèle de Google Ads pour élargir la couverture."),
        ]},
        {'type': 'h2', 'text': "Pour quels types d'entreprises"},
        {'type': 'list', 'items': [
            "Entreprises B2B ciblant des profils seniors ou professionnels",
            "Comptes Google Ads déjà matures cherchant un canal d'expansion à moindre coût",
            "Entreprises voulant diversifier leur dépendance à une seule régie publicitaire",
        ]},
        {'type': 'faq', 'items': [
            ("Bing Ads, ça vaut vraiment le coup en France ?", "La part de marché est plus faible qu'aux États-Unis, mais reste pertinente en B2B où l'audience professionnelle utilise davantage Edge/Windows par défaut."),
            ("Faut-il dupliquer toute sa structure Google Ads ?", "Non, un import ciblé des campagnes les plus performantes suffit généralement pour démarrer, avec des ajustements spécifiques à l'audience Bing."),
            ("Quel budget prévoir pour tester ?", "Un budget de test peut rester modeste (quelques centaines d'euros par mois) pour évaluer le potentiel avant de scaler."),
            ("Le tracking fonctionne-t-il de la même façon que sur Google Ads ?", "Les principes sont proches, mais nécessitent une configuration dédiée (UET tag de Microsoft) en plus du tracking Google existant."),
        ]},
    ],
    'faq_items': [
        ("Bing Ads, ça vaut vraiment le coup en France ?", "La part de marché est plus faible qu'aux États-Unis, mais reste pertinente en B2B."),
        ("Faut-il dupliquer toute sa structure Google Ads ?", "Non, un import ciblé des campagnes les plus performantes suffit généralement pour démarrer."),
        ("Quel budget prévoir pour tester ?", "Un budget de test peut rester modeste (quelques centaines d'euros par mois)."),
        ("Le tracking fonctionne-t-il de la même façon que sur Google Ads ?", "Les principes sont proches, mais nécessitent une configuration dédiée (UET tag de Microsoft)."),
    ],
    'cta_title': "Discutons d'élargir votre couverture au-delà de Google",
    'cta_primary_label': 'Réserver un audit gratuit',
    'cta_footer_html': 'Pour une vue complète de mon expertise SEA, voir la page <a href="/sea">SEA</a>.',
    'band_text': "Cette page fait partie de l'expertise SEA.",
    'related_links': [('/sea', 'SEA'), ('/google-ads-petit-budget', 'Google Ads petit budget'), ('/google-shopping', 'Google Shopping')],
},

# ============================================================
# 7. Consultant GA4
# ============================================================
{
    'slug': 'consultant-ga4',
    'pillar_label': 'Analytics',
    'pillar_slug': '/analytics',
    'active_service_path': '/analytics',
    'h1_short': 'Consultant GA4',
    'h1': "GA4 : la fondation d'une mesure fiable, encore mal exploitée par beaucoup d'entreprises",
    'hook': "Beaucoup d'entreprises ont migré vers GA4 par obligation, sans repenser leur plan de mesure. Résultat : un outil sous-exploité, avec des événements de conversion mal définis ou incomplets — ce qui fausse toutes les décisions prises à partir de ces données.",
    'title_seo': 'Consultant GA4 Freelance | Migration & Implémentation',
    'meta_description': "Consultant GA4 freelance : migration, plan de taggage, événements de conversion. Fondation du tracking ayant contribué à x10 conversions chez SkillValue.",
    'canonical': 'https://johansimonneau.fr/consultant-ga4',
    'service_name': 'Consultant GA4',
    'schema_type': 'Service',
    'blocks': [
        {'type': 'case', 'label': 'Le cas SkillValue & Pentalog', 'paragraphs': [
            "SkillValue cherchait à accélérer sa croissance B2B et B2C avec une forte montée en puissance des investissements marketing. Une partie du dispositif mis en place a consisté en une refonte du tracking et une amélioration de l'attribution, avec un écosystème connecté à Google Analytics, Google Tag Manager, le CRM et les outils de marketing automation.",
            "Cette fondation de mesure fiable a contribué aux résultats obtenus. Un exemple similaire chez Pentalog — infrastructure data et tracking renforcée via GTM et GA — a contribué à +62% de conversions et -55% de coût par acquisition.",
        ], 'stats': [('x10', 'des conversions (SkillValue)'), ('78%', 'transformation rate'), ('4,7', 'en ROI')]},
        {'type': 'h2', 'text': "Ce qui fait la différence dans une implémentation GA4"},
        {'type': 'points', 'items': [
            ("Un plan de taggage pensé pour le business, pas pour la technique seule.", " Les événements suivis doivent répondre à de vraies questions business, pas juste cocher une liste de fonctionnalités."),
            ("Une distinction claire entre conversions primaires et secondaires.", " Toutes les actions ne se valent pas — les confondre dilue la lecture de la performance réelle."),
            ("Une fiabilité renforcée par le Consent Mode et le server-side.", " Pour limiter la perte de données liée aux bloqueurs de cookies et aux restrictions de confidentialité."),
            ("Une intégration avec Google Tag Manager.", " Pour centraliser la gestion des tags sans dépendre d'interventions techniques répétées sur le site."),
        ]},
        {'type': 'h2', 'text': "Pour quels types d'entreprises"},
        {'type': 'list', 'items': [
            "Entreprises ayant migré vers GA4 sans refonte de leur plan de mesure",
            "Sites avec des données de conversion incomplètes ou incohérentes entre les plateformes",
            "Équipes marketing voulant reprendre la main sur leurs propres tableaux de bord",
        ]},
        {'type': 'faq', 'items': [
            ("J'ai déjà GA4 installé, pourquoi refaire une implémentation ?", "Avoir GA4 installé ne signifie pas que le plan de taggage est pertinent — beaucoup d'installations se limitent à une configuration par défaut, insuffisante pour piloter de vraies décisions."),
            ("Combien de temps prend une implémentation GA4 complète ?", "Généralement 2 à 4 semaines selon la complexité du site et le nombre d'événements de conversion à définir."),
            ("GA4 remplace-t-il un outil comme Amplitude ou Mixpanel ?", "Pas nécessairement — GA4 couvre bien la mesure marketing globale, tandis qu'Amplitude et Mixpanel sont plus adaptés à l'analyse fine du comportement produit."),
            ("Formez-vous les équipes à l'utilisation de GA4 après la mise en place ?", "Oui, la formation fait partie de la mission pour garantir l'autonomie des équipes sur la lecture des données."),
        ]},
    ],
    'faq_items': [
        ("J'ai déjà GA4 installé, pourquoi refaire une implémentation ?", "Avoir GA4 installé ne signifie pas que le plan de taggage est pertinent."),
        ("Combien de temps prend une implémentation GA4 complète ?", "Généralement 2 à 4 semaines selon la complexité du site."),
        ("GA4 remplace-t-il un outil comme Amplitude ou Mixpanel ?", "Pas nécessairement — GA4 couvre la mesure marketing globale, ces outils apportent l'analyse produit."),
        ("Formez-vous les équipes à l'utilisation de GA4 après la mise en place ?", "Oui, la formation fait partie de la mission."),
    ],
    'cta_title': 'Discutons de votre implémentation GA4',
    'cta_primary_label': 'Réserver un audit gratuit',
    'cta_footer_html': 'Pour une vue complète de mon expertise Analytics, voir la page <a href="/analytics">Analytics</a>.',
    'band_text': "Cette page fait partie de l'expertise Analytics.",
    'related_links': [('/analytics', 'Analytics'), ('/conversion-api-tracking-server-side', 'Conversion API'), ('/amplitude-mixpanel', 'Amplitude & Mixpanel')],
},

# ============================================================
# 8. Conversion API
# ============================================================
{
    'slug': 'conversion-api-tracking-server-side',
    'pillar_label': 'Analytics',
    'pillar_slug': '/analytics',
    'active_service_path': '/analytics',
    'h1_short': 'Conversion API',
    'h1': 'Conversion API : récupérer les données que le navigateur ne transmet plus',
    'hook': "Les bloqueurs de publicité, les restrictions de cookies tiers et les navigateurs de plus en plus stricts (Safari, Firefox) font perdre une part croissante des données de conversion mesurées côté navigateur. Le tracking server-side permet de compenser une partie de cette perte.",
    'title_seo': 'Conversion API & Tracking Server-Side | Freelance',
    'meta_description': "Mise en place de la Conversion API (Meta CAPI) et du tracking server-side pour fiabiliser vos données de conversion malgré les bloqueurs de cookies.",
    'canonical': 'https://johansimonneau.fr/conversion-api-tracking-server-side',
    'service_name': 'Conversion API & tracking server-side',
    'schema_type': 'Service',
    'blocks': [
        {'type': 'h2', 'text': 'Pourquoi c\'est devenu nécessaire'},
        {'type': 'p', 'text': "Historiquement, le tracking publicitaire reposait presque entièrement sur des pixels côté navigateur (Meta Pixel, Google Tag). Ces pixels sont de plus en plus souvent bloqués ou limités, ce qui fausse la mesure de performance des campagnes — un problème d'autant plus critique que les plateformes publicitaires utilisent ces données pour optimiser leurs enchères automatiquement."},
        {'type': 'case', 'label': 'Contexte — Pentalog', 'paragraphs': [
            "C'est un enjeu qui a fait partie du travail d'infrastructure data et tracking mené chez Pentalog, dans le cadre d'une stratégie multicanale ayant contribué à :",
        ], 'stats': [('+62%', 'de conversions'), ('-55%', 'de coût par acquisition')]},
        {'type': 'h2', 'text': 'Ce que couvre la mise en place'},
        {'type': 'points', 'items': [
            ("Conversion API Meta (CAPI).", " Transmission des événements de conversion directement depuis votre serveur vers Meta, en complément (pas en remplacement) du Pixel classique."),
            ("Google Enhanced Conversions.", " L'équivalent côté Google Ads, pour fiabiliser les conversions mesurées."),
            ("Déduplication des événements.", " Éviter de compter deux fois une même conversion entre le tracking navigateur et le tracking serveur."),
            ("Respect du consentement utilisateur.", " Le tracking server-side ne dispense pas de la gestion du consentement — il doit rester conforme aux mêmes règles que le tracking classique."),
        ]},
        {'type': 'h2', 'text': "Pour quels types d'entreprises"},
        {'type': 'list', 'items': [
            "Entreprises qui investissent significativement en Meta Ads ou Google Ads et constatent un écart entre les conversions mesurées et les conversions réelles (CRM, ventes)",
            "Sites avec un fort trafic Safari/iOS, particulièrement impactés par les restrictions de tracking",
            "Comptes publicitaires dont la phase d'apprentissage semble anormalement instable",
        ]},
        {'type': 'faq', 'items': [
            ("La Conversion API remplace-t-elle le Pixel Meta classique ?", "Non, les deux fonctionnent ensemble — la CAPI vient compléter les données que le Pixel ne parvient plus à capter seul."),
            ("Faut-il des compétences en développement pour la mettre en place ?", "Une intervention technique est nécessaire (accès au serveur ou au CMS), mais elle peut être menée en configuration standard sans développement sur-mesure dans la plupart des cas."),
            ("Est-ce compatible avec le RGPD ?", "Oui, à condition de respecter les mêmes règles de consentement que pour le tracking classique — la CAPI ne contourne pas ces obligations."),
            ("Comment savoir si mon tracking actuel a besoin de cette mise à niveau ?", "Un écart significatif entre les conversions rapportées par les plateformes publicitaires et vos données réelles (CRM, ventes) est généralement un bon indicateur."),
        ]},
    ],
    'faq_items': [
        ("La Conversion API remplace-t-elle le Pixel Meta classique ?", "Non, les deux fonctionnent ensemble."),
        ("Faut-il des compétences en développement pour la mettre en place ?", "Une intervention technique est nécessaire mais généralement en configuration standard."),
        ("Est-ce compatible avec le RGPD ?", "Oui, à condition de respecter les mêmes règles de consentement que pour le tracking classique."),
        ("Comment savoir si mon tracking actuel a besoin de cette mise à niveau ?", "Un écart entre conversions plateformes et données réelles est un bon indicateur."),
    ],
    'cta_title': 'Discutons de la fiabilité de votre tracking publicitaire',
    'cta_primary_label': 'Réserver un audit gratuit',
    'cta_footer_html': 'Pour une vue complète de mon expertise Analytics, voir la page <a href="/analytics">Analytics</a>.',
    'band_text': "Cette page centralise un sujet mentionné à la fois sur les pages SEA et SMA.",
    'related_links': [('/analytics', 'Analytics'), ('/consultant-ga4', 'Consultant GA4'), ('/sea', 'SEA'), ('/sma', 'SMA')],
},

# ============================================================
# 9. Données Structurées
# ============================================================
{
    'slug': 'donnees-structurees',
    'pillar_label': 'SEO',
    'pillar_slug': '/seo',
    'active_service_path': '/seo',
    'h1_short': 'Données structurées',
    'h1': 'Données structurées : le langage commun entre votre site et les moteurs',
    'hook': "Les moteurs de recherche et les IA génératives ne « lisent » pas une page comme un humain — ils s'appuient largement sur des indices structurés pour comprendre de quoi elle parle. Les données structurées (Schema.org, format JSON-LD) sont ce langage commun.",
    'title_seo': 'Données Structurées & Schema.org | Guide Pratique',
    'meta_description': "Qu'est-ce que le balisage Schema.org / JSON-LD, et pourquoi il aide autant le SEO classique que la visibilité dans les réponses des IA génératives.",
    'canonical': 'https://johansimonneau.fr/donnees-structurees',
    'service_name': 'Données structurées & Schema.org',
    'schema_type': 'Article',
    'blocks': [
        {'type': 'h2', 'text': 'Qu\'est-ce que le Schema.org concrètement'},
        {'type': 'p', 'text': "Le Schema.org est un vocabulaire standardisé qui permet de décrire explicitement le contenu d'une page à un moteur de recherche : « ceci est une question et sa réponse », « ceci est un service et son prix », « ceci est un article et son auteur ». Le format JSON-LD est la manière la plus courante de l'implémenter — un bloc de code invisible pour le visiteur, mais lisible par les moteurs."},
        {'type': 'h2', 'text': 'Pourquoi ça sert le SEO ET le GEO'},
        {'type': 'points', 'items': [
            ("Pour le SEO classique :", " ça augmente les chances d'obtenir des résultats enrichis (étoiles d'avis, FAQ dépliable directement dans les résultats de recherche, fil d'Ariane)."),
            ("Pour le GEO :", " une page bien balisée est plus facilement comprise et citée par les moteurs de réponse IA, qui s'appuient aussi sur ces indices structurés pour extraire une information fiable."),
        ]},
        {'type': 'h2', 'text': 'Les types de balisage les plus utiles'},
        {'type': 'points', 'items': [
            ("FAQPage.", " Pour toute section de questions-réponses — l'un des formats les plus efficaces pour l'extraction par les IA génératives."),
            ("Service.", " Pour décrire une offre de service, son public cible, sa zone géographique."),
            ("Article.", " Pour du contenu éditorial/guide, avec auteur et date de publication."),
            ("BreadcrumbList.", " Pour la structure de navigation, utile à la fois pour le SEO et la compréhension de la hiérarchie du site."),
        ]},
        {'type': 'h2', 'text': 'Un exemple concret'},
        {'type': 'p', 'text': "Chaque page de ce site intègre un balisage <strong>Service</strong> et <strong>FAQPage</strong> — c'est ce même principe qui est expliqué ici, appliqué concrètement plutôt que théoriquement."},
        {'type': 'faq', 'items': [
            ("Faut-il des compétences techniques pour ajouter ce balisage ?", "Une intervention technique est nécessaire pour l'intégrer correctement, mais la structure elle-même reste accessible à comprendre sans expertise développeur poussée."),
            ("Le balisage garantit-il d'apparaître en résultat enrichi ?", "Non, il augmente les chances mais Google et les moteurs génératifs décident librement de l'affichage final."),
            ("Est-ce risqué d'ajouter un balisage incorrect ?", "Un balisage qui ne correspond pas au contenu réel de la page peut être ignoré, voire pénalisé si l'écart est jugé trompeur — la cohérence entre balisage et contenu visible est essentielle."),
            ("Combien de temps pour voir un effet ?", "Les résultats enrichis peuvent apparaître en quelques semaines une fois le balisage indexé, sans délai garanti."),
        ]},
    ],
    'faq_items': [
        ("Faut-il des compétences techniques pour ajouter ce balisage ?", "Une intervention technique est nécessaire, mais la structure reste accessible à comprendre."),
        ("Le balisage garantit-il d'apparaître en résultat enrichi ?", "Non, il augmente les chances mais les moteurs décident librement de l'affichage final."),
        ("Est-ce risqué d'ajouter un balisage incorrect ?", "Un balisage incohérent avec le contenu réel peut être ignoré, voire pénalisé."),
        ("Combien de temps pour voir un effet ?", "Les résultats enrichis peuvent apparaître en quelques semaines, sans délai garanti."),
    ],
    'cta_title': 'Envie de vérifier si votre site est correctement balisé ?',
    'cta_primary_label': 'Échanger sur votre structuration technique',
    'cta_footer_html': 'Pour aller plus loin, voir la page <a href="/seo">SEO</a> et la page <a href="/geo">GEO</a>.',
    'band_text': "Cette page est à cheval sur deux expertises.",
    'related_links': [('/seo', 'SEO'), ('/geo', 'GEO'), ('/audit-visibilite-ia', 'Audit visibilité IA')],
},

# ============================================================
# 10. Google Ads Petit Budget
# ============================================================
{
    'slug': 'google-ads-petit-budget',
    'pillar_label': 'SEA',
    'pillar_slug': '/sea',
    'active_service_path': '/sea',
    'h1_short': 'Google Ads petit budget',
    'h1': "Google Ads pour petits budgets : une expertise différente, pas une version au rabais",
    'hook': "Beaucoup d'agences réservent leur meilleure expertise aux comptes à 6 chiffres. Sur un budget de quelques centaines à quelques milliers d'euros par mois, chaque euro compte différemment — moins de données, moins de marge d'erreur, et une méthodologie de test qui doit s'adapter en conséquence.",
    'title_seo': 'Google Ads Petit Budget | Consultant pour PME',
    'meta_description': "Consultant Google Ads spécialisé petits et moyens budgets (100€ à 20K€/mois). Cas client Swapn : +230% de croissance, -75% de CPA.",
    'canonical': 'https://johansimonneau.fr/google-ads-petit-budget',
    'service_name': 'Google Ads pour petits budgets',
    'schema_type': 'Service',
    'blocks': [
        {'type': 'case', 'label': 'Le cas Swapn', 'paragraphs': [
            "Swapn souhaitait structurer et scaler son acquisition digitale B2C et B2B via une stratégie de performance multicanale, avec des budgets évolutifs allant de 100€ à 20 000€ par mois selon les phases de croissance. L'enjeu n'était pas de gérer un gros compte, mais de construire une infrastructure publicitaire scalable dès les premiers euros investis.",
            "La stratégie a démarré par un déploiement de comptes publicitaires from scratch, une structuration SEA orientée génération de leads, et un suivi stratégique resserré à chaque palier de budget — en partant d'un budget de test minimal, pas d'un compte déjà mature.",
        ], 'stats': [('+230%', 'croissance moyenne'), ('-75%', 'de CPA'), ('4,6', 'en ROAS')]},
        {'type': 'h2', 'text': 'Ce qui change vraiment sur un petit budget'},
        {'type': 'points', 'items': [
            ("Moins de données, donc moins de tests simultanés.", " Sur un gros compte, on peut tester 5 variantes en parallèle. Sur un petit budget, il faut prioriser un test à la fois pour obtenir un signal exploitable."),
            ("Une structure de compte plus resserrée.", " Trop de campagnes ou de groupes d'annonces dispersent un budget limité sans jamais sortir de la phase d'apprentissage."),
            ("Des paliers de montée en budget pilotés.", " Passer de 500€ à 5000€/mois change les dynamiques d'enchères — la transition doit être progressive, pas brutale."),
            ("Une transparence totale sur ce qui est réaliste.", " Sur un petit budget, certains objectifs (volume élevé + CPA très bas simultanément) ne sont simplement pas atteignables tout de suite — mieux vaut le dire clairement."),
        ]},
        {'type': 'h2', 'text': "Pour quels types d'entreprises"},
        {'type': 'list', 'items': [
            "Startups et TPE en phase de test de leur premier canal payant",
            "PME dont le budget marketing ne justifie pas (encore) une agence à honoraires fixes élevés",
            "Entreprises qui montent progressivement en budget et veulent un accompagnement qui évolue avec elles",
        ]},
        {'type': 'faq', 'items': [
            ("Quel est le budget minimum pour commencer ?", "Il n'y a pas de seuil strict, mais en dessous de quelques centaines d'euros par mois, la marge d'optimisation reste limitée le temps de collecter des données exploitables."),
            ("Une agence n'est-elle pas plus adaptée pour un petit budget ?", "Beaucoup d'agences appliquent la même méthodologie quel que soit le budget, ce qui convient mal à un petit compte. Une approche pensée spécifiquement pour ces volumes fait souvent la différence."),
            ("Comment savoir si mon budget est prêt à augmenter ?", "Un budget est prêt à scaler quand les indicateurs clés (CPA, taux de conversion) sont stables sur plusieurs semaines, pas seulement sur un pic ponctuel."),
            ("Travaillez-vous aussi avec des budgets plus importants ?", "Oui, l'accompagnement évolue avec la croissance du compte — jusqu'à 20K€/mois et au-delà selon les projets."),
        ]},
    ],
    'faq_items': [
        ("Quel est le budget minimum pour commencer ?", "Il n'y a pas de seuil strict, mais en dessous de quelques centaines d'euros par mois, la marge d'optimisation reste limitée."),
        ("Une agence n'est-elle pas plus adaptée pour un petit budget ?", "Beaucoup d'agences appliquent la même méthodologie quel que soit le budget, ce qui convient mal à un petit compte."),
        ("Comment savoir si mon budget est prêt à augmenter ?", "Un budget est prêt à scaler quand les indicateurs clés sont stables sur plusieurs semaines."),
        ("Travaillez-vous aussi avec des budgets plus importants ?", "Oui, l'accompagnement évolue avec la croissance du compte, jusqu'à 20K€/mois et au-delà."),
    ],
    'cta_title': 'Discutons de votre budget, quel que soit son montant',
    'cta_primary_label': 'Réserver un audit gratuit',
    'cta_footer_html': 'Pour une vue complète de mon expertise SEA, voir la page <a href="/sea">SEA</a>.',
    'band_text': "Cette page fait partie de l'expertise SEA — une spécialisation forte de l'accompagnement proposé.",
    'related_links': [('/sea', 'SEA'), ('/bing-ads-freelance', 'Bing Ads'), ('/google-shopping', 'Google Shopping')],
},

]
