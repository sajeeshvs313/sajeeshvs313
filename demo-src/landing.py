"""demo.qrenzy.com landing page in the qrenzy.com visual style. SEO + AEO ready."""
import json
from template import DOMAIN, WA_SVG, ARROW, PHONE_SVG, e

GROUPS = [
    ("health", "Health & Fitness", ["gym", "clinic", "dental", "yoga", "pet-care"]),
    ("food", "Food, Stay & Travel", ["restaurant", "homestay", "travel"]),
    ("home", "Home, Property & Construction", ["real-estate", "interior", "landscaping", "cleaning", "pest-control", "solar", "crane"]),
    ("events", "Events & Creative", ["auditorium", "wedding", "photography"]),
    ("retail", "Retail & Fashion", ["jewellery", "fashion", "ecommerce", "beauty"]),
    ("pro", "Education & Professional", ["tuition", "accounting", "legal", "finance-insurance"]),
    ("tech", "Tech, Industry & Auto", ["it-software", "manufacturing", "corporate-b2b", "car-care"]),
]
SLUG_GROUP = {s: (k, n) for k, n, ss in GROUPS for s in ss}

# the 15 industries on www.qrenzy.com and the demo that represents each
ADDRESS = "Medical College Road, Kodankandan Jn, Deepti Nagar, Mundur P.O., Thrissur – 680541"
MAPS_QUERY = "Qrenzy Digital Solutions, Medical College Road, Kodankandan Junction, Deepti Nagar, Mundur, Thrissur 680541"
MAPS_LINK = "https://www.google.com/maps/search/?api=1&query=" + MAPS_QUERY.replace(" ", "+").replace(",", "%2C")
INCLUDED = ["Domain name for the first year (.com or .in)", "Website design and setup on managed hosting (first year)", "SSL certificate and mobile-first layout", "On-page SEO and structured data as per package", "WhatsApp enquiry form and Google Maps embed", "Handover of your website files"]
EXCLUDED = ["Domain and hosting renewal: ₹5,000 per year, from the second year", "Optional care plan: ₹1,000 per month for up to 8 hours of updates and support, when required", "Business email (Zoho Mail): one-time setup ₹500 per mailbox with 5 GB. 10 GB mailbox: ₹1,800, renewed yearly", "Product or shop photography by us: available at an extra charge, quoted on request", "Extensive content writing beyond the details you supply", "Paid advertising budgets"]
INDUSTRIES = [
    ("💎", "Jewellery & Retail", "jewellery"), ("🏥", "Healthcare & Clinics", "clinic"), ("🏫", "Education & Coaching", "tuition"),
    ("🏗️", "Real Estate", "real-estate"), ("🍽️", "Restaurants & F&B", "restaurant"), ("✈️", "Tourism & Hospitality", "travel"),
    ("🏭", "Manufacturing", "manufacturing"), ("💻", "IT & Software", "it-software"), ("👗", "Fashion & Lifestyle", "fashion"),
    ("🔧", "Professional Services", "legal"), ("🛒", "E-commerce", "ecommerce"), ("🏢", "Corporate & B2B", "corporate-b2b"),
    ("🚗", "Automotive", "car-care"), ("🏋️", "Fitness & Wellness", "gym"), ("🏦", "Finance & Insurance", "finance-insurance"),
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
TICKER = ["{n} LIVE DEMOS", "15 INDUSTRIES", "SEO + AEO READY", "WHATSAPP LEADS", "FAST LAUNCH", "MOBILE-FIRST DESIGN", "WEBSITES FROM ₹5,000", "FAQ & SCHEMA INCLUDED"]


def build_landing(sites):
    n = len(sites)
    faq_items = [
        ("What is demo.qrenzy.com?", f"demo.qrenzy.com is a showcase of {n} ready-made website designs by Qrenzy Digital Solutions, covering 15 industries such as jewellery, healthcare, real estate, restaurants, manufacturing, IT, fashion, e-commerce, automotive and finance. Each demo is a fully working sample you can open on your phone."),
        ("How much does a business website cost in Kerala?", "Websites from Qrenzy Digital Solutions start at ₹5,000 (introductory pricing, not a final quotation). This includes the website, a domain name for the first year and managed hosting for the first year. From the second year, domain and hosting renewal is ₹5,000 a year. An optional care plan is ₹1,000 a month for up to 8 hours of updates and support."),
        ("What is included in the website price?", "Every package includes design and setup, a domain name and managed hosting for the first year, SSL, a mobile-first layout, on-page SEO and structured data as per the package, a WhatsApp enquiry form, a Google Maps embed and handover of your website files. Business email, product or shop photography, extensive content writing and ad spend are separate."),
        ("What is the yearly renewal cost?", "From the second year, domain and hosting renewal is ₹5,000 per year. An optional care plan for updates and support is ₹1,000 per month, covering up to 8 hours a month, when required."),
        ("Do you offer product or shop photography?", "Yes. We can photograph your products or shop for your website at an extra charge, quoted on request. If you already have good photos, you can send them and we will use those at no extra cost."),
        ("Do you provide business email?", "Yes. We set up business email on Zoho Mail with a one-time setup charge of ₹500 per mailbox with 5 GB. A 10 GB mailbox is ₹1,800 and renews yearly."),
        ("How long does it take to build a website?", "A demo-based website typically launches in about 48 hours after we receive all required content (logo, photos, services, prices and contact details) and your approvals. Revisions, domain setup and larger websites can take longer, usually 5 to 10 days."),
        ("Will my website show up on Google?", "Every site is built with SEO and AEO foundations: a unique title and description, structured data (LocalBusiness, FAQ), mobile-first speed and clear question-and-answer content that search engines and AI assistants can read. Rankings also depend on competition, content and your Google Business Profile."),
        ("Can you customise a demo for my business?", "Yes. Pick any demo, send us your business name, services, prices, photos and location, and we will customise colours, content and structured data for your business."),
        ("Do I own my website?", "Yes. Your domain and website files belong to you. We can host the site on fast, free-to-run static hosting and hand over all files if you ever want to move."),
    ]
    cards, items = [], []
    for i, s in enumerate(sites, 1):
        gk, gn = SLUG_GROUP[s["slug"]]
        short = s["desc"].split(": ", 1)[-1] if ": " in s["desc"] else s["desc"]
        short = (short[:118].rsplit(" ", 1)[0] + "…") if len(short) > 120 else short
        short = short[0].upper() + short[1:]
        items.append({"@type": "ListItem", "position": i, "url": f"{DOMAIN}/{s['slug']}/", "name": f"{s['cat']} website demo"})
        gd = e(f"Hi Qrenzy, I am interested in getting this design: {s['cat']} demo, {s['name']} ({DOMAIN}/{s['slug']}/). Please share the details and next steps.")
        rc = e(f"Hi Qrenzy, I would like to customise the {s['cat']} demo ({s['name']}, {DOMAIN}/{s['slug']}/) for my business. My business name is: ")
        cards.append(
            f'<li class="dcard rv" data-g="{gk}" data-q="{e((s["cat"] + " " + s["name"] + " " + gn).lower())}"><article>'
            f'<a class="cover" href="{s["slug"]}/" data-ev="demo_open" aria-label="View {e(s["cat"])} website demo">'
            f'<div class="shot"><div class="bar"><i></i><i></i><i></i><span>{e(s["slug"])}.qrenzy.com</span></div>'
            f'<img src="assets/thumbs/{s["slug"]}.jpg" width="960" height="600" loading="{"eager" if i <= 3 else "lazy"}" decoding="async" '
            f'alt="{e(s["cat"])} website demo preview: {e(s["name"])}"></div>'
            f'<div class="meta"><span class="tag" style="--c:{s["acc"] if s.get("theme") != "dark" else s["acc2"]}">{s["emoji"]} {e(s["cat"])}</span>'
            f'<h3>{e(s["name"])}</h3><p>{e(short)}</p></div></a>'
            f'<div class="acts"><a class="view" href="{s["slug"]}/" data-ev="demo_open" data-demo="{s["slug"]}">View Live Website {ARROW}</a>'
            f'<div class="two"><a data-wa="{gd}" data-ev="get_design" data-demo="{s["slug"]}" href="#">Get This Design</a>'
            f'<a data-wa="{rc}" data-ev="request_customisation" data-demo="{s["slug"]}" href="#">Request Customisation</a></div></div></article></li>')
    chips = f'<button class="chip on" data-f="all" type="button">All <b>{n}</b></button>' + "".join(
        f'<button class="chip" data-f="{k}" type="button">{e(nm)} <b>{len(ss)}</b></button>' for k, nm, ss in GROUPS)
    inds = "".join(f'<a class="ind rv" href="{sl}/"><i aria-hidden="true">{em}</i><span>{e(nm)}</span>{ARROW}</a>' for em, nm, sl in INDUSTRIES)
    inc = "".join(f'<article class="inc rv"><div class="ico" aria-hidden="true">{i}</div><h3>{e(t)}</h3><p>{e(d)}</p></article>' for i, t, d in INCLUDES)
    plans = "".join(
        f'<article class="plan rv{" pop" if pop else ""}">{"<span class=ptag>MOST POPULAR</span>" if pop else ""}<h3>{e(nm)}</h3><p class="for">{e(fr)}</p>'
        f'<div class="price"><sup>₹</sup>{pr}<small> one-time*</small></div><ul>{"".join(f"<li>{e(x)}</li>" for x in fe)}</ul>'
        f'<a class="btn {"btn-p" if pop else "btn-o"}" data-wa="Hi, I am interested in the {e(nm)} website package." href="#">Choose {e(nm)}</a></article>'
        for nm, fr, pr, fe, pop in PLANS)
    faq = "".join(f'<details class="rv"><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in faq_items)
    tick = "".join(f"<span>{e(t.format(n=n))}</span><span class='st'>★</span>" for t in TICKER)
    opts = "".join(f"<option>{e(nm)}</option>" for _, nm, _ in INDUSTRIES) + "<option>Other</option>"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "ProfessionalService", "@id": "https://www.qrenzy.com/#org", "name": "Qrenzy Digital Solutions", "url": "https://www.qrenzy.com",
         "telephone": "+919905700600", "email": "info@qrenzy.com", "foundingDate": "2020",
         "address": {"@type": "PostalAddress", "streetAddress": "Medical College Road, Kodankandan Jn, Deepti Nagar, Mundur P.O.", "addressLocality": "Thrissur", "addressRegion": "Kerala", "postalCode": "680541", "addressCountry": "IN"}, "hasMap": MAPS_LINK,
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:30", "closes": "19:30"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "09:30", "closes": "18:00"}],
         "areaServed": ["India", "Oman", "United Arab Emirates", "Bahrain"],
         "description": "AI-powered digital marketing, SEO and website design agency in Thrissur, Kerala.",
         "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Business website design"}, "priceCurrency": "INR", "price": "5000", "description": "Introductory starting price. Includes first-year domain and hosting. Renewal, email and extras are quoted separately."}]},
        {"@type": "WebSite", "@id": DOMAIN + "/#website", "url": DOMAIN + "/", "name": "Qrenzy Website Demos", "publisher": {"@id": "https://www.qrenzy.com/#org"}, "inLanguage": "en-IN"},
        {"@type": "CollectionPage", "@id": DOMAIN + "/#page", "url": DOMAIN + "/", "name": "Website demos for local businesses", "isPartOf": {"@id": DOMAIN + "/#website"},
         "mainEntity": {"@type": "ItemList", "numberOfItems": n, "itemListElement": items}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq_items]},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Qrenzy Digital Solutions", "item": "https://www.qrenzy.com"},
                                                         {"@type": "ListItem", "position": 2, "name": "Website demos", "item": DOMAIN + "/"}]},
    ]}
    import os
    office = ""
    if os.path.exists(os.path.join(os.path.dirname(__file__), "..", "demo", "assets", "office.jpg")):
        office += '<img class="office rv" src="assets/office.jpg" width="1200" height="800" loading="lazy" alt="Qrenzy Digital Solutions office, Mundur, Thrissur">'
    office += f'<iframe class="map rv" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Map showing Qrenzy Digital Solutions, Mundur, Thrissur" src="https://maps.google.com/maps?q={MAPS_QUERY.replace(" ", "+")}&output=embed"></iframe>'
    title = f"{n} Website Demos for Local Businesses | Qrenzy Digital"
    desc = f"Browse {n} ready-made website demos across 15 industries: clinics, real estate, restaurants, jewellery, IT and more. Websites from ₹5,000 (introductory pricing)."
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
<meta name="theme-color" content="#E31E24">
<meta property="og:type" content="website"><meta property="og:site_name" content="Qrenzy Digital Solutions">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{DOMAIN}/"><meta property="og:locale" content="en_IN">
<meta property="og:image" content="{DOMAIN}/assets/thumbs/gym.jpg">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(desc)}">
<link rel="icon" href="logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#demos">Skip to demos</a>
<header class="site"><div class="container nav">
  <a href="./" aria-label="Qrenzy Digital Solutions"><img class="logo" src="logo.png" alt="Qrenzy Digital Solutions" width="150" height="52"></a>
  <nav aria-label="Main"><ul class="menu" id="menu"><li><a class="on" href="#demos">Demos</a></li><li><a href="#industries">Industries</a></li><li><a href="#included">What's included</a></li><li><a href="#pricing">Pricing</a></li><li><a href="#faq">FAQ</a></li><li><a href="#contact">Contact</a></li></ul></nav>
  <div class="nav-cta"><a class="tl" data-wa="Hi Qrenzy, I want a website for my business." href="#">{WA_SVG} WhatsApp</a><span class="sep"></span><a class="tl red" href="#contact">Free Demo →</a>
  <button class="burger" id="burger" aria-label="Menu" aria-expanded="false" aria-controls="menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button></div>
