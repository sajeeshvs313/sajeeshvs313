"""Indexable industry landing pages (30) + hub page, in the qrenzy.com style."""
import json
from template import DOMAIN, WA_SVG, ARROW, PHONE_SVG, e
import landing
from landing import CSS as LCSS, GROUPS, ADDRESS, INCLUDED, EXCLUDED, PLANS
import ind1, ind2, ind3  # noqa: F401  (importing registers the entries)
from ind1 import INDS

ORG_ID = "https://www.qrenzy.com/#org"
WEBSITE_ID = DOMAIN + "/#website"
ORG = {"@type": "ProfessionalService", "@id": ORG_ID, "name": "Qrenzy Digital Solutions", "url": "https://www.qrenzy.com",
       "telephone": "+919905700600", "email": "info@qrenzy.com",
       "address": {"@type": "PostalAddress", "streetAddress": "Medical College Road, Kodankandan Jn, Deepti Nagar, Mundur P.O.", "addressLocality": "Thrissur",
                   "addressRegion": "Kerala", "postalCode": "680541", "addressCountry": "IN"}}
LASTMOD = "2026-10-09"
URL_OF = {i["demo"]: i["url"] for i in INDS}
NAME_OF = {i["demo"]: i for i in INDS}

EXTRA_CSS = r"""
.crumbs{font-size:13px;color:var(--muted);margin-bottom:18px;display:flex;flex-wrap:wrap;gap:6px}.crumbs a{color:var(--grey);font-weight:600}.crumbs a:hover{color:var(--red)}.crumbs span{opacity:.5}
.hero--ind{padding-bottom:56px}
.shotcard{display:block;background:#fff;border:1.5px solid var(--line);border-radius:24px;overflow:hidden;box-shadow:var(--shadow);transition:.25s}
.shotcard:hover{transform:translateY(-4px);border-color:rgba(227,30,36,.2)}
.shotcard .bar{height:30px;display:flex;align-items:center;gap:6px;padding:0 14px;background:#f6f6f4}.shotcard .bar i{width:9px;height:9px;border-radius:50%;background:#d4d4d9}.shotcard .bar i:nth-child(1){background:#ff5f56}.shotcard .bar i:nth-child(2){background:#ffbd2e}.shotcard .bar i:nth-child(3){background:#27c93f}
.shotcard .bar span{margin-left:8px;font-size:12px;color:var(--muted);background:#fff;border-radius:999px;padding:2px 12px}
.shotcard img{width:100%;height:auto;aspect-ratio:8/5;object-fit:cover;object-position:top}
.shotcard p{padding:14px 20px 18px;font-weight:800;font-size:14.5px;color:var(--red);display:flex;justify-content:space-between;align-items:center}.shotcard p svg{width:17px;height:17px}
.qa{padding:0}.qcard{background:var(--warm);border:1px solid var(--line);border-radius:var(--r);padding:clamp(22px,3vw,34px);display:grid;grid-template-columns:1.2fr 1fr;gap:clamp(20px,3vw,40px);align-items:center}
.qcard h2{font-size:clamp(20px,2.4vw,26px);margin:10px 0 8px}.qcard p{color:#555;font-size:14px}
.qcard dl{display:grid;gap:10px}.qcard dl div{background:#fff;border:1px solid var(--line);border-radius:14px;padding:12px 16px;display:flex;justify-content:space-between;gap:12px;font-size:14.5px}.qcard dt{color:var(--muted);font-weight:600}.qcard dd{font-weight:800;color:var(--ink);text-align:right}
.qchips{display:flex;flex-wrap:wrap;gap:10px}.qchips li{background:#fff;border:1px solid var(--line);border-radius:999px;padding:10px 18px;font-weight:600;font-size:13px}.qchips li:before{content:"🔎 ";font-size:13px}
.needs{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.need{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:24px}.need b{display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--red);color:#fff;font-size:14px;margin-bottom:12px}.need h3{font-size:17.5px;letter-spacing:-.02em}.need p{color:var(--grey);font-size:14.5px;margin-top:8px}
.mist{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.mi{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:24px}.mi .no{font-weight:800;color:#b3121a;font-size:15px;display:flex;gap:8px}.mi .no:before{content:"✕";background:#fde8e8;border-radius:50%;width:22px;height:22px;display:grid;place-items:center;font-size:11px;flex:none}.mi .fix{margin-top:12px;color:var(--grey);font-size:14.5px;display:flex;gap:8px}.mi .fix:before{content:"✓";color:#1faa59;font-weight:900}
.seeit{display:grid;grid-template-columns:1.15fr .85fr;gap:clamp(24px,4vw,56px);align-items:center}
.seeit ul{display:grid;gap:10px;margin:18px 0 26px}.seeit li{display:flex;gap:10px;font-size:15px;color:var(--grey)}.seeit li:before{content:"✓";color:var(--red);font-weight:900}
.btns{display:flex;flex-wrap:wrap;gap:10px}.btns .btn{min-height:48px;padding:0 22px;font-size:14.5px}
.mini{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.mini .plan{padding:26px 24px}.mini .price{font-size:40px}
.rel{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.rel a{display:flex;flex-direction:column;gap:8px;background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:22px;transition:.2s}.rel a:hover{border-color:var(--red);transform:translateY(-4px);box-shadow:var(--shadow)}.rel b{font-size:17px;letter-spacing:-.02em;color:var(--ink)}.rel span{font-size:14px;color:var(--grey)}.rel i{font-style:normal;color:var(--red);font-weight:800;font-size:14px}
.hubg{margin-top:44px}.hubg h2{font-size:clamp(22px,3vw,30px);margin:0 0 18px}.hubgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.hubgrid a{display:flex;flex-direction:column;gap:6px;background:#fff;border:1px solid var(--line);border-radius:20px;padding:22px;transition:.2s}.hubgrid a:hover{border-color:var(--red);transform:translateY(-4px);box-shadow:var(--shadow)}.hubgrid b{font-size:17px;letter-spacing:-.02em;color:var(--ink)}.hubgrid span{font-size:14px;color:var(--grey)}.hubgrid i{font-style:normal;color:var(--red);font-weight:800;font-size:14px;margin-top:4px}
@media(max-width:1020px){.qcard,.seeit{grid-template-columns:1fr}.needs,.mist,.mini,.rel,.hubgrid{grid-template-columns:1fr 1fr}}
@media(max-width:680px){.needs,.mist,.mini,.rel,.hubgrid{grid-template-columns:1fr}}
"""

