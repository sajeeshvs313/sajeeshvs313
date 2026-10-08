# demo.qrenzy.com source

Generates the 21 demo websites and the landing page in `../demo`.

    python3 build.py        # rebuild all pages, landing, sitemap.xml, robots.txt, llms.txt
    python3 build.py gym    # rebuild one demo
    python3 thumbs.py       # refresh landing-page thumbnails (needs Chromium + Pillow)

* `template.py`  : the shared page template (design, SEO and AEO markup)
* `data1-3.py`   : content for each demo (copy, prices, FAQs)
* `landing.py`   : the demo.qrenzy.com grid page
* `INDEXABLE = False` in `template.py` adds `noindex` to demo pages (sample content). Set `True` only for a real client site.
