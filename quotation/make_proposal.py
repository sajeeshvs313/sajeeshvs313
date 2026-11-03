import re
t=open('Intarc-Workflow.html').read()
css=re.search(r'<style>(.*?)</style>',t,re.S).group(1)
def foot(n): return f'<div class="foot"><span><b>Qrenzy Digital Solutions</b> · Thrissur, Kerala</span><span>+91 99057 00600 · info@qrenzy.com · www.qrenzy.com</span><span>Page {n} of 4</span></div>'
html=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Proposal | Digital Marketing for North America | Qrenzy Digital Solutions</title><style>{css}</style></head><body>

<section class="page"><div class="bar"></div>
<div class="top"><img src="logo.png" alt="Qrenzy Digital Solutions"><div class="qt"><h1>PRO<em>POSAL</em></h1><span class="tag">DIGITAL MARKETING · NORTH AMERICA</span></div></div>
<div class="meta"><div><small>Document no.</small><b>QZ-PR-2026-002 (rev 3)</b></div><div><small>Date</small><b>3 Nov 2026</b></div><div><small>Status</small><b>For discussion</b></div></div>
<div class="parties"><div><h3>From</h3><p><b>Qrenzy Digital Solutions</b><br>Sajeesh V S, Proprietor<br>Thrissur, Kerala, India<br>+91 99057 00600 · info@qrenzy.com</p></div>
<div><h3>Prepared for</h3><p><b>Vinod Menon</b><br>Business 1: Canadian immigration services (RCIC)<br>Business 2: Accounting and bookkeeping (new)</p></div></div>
<h2 style="margin-top:2mm">What we <em>understood</em></h2>
<table class="dt"><thead><tr><th style="width:36mm"></th><th>Business 1: Immigration</th><th>Business 2: Accounting / bookkeeping</th></tr></thead><tbody>
<tr><td><b>Who</b></td><td>Established practice. Licensed RCICs.</td><td>New business, starting in the US.</td></tr>
<tr><td><b>Who to reach</b></td><td>People in Canada, the US, the Middle East and possibly India.</td><td>US small businesses, e-commerce sellers and contractors first. Canada later.</td></tr>
<tr><td><b>Today</b></td><td>Has a website and three social pages, reviewed on 3 Nov 2026. See page 3.</td><td>Starting from the beginning.</td></tr>
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
<div class="box"><ul class="terms" style="padding:0"><li>RCIC licence number and the registry link, shown on the ads and the site.</li><li>Access to your website, analytics and ad accounts (ad accounts stay in your name). Viewer access to Google Analytics and Google Search Console is enough to start.</li><li>Who answers new enquiries, and how fast. <b>Fast replies decide whether ad money is wasted.</b></li><li>Feedback on which enquiries became clients.</li></ul></div>
{foot(2)}</section>