JS = r"""
(function(){var d=document,r=d.documentElement;r.classList.add('js');var NUM='919905700600';var GA4='G-9ZYRDQ7B4V';
var wa=function(t){return 'https://wa.me/'+NUM+'?text='+encodeURIComponent(t)};
d.querySelectorAll('[data-wa]').forEach(function(a){a.href=wa(a.getAttribute('data-wa'));a.target='_blank';a.rel='noopener'});
d.querySelectorAll('[data-tel]').forEach(function(a){a.href='tel:+'+NUM;if(!a.classList.contains('c'))a.textContent='+91 99057 00600'});
d.getElementById('yr').textContent=new Date().getFullYear();
if(GA4){var gs=d.createElement('script');gs.async=1;gs.src='https://www.googletagmanager.com/gtag/js?id='+GA4;d.head.appendChild(gs);window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};gtag('js',new Date());gtag('config',GA4)}
var ev=function(n,p){if(window.gtag)gtag('event',n,p||{})};
d.addEventListener('click',function(e){var a=e.target.closest('a');if(!a)return;var n=a.getAttribute('data-ev');if(n)ev(n,{page:location.pathname,demo:a.getAttribute('data-demo')||''});else if(a.hasAttribute('data-wa'))ev('whatsapp_click',{page:location.pathname});else if(a.hasAttribute('data-tel'))ev('call_click',{page:location.pathname})});
var b=d.getElementById('burger'),mn=d.getElementById('menu');
if(b){b.addEventListener('click',function(){var o=mn.classList.toggle('open');b.setAttribute('aria-expanded',o)});mn.addEventListener('click',function(e){if(e.target.tagName==='A'){mn.classList.remove('open');b.setAttribute('aria-expanded','false')}})}
var els=d.querySelectorAll('.rv');
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.1,rootMargin:'0px 0px -30px 0px'});els.forEach(function(e){io.observe(e)})}else{els.forEach(function(e){e.classList.add('in')})}
})();
"""


