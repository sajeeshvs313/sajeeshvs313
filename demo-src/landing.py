"""demo.qrenzy.com landing page: grid of all demos, SEO + AEO ready."""
import html, json, os
from template import DOMAIN, WA_SVG, ARROW, PHONE_SVG, e

GROUPS = [
    ("health", "Health & Fitness", ["gym", "clinic", "dental", "yoga", "pet-care"]),
    ("food", "Food & Stay", ["restaurant", "homestay"]),
    ("home", "Home & Property", ["real-estate", "interior", "landscaping", "cleaning", "pest-control", "solar"]),
    ("events", "Events & Creative", ["auditorium", "wedding", "photography", "beauty"]),
    ("pro", "Education & Pro", ["tuition", "accounting"]),
    ("auto", "Auto & Industry", ["car-care", "crane"]),
]
SLUG_GROUP = {s: (k, n) for k, n, ss in GROUPS for s in ss}

FAQ = [
    ("What is demo.qrenzy.com?", "demo.qrenzy.com is a showcase of 21 ready-made website designs by Qrenzy Digital Solutions for local businesses such as gyms, clinics, dental clinics, restaurants, real estate agents, crane services and cleaning companies. Each demo is a fully working sample you can open on your phone."),
    ("How much does a business website cost in Kerala?", "A professional business website from Qrenzy Digital Solutions starts at ₹5,000 for a single-page lead website, with monthly care plans from ₹1,000 (sample pricing). The final price depends on pages, features and content."),
    ("How long does it take to build a website?", "Most demo-based websites go live in about 48 hours once we have your logo, photos, services and contact details."),
    ("Will my website show up on Google?", "Every site is built with SEO and AEO foundations: a unique title and description, structured data (LocalBusiness, FAQ), mobile-first speed and clear question-and-answer content that search engines and AI assistants can read. Rankings also depend on your competition, content and Google Business Profile."),
    ("Can you customise a demo for my business?", "Yes. Pick any demo, send us your business name, services, prices, photos and location, and we will customise colours, content and structured data for your business."),
    ("Do I own my website?", "Yes. Your domain and website files belong to you. We can host the site on fast, free-to-run static hosting and hand over all files if you ever want to move."),
]
INCLUDES = [
    ("🔎", "SEO-ready structure", "Unique titles and descriptions, clean headings, canonical tags and LocalBusiness schema on every page."),
    ("🤖", "AEO question-and-answer content", "Quick-answer blocks and FAQ markup so AI assistants and Google can quote your business."),
    ("📱", "Mobile-first design", "Fast, thumb-friendly layouts with a sticky call and WhatsApp bar on phones."),
    ("💬", "WhatsApp lead form", "Enquiries land in your WhatsApp with name, phone and requirement filled in."),
    ("⚡", "Fast and lightweight", "No heavy plugins. Pages load quickly on 4G and keep visitors engaged."),
    ("♿", "Accessible by default", "Keyboard friendly, readable contrast and reduced-motion support."),
]
PLANS = [
    ("Starter", "Single-page lead website", "5,000", ["1 page with enquiry form", "WhatsApp & call buttons", "Mobile-first design", "Basic on-page SEO"], False),
    ("Business", "Most popular", "12,000", ["Complete website, 6 sections", "Full SEO + FAQ schema", "Google Maps & hours", "Free first-month care"], True),
    ("Growth", "Lead generation", "25,000", ["Everything in Business", "Google Business Profile setup", "Ad-ready landing pages", "Monthly report & updates"], False),
]


