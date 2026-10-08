AREAS = ["Kochi", "Ernakulam", "Aluva", "Kakkanad", "Thrippunithura", "Edappally"]
DEFAULTS = dict(
    theme="light", font="sans", hero="split", city="Kochi", addr="Main Road, Your Locality", areas=AREAS, pop=1,
    schema="LocalBusiness", range="₹₹", extra=None, nav_cta="Get Quote", on_acc="#fff",
    services_eye="What we do", plans_eye="Pricing", show_eye="Our work", work_nav="Work",
    steps_h="From enquiry to done in 4 simple steps", faq_h="Frequently asked questions", contact_h="Get in touch",
    hours_spec=[("Mo-Sa", "09:00", "18:00")],
)

def D(**kw):
    d = dict(DEFAULTS); d.update(kw)
    d.setdefault("footer_p", d["desc"])
    d.setdefault("wa_default", f"Hi, I would like to know more about {d['name']}.")
    return d
