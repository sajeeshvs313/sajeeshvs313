import os, sys, importlib, shutil
sys.path.insert(0, os.path.dirname(__file__))
from template import build_page
OUT = os.path.join(os.path.dirname(__file__), "..", "demo")
mods = [m for m in ("data1", "data2", "data3", "data4") if os.path.exists(os.path.join(os.path.dirname(__file__), m + ".py"))]
sites = []
for m in mods:
    sites += importlib.import_module(m).SITES
only = sys.argv[1:]
for s in sites:
    if only and s["slug"] not in only: continue
    d = os.path.join(OUT, s["slug"]); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(build_page(s))
print("built", len([s for s in sites if not only or s["slug"] in only]), "of", len(sites))

# ---- landing page + crawler files -------------------------------------------------
if not only:
    from landing import build_landing, GROUPS
    from template import DOMAIN
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(build_landing(sites))
    from industry import build_industry, build_hub, INDS, LASTMOD
    demos = {x["slug"]: x for x in sites}
    wf = os.path.join(OUT, "websites-for"); os.makedirs(wf, exist_ok=True)
    open(os.path.join(wf, "index.html"), "w", encoding="utf-8").write(build_hub(demos))
    for ind in INDS:
        d = os.path.join(wf, ind["url"]); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(build_industry(ind, demos))
    urls = [(f"{DOMAIN}/", "1.0")] + [(f"{DOMAIN}/websites-for/", "0.9")] + [(f"{DOMAIN}/websites-for/{i['url']}/", "0.8") for i in INDS]
    open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{u}</loc><lastmod>{LASTMOD}</lastmod><changefreq>monthly</changefreq><priority>{p}</priority></url>\n" for u, p in urls)
        + "</urlset>\n")
    open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(
        f"User-agent: *\nAllow: /\n\n# Demo pages use sample content and carry a noindex tag. Industry guides under /websites-for/ are indexable.\nSitemap: {DOMAIN}/sitemap.xml\n")
    lines = ["# Qrenzy Digital Solutions: Website Demos", "",
             f"> {len(sites)} ready-made website demos across 15 industries for local businesses in Kerala, India, built by Qrenzy Digital Solutions (www.qrenzy.com), Thrissur. "
             "Websites start at ₹5,000 and go live in about 48 hours. Contact: +91 99057 00600 (WhatsApp).", "", "## Demos", ""]
    for s in sites:
        lines.append(f"- [{s['cat']}: {s['name']}]({DOMAIN}/{s['slug']}/): {s['desc']}")
    lines += ["", "## Website design guides by industry", ""]
    for i in INDS:
        lines.append(f"- [Website design for {i['name']}]({DOMAIN}/websites-for/{i['url']}/): {i['intro']}")
    open(os.path.join(OUT, "llms.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("landing + sitemap + robots + llms.txt written")
