# 🎟️ Event Booking App with Live Spreadsheet

A lightweight event booking application with a modern single-page HTML interface, a FastAPI backend, and **direct real-time saving into an interactive spreadsheet** (Excel `.xlsx`, `.csv`, and Google-Sheets-style live web interface).

---

## ⚡ How It Works

1. Open the Booking Form at **[http://localhost:8000](http://localhost:8000)**.
2. Fill out attendee details and select an event.
3. Click **Confirm & Book Now**.
4. The details are **instantly written into the spreadsheet**:
   - 📊 **Live Interactive Spreadsheet**: View live at **[http://localhost:8000/spreadsheet](http://localhost:8000/spreadsheet)**.
   - 📗 **Microsoft Excel Spreadsheet**: [`bookings_spreadsheet.xlsx`](file:///home/aayush/Documents/Project/bookings_spreadsheet.xlsx) (formatted with headers, column widths, borders).
   - 📄 **CSV Spreadsheet**: [`bookings_spreadsheet.csv`](file:///home/aayush/Documents/Project/bookings_spreadsheet.csv).

---

## 🚀 Running the App

```bash
./run.sh
```

- **Booking Form**: [http://localhost:8000](http://localhost:8000)
- **Live Spreadsheet View**: [http://localhost:8000/spreadsheet](http://localhost:8000/spreadsheet)
- **Download Excel (.xlsx)**: [http://localhost:8000/api/spreadsheet/download](http://localhost:8000/api/spreadsheet/download)
- **Download CSV**: [http://localhost:8000/api/spreadsheet/csv](http://localhost:8000/api/spreadsheet/csv)

---

## 📁 Spreadsheets Generated

| Column | Header | Description |
|---|---|---|
| A | `Booking ID` | Unique ID (e.g. `BK-7F9A2B`) |
| B | `Timestamp (UTC)` | Date and time submitted |
| C | `Full Name` | Attendee's name |
| D | `Email` | Attendee's email |
| E | `Phone` | Phone number |
| F | `Event` | Selected event name |
| G | `Ticket Tier` | Ticket tier |
| H | `Tickets` | Quantity reserved |
| I | `Special Notes` | Notes / dietary requirements |
| J | `Status` | `Confirmed` |

---

## 🌐 Optional: Sync to Google Drive / Cloud Spreadsheet

If you ever want the data to also stream to a remote Google Cloud Sheet, simply add either in `.env`:
- `GOOGLE_SHEET_WEBHOOK_URL=https://script.google.com/macros/s/.../exec`
- OR put `credentials.json` in the root folder.
