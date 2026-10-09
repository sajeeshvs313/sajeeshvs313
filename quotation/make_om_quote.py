"""Generate the MDFC (Oman) quotation. Fill EMAIL_* prices (INR) when known, then run:
   python3 make_om_quote.py && chrome --headless --print-to-pdf ...  (see bottom of file)"""
import subprocess, sys
RATE = 3800/15            # INR per OMR implied by the quoted domain price (indicative)
DOMAIN_OMR, DOMAIN_INR = 15, 3800
EMAIL_MAIN_INR = 2700     # info@mdfc.om, 15 GB  (INR, one line total)
EMAIL_REST_INR = 6800     # 4 mailboxes x 10 GB  (INR, one line total for all 4)
CLIENT = "Modern Bright Future Company"
IFSC = "BARB0PERAMA"; SWIFT = "[SWIFT/BIC – add]"

def omr(inr): return f"{inr/RATE:.1f}"
def inr_s(v): return "To be confirmed" if v is None else f"{v:,}"
def omr_s(v): return "—" if v is None else omr(v)
rows_total = [DOMAIN_INR] + [x for x in (EMAIL_MAIN_INR, EMAIL_REST_INR) if x is not None]
known = EMAIL_MAIN_INR is not None and EMAIL_REST_INR is not None
total_inr = sum(rows_total)
total_omr = DOMAIN_OMR + sum(round(x/RATE,1) for x in rows_total[1:])
tot_lbl = "TOTAL (ADVANCE)"