<section class="page"><div class="bar"></div>
<h2 style="margin-top:4mm">What we noticed on <em>your website and social pages</em></h2>
<p style="font-size:8.6pt;color:var(--grey);margin-bottom:2mm">Based on an automated SEO scan of the home page (score 59 out of 100), the Contact, Business Immigration, Work in Canada, Visit Canada and Other Services pages, and the public Facebook, Instagram and LinkedIn pages, all viewed on 3 Nov 2026. We have not seen the mobile view, tracking or Search Console data, so this is a first look, to confirm together.</p>
<h2 style="margin-top:1.5mm;font-size:10.5pt">Already working</h2>
<div class="box" style="padding:2mm 5mm"><ul class="terms" style="padding:0"><li>Secure (HTTPS), indexable, correct redirects. Separate pages for each service group, and an enquiry form on every page.</li><li>Clear regulated-professional message ("We work within the frameworks of the regulations"). Calgary address and business hours shown.</li></ul></div>
<h2 style="font-size:10.5pt">Opportunities, in order of priority</h2>
<table class="dt"><thead><tr><th style="width:6mm">#</th><th>What we saw</th><th>Why it matters</th><th>First fix</th></tr></thead><tbody>
<tr><td class="n">1</td><td><b>Contact page email is mistyped</b> (info@entra<b>mm</b>igration.com). The footer has the correct one.</td><td>Enquiries sent to the wrong address are lost.</td><td>Correct it today. Check that the forms deliver.</td></tr>
<tr><td class="n">2</td><td><b>WhatsApp is not connected.</b> Three phone numbers (cell, office, other), no clear main one, no online booking.</td><td>Many clients in the Middle East, India and the US prefer WhatsApp or a booked call.</td><td>One main number, a working WhatsApp button, a consultation booking link.</td></tr>
<tr><td class="n">3</td><td><b>The same banner on every page</b> ("We are a Canadian Immigration Company with clients across the globe"). No H1 and no page-specific headline. Title is 30 characters, description cuts off mid-sentence.</td><td>Each service page does not say what it offers, so Google and visitors cannot tell the pages apart.</td><td>A clear headline and a rewritten title and description for each page.</td></tr>
<tr><td class="n">4</td><td><b>Service pages are one short paragraph each.</b> "Be it Immigration or Studies" is promised, but we did not see a study page.</td><td>Ads need pages that explain who qualifies, steps, documents and FAQs, then ask for a booking.</td><td>Build fuller landing pages, starting with your two best services.</td></tr>
<tr><td class="n">5</td><td><b>Licence and team.</b> The licence logo file name suggests the former regulator (ICCRC), and its link looks broken. Licence numbers and team names are not in the page text (the Facebook cover names two RCIC directors).</td><td>Your licence is your strongest trust signal. It must be current, visible and linked.</td><td>Show the current CICC name, each licence number, the register link and the team.</td></tr>
<tr><td class="n">6</td><td><b>No structured data.</b> 3 images without alt text. 82 requests, 75 of them JavaScript.</td><td>Less clarity for Google, and a heavy page on mobile.</td><td>Add schema and alt text. Speed test on mobile, then clean up.</td></tr>
<tr><td class="n">7</td><td><b>Social pages are almost empty.</b> Facebook: 6 followers, last visible post April 2022, and the page category is "Immigration lawyer". Instagram: 4 followers, no posts. LinkedIn: 6 followers.</td><td>A regulated consultant should not be labelled a lawyer. Cold visitors from ads will look for proof and find little.</td><td>Correct the Facebook category, and update the profiles with the licence, services and a booking link.</td></tr>
</tbody></table>
<div class="note" style="margin:2mm 0"><b>The aim:</b> every advertising dollar should land on a page that explains the service, shows your licence and gets a consultation booked. We would fix the top items first (about two weeks), then build the service pages, then start the pilot.</div>
{foot(3)}</section>

<section class="page"><div class="bar"></div>
<h2 style="margin-top:4mm">Our <em>investment</em> structure</h2>
<p style="font-size:8.8pt;color:var(--grey);margin-bottom:2mm">Amounts will be set after the discovery call, once we know the markets, channels and budget. Each business gets its own quotation.</p>
<table class="dt"><thead><tr><th>Item</th><th>What it covers</th><th class="r">Amount</th></tr></thead><tbody>
<tr><td><b>One-time setup</b></td><td>Tracking, landing pages, booking form, ad account setup, first campaign structure.</td><td class="r"><b>After discovery call</b></td></tr>
<tr><td><b>Monthly management</b></td><td>Campaign creation and optimisation, weekly checks, a monthly report and a monthly call.</td><td class="r"><b>After discovery call</b></td></tr>
<tr><td><b>Advertising budget</b></td><td>Paid by you directly to Google and Meta from your own account. Not part of our fee.</td><td class="r"><b>Set by you</b></td></tr>
<tr><td><b>Website fixes</b></td><td>The first fixes and service landing pages for entraimmigration.com (page 3). Included in setup or quoted as a separate item, to be agreed on the call.</td><td class="r"><b>After discovery call</b></td></tr>
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
<tr><td class="n">1</td><td><b>Discovery call</b> (30 minutes). Suggested: <b>Thu 5 Nov, 10:00 am ET</b> (8:30 pm IST) or <b>Fri 6 Nov, 11:00 am ET</b> (9:30 pm IST).</td><td>Both</td></tr>
<tr><td class="n">2</td><td><b>Send budget range</b>, first markets, and viewer access to Google Analytics and Search Console before the call.</td><td>Vinod</td></tr>
<tr><td class="n">3</td><td><b>Final quotation</b> for each business, within 2 working days of the call.</td><td>Qrenzy</td></tr>
<tr><td class="n">4</td><td><b>Start the pilot</b> after the quotation is accepted and the first payment is received.</td><td>Both</td></tr></tbody></table>
<div class="sign"><div><b>For Qrenzy Digital Solutions</b>Sajeesh V S, Proprietor</div><div><b>Noted by Vinod Menon</b>Name and date</div></div>
{foot(4)}</section></body></html>"""
open('Vinod-Menon-Proposal.html','w').write(html)