def build_landing(sites):
    n = len(sites)
    cards = []
    items = []
    for i, s in enumerate(sites, 1):
        gk, gn = SLUG_GROUP[s["slug"]]
        short = s["desc"].split(": ", 1)[-1] if ": " in s["desc"] else s["desc"]
        short = (short[:118].rsplit(" ", 1)[0] + "…") if len(short) > 120 else short
        short = short[0].upper() + short[1:]
        url = f"{DOMAIN}/{s['slug']}/"
        items.append({"@type": "ListItem", "position": i, "url": url, "name": f"{s['cat']} website demo"})
        cards.append(
            f'<li class="dcard rv" data-g="{gk}" data-q="{e((s["cat"] + " " + s["name"] + " " + gn).lower())}">'
            f'<a href="{s["slug"]}/" aria-label="View {e(s["cat"])} website demo">'
            f'<div class="shot"><div class="bar"><i></i><i></i><i></i><span>{e(s["slug"])}.qrenzy.com</span></div>'
            f'<img src="assets/thumbs/{s["slug"]}.jpg" width="960" height="600" loading="{"eager" if i <= 3 else "lazy"}" decoding="async" '
            f'alt="{e(s["cat"])} website demo preview: {e(s["name"])}"></div>'
            f'<div class="meta"><span class="tag" style="--c:{s["acc"]}">{s["emoji"]} {e(s["cat"])}</span>'
            f'<h3>{e(s["name"])}</h3><p>{e(short)}</p>'
            f'<span class="go">View live demo {ARROW}</span></div></a></li>')
    chips = '<button class="chip on" data-f="all" type="button">All <b>%d</b></button>' % n + "".join(
        f'<button class="chip" data-f="{k}" type="button">{e(nm)} <b>{len(ss)}</b></button>' for k, nm, ss in GROUPS)
    inc = "".join(f'<article class="inc rv"><div class="ico" aria-hidden="true">{i}</div><h3>{e(t)}</h3><p>{e(d)}</p></article>' for i, t, d in INCLUDES)
    plans = "".join(
        f'<article class="plan rv{" pop" if pop else ""}">{"<span class=ptag>MOST POPULAR</span>" if pop else ""}<h3>{e(nm)}</h3><p class="for">{e(fr)}</p>'
        f'<div class="price"><sup>₹</sup>{pr}<small> one-time</small></div><ul>{"".join(f"<li>{e(x)}</li>" for x in fe)}</ul>'
        f'<a class="btn {"btn-p" if pop else "btn-o"}" data-wa="Hi, I am interested in the {e(nm)} website package." href="#">Choose {e(nm)}</a></article>'
        for nm, fr, pr, fe, pop in PLANS)
    faq = "".join(f'<details class="rv"><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in FAQ)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "ProfessionalService", "@id": "https://www.qrenzy.com/#org", "name": "Qrenzy Digital Solutions", "url": "https://www.qrenzy.com",
         "telephone": "+919905700600", "areaServed": "India", "address": {"@type": "PostalAddress", "addressRegion": "Kerala", "addressCountry": "IN"},
         "description": "Digital marketing and website design for local businesses in Kerala.",
         "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Business website design"}, "priceCurrency": "INR", "price": "5000"}]},
        {"@type": "WebSite", "@id": DOMAIN + "/#website", "url": DOMAIN + "/", "name": "Qrenzy Website Demos", "publisher": {"@id": "https://www.qrenzy.com/#org"}, "inLanguage": "en-IN"},
        {"@type": "CollectionPage", "@id": DOMAIN + "/#page", "url": DOMAIN + "/", "name": "Website demos for local businesses", "isPartOf": {"@id": DOMAIN + "/#website"},
         "mainEntity": {"@type": "ItemList", "numberOfItems": n, "itemListElement": items}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Qrenzy Digital Solutions", "item": "https://www.qrenzy.com"},
                                                         {"@type": "ListItem", "position": 2, "name": "Website demos", "item": DOMAIN + "/"}]},
    ]}
    title = f"{n} Website Demos for Local Businesses | Qrenzy Digital"
    desc = f"Browse {n} ready-made website demos for gyms, clinics, restaurants, real estate, crane services and more. Business websites from ₹5,000, live in 48 hours."
    return f"""<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<link rel="canonical" href="{DOMAIN}/">
<link rel="alternate" hreflang="en-IN" href="{DOMAIN}/">
<meta name="theme-color" content="#EE1E24">
<meta property="og:type" content="website"><meta property="og:site_name" content="Qrenzy Digital Solutions">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{DOMAIN}/"><meta property="og:locale" content="en_IN">
<meta property="og:image" content="{DOMAIN}/assets/thumbs/gym.jpg">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(desc)}">
<link rel="icon" href="logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#demos">Skip to demos</a>
<header class="site"><div class="container nav">
  <a href="./" aria-label="Qrenzy Digital Solutions"><img class="logo" src="logo.png" alt="Qrenzy Digital Solutions" width="150" height="52"></a>
  <nav aria-label="Main"><ul class="menu" id="menu"><li><a href="#demos">Demos</a></li><li><a href="#included">What's included</a></li><li><a href="#pricing">Pricing</a></li><li><a href="#faq">FAQ</a></li></ul></nav>
  <div class="nav-cta"><a class="btn btn-p btn-sm" data-wa="Hi Qrenzy, I want a website for my business." href="#">{WA_SVG} Get my website</a>
  <button class="burger" id="burger" aria-label="Menu" aria-expanded="false" aria-controls="menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button></div>
</div></header>

<main id="main">
<section class="hero"><div class="container">
  <span class="badge"><b>{n} LIVE DEMOS</b> Open any demo on your phone</span>
  <h1>Websites that bring you <em>real customers</em></h1>
  <p class="lead">Qrenzy Digital Solutions builds fast, SEO-ready websites for local businesses in Kerala. Pick a design below, see it live, and get your own website in 48 hours, from ₹5,000.</p>
  <div class="hero-cta"><a class="btn btn-p" href="#demos">Browse {n} demos {ARROW}</a><a class="btn btn-w" data-wa="Hi Qrenzy, I want a free demo for my business." href="#">{WA_SVG} Get a free demo</a></div>
  <ul class="kpis"><li><b>{n}</b><span>Industry demos</span></li><li><b>48 hrs</b><span>Typical go-live</span></li><li><b>₹5,000</b><span>Websites from</span></li><li><b>SEO + AEO</b><span>Built into every page</span></li></ul>
</div></section>

<section id="demos" aria-labelledby="demos-h"><div class="container">
  <div class="sec-head"><span class="eyebrow">Demo gallery</span><h2 id="demos-h">Choose a design that fits your business</h2><p>Every demo is a complete, working website with services, pricing, FAQ, map and WhatsApp enquiry form. Tap a card to open it.</p></div>
  <div class="tools"><div class="chips" role="group" aria-label="Filter demos by industry">{chips}</div>
    <label class="search"><span class="sr">Search demos</span><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg><input id="q" type="search" placeholder="Search e.g. dental, crane, solar" autocomplete="off"></label></div>
  <p class="count" id="count" aria-live="polite">Showing all {n} demos</p>
  <ul class="grid" id="grid">{"".join(cards)}</ul>
  <p class="empty" id="empty" hidden>No demo matches your search. <a href="#" data-wa="Hi Qrenzy, I need a website for my business type.">Ask us for a custom design</a>.</p>
</div></section>

<section class="alt" id="included" aria-labelledby="inc-h"><div class="container">
  <div class="sec-head center"><span class="eyebrow">Included in every website</span><h2 id="inc-h">Built to be found, trusted and contacted</h2><p>Good design is only half the job. Every demo ships with the technical foundations that help you rank and convert.</p></div>
  <div class="incs">{inc}</div>
</div></section>

<section aria-labelledby="how-h"><div class="container">
  <div class="sec-head center"><span class="eyebrow">How it works</span><h2 id="how-h">From demo to live website in 3 steps</h2></div>
  <ol class="steps"><li class="step rv"><h3>Pick a demo</h3><p>Choose the design closest to your business, or ask for a custom one.</p></li><li class="step rv"><h3>Share your details</h3><p>Send your logo, photos, services, prices and location on WhatsApp.</p></li><li class="step rv"><h3>Go live in 48 hours</h3><p>We customise, connect your domain and launch. You get all the files.</p></li></ol>
</div></section>

<section class="alt" id="pricing" aria-labelledby="pr-h"><div class="container">
  <div class="sec-head center"><span class="eyebrow">Pricing</span><h2 id="pr-h">Simple website packages</h2><p>Sample pricing. Monthly care plans from ₹1,000 cover updates, backups and support.</p></div>
  <div class="plans">{plans}</div>
</div></section>

<section id="faq" aria-labelledby="faq-h"><div class="container">
  <div class="sec-head center"><span class="eyebrow">FAQ</span><h2 id="faq-h">Questions we get asked often</h2></div>
  <div class="faq">{faq}</div>
</div></section>

<section class="cta-band"><div class="container"><div class="cta-box rv">
  <div><h2>Ready to get your business online?</h2><p>Tell us your business type. We'll send a free demo built for you.</p></div>
  <a class="btn" data-wa="Hi Qrenzy, I want a free demo for my business." href="#">{WA_SVG} Chat on WhatsApp</a>
</div></div></section>
</main>

<footer><div class="container">
  <div class="fgrid">
    <div><img class="logo" src="logo.png" alt="Qrenzy Digital Solutions" width="150" height="52" style="filter:brightness(0) invert(1)"><p>Qrenzy Digital Solutions builds websites and digital marketing for local businesses in Kerala.</p></div>
    <div><h3>Explore</h3><ul><li><a href="#demos">All demos</a></li><li><a href="#included">What's included</a></li><li><a href="#pricing">Pricing</a></li><li><a href="#faq">FAQ</a></li></ul></div>
    <div><h3>Contact</h3><ul><li><a data-tel href="#">+91 99057 00600</a></li><li><a href="https://www.qrenzy.com" rel="noopener">www.qrenzy.com</a></li><li>Instagram @sajeeshvs313</li></ul></div>
  </div>
  <div class="fbar"><span>© <span id="yr"></span> Qrenzy Digital Solutions. Demo sites use sample content.</span><span>Kochi, Kerala, India</span></div>
</div></footer>

<nav class="mbar" aria-label="Quick actions"><a class="c" data-tel href="#">{PHONE_SVG} Call</a><a class="w" data-wa="Hi Qrenzy, I want a free demo for my business." href="#">{WA_SVG} WhatsApp</a></nav>
<script>{JS}</script>
</body>
</html>
"""