html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Quotation QZ-2026-002 | Qrenzy Digital Solutions</title>
<style>
@page{{size:A4;margin:0}}
:root{{--red:#E31E24;--ink:#0a0a0a;--text:#1a1a1a;--grey:#555;--muted:#777;--warm:#f8f8f6;--line:#e8e8e4;--pink:#fdecec}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;color:var(--text);font-size:10.5pt;line-height:1.5;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:210mm;height:297mm;padding:12mm 15mm;position:relative;page-break-after:always;overflow:hidden}}.page:last-child{{page-break-after:auto}}
.bar{{position:absolute;left:0;right:0;top:0;height:5mm;background:var(--red)}}
.top{{display:flex;justify-content:space-between;align-items:flex-start;margin-top:4mm}}.top img{{height:15mm}}
.qt{{text-align:right}}.qt h1{{font-size:25pt;font-weight:900;letter-spacing:-.03em;line-height:1}}.qt h1 em{{font-style:normal;color:var(--red)}}
.tag{{display:inline-block;margin-top:2mm;background:var(--pink);color:var(--red);border:.3mm solid #f6c9ca;border-radius:99px;padding:.7mm 3.5mm;font-size:8pt;font-weight:800;letter-spacing:.1em}}
.meta{{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm;margin:5mm 0 4mm}}.meta div{{background:var(--warm);border:.3mm solid var(--line);border-radius:3mm;padding:2.5mm 4mm}}
.meta small{{display:block;font-size:7.5pt;font-weight:700;letter-spacing:.1em;color:var(--muted);text-transform:uppercase}}.meta b{{font-size:10.5pt}}
.parties{{display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-bottom:4mm}}.parties h3{{font-size:8pt;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--red);margin-bottom:1.5mm}}
.parties p{{font-size:9.5pt;color:var(--grey)}}.parties b{{color:var(--ink);font-size:10.5pt}}
table{{width:100%;border-collapse:collapse}}th{{font-size:8pt;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);text-align:left;padding:2mm 3mm;border-bottom:.5mm solid var(--ink)}}
th.r,td.r{{text-align:right;white-space:nowrap}}td{{padding:2.6mm 3mm;border-bottom:.3mm solid var(--line);vertical-align:top;font-size:9.5pt}}td b{{color:var(--ink);font-size:10pt}}
td small{{display:block;color:var(--grey);font-size:8.5pt;margin-top:.8mm}}td.n{{width:8mm;color:var(--muted);font-weight:700}}
.tot{{display:flex;justify-content:flex-end;margin-top:3mm}}.tot div{{width:92mm}}
.grand{{background:var(--red);color:#fff;border-radius:3mm;padding:3mm 4mm;display:flex;justify-content:space-between;font-weight:900;font-size:11pt}}
.grand span:last-child{{text-align:right}}
.fx{{font-size:8.3pt;color:var(--muted);margin-top:2mm;text-align:right}}
h2{{font-size:12pt;font-weight:900;letter-spacing:-.02em;margin:5mm 0 2mm}}h2 em{{font-style:normal;color:var(--red)}}
.box{{background:var(--warm);border:.3mm solid var(--line);border-radius:3mm;padding:3mm 5mm}}
.terms li{{list-style:none;font-size:9pt;color:var(--grey);padding:.8mm 0 .8mm 5mm;position:relative}}.terms li:before{{content:"•";position:absolute;left:0;color:var(--red);font-weight:900}}.terms b{{color:var(--ink)}}
.bank{{display:grid;grid-template-columns:1fr 34mm;gap:6mm;align-items:center}}
.bank dl div{{display:flex;gap:3mm;padding:1.1mm 0;border-bottom:.3mm solid var(--line);font-size:9.3pt}}.bank dl div:last-child{{border:0}}.bank dt{{width:34mm;color:var(--muted);font-weight:600}}.bank dd{{font-weight:800;color:var(--ink)}}
.qr{{text-align:center;font-size:7.5pt;color:var(--muted)}}.qr img{{width:32mm;height:32mm;border:.3mm solid var(--line);border-radius:2mm}}
.ph{{color:var(--red);font-style:italic}}
.sign{{display:grid;grid-template-columns:1fr 1fr;gap:12mm;margin-top:8mm}}.sign div{{border-top:.4mm solid var(--ink);padding-top:2mm;font-size:8.5pt;color:var(--grey)}}.sign b{{display:block;color:var(--ink);font-size:9.5pt}}
.foot{{position:absolute;left:15mm;right:15mm;bottom:7mm;border-top:.3mm solid var(--line);padding-top:2.5mm;display:flex;justify-content:space-between;font-size:8pt;color:var(--muted)}}.foot b{{color:var(--red)}}
</style></head><body>
<section class="page"><div class="bar"></div>
<div class="top"><img src="logo.png" alt="Qrenzy Digital Solutions"><div class="qt"><h1>QUO<em>TATION</em></h1><span class="tag">DOMAIN &amp; BUSINESS EMAIL</span></div></div>
<div class="meta"><div><small>Quotation no.</small><b>QZ-2026-002</b></div><div><small>Date</small><b>09 Oct 2026</b></div><div><small>Valid until</small><b>16 Oct 2026</b></div></div>
<div class="parties"><div><h3>From</h3><p><b>Qrenzy Digital Solutions</b><br>Sajeesh V S, Proprietor<br>Medical College Road, Kodankandan Jn,<br>Deepti Nagar, Mundur P.O., Thrissur – 680541, India<br>+91 99057 00600 · info@qrenzy.com</p></div>
<div><h3>Prepared for</h3><p><b>{CLIENT}</b><br>Domain: <b>mdfc.om</b><br>Attn: Pragadiswaran Raju<br>+968 9943 8701<br>Oman</p></div></div>
<table><thead><tr><th>#</th><th>Description</th><th class="r">OMR</th><th class="r">INR (₹)</th></tr></thead><tbody>
<tr><td class="n">1</td><td><b>.om domain registration: mdfc.om</b><small>Registration for 12 months in your company's name.</small></td><td class="r"><b>{DOMAIN_OMR:.1f}</b></td><td class="r"><b>{DOMAIN_INR:,}</b></td></tr>
<tr><td class="n">2</td><td><b>Zoho Mail: info@mdfc.om (main mailbox, 20 GB)</b><small>10 GB mailbox (₹1,700) + 10 GB storage add-on (₹1,000), per year. Set up and connected to mdfc.om, with webmail and mobile app access.</small></td><td class="r"><b>{omr_s(EMAIL_MAIN_INR)}</b></td><td class="r"><b>{inr_s(EMAIL_MAIN_INR)}</b></td></tr>
<tr><td class="n">3</td><td><b>Zoho Mail: 4 additional mailboxes (10 GB each)</b><small>4 × ₹1,700 per year. Four more users on mdfc.om with the same domain and security settings.</small></td><td class="r"><b>{omr_s(EMAIL_REST_INR)}</b></td><td class="r"><b>{inr_s(EMAIL_REST_INR)}</b></td></tr>
</tbody></table>
<div class="tot"><div><div class="grand"><span>{tot_lbl}</span><span>OMR {total_omr:.1f}<br>₹ {total_inr:,}</span></div>
<p class="fx">INR is the amount to be received in our account. OMR is indicative at ₹{RATE:,.0f} per OMR (based on item 1).</p></div></div>
<h2>What is <em>included</em></h2>
<div class="box"><ul class="terms" style="padding:0">
<li>Domain registration and DNS records for mdfc.om, pointed correctly for email.</li>
<li>Zoho Mail account setup, 5 mailboxes (info@ with 20 GB, four with 10 GB), SPF, DKIM and DMARC records for better inbox delivery.</li>
<li>Help setting up each mailbox on phone and Outlook, and a short hand-over of the admin login.</li></ul></div>
<div class="foot"><span><b>Qrenzy Digital Solutions</b> · Thrissur, Kerala</span><span>+91 99057 00600 · info@qrenzy.com · www.qrenzy.com</span><span>Page 1 of 2</span></div></section>

<section class="page"><div class="bar"></div>
<h2 style="margin-top:4mm">Payment <em>terms</em></h2>
<ul class="terms"><li><b>100% advance.</b> The domain and email subscriptions are paid in full to the providers at the time of ordering, so the full amount is payable in advance. Work starts after payment is received.</li>
<li><b>Bank charges.</b> Remittance charges, if any, are borne by the sender so that the full INR amount reaches our account.</li>
<li><b>Currency.</b> The INR amount is fixed as quoted. OMR figures are indicative and will vary with the exchange rate on the day of transfer.</li></ul>
<h2>Bank <em>details</em></h2>
<div class="box bank"><dl>
<div><dt>Account name</dt><dd>Sajeesh V S (Proprietor, Qrenzy Digital Solutions)</dd></div>
<div><dt>Bank</dt><dd>Bank of Baroda, Peramangalam Branch</dd></div>
<div><dt>Account number</dt><dd>11250100005649</dd></div>
<div><dt>IFSC</dt><dd class="ph">{IFSC}</dd></div>
<div><dt>SWIFT / BIC</dt><dd class="ph">{SWIFT}</dd></div>
</dl>
<div class="qr"><img src="upi-qr.png" alt="UPI QR code"><br>UPI (India only)<br>sajeeshvs313@okhdfcbank</div></div>
<h2>Terms &amp; <em>conditions</em></h2>
<ul class="terms">
<li><b>Validity.</b> This quotation is valid for 7 days, as domain and subscription prices may change.</li>
<li><b>Renewals.</b> The domain and each mailbox renew yearly: domain OMR 15 (₹3,800), 10 GB mailbox ₹1,700, 10 GB add-on ₹1,000, at today's rates. We will remind you before the renewal date. Renewal prices follow the providers' rates at that time.</li>
<li><b>Ownership.</b> The domain is registered in your company's name and the admin login is handed over to you on request.</li>
<li><b>Documents.</b> The .om registry may require company details or a trade licence copy. Please share them when asked, as delays can hold up registration.</li>
<li><b>Not included.</b> Website design and development, content writing and email migration from other providers are quoted separately.</li></ul>
<div class="sign"><div><b>For Qrenzy Digital Solutions</b>Authorised signatory</div><div><b>Accepted by client</b>Name, signature and date</div></div>
<div class="foot"><span><b>Qrenzy Digital Solutions</b> · Thrissur, Kerala</span><span>+91 99057 00600 · info@qrenzy.com · www.qrenzy.com</span><span>Page 2 of 2</span></div></section>
</body></html>"""
open('MDFC-Oman-Quotation.html','w').write(html)
print('html ok; known prices:',known)
