#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génère les 15 sous-pages du site à partir de données structurées,
en utilisant le template subpage.html (distinct des pages piliers).
"""
import re
import json

with open('/tmp/ref_header.html', encoding='utf-8') as f:
    HEADER_TEMPLATE = f.read()
with open('/tmp/ref_footer.html', encoding='utf-8') as f:
    FOOTER = f.read()

def header_with_active(slug_path):
    """Marque le lien de service actif dans le mega-menu si le pilier correspond à un service."""
    h = HEADER_TEMPLATE
    if slug_path:
        h = h.replace(
            f'href="{slug_path}" class="services-menu-item"',
            f'href="{slug_path}" class="services-menu-item" aria-current="page"'
        )
    return h


def render_breadcrumb(pillar_label, pillar_slug, page_title):
    return f'''<nav class="sub-breadcrumb" aria-label="Fil d'Ariane">
  <div class="container">
    <ol>
      <li><a href="/">Accueil</a></li>
      <li class="sep">/</li>
      <li><a href="{pillar_slug}">{pillar_label}</a></li>
      <li class="sep">/</li>
      <li aria-current="page">{page_title}</li>
    </ol>
  </div>
</nav>'''


def render_case(label, paragraphs, stats):
    stats_html = "\n".join(
        f'      <div class="sub-case-stat"><strong>{val}</strong><span>{lbl}</span></div>'
        for val, lbl in stats
    )
    paras_html = "\n".join(f'    <p>{p}</p>' for p in paragraphs)
    return f'''<div class="sub-case">
  <p class="sub-case-label">{label}</p>
{paras_html}
  <div class="sub-case-stats">
{stats_html}
  </div>
</div>'''


def render_points(items):
    lis = "\n".join(
        f'  <li><strong>{title}</strong>{desc}</li>' for title, desc in items
    )
    return f'<ul class="sub-points">\n{lis}\n</ul>'


def render_list(items):
    lis = "\n".join(f'  <li>{i}</li>' for i in items)
    return f'<ul class="sub-list">\n{lis}\n</ul>'


def render_faq(items):
    blocks = "\n".join(
        f'''  <details>
    <summary>{q}</summary>
    <p>{a}</p>
  </details>''' for q, a in items
    )
    return f'<div class="sub-faq">\n{blocks}\n</div>'


def render_json_ld(schema_type, service_desc, faq_items, canonical, service_name):
    graph = []
    if schema_type in ("Service", "both"):
        graph.append({
            "@type": "Service",
            "serviceType": service_name,
            "provider": {
                "@type": "Person",
                "name": "Johan Simonneau",
                "url": "https://johansimonneau.fr",
                "sameAs": ["https://www.linkedin.com/in/johansimonneau/"]
            },
            "areaServed": "FR",
            "description": service_desc
        })
    else:
        graph.append({
            "@type": "Article",
            "headline": service_name,
            "author": {"@type": "Person", "name": "Johan Simonneau"},
            "description": service_desc
        })
    graph.append({
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^<]+?>', '', a)}
            } for q, a in faq_items
        ]
    })
    data = {"@context": "https://schema.org", "@graph": graph}
    return json.dumps(data, ensure_ascii=False, indent=2)


def build_page(cfg):
    slug = cfg['slug']
    header = header_with_active(cfg.get('active_service_path'))
    breadcrumb = render_breadcrumb(cfg['pillar_label'], cfg['pillar_slug'], cfg['h1_short'])

    body_parts = []

    # Intro / hook déjà dans le header d'article, donc on commence par le premier H2
    for block in cfg['blocks']:
        btype = block['type']
        if btype == 'html':
            body_parts.append(block['content'])
        elif btype == 'h2':
            body_parts.append(f"<h2>{block['text']}</h2>")
        elif btype == 'p':
            body_parts.append(f"<p>{block['text']}</p>")
        elif btype == 'case':
            body_parts.append(render_case(block['label'], block['paragraphs'], block['stats']))
        elif btype == 'points':
            body_parts.append(render_points(block['items']))
        elif btype == 'list':
            body_parts.append(render_list(block['items']))
        elif btype == 'faq':
            body_parts.append(f"<h2>FAQ</h2>")
            body_parts.append(render_faq(block['items']))

    body_html = "\n\n".join(body_parts)

    json_ld = render_json_ld(
        cfg['schema_type'], cfg['meta_description'], cfg['faq_items'],
        cfg['canonical'], cfg['service_name']
    )

    related_links_html = "\n".join(
        f'      <a href="{href}">{label} →</a>' for href, label in cfg['related_links']
    )

    cta_secondary = cfg.get('cta_secondary_label', 'Contactez-moi')
    cta_mailto = f"mailto:johansimonneau.pro@gmail.com?subject=Demande%20sur%20portfolio%20!"

    html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{cfg['title_seo']} — Johan Simonneau</title>
<meta name="description" content="{cfg['meta_description']}">

<link rel="canonical" href="{cfg['canonical']}">
<meta property="og:type" content="article">
<meta property="og:title" content="{cfg['title_seo']}">
<meta property="og:description" content="{cfg['meta_description']}">
<meta property="og:url" content="{cfg['canonical']}">
<meta name="twitter:card" content="summary_large_image">

<link rel="icon" type="image/x-icon" href="favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

<link rel="stylesheet" href="style.css">
<link rel="stylesheet" href="subpage.css">

<script type="application/ld+json">
{json_ld}
</script>
</head>
<body>

<a class="skip-link" href="#main">Aller au contenu</a>

<div class="scroll-progress" id="scrollProgress" aria-hidden="true"></div>

{header}

{breadcrumb}

<main id="main">

  <section class="sub-header">
    <div class="container sub-header-inner">
      <a href="{cfg['pillar_slug']}" class="sub-pillar-tag">{cfg['pillar_label']}</a>
      <h1>{cfg['h1']}</h1>
      <p class="sub-hook">{cfg['hook']}</p>
    </div>
  </section>

  <section class="sub-article">
    <div class="container sub-article-inner">

{body_html}

      <div class="sub-cta">
        <h3>{cfg['cta_title']}</h3>
        <div class="sub-cta-actions">
          <a href="{cta_mailto}" class="btn btn-primary">{cfg['cta_primary_label']}</a>
          <span class="sub-cta-mail"><a href="mailto:johansimonneau.pro@gmail.com">johansimonneau.pro@gmail.com</a></span>
        </div>
        <p class="sub-cta-link">{cfg['cta_footer_html']}</p>
      </div>

    </div>
  </section>

  <section class="sub-pillar-band">
    <div class="container sub-pillar-band-inner">
      <p>{cfg['band_text']}</p>
      <div class="sub-pillar-band-links">
{related_links_html}
      </div>
    </div>
  </section>

</main>

{FOOTER}

<script src="script.js"></script>
</body>
</html>
'''
    with open(f'/home/claude/portfolio-v2/{slug}.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'{slug}.html généré ({len(html)} caractères)')


print("Module de génération chargé.")