CSS = r"""
:root{--red:#EE1E24;--red-d:#b3121a;--ink:#25262A;--grey:#58595B;--muted:#6b6f78;--blush:#fff1f1;--bg:#fff;--line:#eadede;--wa:#1faa59;
 --font-head:'Sora',system-ui,sans-serif;--font-body:'Plus Jakarta Sans',system-ui,sans-serif;--r:22px;--shadow:0 1px 2px rgba(37,38,42,.05),0 18px 40px -16px rgba(37,38,42,.2)}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:84px}
body{font-family:var(--font-body);color:var(--ink);background:var(--bg);line-height:1.65;-webkit-font-smoothing:antialiased}
h1,h2,h3{font-family:var(--font-head);line-height:1.12;letter-spacing:-.025em;font-weight:700}
img,svg{display:block;max-width:100%}a{color:inherit;text-decoration:none}ul,ol{list-style:none}
:focus-visible{outline:3px solid var(--red);outline-offset:3px;border-radius:8px}
.container{width:min(1200px,100% - 40px);margin-inline:auto}
.skip{position:absolute;left:-999px;top:8px;background:var(--ink);color:#fff;padding:10px 16px;border-radius:10px;z-index:100}.skip:focus{left:12px}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
section{padding:clamp(56px,8vw,100px) 0}
.alt{background:linear-gradient(180deg,#fff7f7,#fff)}
.eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:12.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--red)}
.eyebrow:before{content:"";width:22px;height:2px;background:var(--red);border-radius:2px}
h2{font-size:clamp(28px,4vw,44px);margin-top:12px}
.sec-head{max-width:700px;margin-bottom:38px}.sec-head p{color:var(--muted);margin-top:14px;font-size:17px}
.sec-head.center{margin-inline:auto;text-align:center}.sec-head.center .eyebrow{justify-content:center}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:50px;padding:0 26px;border-radius:999px;font-weight:700;font-size:15px;border:1.5px solid transparent;cursor:pointer;font-family:inherit;transition:transform .18s,box-shadow .18s;white-space:nowrap}
.btn svg{width:18px;height:18px}.btn:hover{transform:translateY(-2px)}
.btn-p{background:linear-gradient(135deg,var(--red),#ff4a50);color:#fff;box-shadow:0 14px 30px -10px rgba(238,30,36,.6)}
.btn-o{background:#fff;color:var(--ink);border-color:var(--line)}.btn-o:hover{border-color:var(--red)}
.btn-w{background:var(--wa);color:#fff;box-shadow:0 14px 30px -12px rgba(31,170,89,.7)}
.btn-sm{min-height:42px;padding:0 20px;font-size:14px}
header.site{position:sticky;top:0;z-index:60;background:rgba(255,255,255,.86);backdrop-filter:saturate(1.6) blur(16px);-webkit-backdrop-filter:saturate(1.6) blur(16px);border-bottom:1px solid var(--line)}
.nav{display:flex;align-items:center;justify-content:space-between;height:72px;gap:20px}
.logo{height:46px;width:auto}
.menu{display:flex;gap:6px;font-weight:600;font-size:14.5px;color:var(--grey)}
.menu a{padding:9px 14px;border-radius:999px;transition:.15s}.menu a:hover{background:var(--blush);color:var(--red)}
.nav-cta{display:flex;gap:10px;align-items:center}
.burger{display:none;width:44px;height:44px;border-radius:12px;border:1.5px solid var(--line);background:#fff;cursor:pointer;place-items:center;color:var(--ink)}.burger svg{width:22px;height:22px}
.hero{padding:clamp(48px,7vw,96px) 0 clamp(40px,5vw,70px);background:radial-gradient(900px 480px at 85% -10%,rgba(238,30,36,.14),transparent 62%),radial-gradient(600px 400px at 0% 80%,rgba(238,30,36,.07),transparent 70%),#fff;text-align:center}
.badge{display:inline-flex;align-items:center;gap:10px;padding:7px 16px 7px 8px;border-radius:999px;background:#fff;border:1px solid var(--line);font-size:13px;font-weight:600;box-shadow:var(--shadow)}
.badge b{background:var(--red);color:#fff;padding:3px 11px;border-radius:999px;font-size:11.5px;letter-spacing:.06em}
h1{font-size:clamp(36px,6.4vw,74px);margin:22px auto 20px;max-width:900px;letter-spacing:-.035em}
h1 em{font-style:normal;color:var(--red)}
.lead{font-size:clamp(17px,1.7vw,20px);color:var(--grey);max-width:680px;margin-inline:auto}
.hero-cta{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-top:30px}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;max-width:860px;margin:44px auto 0}
.kpis li{background:#fff;border:1px solid var(--line);border-radius:18px;padding:18px 12px;box-shadow:var(--shadow)}
.kpis b{display:block;font-family:var(--font-head);font-size:clamp(22px,3vw,30px);color:var(--red);letter-spacing:-.02em;line-height:1.1}
.kpis span{font-size:13.5px;color:var(--muted);font-weight:500}
.tools{display:flex;gap:16px;justify-content:space-between;align-items:center;flex-wrap:wrap;margin-bottom:12px}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{border:1.5px solid var(--line);background:#fff;color:var(--ink);padding:9px 16px;border-radius:999px;font:600 14px var(--font-body);cursor:pointer;transition:.15s}
.chip b{font-weight:700;color:var(--muted);margin-left:4px;font-size:12.5px}
.chip:hover{border-color:var(--red)}.chip.on{background:var(--ink);border-color:var(--ink);color:#fff}.chip.on b{color:#ffb3b5}
.search{display:flex;align-items:center;gap:10px;border:1.5px solid var(--line);background:#fff;border-radius:999px;padding:0 18px;min-height:46px;min-width:min(100%,300px);transition:.15s}
.search:focus-within{border-color:var(--red);box-shadow:0 0 0 4px rgba(238,30,36,.12)}
.search svg{width:18px;height:18px;color:var(--muted);flex:none}
.search input{border:0;outline:0;font:500 15px var(--font-body);width:100%;background:transparent;color:var(--ink)}
.count{font-size:13.5px;color:var(--muted);margin:14px 2px 18px;font-weight:500}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.dcard a{display:flex;flex-direction:column;height:100%;background:#fff;border:1px solid var(--line);border-radius:var(--r);overflow:hidden;transition:transform .25s,box-shadow .25s,border-color .25s}
.dcard a:hover{transform:translateY(-6px);box-shadow:var(--shadow);border-color:rgba(238,30,36,.4)}
.shot{background:#f1f1f3;border-bottom:1px solid var(--line)}
.shot .bar{height:28px;display:flex;align-items:center;gap:6px;padding:0 12px;background:#f6f6f8}
.shot .bar i{width:9px;height:9px;border-radius:50%;background:#d4d4d9}.shot .bar i:nth-child(1){background:#ff5f56}.shot .bar i:nth-child(2){background:#ffbd2e}.shot .bar i:nth-child(3){background:#27c93f}
.shot .bar span{margin-left:8px;font-size:11.5px;color:var(--muted);background:#fff;border-radius:999px;padding:2px 12px}
.shot img{width:100%;height:auto;aspect-ratio:8/5;object-fit:cover;object-position:top;transition:transform .5s}
.dcard a:hover .shot img{transform:scale(1.04)}
.shot{overflow:hidden}
.meta{padding:20px 22px 22px;display:flex;flex-direction:column;gap:8px;flex:1}
.tag{align-self:flex-start;font-size:12px;font-weight:700;padding:5px 12px;border-radius:999px;background:color-mix(in srgb,var(--c) 12%,#fff);color:color-mix(in srgb,var(--c) 75%,#000)}
.meta h3{font-size:20px}.meta p{font-size:14.5px;color:var(--muted)}
.go{margin-top:auto;padding-top:6px;font-weight:700;font-size:14.5px;color:var(--red);display:inline-flex;align-items:center;gap:8px}
.go svg{width:17px;height:17px;transition:transform .2s}.dcard a:hover .go svg{transform:translateX(5px)}
.empty{text-align:center;color:var(--muted);padding:40px 0}.empty a{color:var(--red);font-weight:700;text-decoration:underline}
.incs{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.inc{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:28px}
.ico{width:54px;height:54px;border-radius:16px;background:var(--blush);display:grid;place-items:center;font-size:27px;margin-bottom:14px}
.inc h3{font-size:19px}.inc p{color:var(--muted);font-size:15px;margin-top:8px}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;counter-reset:s;max-width:980px;margin-inline:auto}
.step{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:28px}
.step:before{counter-increment:s;content:counter(s);display:grid;place-items:center;width:44px;height:44px;border-radius:50%;background:var(--red);color:#fff;font-weight:800;margin-bottom:16px}
.step h3{font-size:19px}.step p{color:var(--muted);margin-top:6px;font-size:15px}
.plans{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;max-width:1040px;margin-inline:auto}
.plan{background:#fff;border:1px solid var(--line);border-radius:26px;padding:34px 28px;display:flex;flex-direction:column;position:relative}
.plan.pop{border:2px solid var(--red);box-shadow:0 30px 60px -30px rgba(238,30,36,.5);transform:translateY(-10px)}
.ptag{position:absolute;top:-14px;left:28px;background:var(--red);color:#fff;font-size:11.5px;font-weight:800;letter-spacing:.1em;padding:5px 14px;border-radius:999px}
.plan h3{font-size:22px}.plan .for{color:var(--muted);font-size:14px}
.price{font-family:var(--font-head);font-size:50px;font-weight:800;letter-spacing:-.03em;margin:18px 0 4px;line-height:1}
.price sup{font-size:.45em;vertical-align:top;position:relative;top:.35em;margin-right:2px}.price small{font:500 14px var(--font-body);color:var(--muted);letter-spacing:0}
.plan ul{margin:22px 0 28px;display:grid;gap:11px;font-size:15px;flex:1}.plan li{display:flex;gap:10px}.plan li:before{content:"✓";color:var(--red);font-weight:800}
.faq{max-width:820px;margin-inline:auto;display:grid;gap:12px}
details{background:#fff;border:1px solid var(--line);border-radius:16px;padding:0 22px;transition:.2s}
details[open]{border-color:rgba(238,30,36,.4);box-shadow:var(--shadow)}
summary{cursor:pointer;list-style:none;padding:20px 0;font:700 17px var(--font-head);display:flex;justify-content:space-between;gap:16px;align-items:center;letter-spacing:-.01em}
summary::-webkit-details-marker{display:none}
summary:after{content:"+";flex:0 0 30px;height:30px;border-radius:50%;background:var(--blush);color:var(--red);display:grid;place-items:center;font-size:20px;font-weight:700}
details[open] summary:after{content:"–";background:var(--red);color:#fff}
details p{padding:0 0 22px;color:var(--muted);font-size:15.5px}
.cta-band{padding:0 0 clamp(56px,8vw,100px)}
.cta-box{border-radius:32px;padding:clamp(34px,5vw,60px);background:radial-gradient(60% 120% at 100% 0%,rgba(255,120,120,.5),transparent 70%),linear-gradient(135deg,var(--red),var(--red-d));color:#fff;display:flex;justify-content:space-between;gap:28px;align-items:center;flex-wrap:wrap}
.cta-box h2{font-size:clamp(26px,3.6vw,40px);margin:0}.cta-box p{opacity:.92;margin-top:10px;max-width:520px}.cta-box .btn{background:#fff;color:var(--ink)}
footer{background:var(--ink);color:#d9dbe1;padding:60px 0 100px;border-top:5px solid var(--red)}
.fgrid{display:grid;grid-template-columns:1.6fr 1fr 1fr;gap:36px}
footer h3{font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:#fff;margin-bottom:14px}
footer li{margin:8px 0;font-size:14.5px}footer a:hover{color:#fff;text-decoration:underline}footer p{font-size:14.5px;color:#a8acb7;margin-top:14px;max-width:340px}
.fbar{margin-top:40px;padding-top:22px;border-top:1px solid rgba(255,255,255,.12);display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;font-size:13.5px;color:#9096a3}
.mbar{display:none;position:fixed;left:12px;right:12px;bottom:12px;z-index:70;background:#fff;border:1px solid var(--line);border-radius:20px;padding:8px;gap:8px;box-shadow:0 18px 44px -10px rgba(0,0,0,.35)}
.mbar a{flex:1;min-height:46px;border-radius:14px;display:flex;align-items:center;justify-content:center;gap:8px;font-weight:700;font-size:14.5px}.mbar a svg{width:18px;height:18px}
.mbar .c{background:#f4f4f6}.mbar .w{background:var(--wa);color:#fff}
html.js .rv{opacity:0;transform:translateY(18px);transition:opacity .6s ease,transform .6s ease}html.js .rv.in{opacity:1;transform:none}
.dcard[hidden]{display:none}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}html.js .rv{opacity:1;transform:none;transition:none}.dcard a,.shot img{transition:none}}
@media(max-width:1020px){.menu,.nav-cta .btn{display:none}.burger{display:grid}
 .menu.open{display:flex;flex-direction:column;position:absolute;left:0;right:0;top:72px;background:#fff;padding:14px 20px 22px;border-bottom:1px solid var(--line);box-shadow:var(--shadow)}.menu.open a{padding:14px;font-size:16px}
 .grid{grid-template-columns:1fr 1fr}.incs{grid-template-columns:1fr 1fr}.plan.pop{transform:none}}
@media(max-width:680px){.grid,.incs,.steps,.plans,.fgrid{grid-template-columns:1fr}.kpis{grid-template-columns:1fr 1fr}.mbar{display:flex}footer{padding-bottom:120px}.hero-cta .btn{flex:1 1 100%}.tools{flex-direction:column;align-items:stretch}.search{width:100%}}
"""

