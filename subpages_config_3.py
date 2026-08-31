# -*- coding: utf-8 -*-
"""Configuration des sous-pages — batch 3/3"""

PAGES_BATCH_3 = [

# ============================================================
# 11. Google Shopping
# ============================================================
{
    'slug': 'google-shopping',
    'pillar_label': 'SEA',
    'pillar_slug': '/sea',
    'active_service_path': '/sea',
    'h1_short': 'Google Shopping',
    'h1': 'Google Shopping : la vitrine produit qui précède souvent le clic',
    'hook': "Pour un site e-commerce, Google Shopping affiche directement le produit, son prix et sa disponibilité avant même que l'utilisateur clique — la qualité du flux produit devient alors aussi importante que la stratégie d'enchères elle-même.",
    'title_seo': 'Consultant Google Shopping | Campagnes Produits',
    'meta_description': "Consultant Google Shopping freelance pour e-commerce : structuration du flux produit, campagnes Performance Max et Shopping classiques.",
    'canonical': 'https://johansimonneau.fr/google-shopping',
    'service_name': 'Consultant Google Shopping',
    'schema_type': 'Article',
    'blocks': [
        {'type': 'h2', 'text': "Où ça s'intègre dans une stratégie SEA"},
        {'type': 'p', 'text': "La gestion du Shopping fait partie du périmètre couvert aux côtés du Search, du Display et de YouTube — avec une spécificité propre : la performance dépend autant de la qualité des données produit (Google Merchant Center) que du pilotage des enchères."},
        {'type': 'h2', 'text': 'Ce qui fait la différence sur Google Shopping'},
        {'type': 'points', 'items': [
            ("La qualité du flux produit avant tout.", " Titres, descriptions, catégorisation — un flux mal structuré limite la performance quelle que soit la stratégie d'enchères."),
            ("La segmentation des campagnes.", " Regrouper les produits par marge, popularité ou catégorie permet un pilotage plus fin qu'une campagne unique fourre-tout."),
            ("L'arbitrage Shopping classique vs Performance Max.", " Chaque approche a ses avantages selon le niveau de contrôle souhaité sur les enchères et les emplacements."),
            ("Le suivi de la marge, pas seulement du ROAS.", " Un ROAS élevé sur des produits à faible marge peut être moins rentable qu'un ROAS plus modeste sur des produits à forte marge."),
        ]},
        {'type': 'h2', 'text': "Pour quels types d'entreprises"},
        {'type': 'list', 'items': [
            "Sites e-commerce avec un catalogue produit structuré",
            "Marketplaces cherchant à optimiser leur visibilité produit",
            "Entreprises déjà présentes en Search cherchant à couvrir aussi l'intention d'achat visuelle",
        ]},
        {'type': 'faq', 'items': [
            ("Faut-il un catalogue produit minimum pour faire du Shopping ?", "Non, mais un flux propre et bien catégorisé est indispensable, quel que soit le nombre de produits."),
            ("Quelle différence entre Shopping classique et Performance Max ?", "Le Shopping classique offre plus de contrôle et de visibilité sur la performance par produit. Performance Max automatise davantage mais réduit la granularité du pilotage."),
            ("Le Shopping fonctionne-t-il pour du B2B ?", "Moins naturellement — le format est pensé pour la vente directe au consommateur, avec prix et disponibilité affichés."),
            ("Comment est structuré le flux produit ?", "Via Google Merchant Center, connecté à votre catalogue (CMS e-commerce, ERP, ou flux généré manuellement)."),
        ]},
    ],
    'faq_items': [
        ("Faut-il un catalogue produit minimum pour faire du Shopping ?", "Non, mais un flux propre et bien catégorisé est indispensable."),
        ("Quelle différence entre Shopping classique et Performance Max ?", "Le Shopping classique offre plus de contrôle, Performance Max automatise davantage."),
        ("Le Shopping fonctionne-t-il pour du B2B ?", "Moins naturellement — le format est pensé pour la vente directe au consommateur."),
        ("Comment est structuré le flux produit ?", "Via Google Merchant Center, connecté à votre catalogue."),
    ],
    'cta_title': "Envie d'auditer la performance actuelle de votre flux Shopping ?",
    'cta_primary_label': 'Échanger sur votre stratégie Shopping',
    'cta_footer_html': 'Pour une vue complète de mon expertise SEA, voir la page <a href="/sea">SEA</a>.',
    'band_text': "Cette page fait partie de l'expertise SEA.",
    'related_links': [('/sea', 'SEA'), ('/google-ads-petit-budget', 'Google Ads petit budget'), ('/bing-ads-freelance', 'Bing Ads')],
},

# ============================================================
# 12. Optimisation Landing Page
# ============================================================
{
    'slug': 'optimisation-landing-page',
    'pillar_label': 'CRO',
    'pillar_slug': '/cro',
    'active_service_path': '/cro',
    'h1_short': 'Optimisation landing page',
    'h1': 'Optimisation de landing page : le trafic que vous avez déjà mérite mieux',
    'hook': "Avant d'augmenter un budget publicitaire, il vaut souvent mieux vérifier que la page qui reçoit ce trafic convertit correctement. Une landing page mal structurée peut faire perdre plus de la moitié des visiteurs qualifiés qu'elle reçoit.",
    'title_seo': 'Optimisation de Landing Page | Consultant Freelance',
    'meta_description': "Optimisation de vos pages de destination pour transformer le trafic déjà acquis. Cas client L-Expert-Comptable.com : +12% de taux de conversion.",
    'canonical': 'https://johansimonneau.fr/optimisation-landing-page',
    'service_name': 'Optimisation de landing page',
    'schema_type': 'Service',
    'blocks': [
        {'type': 'case', 'label': 'Le cas L-Expert-Comptable.com', 'paragraphs': [
            "Lexpertcomptable.com souhaitait améliorer la rentabilité de ses campagnes d'acquisition et structurer davantage ses opérations marketing. Le travail mené a inclus une optimisation du taux de conversion, aux côtés d'un audit stratégique SEA/SMA et d'une formation des équipes internes.",
            "Résultat obtenu sans augmenter le budget d'acquisition, uniquement en améliorant la capacité de la page à transformer le trafic déjà en place :",
        ], 'stats': [('+12%', 'de taux de conversion'), ('+10', 'leads / mois')]},
        {'type': 'h2', 'text': 'Ce qui fait la différence sur une landing page'},
        {'type': 'points', 'items': [
            ("Une proposition de valeur claire dès les premières secondes.", " Le visiteur doit comprendre en un coup d'œil ce qui lui est proposé et pourquoi ça le concerne."),
            ("Un seul objectif de conversion par page.", " Une page qui propose plusieurs actions concurrentes (télécharger, s'inscrire, contacter) dilue le taux de conversion global."),
            ("Un formulaire réduit au strict nécessaire.", " Chaque champ supplémentaire est un point de friction — la longueur du formulaire doit être justifiée par la valeur de ce qui est demandé en échange."),
            ("Une cohérence avec la source de trafic.", " Le message de l'annonce (Google Ads, Meta) doit se retrouver immédiatement sur la landing page — toute rupture de message fait chuter la conversion."),
        ]},
        {'type': 'h2', 'text': "Pour quels types d'entreprises"},
        {'type': 'list', 'items': [
            "Entreprises qui investissent en acquisition payante et veulent maximiser le rendement de chaque euro dépensé",
            "Sites avec un taux de conversion en dessous de la moyenne de leur secteur",
            "Toute entreprise qui lance une nouvelle offre et veut valider sa landing page avant de scaler le budget média",
        ]},
        {'type': 'faq', 'items': [
            ("Comment savoir si ma landing page a besoin d'être optimisée ?", "Un taux de conversion nettement en dessous des standards de votre secteur, ou un écart important entre le taux de clic publicitaire et le taux de conversion final, sont de bons indicateurs."),
            ("Faut-il refaire toute la page, ou peut-on l'optimiser progressivement ?", "L'approche progressive (test d'un élément à la fois) est généralement préférable — elle permet d'identifier précisément ce qui fonctionne, plutôt que de tout changer d'un coup sans savoir ce qui a eu de l'impact."),
            ("Travaillez-vous sur des pages Webflow, WordPress, ou sur-mesure ?", "Oui, l'approche s'adapte à la plateforme technique existante."),
            ("Combien de temps pour voir un premier gain de conversion ?", "Les premières optimisations qualitatives peuvent produire des effets en quelques semaines, selon le volume de trafic disponible pour valider les changements."),
        ]},
    ],
    'faq_items': [
        ("Comment savoir si ma landing page a besoin d'être optimisée ?", "Un taux de conversion nettement en dessous des standards de votre secteur est un bon indicateur."),
        ("Faut-il refaire toute la page, ou peut-on l'optimiser progressivement ?", "L'approche progressive est généralement préférable."),
        ("Travaillez-vous sur des pages Webflow, WordPress, ou sur-mesure ?", "Oui, l'approche s'adapte à la plateforme technique existante."),
        ("Combien de temps pour voir un premier gain de conversion ?", "Les premières optimisations peuvent produire des effets en quelques semaines."),
    ],
    'cta_title': 'Discutons de l\'optimisation de votre landing page',
    'cta_primary_label': 'Réserver un audit gratuit',
    'cta_footer_html': 'Pour une vue complète de mon expertise CRO, voir la page <a href="/cro">CRO</a>.',
    'band_text': "Cette page fait partie de l'expertise CRO.",
    'related_links': [('/cro', 'CRO'), ('/analyse-comportementale', 'Analyse comportementale'), ('/ab-testing-faible-trafic', 'A/B Testing faible trafic')],
},

# ============================================================
# 13. TikTok Ads
# ============================================================
{
    'slug': 'tiktok-ads',
    'pillar_label': 'SMA',
    'pillar_slug': '/sma',
    'active_service_path': '/sma',
    'h1_short': 'TikTok Ads',
    'h1': 'TikTok Ads : un canal encore jeune, mais déjà déterminant pour toucher une audience plus large',
    'hook': "TikTok n'est plus une plateforme de niche — elle capte aujourd'hui une audience large et diversifiée. Peu de freelances français se positionnent spécifiquement dessus, alors que les codes créatifs et les mécaniques d'enchères diffèrent nettement de Meta.",
    'title_seo': 'TikTok Ads Freelance | Consultant Publicité TikTok',
    'meta_description': "Consultant TikTok Ads freelance. Cas clients Swapn et Tiime : scaling paid social multi-plateformes, +230% et +900% de croissance.",
    'canonical': 'https://johansimonneau.fr/tiktok-ads',
    'service_name': 'TikTok Ads',
    'schema_type': 'Service',
    'blocks': [
        {'type': 'case', 'label': 'Les cas Swapn et Tiime', 'paragraphs': [
            "Swapn a construit son infrastructure d'acquisition en s'appuyant notamment sur Meta, LinkedIn, TikTok et X Ads, dans le cadre d'une stratégie qui a généré +230% de croissance moyenne et -75% de coût par acquisition.",
            "Chez Tiime, le scaling du paid media s'est étendu sur Google Ads, Meta, LinkedIn, TikTok et Instagram, avec une production de contenus UGC pensée pour ces formats natifs. Dans les deux cas, TikTok a fait partie d'un dispositif multicanale plutôt que d'être isolé — c'est généralement ainsi que le canal performe le mieux, en complément de Meta plutôt qu'en remplacement.",
        ], 'stats': [('+230%', 'croissance (Swapn)'), ('+900%', 'croissance en 3 ans (Tiime)'), ('-81%', 'de CAC (Tiime)')]},
        {'type': 'h2', 'text': 'Ce qui fait la différence sur TikTok Ads'},
        {'type': 'points', 'items': [
            ("Des codes créatifs propres à la plateforme.", " Un contenu qui ressemble à une publicité classique performe mal — le format natif, proche du contenu organique, reste déterminant."),
            ("Une audience plus jeune, mais en élargissement rapide.", " Le profil démographique s'étend chaque année, ce qui ouvre le canal à des cibles auparavant réservées à Meta."),
            ("Des enchères encore moins matures que sur Meta.", " Ce qui peut se traduire par des coûts d'acquisition plus bas sur certains segments, à condition de tester rapidement."),
            ("Un lien direct avec la production UGC.", " La performance créative et le format publicitaire sont indissociables sur cette plateforme."),
        ]},
        {'type': 'h2', 'text': "Pour quels types d'entreprises"},
        {'type': 'list', 'items': [
            "Marques B2C cherchant à élargir leur audience au-delà de Meta",
            "Applications mobiles en phase de scaling",
            "Entreprises disposant déjà d'une production de contenu créatif régulière",
        ]},
        {'type': 'faq', 'items': [
            ("TikTok Ads fonctionne-t-il pour toutes les cibles ?", "L'audience s'est beaucoup élargie, mais certains secteurs très B2B ou seniors y trouvent moins de pertinence qu'ailleurs."),
            ("Faut-il un contenu spécifique pour TikTok, ou peut-on réutiliser ses créas Meta ?", "Le format natif fonctionne nettement mieux — réutiliser telle quelle une créa pensée pour Meta donne généralement de moins bons résultats."),
            ("Quel budget minimum pour tester TikTok Ads ?", "Comparable à un test Meta classique — l'important est de pouvoir tester plusieurs créas rapidement, plus que d'avoir un budget élevé dès le départ."),
            ("TikTok Ads remplace-t-il Meta Ads ?", "Non, les deux canaux se complètent généralement plutôt qu'ils ne se substituent l'un à l'autre."),
        ]},
    ],
    'faq_items': [
        ("TikTok Ads fonctionne-t-il pour toutes les cibles ?", "L'audience s'est beaucoup élargie, mais certains secteurs très B2B y trouvent moins de pertinence."),
        ("Faut-il un contenu spécifique pour TikTok, ou peut-on réutiliser ses créas Meta ?", "Le format natif fonctionne nettement mieux."),
        ("Quel budget minimum pour tester TikTok Ads ?", "Comparable à un test Meta classique."),
        ("TikTok Ads remplace-t-il Meta Ads ?", "Non, les deux canaux se complètent généralement."),
    ],
    'cta_title': 'Discutons d\'intégrer TikTok à votre stratégie',
    'cta_primary_label': 'Réserver un audit gratuit',
    'cta_footer_html': 'Pour une vue complète de mon expertise SMA, voir la page <a href="/sma">SMA</a>.',
    'band_text': "Cette page fait partie de l'expertise SMA.",
    'related_links': [('/sma', 'SMA'), ('/sea', 'SEA')],
},

# ============================================================
# 14. Tracking Mobile
# ============================================================
{
    'slug': 'tracking-mobile',
    'pillar_label': 'Mobile Marketing',
    'pillar_slug': '/mobile-marketing',
    'active_service_path': '/mobile-marketing',
    'h1_short': 'Tracking mobile',
    'h1': "Tracking mobile : mesurer fiablement au-delà de l'installation",
    'hook': "Une application qui ne mesure que ses installations passe à côté de l'essentiel — ce qui compte vraiment, c'est ce qui se passe après : rétention, activation, valeur générée. Un tracking mal configuré fausse ces mesures sans que ça se voie immédiatement.",
    'title_seo': 'Tracking Mobile Firebase & Adjust | Attribution App',
    'meta_description': "Mise en place du tracking mobile (Firebase, Adjust) pour mesurer fiablement l'acquisition et la rétention de votre application, malgré les restrictions iOS.",
    'canonical': 'https://johansimonneau.fr/tracking-mobile',
    'service_name': 'Tracking mobile — Firebase & Adjust',
    'schema_type': 'Article',
    'blocks': [
        {'type': 'h2', 'text': "Pourquoi c'est devenu plus complexe"},
        {'type': 'p', 'text': "Depuis les restrictions iOS 14.5+ (App Tracking Transparency), l'attribution mobile classique a perdu une partie de sa fiabilité côté navigateur et app. Les solutions actuelles (SKAdNetwork, tracking probabiliste) demandent une configuration plus fine qu'auparavant pour rester exploitables."},
        {'type': 'h2', 'text': 'Ce que couvre la mise en place'},
        {'type': 'points', 'items': [
            ("Firebase.", " Suivi des événements in-app, des conversions et du comportement utilisateur, avec une intégration native à l'écosystème Google."),
            ("Adjust (ou équivalent MMP).", " Attribution multi-source pour identifier quelle campagne, quel canal a réellement généré chaque installation — indispensable dès que plusieurs canaux d'acquisition sont actifs en parallèle."),
            ("Configuration SKAdNetwork.", " Adaptation aux contraintes de confidentialité iOS pour conserver un niveau d'attribution exploitable."),
            ("Connexion aux plateformes publicitaires.", " Pour que les données de conversion remontent correctement vers Google Ads, Meta, TikTok et alimentent les optimisations d'enchères."),
        ]},
        {'type': 'h2', 'text': 'Pourquoi ça compte concrètement'},
        {'type': 'p', 'text': "Sans cette infrastructure, il devient impossible de savoir quel canal d'acquisition ramène des utilisateurs qui restent et génèrent de la valeur, par opposition à ceux qui installent puis désinstallent rapidement. Les décisions de budget se prennent alors sur des données incomplètes."},
        {'type': 'h2', 'text': "Pour quels types d'applications"},
        {'type': 'list', 'items': [
            "Applications avec plusieurs canaux d'acquisition actifs simultanément (Apple Search Ads, Meta, TikTok, Google)",
            "Applications en phase de scaling où le pilotage précis du budget devient critique",
            "Éditeurs voulant fiabiliser leur mesure de rétention, pas seulement d'acquisition",
        ]},
        {'type': 'faq', 'items': [
            ("Firebase suffit-il, ou faut-il aussi un MMP comme Adjust ?", "Firebase couvre bien le comportement in-app. Un MMP devient nécessaire dès que plusieurs canaux publicitaires doivent être comparés entre eux de façon fiable."),
            ("Les restrictions iOS rendent-elles le tracking mobile impossible ?", "Non, mais elles imposent une configuration plus rigoureuse (SKAdNetwork) et une attribution partiellement probabiliste plutôt que déterministe."),
            ("Combien de temps pour mettre en place ce tracking ?", "Généralement 2 à 3 semaines selon la complexité de l'application et le nombre de canaux à connecter."),
            ("Ce tracking fonctionne-t-il aussi bien sur Android ?", "Android est moins contraint par les restrictions de confidentialité qu'iOS, ce qui simplifie une partie de la configuration."),
        ]},
    ],
    'faq_items': [
        ("Firebase suffit-il, ou faut-il aussi un MMP comme Adjust ?", "Firebase couvre le comportement in-app. Un MMP devient nécessaire avec plusieurs canaux publicitaires."),
        ("Les restrictions iOS rendent-elles le tracking mobile impossible ?", "Non, mais elles imposent une configuration plus rigoureuse (SKAdNetwork)."),
        ("Combien de temps pour mettre en place ce tracking ?", "Généralement 2 à 3 semaines selon la complexité de l'application."),
        ("Ce tracking fonctionne-t-il aussi bien sur Android ?", "Android est moins contraint par les restrictions de confidentialité qu'iOS."),
    ],
    'cta_title': 'Envie de vérifier si votre tracking mobile actuel est fiable ?',
    'cta_primary_label': 'Échanger sur votre tracking mobile',
    'cta_footer_html': 'Pour une vue complète de mon expertise, voir la page <a href="/mobile-marketing">Mobile Marketing</a> et la page <a href="/analytics">Analytics</a>.',
    'band_text': "Cette page est à cheval sur deux expertises.",
    'related_links': [('/mobile-marketing', 'Mobile Marketing'), ('/analytics', 'Analytics'), ('/apple-search-ads', 'Apple Search Ads')],
},

# ============================================================
# 15. YouTube Ads
# ============================================================
{
    'slug': 'youtube-ads',
    'pillar_label': 'SEA',
    'pillar_slug': '/sea',
    'active_service_path': '/sea',
    'h1_short': 'YouTube Ads',
    'h1': 'YouTube Ads : un format encore sous-exploité par beaucoup d\'annonceurs',
    'hook': "YouTube Ads reste géré via la même plateforme que Google Ads Search et Shopping, mais avec une logique différente — on y capte une attention plus longue, avec des formats qui se prêtent à la notoriété autant qu'à la conversion directe.",
    'title_seo': 'YouTube Ads Freelance | Publicité Vidéo Google Ads',
    'meta_description': "Consultant YouTube Ads freelance : stratégie vidéo intégrée à votre écosystème Google Ads, du ciblage au format le plus adapté à votre objectif.",
    'canonical': 'https://johansimonneau.fr/youtube-ads',
    'service_name': 'YouTube Ads',
    'schema_type': 'Article',
    'blocks': [
        {'type': 'h2', 'text': "Où ça s'intègre dans une stratégie SEA"},
        {'type': 'p', 'text': "YouTube Ads fait partie du périmètre géré aux côtés du Search, du Shopping et du Display sur les comptes suivis — un complément naturel plutôt qu'un canal isolé, en particulier pour les marques qui cherchent à toucher une audience en amont de la recherche active."},
        {'type': 'h2', 'text': 'Les formats à connaître'},
        {'type': 'points', 'items': [
            ("In-stream skippable.", " Le format le plus courant — l'utilisateur peut passer la publicité après 5 secondes, ce qui impose un message fort dès le début."),
            ("In-feed.", " Apparaît dans les résultats de recherche YouTube et sur la page d'accueil, plus proche d'une logique « pull »."),
            ("Bumper ads.", " Format court non-skippable (6 secondes max), utile pour la notoriété pure."),
            ("Shorts ads.", " Format vertical, en forte croissance, aligné sur les usages mobiles actuels."),
        ]},
        {'type': 'h2', 'text': "Pour quels types d'entreprises"},
        {'type': 'list', 'items': [
            "Marques cherchant à construire de la notoriété en amont du tunnel de conversion",
            "Entreprises avec des assets vidéo déjà produits (ou prêtes à en produire)",
            "Comptes Google Ads matures cherchant à diversifier au-delà du Search et du Shopping",
        ]},
        {'type': 'faq', 'items': [
            ("Faut-il une vidéo professionnelle pour démarrer ?", "Non, certains formats (notamment les formats courts) fonctionnent bien avec des vidéos plus simples, à condition que le message soit clair dès les premières secondes."),
            ("YouTube Ads convient-il à tous les budgets ?", "Le coût par vue est généralement bas, mais un budget minimum est nécessaire pour sortir de la phase d'apprentissage sur le ciblage vidéo."),
            ("Comment mesure-t-on la performance d'une campagne YouTube Ads ?", "Selon l'objectif : vues, taux de complétion, ou conversions si l'objectif est direct plutôt que la notoriété."),
            ("Est-ce complémentaire avec le Search ?", "Oui, souvent utilisé en amont pour créer de la familiarité avant que l'utilisateur ne recherche activement la marque."),
        ]},
    ],
    'faq_items': [
        ("Faut-il une vidéo professionnelle pour démarrer ?", "Non, certains formats fonctionnent bien avec des vidéos plus simples."),
        ("YouTube Ads convient-il à tous les budgets ?", "Le coût par vue est généralement bas, mais un budget minimum est nécessaire."),
        ("Comment mesure-t-on la performance d'une campagne YouTube Ads ?", "Selon l'objectif : vues, taux de complétion, ou conversions."),
        ("Est-ce complémentaire avec le Search ?", "Oui, souvent utilisé en amont pour créer de la familiarité."),
    ],
    'cta_title': 'Envie d\'explorer si YouTube Ads a sa place dans votre stratégie d\'acquisition ?',
    'cta_primary_label': 'Échanger sur votre stratégie vidéo',
    'cta_footer_html': 'Pour une vue complète de mon expertise SEA, voir la page <a href="/sea">SEA</a>.',
    'band_text': "Cette page fait partie de l'expertise SEA.",
    'related_links': [('/sea', 'SEA'), ('/google-shopping', 'Google Shopping'), ('/google-ads-petit-budget', 'Google Ads petit budget')],
},

]
