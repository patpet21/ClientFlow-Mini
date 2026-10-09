# ClientFlow Mini

ClientFlow Mini is a lightweight, offline-first client follow-up and quote manager for independent professionals and small businesses.

## Open the app

Open [ClientFlow-Mini.html](ClientFlow-Mini.html) in a modern desktop or mobile browser. No installation, account, server or subscription is required. If deployed to static hosting, open the [site entry point](index.html).

## Features

- Manage clients and lead stages (New, Contacted, Quoted, Won and Lost)
- Track follow-up dates and urgent tasks
- Create itemized quotes and save them as PDF with **Print → Save as PDF**
- Prepare follow-up emails in your mail application
- Import and export client lists as CSV
- Back up and restore your data with JSON files
- Customize business contact details and quote terms
- Responsive layout for desktop and mobile

## Important limitations

- Records are saved in **this browser's local storage**. They are not synchronized between browsers or devices.
- Deleting browser data or using private/incognito sessions can remove records. Export JSON backups regularly.
- Follow-up emails are **not sent automatically**. The app prepares a draft in your email app.
- Quotes are printable and can be saved to PDF via the browser print dialog; there is no PDF backend.
- No payment gateway or purchase checkout is included.
- This is an early product; validate suitability and your data-handling obligations before using real client data.

## Documentation

- [Quick start (English)](docs/START-HERE-EN.txt)
- [Guida rapida (Italiano)](docs/START-HERE-IT.txt)
- [Prepared sales copy](docs/SALES-COPY-READY.md)
- [Buyer license draft](docs/BUYER-LICENSE-DRAFT.txt) — **draft only, not a definitive legal license**

## Project structure

```text
ClientFlow-Mini.html       Standalone application
index.html                 Static-hosting entry page
docs/                      Documentation and commercial copy
assets/                    Promotional screenshots (where available)
```

**Repository visibility:** This repository is public. Anyone can view and download the source files. Consider private distribution before selling a copy of this app.
