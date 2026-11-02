import re
t=open('Intarc-Workflow.html').read()
css=re.search(r'<style>(.*?)</style>',t,re.S).group(1)
def foot(n): return f'<div class="foot"><span><b>Qrenzy Digital Solutions</b> · Thrissur, Kerala</span><span>+91 99057 00600 · info@qrenzy.com · www.qrenzy.com</span><span>Page {n} of 3</span></div>'
html=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Proposal | Digital Marketing for North America | Qrenzy Digital Solutions</title><style>{css}</style></head><body>

<section class="page"><div class="bar"></div>
<div class="top"><img src="logo.png" alt="Qrenzy Digital Solutions"><div class="qt"><h1>PRO<em>POSAL</em></h1><span class="tag">DIGITAL MARKETING · NORTH AMERICA</span></div></div>
<div class="meta"><div><small>Document no.</small><b>QZ-PR-2026-002</b></div><div><small>Date</small><b>2 Nov 2026</b></div><div><small>Status</small><b>Draft for discussion</b></div></div>
<div class="parties"><div><h3>From</h3><p><b>Qrenzy Digital Solutions</b><br>Sajeesh V S, Proprietor<br>Thrissur, Kerala, India<br>+91 99057 00600 · info@qrenzy.com</p></div>
<div><h3>Prepared for</h3><p><b>Vinod Menon</b><br>Business 1: Canadian immigration services (RCIC)<br>Business 2: Accounting and bookkeeping (new)</p></div></div>
<h2 style="margin-top:2mm">What we <em>understood</em></h2>
<table class="dt"><thead><tr><th style="width:36mm"></th><th>Business 1: Immigration</th><th>Business 2: Accounting / bookkeeping</th></tr></thead><tbody>
<tr><td><b>Who</b></td><td>Established practice. Licensed RCICs.</td><td>New business, starting in the US.</td></tr>
<tr><td><b>Who to reach</b></td><td>People in Canada, the US, the Middle East and possibly India.</td><td>US small businesses, e-commerce sellers and contractors first. Canada later.</td></tr>
<tr><td><b>Today</b></td><td>Has an immigration website.</td><td>Starting from the beginning.</td></tr>
<tr><td><b>Budget</b></td><td colspan="2">Open for discussion. To be set together after the call.</td></tr>
<tr><td><b>Your question</b></td><td colspan="2">"What is beneficial to us as a company?" Answered below.</td></tr></tbody></table>
<h2>What is <em>beneficial</em> to you</h2>
<div class="note"><b>Measure booked consultations, then signed clients, not clicks.</b> Cheap enquiries that never book cost you time. We track every enquiry from the first click to a booked call, and judge the campaigns on the <b>cost of a booked consultation</b>. Once you share which enquiries became clients, we move to the <b>cost of a signed client</b>, the number that really matters for your company.</div>
<table class="dt"><thead><tr><th>Measure</th><th>Good for</th><th>Watch out for</th></tr></thead><tbody>
<tr><td><b>Enquiries (leads)</b></td><td>Early speed, quick learning</td><td>Low quality, wasted follow-up time</td></tr>
<tr><td><b>Booked consultations</b></td><td>Real interest. Our main measure from day one</td><td>Needs fast replies from your team</td></tr>
<tr><td><b>Signed clients</b></td><td>The true result</td><td>Needs your feedback, results come later</td></tr></tbody></table>
{foot(1)}</section>