def head(title, desc, url, depth, image):
    return f"""<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en-IN" href="{url}">
<meta name="theme-color" content="#E31E24">
<meta property="og:type" content="website"><meta property="og:site_name" content="Qrenzy Digital Solutions">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}"><meta property="og:locale" content="en_IN"><meta property="og:image" content="{image}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(desc)}">
<link rel="icon" href="{'../' * depth}logo.png">
"""


def header(root, hub):
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="container nav">
  <a href="{root}" aria-label="Qrenzy Digital Solutions"><img class="logo" src="{root}logo.png" alt="Qrenzy Digital Solutions" width="150" height="52"></a>
  <nav aria-label="Main"><ul class="menu" id="menu"><li><a href="{root}#demos">Demos</a></li><li><a class="on" href="{hub}">Industries</a></li><li><a href="{root}#included">What's included</a></li><li><a href="{root}#pricing">Pricing</a></li><li><a href="{root}#faq">FAQ</a></li><li><a href="{root}#contact">Contact</a></li></ul></nav>
  <div class="nav-cta"><a class="tl" data-wa="Hi Qrenzy, I want a website for my business." href="#">{WA_SVG} WhatsApp</a><span class="sep"></span><a class="tl red" href="{root}#contact">Free Demo →</a>
  <button class="burger" id="burger" aria-label="Menu" aria-expanded="false" aria-controls="menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button></div>
</div></header>
"""


def footer(root, hub):
    return f"""<footer><div class="container">
  <div class="fgrid">
    <div><img class="logo" src="{root}logo.png" alt="Qrenzy Digital Solutions" width="150" height="52" style="filter:brightness(0) invert(1)"><p>Qrenzy Digital Solutions is an AI-powered digital marketing and website design agency in Thrissur, Kerala.</p><p>{e(ADDRESS)}</p></div>
    <div><h3>Explore</h3><ul><li><a href="{root}#demos">All demos</a></li><li><a href="{hub}">Industry guides</a></li><li><a href="{root}#pricing">Pricing</a></li><li><a href="{root}#faq">FAQ</a></li></ul></div>
    <div><h3>Contact</h3><ul><li><a data-tel href="#">+91 99057 00600</a></li><li><a href="mailto:info@qrenzy.com">info@qrenzy.com</a></li><li><a href="https://www.qrenzy.com" rel="noopener">www.qrenzy.com</a></li></ul></div>
  </div>
  <div class="fbar"><span>© <span id="yr"></span> Qrenzy Digital Solutions. Demo sites use sample content. This site uses Google Analytics to measure visits.</span><span>Thrissur, Kerala, India</span></div>