</div></header>

<main id="main">
<section class="hero"><div class="container hgrid">
  <div>
    <p class="kicker"><span></span>Website demos for local businesses</p>
    <h1>Your Business Deserves a Website That <em>Wins Customers.</em></h1>
    <p class="lead">Browse ready-made website designs for your industry. Choose a layout, customise it for your business, and launch with Qrenzy Digital Solutions.</p>
    <ul class="pills"><li><b>📱</b> Mobile-first</li><li><b>🔎</b> SEO + AEO</li><li><b>⚡</b> Fast launch</li><li><b>💬</b> WhatsApp leads</li><li><b>🇮🇳</b> Made in Kerala</li></ul>
    <div class="hero-cta"><a class="btn btn-p" href="#demos">Explore Website Demos →</a><a class="btn btn-w" data-wa="Hi Qrenzy, I would like to request a free demo for my business." data-ev="request_demo" href="#">💬 Request a Free Demo</a></div>
    <p class="proof"><b>{n} Website Demos</b> · <b>15 Industries</b> · <b>Starting at ₹5,000*</b></p>
    <p class="fine">*Introductory pricing, not a final quotation. Includes the first-year domain and hosting. Typical launch is 48 hours after we receive all content and approvals. Renewal, email and extras are quoted separately.</p>
  </div>
  <aside class="card-hero" aria-label="What every demo includes">
    <div class="ch-top"><h2>Demo Gallery</h2><span class="live">Live</span></div>
    <div class="tiles"><div><small>LIVE DEMOS</small><b>{n}</b><i>↑ new this month</i></div><div><small>INDUSTRIES</small><b>15</b><i>↑ covered</i></div><div><small>TYPICAL LAUNCH</small><b>48 hrs*</b><i>↑ after content &amp; approval</i></div><div><small>WEBSITES FROM</small><b>₹5,000*</b><i>↑ introductory</i></div></div>
    <ul class="bars"><li><span>SEO + FAQ schema<em>Included</em></span><div><u style="--c:#E31E24"></u></div></li><li><span>WhatsApp lead form<em>Included</em></span><div><u style="--c:#1f6feb"></u></div></li><li><span>Mobile-first speed<em>Included</em></span><div><u style="--c:#1faa59"></u></div></li><li><span>Maps, hours &amp; FAQ<em>Included</em></span><div><u style="--c:#f5a623"></u></div></li></ul>
    <p class="foot">Active: Kerala · India · Gulf</p>
  </aside>
