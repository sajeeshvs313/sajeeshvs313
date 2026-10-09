# Home Build Ledger

A simple app to track home construction costs by category, and contractor payments slab by slab.

## Features
- Dashboard: total spent, budget, balance, spending by category and by month
- Expenses: date, category, amount, shop, payment mode; search and filter
- Contractor: contract amount, paid and balance for each slab or stage
- Category-wise budgets
- CSV (Excel) export, backup and restore
- Installable on a phone (PWA) and works offline
- Data stays on the user's device (localStorage)

## Run
Run `python3 -m http.server 8080` in this folder and open http://localhost:8080.
It is a static site, so it can be uploaded as is to Netlify, Vercel or GitHub Pages.