</div></footer>
<nav class="mbar" aria-label="Quick actions"><a class="c" data-tel href="#">{PHONE_SVG} Call</a><a class="w" data-wa="Hi Qrenzy, I want a free demo for my business." href="#">{WA_SVG} WhatsApp</a></nav>
<script>{JS}</script>
</body>
</html>
"""


def build_industry(ind, demos):
    d = demos[ind["demo"]]
    page_url = f"{DOMAIN}/websites-for/{ind['url']}/"
    demo_url = f"{DOMAIN}/{ind['demo']}/"
    hub = "../"
    root = "../../"
    title = f"{ind['short']} Website Design in Kerala | Qrenzy"
    desc = f"{ind['name']} website design in Kerala: {ind['kf']}. See the live demo and pricing from ₹5,000."
    if len(desc) > 160:
        desc = desc[:157].rsplit(" ", 1)[0] + "…"
    image = f"{DOMAIN}/assets/thumbs/{ind['demo']}.jpg"
    get_msg = e(f"Hi Qrenzy, I run a {ind['singular']} and I am interested in this website design: {d['name']} ({demo_url}). Please share details and next steps. [Page: websites-for/{ind['url']}]")
    cust_msg = e(f"Hi Qrenzy, I run a {ind['singular']} and would like the {d['cat']} demo customised for my business ({demo_url}). My business name is: ")
    ld = {"@context": "https://schema.org", "@graph": [
        ORG,
        {"@type": "WebPage", "@id": page_url + "#page", "url": page_url, "name": title, "description": desc, "inLanguage": "en-IN",
         "isPartOf": {"@id": WEBSITE_ID}, "about": {"@id": page_url + "#service"}, "primaryImageOfPage": {"@type": "ImageObject", "url": image},
         "dateModified": LASTMOD},
        {"@type": "Service", "@id": page_url + "#service", "name": f"Website design for {ind['name'].lower()}", "serviceType": "Website design",
         "provider": {"@id": ORG_ID}, "areaServed": {"@type": "State", "name": "Kerala"}, "description": ind["intro"], "url": page_url,
         "offers": {"@type": "Offer", "priceCurrency": "INR", "price": "5000", "url": page_url,
                    "description": "Introductory starting price for a single-page website, including first-year domain and hosting. A complete six-section website is typically ₹12,000. Renewal, email and extras are quoted separately."}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in ind["faq"]]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Qrenzy website demos", "item": DOMAIN + "/"},
            {"@type": "ListItem", "position": 2, "name": "Website design by industry", "item": DOMAIN + "/websites-for/"},
            {"@type": "ListItem", "position": 3, "name": ind["name"], "item": page_url}]},
    ]}
    queries = "".join(f"<li>{e(q)}</li>" for q in ind["queries"])
    needs = "".join(f'<article class="need rv"><b>{i}</b><h3>{e(t)}</h3><p>{e(x)}</p></article>' for i, (t, x) in enumerate(ind["needs"], 1))
    mist = "".join(f'<article class="mi rv"><p class="no">{e(w)}</p><p class="fix">{e(f)}</p></article>' for w, f in ind["mistakes"])
    faq = "".join(f'<details class="rv"><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in ind["faq"])
    svc_text = ", ".join(t for _, t, _ in d["services"][:4])
    plans = "".join(
        f'<article class="plan rv{" pop" if pop else ""}">{"<span class=ptag>MOST POPULAR</span>" if pop else ""}<h3>{e(nm)}</h3><p class="for">{e(fr)}</p>'
        f'<div class="price"><sup>₹</sup>{pr}<small> one-time*</small></div><ul>{"".join(f"<li>{e(x)}</li>" for x in fe)}</ul>'
        f'<a class="btn {"btn-p" if pop else "btn-o"}" data-wa="Hi Qrenzy, I run a {e(ind["singular"])} and I am interested in the {e(nm)} website package." data-ev="plan_click" data-demo="{ind["demo"]}" href="#">Choose {e(nm)}</a></article>'
        for nm, fr, pr, fe, pop in PLANS)
    rel = "".join(f'<a href="../{URL_OF[r]}/"><b>{e(NAME_OF[r]["name"])}</b><span>{e(NAME_OF[r]["kf"][:1].upper() + NAME_OF[r]["kf"][1:])}.</span><i>Read the guide →</i></a>' for r in ind["related"])
    body = head(title, desc, page_url, 2, image) + f"""<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{LCSS}{EXTRA_CSS}</style>
</head>
<body>
{header(root, hub)}
<main id="main">
<section class="hero hero--ind"><div class="container hgrid">
  <div>
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{root}">Qrenzy demos</a><span>/</span><a href="{hub}">Industries</a><span>/</span><span style="opacity:1;color:var(--ink);font-weight:700">{e(ind['name'])}</span></nav>
    <p class="kicker"><span></span>Website design for {e(ind['name'].lower())}</p>
    <h1>Website Design for <em>{e(ind['name'])}</em> in Kerala</h1>
    <p class="lead">{e(ind['intro'])}</p>
    <ul class="pills"><li><b>₹</b> From ₹5,000*</li><li><b>🌐</b> First-year domain &amp; hosting included</li><li><b>⚡</b> Typical launch in 48 hrs*</li></ul>
    <div class="hero-cta"><a class="btn btn-p" href="{root}{ind['demo']}/" data-ev="demo_open" data-demo="{ind['demo']}">View the live demo →</a><a class="btn btn-w" data-wa="{get_msg}" data-ev="get_design" data-demo="{ind['demo']}" href="#">💬 Get This Design</a></div>
    <p class="fine">*Introductory pricing, not a final quotation. Typical launch is 48 hours after we receive all content and approvals. Renewal, email and extras are quoted separately.</p>
  </div>
  <a class="shotcard" href="{root}{ind['demo']}/" data-ev="demo_open" data-demo="{ind['demo']}" aria-label="Open the live {e(ind['short'])} website demo">
    <div class="bar"><i></i><i></i><i></i><span>{e(ind['demo'])}.qrenzy.com</span></div>
    <img src="{root}assets/thumbs/{ind['demo']}.jpg" width="960" height="600" decoding="async" alt="Live {e(ind['short'])} website demo preview: {e(d['name'])}">
    <p>Open the live demo {ARROW}</p>
  </a>