</div></section>

<div class="ticker" aria-hidden="true"><div class="track">{tick}{tick}</div></div>

<section class="statrow"><div class="container"><ul>
  <li><b>{n}</b><span>Live demos</span></li><li><b>15</b><span>Industries</span></li><li><b>48h*</b><span>Typical launch, after content &amp; approval</span></li><li><b>₹5K*</b><span>Websites from (introductory)</span></li>
</ul></div></section>

<section id="demos" aria-labelledby="demos-h"><div class="container">
  <div class="sec-head"><span class="eyebrow">✦ Demo gallery</span><h2 id="demos-h">Choose a design that <em>fits your business</em></h2><p>Every demo is a complete, working website with services, pricing, FAQ, map and WhatsApp enquiry form. Tap a card to open it.</p></div>
  <div class="tools"><div class="chips" role="group" aria-label="Filter demos by industry">{chips}</div>
    <label class="search"><span class="sr">Search demos</span><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg><input id="q" type="search" placeholder="Search e.g. dental, crane, solar" autocomplete="off"></label></div>
  <p class="count" id="count" aria-live="polite">Showing all {n} demos</p>
  <ul class="grid" id="grid">{"".join(cards)}</ul>
  <p class="empty" id="empty" hidden>No demo matches your search. <a href="#" data-wa="Hi Qrenzy, I need a website for my business type.">Ask us for a custom design</a>.</p>
