# 📋 Book My Events — Project Status & Roadmap

> **Current Status**: Core application is fully functional, live-ready, styled in Positivus design, and pushed to GitHub.

---

## ✅ What Has Been Completed

### 1. Architecture & Backend API (`app.py`)
- [x] **FastAPI Server**: High-performance asynchronous Python backend with CORS and clean modular routing.
- [x] **Data Validation**: Strict Pydantic models for payload sanitization (`full_name`, `email`, `phone`, `event_name`, `ticket_tier`, `ticket_count`, `notes`).
- [x] **Booking Generator**: Automatically generates unique, clean booking identifiers (e.g. `BK-43195E`).
- [x] **API Endpoints**:
  - `GET /` — Serves landing page.
  - `GET /api/events` — Returns available dining/event experiences.
  - `GET /api/status` — Checks spreadsheet connection status.
  - `POST /api/bookings` — Submits reservation and appends to spreadsheets.
  - `GET /api/bookings` — Audit list of recent submissions.
  - `GET /spreadsheet` — Live interactive spreadsheet interface.
  - `GET /api/spreadsheet/data` — JSON spreadsheet row data.
  - `GET /api/spreadsheet/download` — Direct download of formatted Excel `.xlsx` file.
  - `GET /api/spreadsheet/csv` — Direct download of `.csv` file.

---

### 2. Dual Spreadsheet Engine (`sheets.py`)
- [x] **Direct Local Excel File (`bookings_spreadsheet.xlsx`)**: Formatted Microsoft Excel spreadsheet with custom green headers, column dimension auto-sizing, and borders.
- [x] **Direct CSV File (`bookings_spreadsheet.csv`)**: Standard comma-separated spreadsheet updated with each booking.
- [x] **In-Browser Interactive Spreadsheet (`/spreadsheet`)**:
  - Complete Google-Sheets-style view with row numbers (1, 2, 3...) and column headers (A–J).
  - Formula bar with active cell coordinate inspector.
  - Search & filter functionality to quickly find attendees.
  - Auto-refreshing grid.
  - 1-click `.xlsx` and `.csv` download buttons.
- [x] **Cloud Google Sheets Bridge**:
  - Integrated support for Google Apps Script Webhooks (`GOOGLE_SHEET_WEBHOOK_URL`).
  - Integrated support for Google Cloud Service Account keys (`credentials.json`).
  - Fail-safe fallback that prevents crashes if cloud keys are omitted.

---

### 3. Frontend & Visual Design (`templates/index.html`)
- [x] **Positivus Aesthetic System**:
  - Soft-brutalist styling with signature Acid Lime (`#B9FF66`), Deep Charcoal (`#191A23`), and Soft Gray (`#F3F3F3`).
  - Google Fonts: **Space Grotesk** (display) and **Inter** (body).
  - Solid 1px black borders, 36px card radii, and 5px neubrutalist drop shadows.
- [x] **Branding**: Official **Book My Events** logo with star icon (`✦ Book My Events`).
- [x] **Pricing Model**: Flat rate of **Rs 1,000 per ticket** across all experiences.
- [x] **Experiences Offered**:
  - 🍽️ **Full Dinner**: Gourmet buffet and plated evening dinner.
  - 🍷 **Fine Dining**: Multi-course chef's tasting gala & wine pairing.
  - 🍸 **Bar Services**: Craft cocktails & open mixology lounge pass.
- [x] **Interactive Booking Form**:
  - Instant experience selector (radio pills).
  - Dynamic ticket quantity counter (`−` / `+`) with real-time total calculation (`Rs 1,000 × Count`).
  - Responsive layout (mobile & desktop friendly).
  - Positivus-style confirmation modal with unique Booking ID.
- [x] **Distraction-Free UI**: Cleaned up all technical/warning banners from visitor view.

---

### 4. Git & Cloud Deployment Setup
- [x] **Git Repository**: Initialized, cleanly structured, and tracked on GitHub.
  - Repository URL: [`https://github.com/aayushkarkiii/Project1`](https://github.com/aayushkarkiii/Project1)
- [x] **Security**: `.gitignore` configured to keep sensitive files (`.env`, `credentials.json`, `venv/`) out of version control.
- [x] **Deployment Configurations**:
  - `Procfile` for platform process definition.
  - `render.yaml` for Render.com blueprint setup.
  - `Dockerfile` configured to dynamically adapt to cloud container ports (`${PORT:-8000}`).
- [x] **Auto-Deploy**: Pushes to `main` branch trigger automated redeployments on Render.

---

## ⏳ What Is Left To Be Done (Suggested Next Steps)

Here are the remaining items and optional enhancements that can be implemented next:

### High Priority
- [ ] **Verify Live Render Deployment**:
  - Open your deployed Render URL (e.g. `https://your-service.onrender.com`) to confirm the live website is accessible worldwide.
- [ ] **Activate Remote Google Sheet Sync** *(Optional)*:
  - If you want submissions to appear on your Google Sheets mobile app in addition to the built-in Excel/browser spreadsheet, deploy the 10-line Apps Script Webhook on your Google Sheet (`1j-G7aIQhe5SxkbXJxraAcYc1WzFJP0yvCJBf8y29FkY`) and add the webhook URL to Render's Environment Variables.

---

### Medium Priority / Product Enhancements
- [ ] **Admin Authentication for Spreadsheet**:
  - Protect `/spreadsheet` with a simple password or login token so the general public cannot view attendee contact details.
- [ ] **Automated Email Confirmations**:
  - Integrate an email service (e.g. SendGrid, Resend, or standard Gmail SMTP) to automatically send booking passes and receipts to attendees after submission.
- [ ] **Date & Time Slot Selection**:
  - Add calendar date selection and time slot pickers if bookings need to be scheduled for specific dates.
- [ ] **Capacity / Seat Limits**:
  - Set a maximum ticket quota per date or experience to prevent overbooking.

---

### Low Priority / Future Polish
- [ ] **Online Payment Gateway Integration**:
  - Integrate Nepali payment gateways (eSewa / Khalti) or international card processing (Stripe) for direct online payments.
- [ ] **Custom Domain**:
  - Attach a custom branded domain (e.g. `bookmyevents.com` or `bookmyevents.com.np`) via Render DNS settings.
- [ ] **PDF Ticket / Pass Generation**:
  - Generate downloadable PDF tickets with QR codes for on-site scanning at the event door.