<section class="page"><div class="bar"></div>
<h2 style="margin-top:4mm">Recommended <em>approach</em></h2>
<p style="font-size:8.8pt;color:var(--grey);margin-bottom:2mm">Start small, learn fast, then grow. We suggest a <b>90-day pilot</b>, one or two markets per business, not every market at once.</p>
<table class="dt"><thead><tr><th style="width:32mm"></th><th>Business 1: Immigration</th><th>Business 2: Accounting / bookkeeping</th></tr></thead><tbody>
<tr><td><b>Start with</b></td><td>The one or two markets that give you your best clients today (suggested: people already in Canada or the US). Middle East and India follow once the first results are clear.</td><td>The US only. One niche first (contractors or e-commerce sellers), then test the second.</td></tr>
<tr><td><b>Main channels</b></td><td>Google Search for people actively looking for help. Meta (Facebook and Instagram) for awareness and lead forms. YouTube later.</td><td>Google Search for searches such as "bookkeeper for contractors". LinkedIn for owners and managers. Google Business Profile.</td></tr>
<tr><td><b>Landing pages</b></td><td>One page per service (for example Express Entry, study permit, work permit), each with a booking form.</td><td>One page per niche, each with a clear offer and a call-booking form.</td></tr>
<tr><td><b>Before ads start</b></td><td>Tracking, consultation booking, review of your website and RCIC licence display.</td><td>Brand basics, a simple website or landing pages, and Google Business Profile (we can build these, quoted separately).</td></tr>
<tr><td><b>After 90 days</b></td><td colspan="2">Clear data: cost of a booked consultation per market, which services and messages work, and a plan for the next quarter. We do not promise a number of clients.</td></tr></tbody></table>
<h2>90-day <em>timeline</em></h2>
<table class="dt"><thead><tr><th style="width:30mm">When</th><th>What happens</th></tr></thead><tbody>
<tr><td><b>Weeks 1 – 2</b></td><td>Discovery call. Access to accounts. Tracking, landing pages, consultation booking, compliance check, creative.</td></tr>
<tr><td><b>Weeks 3 – 6</b></td><td>Launch the first campaigns with a small test budget. Fix what is not working every week.</td></tr>
<tr><td><b>Weeks 7 – 10</b></td><td>Put more budget on what works. Test new messages and a second market or niche.</td></tr>
<tr><td><b>Weeks 11 – 13</b></td><td>Results review. Plan for the next quarter.</td></tr></tbody></table>
<h2>What we need from <em>you</em></h2>
<div class="box"><ul class="terms" style="padding:0"><li>RCIC licence number and the registry link, shown on the ads and the site.</li><li>Access to your website, analytics and ad accounts (ad accounts stay in your name).</li><li>Who answers new enquiries, and how fast. <b>Fast replies decide whether ad money is wasted.</b></li><li>Feedback on which enquiries became clients.</li></ul></div>
{foot(2)}</section>

<section class="page"><div class="bar"></div>
<h2 style="margin-top:4mm">Our <em>investment</em> structure</h2>
<p style="font-size:8.8pt;color:var(--grey);margin-bottom:2mm">Amounts will be set after the discovery call, once we know the markets, channels and budget. Each business gets its own quotation.</p>
<table class="dt"><thead><tr><th>Item</th><th>What it covers</th><th class="r">Amount</th></tr></thead><tbody>
<tr><td><b>One-time setup</b></td><td>Tracking, landing pages, booking form, ad account setup, first campaign structure.</td><td class="r"><b>After discovery call</b></td></tr>
<tr><td><b>Monthly management</b></td><td>Campaign creation and optimisation, weekly checks, a monthly report and a monthly call.</td><td class="r"><b>After discovery call</b></td></tr>
<tr><td><b>Advertising budget</b></td><td>Paid by you directly to Google and Meta from your own account. Not part of our fee.</td><td class="r"><b>Set by you</b></td></tr>
<tr><td><b>Optional</b></td><td>Website, branding, Google Business Profile, ad creative and video for Business 2.</td><td class="r"><b>Quoted separately</b></td></tr></tbody></table>
<h2>Working <em>terms</em></h2>
<ul class="terms">
<li><b>Pilot:</b> 90 days, then month to month with 30 days' notice.</li>
<li><b>Payment:</b> in USD, invoiced in advance. Wise, Payoneer or bank transfer.</li>
<li><b>Ownership:</b> ad accounts, pages and data belong to you. We work as managers.</li>
<li><b>No guarantees:</b> we cannot promise rankings, leads or clients. Results depend on the market, budget, offer and how enquiries are handled.</li>
<li><b>Compliance:</b> as RCICs you are responsible for what your ads say. We will not write guarantees such as "100% approval". Ads show your licence. Email and text marketing follows the rules that apply to you (CASL in Canada, TCPA in the US), and you should confirm them with your own adviser.</li>
<li><b>Time zones:</b> we work Indian time and schedule calls for your morning or evening.</li></ul>
<h2>Next <em>steps</em></h2>
<table class="dt"><thead><tr><th>#</th><th>Action</th><th>By</th></tr></thead><tbody>
<tr><td class="n">1</td><td><b>Discovery call</b> (30 minutes). Suggested: <b>Tue 3 Nov, 10:00 am ET</b> (8:30 pm IST) or <b>Wed 4 Nov, 11:00 am ET</b> (9:30 pm IST).</td><td>Both</td></tr>
<tr><td class="n">2</td><td><b>Send budget range</b>, first markets, and your website link before the call.</td><td>Vinod</td></tr>
<tr><td class="n">3</td><td><b>Final quotation</b> for each business, within 2 working days of the call.</td><td>Qrenzy</td></tr>
<tr><td class="n">4</td><td><b>Start the pilot</b> after the quotation is accepted and the first payment is received.</td><td>Both</td></tr></tbody></table>
<div class="sign"><div><b>For Qrenzy Digital Solutions</b>Sajeesh V S, Proprietor</div><div><b>Noted by Vinod Menon</b>Name and date</div></div>
{foot(3)}</section></body></html>"""
open('Vinod-Menon-Proposal.html','w').write(html)