</div></section>

<section class="warm" id="industries" aria-labelledby="ind-h"><div class="container">
  <div class="sec-head center"><span class="eyebrow">✦ Industries we serve</span><h2 id="ind-h">Websites for <em>every kind of business</em></h2><p>From jewellery showrooms to software companies, we build websites that match how your customers search and buy.</p></div>
  <div class="inds">{inds}</div>
</div></section>

<section id="included" aria-labelledby="inc-h"><div class="container">
  <div class="sec-head center"><span class="eyebrow">✦ Included in every website</span><h2 id="inc-h">Built to be <em>found, trusted and contacted</em></h2><p>Good design is only half the job. Every demo ships with the technical foundations that help you rank and convert.</p></div>
  <div class="incs">{inc}</div>
</div></section>

<section class="warm" aria-labelledby="how-h"><div class="container">
  <div class="sec-head center"><span class="eyebrow">✦ How it works</span><h2 id="how-h">From demo to live website <em>in 3 steps</em></h2></div>
  <ol class="steps"><li class="step rv"><h3>Pick a demo</h3><p>Choose the design closest to your business, or ask for a custom one.</p></li><li class="step rv"><h3>Share your details</h3><p>Send your logo, photos, services, prices and location on WhatsApp.</p></li><li class="step rv"><h3>Launch, typically in 48 hours</h3><p>After we receive all content and your approvals, we customise, connect your domain and launch. You get the files.</p></li></ol>
</div></section>

<section id="pricing" aria-labelledby="pr-h"><div class="container">
  <div class="sec-head center"><span class="eyebrow">✦ Pricing</span><h2 id="pr-h">Simple <em>website packages</em></h2><p>*Introductory pricing, not a final quotation. Includes the first-year domain and hosting. Optional care plan: ₹1,000 a month for up to 8 hours of updates and support.</p></div>
  <div class="plans">{plans}</div>
  <div class="pnotes"><div class="rv"><h3>✅ Included</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in INCLUDED)}</ul></div><div class="rv"><h3>➕ Quoted separately</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in EXCLUDED)}</ul></div><div class="rv"><h3>⏱ Timeline</h3><p>The 48-hour launch is typical for Starter and Business websites and starts after we receive all content (logo, photos, text, prices) and your approvals. Revisions, domain setup and larger websites usually take 5 to 10 days.</p></div></div>
  <p class="fine" style="text-align:center;max-width:none;margin-top:18px">All prices are in Indian rupees.</p>
</div></section>

<section class="warm" id="faq" aria-labelledby="faq-h"><div class="container">
  <div class="sec-head center"><span class="eyebrow">✦ FAQ</span><h2 id="faq-h">Questions we get <em>asked often</em></h2></div>
  <div class="faq">{faq}</div>
</div></section>

<section id="contact" aria-labelledby="contact-h"><div class="container">
  <div class="sec-head center"><span class="eyebrow">✦ Get in touch</span><h2 id="contact-h">Let's Grow Your <em>Business Together</em></h2><p>Based in Thrissur, Kerala, serving businesses in India, Oman, UAE and worldwide. Book a free demo or just say hello.</p></div>
  <div class="cgrid">
    <div class="panel rv"><h3>Tell us about your business</h3><p class="note">We reply within 24 hours on business days.</p>
      <form id="enq">
        <div class="two"><div><label for="f-name">Name *</label><input id="f-name" name="name" required autocomplete="name"></div><div><label for="f-phone">Phone *</label><input id="f-phone" name="phone" required inputmode="tel" autocomplete="tel"></div></div>
        <div><label for="f-ind">Your industry</label><select id="f-ind" name="ind">{opts}</select></div>
        <div><label for="f-msg">Comment or message</label><textarea id="f-msg" name="msg" placeholder="Which demo do you like? Any special requirement?"></textarea></div>
        <button class="btn btn-p" type="submit">💬 Send on WhatsApp</button>
      </form></div>
    <div><div class="quick rv"><h3>Quick Contact</h3>
        <ul><li><i>{PHONE_SVG}</i><p><small>CALL / WHATSAPP</small><a data-tel href="#">+91 99057 00600</a></p></li>
        <li><i>✉️</i><p><small>EMAIL US</small><a href="mailto:info@qrenzy.com">info@qrenzy.com</a></p></li>
        <li><i>📍</i><p><small>OFFICE ADDRESS</small><span>{ADDRESS}, India</span><a class="maplink" href="{MAPS_LINK}" target="_blank" rel="noopener">Open in Google Maps →</a></p></li></ul></div>
      <div class="hours rv"><h3>🕒 Working Hours</h3><dl><div><dt>Monday – Friday</dt><dd>9:30 AM – 7:30 PM</dd></div><div><dt>Saturday</dt><dd>9:30 AM – 6:00 PM</dd></div></dl></div>{office}</div>
  </div>
</div></section>
</main>