JS = r"""
(function(){var d=document,r=d.documentElement;r.classList.add('js');var NUM='919905700600';
var wa=function(t){return 'https://wa.me/'+NUM+'?text='+encodeURIComponent(t)};
d.querySelectorAll('[data-wa]').forEach(function(a){a.href=wa(a.getAttribute('data-wa'));a.target='_blank';a.rel='noopener'});
d.querySelectorAll('[data-tel]').forEach(function(a){a.href='tel:+'+NUM;if(!a.classList.contains('c'))a.textContent='+91 99057 00600'});
d.getElementById('yr').textContent=new Date().getFullYear();
var b=d.getElementById('burger'),mn=d.getElementById('menu');
b.addEventListener('click',function(){var o=mn.classList.toggle('open');b.setAttribute('aria-expanded',o)});
mn.addEventListener('click',function(e){if(e.target.tagName==='A'){mn.classList.remove('open');b.setAttribute('aria-expanded','false')}});
var els=d.querySelectorAll('.rv');
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.1,rootMargin:'0px 0px -30px 0px'});els.forEach(function(e){io.observe(e)})}else{els.forEach(function(e){e.classList.add('in')})}
var cards=[].slice.call(d.querySelectorAll('.dcard')),chips=[].slice.call(d.querySelectorAll('.chip')),q=d.getElementById('q'),cnt=d.getElementById('count'),emp=d.getElementById('empty'),f='all';
function apply(){var t=q.value.trim().toLowerCase(),n=0;cards.forEach(function(c){var ok=(f==='all'||c.dataset.g===f)&&(!t||c.dataset.q.indexOf(t)>-1);c.hidden=!ok;if(ok){n++;c.classList.add('in')}});
cnt.textContent=(n===cards.length?'Showing all '+n+' demos':'Showing '+n+' of '+cards.length+' demos');emp.hidden=n!==0}
chips.forEach(function(c){c.addEventListener('click',function(){chips.forEach(function(x){x.classList.remove('on')});c.classList.add('on');f=c.dataset.f;apply()})});
q.addEventListener('input',apply);
})();
"""