</div></section>

<section class="qa" aria-labelledby="qa-h"><div class="container"><div class="qcard rv">
  <div><span class="eyebrow">✦ Quick answer</span><h2 id="qa-h">How much does a {e(ind['singular'])} website cost in Kerala?</h2>
  <p>A one-page {e(ind['singular'])} website with a WhatsApp enquiry form starts at ₹5,000 with Qrenzy Digital Solutions, and a complete six-section website with SEO and FAQ markup is typically ₹12,000. The first-year domain and hosting are included.</p></div>
  <dl><div><dt>Starting price</dt><dd>₹5,000 (one page)</dd></div><div><dt>Complete website</dt><dd>Typically ₹12,000</dd></div><div><dt>Includes</dt><dd>Domain + hosting, year 1</dd></div><div><dt>Typical launch</dt><dd>48 hours after content</dd></div></dl>
</div></div></section>

<section aria-labelledby="s-h"><div class="container">
  <div class="sec-head"><span class="eyebrow">✦ What customers search for</span><h2 id="s-h">The searches your {e(ind['short'].lower())} website should answer</h2><p>These are examples of how people look for {e(ind['name'].lower())} in Kerala. Each one points to a page, a question or a detail that your website should cover clearly.</p></div>
  <ul class="qchips rv">{queries}</ul>
</div></section>

<section class="warm" aria-labelledby="n-h"><div class="container">
  <div class="sec-head"><span class="eyebrow">✦ What your website needs</span><h2 id="n-h">Six things a {e(ind['short'].lower())} website must do well</h2></div>
  <div class="needs">{needs}</div>
</div></section>

<section aria-labelledby="m-h"><div class="container">
  <div class="sec-head"><span class="eyebrow">✦ Common mistakes</span><h2 id="m-h">Mistakes we see, and how to fix them</h2></div>
  <div class="mist">{mist}</div>
</div></section>

<section class="warm" aria-labelledby="l-h"><div class="container seeit">
  <div class="rv"><span class="eyebrow">✦ See it live</span><h2 id="l-h">Open the {e(ind['short'])} demo on your phone</h2>
    <p class="lead" style="margin-top:14px">This is a working sample website with sample content: {e(d['name'])}. It shows how services, pricing, FAQ, map and a WhatsApp enquiry form fit together. Your version uses your name, photos, prices and location.</p>
    <ul><li>Quick-answer block and FAQ written for Google and AI assistants</li><li>Services such as {e(svc_text)}</li><li>Sticky call and WhatsApp bar on mobile</li><li>Google Maps, opening hours and enquiry form</li></ul>
    <div class="btns"><a class="btn btn-p" href="{root}{ind['demo']}/" data-ev="demo_open" data-demo="{ind['demo']}">View Live Website →</a><a class="btn btn-o" data-wa="{get_msg}" data-ev="get_design" data-demo="{ind['demo']}" href="#">Get This Design</a><a class="btn btn-o" data-wa="{cust_msg}" data-ev="request_customisation" data-demo="{ind['demo']}" href="#">Request Customisation</a></div></div>
  <a class="shotcard rv" href="{root}{ind['demo']}/" data-ev="demo_open" data-demo="{ind['demo']}" tabindex="-1" aria-hidden="true"><div class="bar"><i></i><i></i><i></i><span>{e(ind['demo'])}.qrenzy.com</span></div><img src="{root}assets/thumbs/{ind['demo']}.jpg" width="960" height="600" loading="lazy" decoding="async" alt=""><p>Sample content for demonstration {ARROW}</p></a>
</div></section>

<section aria-labelledby="p-h"><div class="container">
  <div class="sec-head center"><span class="eyebrow">✦ Pricing</span><h2 id="p-h">Website packages for {e(ind['name'].lower())}</h2><p>*Introductory pricing, not a final quotation. Includes the first-year domain and hosting. Optional care plan: ₹1,000 a month for up to 8 hours of updates and support. <a href="{root}#pricing" style="color:var(--red);font-weight:700;text-decoration:underline">See what is included and what is quoted separately →</a></p></div>
  <div class="plans mini">{plans}</div>