<footer><div class="container">
  <div class="fgrid">
    <div><img class="logo" src="logo.png" alt="Qrenzy Digital Solutions" width="150" height="52" style="filter:brightness(0) invert(1)"><p>Qrenzy Digital Solutions is an AI-powered digital marketing and website design agency in Thrissur, Kerala.</p><p>{ADDRESS}</p></div>
    <div><h3>Explore</h3><ul><li><a href="#demos">All demos</a></li><li><a href="#industries">Industries</a></li><li><a href="#pricing">Pricing</a></li><li><a href="#faq">FAQ</a></li></ul></div>
    <div><h3>Contact</h3><ul><li><a data-tel href="#">+91 99057 00600</a></li><li><a href="mailto:info@qrenzy.com">info@qrenzy.com</a></li><li><a href="https://www.qrenzy.com" rel="noopener">www.qrenzy.com</a></li><li>Instagram @sajeeshvs313</li></ul></div>
  </div>
  <div class="fbar"><span>© <span id="yr"></span> Qrenzy Digital Solutions. Demo sites use sample content. This site uses Google Analytics to measure visits.</span><span>Thrissur, Kerala, India</span></div>
</div></footer>

<nav class="mbar" aria-label="Quick actions"><a class="c" data-tel href="#">{PHONE_SVG} Call</a><a class="w" data-wa="Hi Qrenzy, I want a free demo for my business." href="#">{WA_SVG} WhatsApp</a></nav>
<script>{JS}</script>
</body>
</html>
"""


CSS = r"""
:root{--red:#E31E24;--red-d:#b3121a;--ink:#0b0b0d;--text:#1c1d21;--grey:#5b5f69;--muted:#6f737d;--warm:#f7f6f2;--pink:#fff0f0;--line:#e9e7e2;--wa:#1fc761;
 --font:'Inter',system-ui,-apple-system,'Segoe UI',sans-serif;--r:24px;--shadow:0 1px 2px rgba(11,11,13,.04),0 22px 44px -20px rgba(11,11,13,.22)}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;scroll-padding-top:90px}
body{font-family:var(--font);color:var(--text);background:#fff;line-height:1.65;-webkit-font-smoothing:antialiased}
h1,h2,h3{font-family:var(--font);line-height:1.08;letter-spacing:-.035em;font-weight:900;color:var(--ink)}
h2 em,h1 em{font-style:normal;color:var(--red)}
img,svg{display:block;max-width:100%}a{color:inherit;text-decoration:none}ul,ol{list-style:none}
:focus-visible{outline:3px solid var(--red);outline-offset:3px;border-radius:8px}
.container{width:min(1180px,100% - 40px);margin-inline:auto}
.skip{position:absolute;left:-999px;top:8px;background:var(--ink);color:#fff;padding:10px 16px;border-radius:10px;z-index:100}.skip:focus{left:12px}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
section{padding:clamp(56px,8vw,100px) 0}.warm{background:var(--warm)}
.eyebrow{display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--red);background:var(--pink);border:1px solid #f6c9ca;padding:8px 16px;border-radius:999px}
h2{font-size:clamp(30px,4.6vw,52px);margin-top:18px}
.sec-head{max-width:760px;margin-bottom:38px}.sec-head p{color:var(--grey);margin-top:16px;font-size:17.5px}
.sec-head.center{margin-inline:auto;text-align:center}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:54px;padding:0 30px;border-radius:999px;font-weight:800;font-size:16px;border:1.5px solid transparent;cursor:pointer;font-family:inherit;transition:transform .18s,box-shadow .18s;white-space:nowrap}
.btn svg{width:18px;height:18px}.btn:hover{transform:translateY(-2px)}
.btn-p{background:var(--red);color:#fff;box-shadow:0 16px 30px -12px rgba(227,30,36,.7)}
.btn-o{background:#fff;color:var(--ink);border-color:var(--line)}.btn-o:hover{border-color:var(--red)}
.btn-w{background:var(--wa);color:#fff;box-shadow:0 16px 30px -14px rgba(31,199,97,.8)}
/* header: outlined nav buttons like qrenzy.com */
header.site{position:sticky;top:0;z-index:60;background:rgba(255,255,255,.92);backdrop-filter:saturate(1.6) blur(14px);-webkit-backdrop-filter:saturate(1.6) blur(14px);border-bottom:1px solid var(--line)}
.nav{display:flex;align-items:center;justify-content:space-between;height:76px;gap:18px}
.logo{height:44px;width:auto}
.menu{display:flex;gap:10px}
.menu a{display:block;padding:10px 18px;border:1px solid var(--line);border-radius:10px;font-weight:600;font-size:14.5px;color:var(--text);background:#fff;transition:.15s}
.menu a:hover,.menu a.on{border-color:var(--red);color:var(--red)}
.nav-cta{display:flex;gap:14px;align-items:center}
.tl{display:inline-flex;align-items:center;gap:8px;font-weight:600;font-size:14.5px;color:var(--text)}.tl svg{width:16px;height:16px}.tl.red{color:var(--red);font-weight:800}
.sep{width:1px;height:18px;background:var(--red);opacity:.6}
.burger{display:none;width:44px;height:44px;border-radius:12px;border:1.5px solid var(--line);background:#fff;cursor:pointer;place-items:center;color:var(--ink)}.burger svg{width:22px;height:22px}
/* hero */
.hero{padding:clamp(40px,6vw,84px) 0 clamp(48px,6vw,84px)}
.hgrid{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(30px,5vw,70px);align-items:center}
.kicker{display:flex;align-items:center;gap:12px;font-size:12.5px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--grey)}.kicker span{width:28px;height:2px;background:var(--red)}
h1{font-size:clamp(40px,6.2vw,76px);margin:22px 0 22px;letter-spacing:-.04em}
.lead{font-size:clamp(17px,1.6vw,20px);color:var(--grey);max-width:560px}
.pills{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px}
.pills li{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--line);background:var(--warm);border-radius:999px;padding:8px 16px;font-weight:600;font-size:14px}.pills b{font-size:13px}
.hero-cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}
.proof{margin-top:26px;color:var(--grey);font-size:14.5px}.proof b{color:var(--ink)}
.fine{margin-top:10px;color:var(--muted);font-size:12.5px;max-width:560px}
.pnotes{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;max-width:1040px;margin:34px auto 0}.pnotes>div{background:var(--warm);border:1px solid var(--line);border-radius:var(--r);padding:24px}.pnotes h3{font-size:17px;letter-spacing:-.02em;margin-bottom:10px}.pnotes li{font-size:14.5px;color:var(--grey);padding:5px 0;border-bottom:1px solid var(--line)}.pnotes li:last-child{border:0}.pnotes p{font-size:14.5px;color:var(--grey)}
.maplink{display:block;margin-top:6px;font-size:14px;color:#fff;text-decoration:underline;text-underline-offset:3px}
.map{width:100%;height:240px;border:0;border-radius:var(--r);margin-top:18px}.office{width:100%;height:auto;border-radius:var(--r);margin-top:18px}
.card-hero{background:#fff;border:1px solid var(--line);border-radius:28px;padding:28px;box-shadow:var(--shadow)}
.ch-top{display:flex;justify-content:space-between;align-items:center}.ch-top h2{font-size:17px;margin:0;letter-spacing:-.01em}
.live{font-size:13px;font-weight:700;color:#1faa59;display:inline-flex;align-items:center;gap:8px}.live:before{content:"";width:8px;height:8px;border-radius:50%;background:#1faa59}
.tiles{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:18px 0}
.tiles div{background:#f6f6f4;border-radius:16px;padding:16px 18px}
.tiles small{font-size:11px;font-weight:700;letter-spacing:.1em;color:var(--muted)}
.tiles b{display:block;font-size:28px;font-weight:900;letter-spacing:-.03em;line-height:1.15;color:var(--ink)}.tiles i{font-style:normal;font-size:12px;color:#1faa59;font-weight:600}
.bars{display:grid;gap:14px;margin-top:6px}
.bars span{display:flex;justify-content:space-between;font-size:14px;font-weight:600;margin-bottom:6px}.bars em{font-style:normal;color:var(--muted);font-weight:500}
.bars div{height:6px;background:#eceae6;border-radius:6px;overflow:hidden}.bars u{display:block;height:100%;width:100%;background:var(--c);border-radius:6px}
.foot{text-align:center;font-size:12.5px;color:var(--muted);margin-top:18px}
/* ticker */
.ticker{background:var(--red);color:#fff;overflow:hidden;padding:20px 0;white-space:nowrap}
.track{display:inline-flex;gap:38px;animation:tick 38s linear infinite;font-weight:800;font-size:15px;letter-spacing:.05em;padding-left:38px}.track span{display:inline-block}.track .st{opacity:.7}
@keyframes tick{to{transform:translateX(-50%)}}
.statrow{padding:clamp(30px,4vw,48px) 0}
.statrow ul{display:grid;grid-template-columns:repeat(4,1fr);text-align:center}
.statrow li{padding:18px 10px;border-right:1px solid var(--line)}.statrow li:last-child{border:0}
.statrow b{display:block;font-size:clamp(40px,6vw,64px);font-weight:900;letter-spacing:-.04em;color:var(--ink);line-height:1.1}.statrow span{color:var(--muted);font-weight:600;font-size:14.5px;display:block;max-width:190px;margin-inline:auto}
/* demos grid */
.tools{display:flex;gap:16px;justify-content:space-between;align-items:center;flex-wrap:wrap;margin-bottom:12px}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{border:1px solid var(--line);background:#fff;color:var(--text);padding:10px 16px;border-radius:10px;font:600 14px var(--font);cursor:pointer;transition:.15s}
.chip b{font-weight:700;color:var(--muted);margin-left:4px;font-size:12.5px}
.chip:hover{border-color:var(--red);color:var(--red)}.chip.on{background:#fff;border-color:var(--red);color:var(--red)}.chip.on b{color:var(--red)}
.search{display:flex;align-items:center;gap:10px;border:1px solid var(--line);background:#fff;border-radius:10px;padding:0 16px;min-height:46px;min-width:min(100%,300px);transition:.15s}
.search:focus-within{border-color:var(--red);box-shadow:0 0 0 4px rgba(227,30,36,.12)}
.search svg{width:18px;height:18px;color:var(--muted);flex:none}.search input{border:0;outline:0;font:500 15px var(--font);width:100%;background:transparent;color:var(--ink)}
.count{font-size:13.5px;color:var(--muted);margin:14px 2px 18px;font-weight:500}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.dcard article{display:flex;flex-direction:column;height:100%;background:#fff;border:1px solid var(--line);border-radius:var(--r);overflow:hidden;transition:transform .25s,box-shadow .25s,border-color .25s}
.dcard article:hover{transform:translateY(-6px);box-shadow:var(--shadow);border-color:rgba(227,30,36,.45)}
.cover{display:flex;flex-direction:column;flex:1}
.acts{padding:0 22px 22px;display:grid;gap:10px}
.acts .view{display:flex;justify-content:center;align-items:center;gap:8px;min-height:46px;border-radius:999px;background:var(--red);color:#fff;font-weight:800;font-size:14.5px;transition:.2s}.acts .view:hover{background:var(--red-d)}.acts .view svg{width:16px;height:16px}
.acts .two{display:grid;grid-template-columns:1fr 1fr;gap:8px}.acts .two a{display:flex;justify-content:center;align-items:center;text-align:center;min-height:42px;padding:6px 8px;border:1px solid var(--line);border-radius:10px;font-weight:700;font-size:13px;line-height:1.25;transition:.15s}.acts .two a:hover{border-color:var(--red);color:var(--red)}
.shot{background:#f1f1f3;border-bottom:1px solid var(--line);overflow:hidden}
.shot .bar{height:28px;display:flex;align-items:center;gap:6px;padding:0 12px;background:#f6f6f4}
.shot .bar i{width:9px;height:9px;border-radius:50%;background:#d4d4d9}.shot .bar i:nth-child(1){background:#ff5f56}.shot .bar i:nth-child(2){background:#ffbd2e}.shot .bar i:nth-child(3){background:#27c93f}
.shot .bar span{margin-left:8px;font-size:11.5px;color:var(--muted);background:#fff;border-radius:999px;padding:2px 12px}
.shot img{width:100%;height:auto;aspect-ratio:8/5;object-fit:cover;object-position:top;transition:transform .5s}.dcard article:hover .shot img{transform:scale(1.04)}
.meta{padding:20px 22px 22px;display:flex;flex-direction:column;gap:8px;flex:1}
.tag{align-self:flex-start;font-size:12px;font-weight:700;padding:5px 12px;border-radius:999px;background:color-mix(in srgb,var(--c) 12%,#fff);color:color-mix(in srgb,var(--c) 70%,#000)}
.meta h3{font-size:20px;letter-spacing:-.02em}.meta p{font-size:14.5px;color:var(--muted)}
.dcard[hidden]{display:none}
.empty{text-align:center;color:var(--muted);padding:40px 0}.empty a{color:var(--red);font-weight:700;text-decoration:underline}
/* industries */
.inds{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}
.ind{display:flex;flex-direction:column;align-items:flex-start;gap:10px;background:#fff;border:1px solid var(--line);border-radius:20px;padding:20px;font-weight:700;font-size:15px;transition:.2s;position:relative}
.ind i{font-style:normal;font-size:32px}.ind svg{position:absolute;right:16px;top:20px;width:18px;height:18px;color:var(--red);opacity:0;transition:.2s}
.ind:hover{border-color:var(--red);transform:translateY(-4px);box-shadow:var(--shadow)}.ind:hover svg{opacity:1}
/* included, steps, plans */
.incs{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.inc,.step{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:28px}
.ico{width:54px;height:54px;border-radius:16px;background:var(--pink);display:grid;place-items:center;font-size:27px;margin-bottom:14px}
.inc h3{font-size:19px;letter-spacing:-.02em}.inc p,.step p{color:var(--grey);font-size:15px;margin-top:8px}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;counter-reset:s;max-width:980px;margin-inline:auto}
.step:before{counter-increment:s;content:counter(s);display:grid;place-items:center;width:44px;height:44px;border-radius:50%;background:var(--red);color:#fff;font-weight:900;margin-bottom:16px}
.step h3{font-size:19px}
.plans{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;max-width:1040px;margin-inline:auto}
.plan{background:#fff;border:1px solid var(--line);border-radius:28px;padding:34px 28px;display:flex;flex-direction:column;position:relative}
.plan.pop{border:2px solid var(--red);box-shadow:0 30px 60px -30px rgba(227,30,36,.5);transform:translateY(-10px)}
.ptag{position:absolute;top:-14px;left:28px;background:var(--red);color:#fff;font-size:11.5px;font-weight:800;letter-spacing:.1em;padding:5px 14px;border-radius:999px}
.plan h3{font-size:22px}.plan .for{color:var(--muted);font-size:14px}
.price{font-size:50px;font-weight:900;letter-spacing:-.04em;margin:18px 0 4px;line-height:1}.price sup{font-size:.45em;vertical-align:top;position:relative;top:.35em;margin-right:2px}
.price small{font:500 13px var(--font);color:var(--muted);letter-spacing:0}
.plan ul{margin:22px 0 28px;display:grid;gap:11px;font-size:15px;flex:1}.plan li{display:flex;gap:10px}.plan li:before{content:"✓";color:var(--red);font-weight:900}
.faq{max-width:820px;margin-inline:auto;display:grid;gap:12px}
details{background:#fff;border:1px solid var(--line);border-radius:16px;padding:0 22px;transition:.2s}
details[open]{border-color:rgba(227,30,36,.45);box-shadow:var(--shadow)}
summary{cursor:pointer;list-style:none;padding:20px 0;font:800 17px var(--font);display:flex;justify-content:space-between;gap:16px;align-items:center;letter-spacing:-.02em;color:var(--ink)}
summary::-webkit-details-marker{display:none}
summary:after{content:"+";flex:0 0 30px;height:30px;border-radius:50%;background:var(--pink);color:var(--red);display:grid;place-items:center;font-size:20px;font-weight:700}
details[open] summary:after{content:"–";background:var(--red);color:#fff}
details p{padding:0 0 22px;color:var(--grey);font-size:15.5px}
/* contact */
.cgrid{display:grid;grid-template-columns:1.35fr 1fr;gap:24px;align-items:start;max-width:1100px;margin-inline:auto}
.panel{background:var(--warm);border:1px solid var(--line);border-radius:var(--r);padding:clamp(24px,3vw,38px)}.panel h3{font-size:26px}
.note{font-size:14px;color:var(--muted);margin-top:6px}
form{display:grid;gap:16px;margin-top:22px}.two{display:grid;grid-template-columns:1fr 1fr;gap:14px}
label{font-size:14px;font-weight:700;color:var(--text);display:block}
input,select,textarea{width:100%;background:#fff;border:1px solid #cfccc5;border-radius:6px;padding:0 14px;min-height:48px;color:var(--ink);font:inherit;font-size:15.5px;margin-top:6px}
textarea{padding:12px 14px;min-height:120px;resize:vertical}
input:focus,select:focus,textarea:focus{outline:0;border-color:var(--red);box-shadow:0 0 0 4px rgba(227,30,36,.12)}
.quick{background:var(--red);color:#fff;border-radius:var(--r);padding:30px}.quick h3{color:#fff;font-size:20px;letter-spacing:-.02em}
.quick li{display:flex;gap:14px;align-items:center;padding:16px 0;border-bottom:1px solid rgba(255,255,255,.25)}.quick li:last-child{border:0;padding-bottom:0}
.quick i{font-style:normal;flex:0 0 28px;display:grid;place-items:center;font-size:20px}.quick svg{width:24px;height:24px}
.quick small{display:block;font-size:11px;font-weight:700;letter-spacing:.1em;opacity:.8}.quick a,.quick span{font-weight:800;font-size:16px}
.hours{background:var(--warm);border:1px solid var(--line);border-radius:var(--r);padding:26px;margin-top:18px}.hours h3{font-size:18px;letter-spacing:-.02em}
.hours dl div{display:flex;justify-content:space-between;gap:12px;padding:12px 0;border-bottom:1px solid var(--line);font-size:14.5px}.hours dl div:last-child{border:0;padding-bottom:0}.hours dt{color:var(--grey)}.hours dd{font-weight:800}
footer{background:var(--ink);color:#d9dbe1;padding:60px 0 100px;border-top:5px solid var(--red)}
.fgrid{display:grid;grid-template-columns:1.6fr 1fr 1fr;gap:36px}
footer h3{font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:#fff;margin-bottom:14px}
footer li{margin:8px 0;font-size:14.5px}footer a:hover{color:#fff;text-decoration:underline}footer p{font-size:14.5px;color:#a8acb7;margin-top:14px;max-width:360px}
.fbar{margin-top:40px;padding-top:22px;border-top:1px solid rgba(255,255,255,.12);display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;font-size:13.5px;color:#9096a3}
.mbar{display:none;position:fixed;left:12px;right:12px;bottom:12px;z-index:70;background:#fff;border:1px solid var(--line);border-radius:20px;padding:8px;gap:8px;box-shadow:0 18px 44px -10px rgba(0,0,0,.35)}
.mbar a{flex:1;min-height:46px;border-radius:14px;display:flex;align-items:center;justify-content:center;gap:8px;font-weight:800;font-size:14.5px}.mbar a svg{width:18px;height:18px}
.mbar .c{background:#f4f4f2}.mbar .w{background:var(--wa);color:#fff}
html.js .rv{opacity:0;transform:translateY(18px);transition:opacity .6s ease,transform .6s ease}html.js .rv.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}html.js .rv{opacity:1;transform:none;transition:none}.dcard a,.shot img{transition:none}.track{animation:none}}
@media(max-width:1020px){.menu,.nav-cta .tl,.sep{display:none}.burger{display:grid}
 .menu.open{display:flex;flex-direction:column;position:absolute;left:0;right:0;top:76px;background:#fff;padding:14px 20px 22px;border-bottom:1px solid var(--line);box-shadow:var(--shadow)}.menu.open a{font-size:16px}
 .hgrid,.cgrid{grid-template-columns:1fr}.grid{grid-template-columns:1fr 1fr}.incs{grid-template-columns:1fr 1fr}.inds{grid-template-columns:repeat(3,1fr)}.plan.pop{transform:none}.pnotes{grid-template-columns:1fr}}
@media(max-width:680px){.grid,.incs,.steps,.plans,.fgrid,.two{grid-template-columns:1fr}.inds{grid-template-columns:1fr 1fr}.statrow ul{grid-template-columns:1fr 1fr}.statrow li:nth-child(2){border-right:0}.statrow li:nth-child(-n+2){border-bottom:1px solid var(--line)}
 .mbar{display:flex}footer{padding-bottom:120px}.hero-cta .btn{flex:1 1 100%}.tools{flex-direction:column;align-items:stretch}.search{width:100%}}
"""

JS = r"""
(function(){var d=document,r=d.documentElement;r.classList.add('js');var NUM='919905700600';
var GA4='G-9ZYRDQ7B4V';
var wa=function(t){return 'https://wa.me/'+NUM+'?text='+encodeURIComponent(t)};
if(GA4){var gs=d.createElement('script');gs.async=1;gs.src='https://www.googletagmanager.com/gtag/js?id='+GA4;d.head.appendChild(gs);window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};gtag('js',new Date());gtag('config',GA4)}
var ev=function(n,p){if(window.gtag)gtag('event',n,p||{})};
d.addEventListener('click',function(e){var a=e.target.closest('a');if(!a)return;var n=a.getAttribute('data-ev');if(n)ev(n,{demo:a.getAttribute('data-demo')||''});else if(a.hasAttribute('data-wa'))ev('whatsapp_click',{});else if(a.hasAttribute('data-tel'))ev('call_click',{})});
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
var form=d.getElementById('enq');form.addEventListener('submit',function(e){e.preventDefault();var v=new FormData(form);
var t='Hi Qrenzy, I would like a free website demo.\nName: '+v.get('name')+'\nPhone: '+v.get('phone')+'\nIndustry: '+v.get('ind');if(v.get('msg'))t+='\nMessage: '+v.get('msg');ev('form_submit_whatsapp',{industry:v.get('ind')});window.open(wa(t),'_blank','noopener')});
})();
"""