</div></section>

<section class="warm" id="faq" aria-labelledby="f-h"><div class="container">
  <div class="sec-head center"><span class="eyebrow">✦ FAQ</span><h2 id="f-h">Questions {e(ind['name'].lower())} ask us</h2></div>
  <div class="faq">{faq}</div>
</div></section>

<section aria-labelledby="r-h"><div class="container">
  <div class="sec-head"><span class="eyebrow">✦ Related guides</span><h2 id="r-h">More website guides</h2></div>
  <div class="rel">{rel}</div>
</div></section>

<section class="cta-band"><div class="container"><div class="cta-box rv">
  <div><h2>Ready for a {e(ind['short'].lower())} website that wins customers?</h2><p>Tell us about your business. We'll customise this design for you.</p></div>
  <a class="btn" data-wa="{cust_msg}" data-ev="request_customisation" data-demo="{ind['demo']}" href="#">{WA_SVG} Request Customisation</a>
</div></div></section>
</main>
{footer(root, hub)}"""
    return body


def build_hub(demos):
    url = DOMAIN + "/websites-for/"
    title = "Website Design for Every Industry in Kerala | Qrenzy"
    desc = f"Website design guides for {len(INDS)} industries in Kerala: clinics, gyms, restaurants, real estate, jewellery and more. Live demos and pricing from ₹5,000."
    items = [{"@type": "ListItem", "position": i, "url": f"{DOMAIN}/websites-for/{ind['url']}/", "name": f"Website design for {ind['name'].lower()}"} for i, ind in enumerate(INDS, 1)]
    ld = {"@context": "https://schema.org", "@graph": [
        ORG,
        {"@type": "CollectionPage", "@id": url + "#page", "url": url, "name": title, "description": desc, "inLanguage": "en-IN", "isPartOf": {"@id": WEBSITE_ID},
         "mainEntity": {"@type": "ItemList", "numberOfItems": len(INDS), "itemListElement": items}},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Qrenzy website demos", "item": DOMAIN + "/"},
                                                         {"@type": "ListItem", "position": 2, "name": "Website design by industry", "item": url}]}]}
    groups = ""
    for _, gname, slugs in GROUPS:
        cards = "".join(f'<a class="rv" href="{NAME_OF[s]["url"]}/"><b>{e(NAME_OF[s]["name"])}</b><span>{e(NAME_OF[s]["kf"][:1].upper() + NAME_OF[s]["kf"][1:])}.</span><i>Read the guide →</i></a>' for s in slugs)
        groups += f'<div class="hubg"><h2>{e(gname)}</h2><div class="hubgrid">{cards}</div></div>'
    return head(title, desc, url, 1, DOMAIN + "/assets/thumbs/gym.jpg") + f"""<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{LCSS}{EXTRA_CSS}</style>
</head>
<body>
{header('../', './')}
<main id="main">
<section class="hero hero--ind"><div class="container">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="../">Qrenzy demos</a><span>/</span><span style="opacity:1;color:var(--ink);font-weight:700">Industries</span></nav>
  <p class="kicker"><span></span>Website design guides</p>
  <h1 style="max-width:900px">Website Design for <em>Every Industry</em> in Kerala</h1>
  <p class="lead" style="max-width:720px">Each guide explains what customers in that industry search for, what the website needs and the mistakes to avoid, with a live demo you can open on your phone. Websites start at ₹5,000*, including the first-year domain and hosting.</p>
  <p class="fine">*Introductory pricing, not a final quotation. Typical launch is 48 hours after we receive all content and approvals.</p>
  {groups}
</div></section>
<section class="cta-band"><div class="container"><div class="cta-box rv">
  <div><h2>Don't see your industry?</h2><p>Tell us what you do. We'll design a website that fits.</p></div>
  <a class="btn" data-wa="Hi Qrenzy, I need a website for my business type." data-ev="request_demo" href="#">{WA_SVG} Chat on WhatsApp</a>
</div></div></section>
</main>
{footer('../', './')}"""
