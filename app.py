import os
import uuid
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field

# Load environment variables
load_dotenv()

from sheets import GoogleSheetsManager

app = FastAPI(title="Event Booking API", version="1.0.0")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Google Sheets Manager
sheets_manager = GoogleSheetsManager()

# Simplified events list with flat Rs 1,000 pricing
AVAILABLE_EVENTS = [
    {
        "id": "full-dinner",
        "name": "Full Dinner",
        "price": 1000,
        "price_display": "Rs 1,000",
        "subtitle": "Buffet & plated dinner service",
        "tiers": [{"name": "Standard Pass", "price": "Rs 1,000"}]
    },
    {
        "id": "fine-dining",
        "name": "Fine Dining",
        "price": 1000,
        "price_display": "Rs 1,000",
        "subtitle": "Chef's gourmet multi-course experience",
        "tiers": [{"name": "Standard Pass", "price": "Rs 1,000"}]
    },
    {
        "id": "bar-services",
        "name": "Bar Services",
        "price": 1000,
        "price_display": "Rs 1,000",
        "subtitle": "Cocktails & premium beverage access",
        "tiers": [{"name": "Standard Pass", "price": "Rs 1,000"}]
    }
]

# Pydantic Booking Request Model
class BookingRequest(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone: Optional[str] = Field(default="", max_length=25)
    event_name: str = Field(..., min_length=2)
    ticket_tier: str = Field(default="General Admission")
    ticket_count: int = Field(default=1, ge=1, le=10)
    notes: Optional[str] = Field(default="", max_length=500)


@app.get("/", response_class=HTMLResponse)
async def serve_index():
    index_file = os.path.join(os.path.dirname(__file__), "templates", "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return HTMLResponse("<h1>Event Booking App</h1><p>Template not found.</p>")


@app.get("/api/events")
async def get_events():
    """Returns list of curated events available for booking."""
    return {"events": AVAILABLE_EVENTS}


@app.get("/api/status")
async def get_status():
    """Returns Google Sheets connectivity info and service account/webhook status."""
    is_connected = sheets_manager.is_connected()
    has_webhook = bool(sheets_manager.webhook_url)
    service_email = sheets_manager.get_service_account_email()
    
    mode = "google_sheets_webhook" if has_webhook else ("google_sheets_service_account" if sheets_manager.worksheet else "local_fallback")

    return {
        "status": "online",
        "google_sheets_connected": is_connected,
        "mode": mode,
        "spreadsheet_name": sheets_manager.sheet_name,
        "has_webhook": has_webhook,
        "service_account_email": service_email,
        "instructions": (
            "Connected directly to Google Sheets via Webhook!"
            if has_webhook
            else ("Connected directly to Google Sheets via Service Account!" if is_connected else "Configure GOOGLE_SHEET_WEBHOOK_URL or credentials.json to stream directly into your Google Spreadsheet.")
        )
    }


@app.post("/api/bookings", status_code=201)
async def create_booking(booking: BookingRequest):
    """
    Submits booking form data directly into Google Spreadsheet (or fallback store).
    """
    # Generate clean human-readable booking ID
    unique_suffix = uuid.uuid4().hex[:6].upper()
    booking_id = f"BK-{unique_suffix}"

    booking_data = booking.model_dump()
    booking_data["booking_id"] = booking_id

    result = sheets_manager.append_booking(booking_data)
    
    return {
        "status": "success",
        "message": "Booking successfully confirmed!",
        "booking_id": booking_id,
        "destination": result.get("destination"),
        "timestamp": result.get("timestamp"),
        "booking": {
            "full_name": booking.full_name,
            "email": booking.email,
            "event_name": booking.event_name,
            "ticket_tier": booking.ticket_tier,
            "ticket_count": booking.ticket_count
        }
    }


@app.get("/api/bookings")
async def list_recent_bookings():
    """Retrieve recent bookings for administrative display."""
    return {"bookings": sheets_manager.get_recent_bookings(limit=50)}


@app.get("/spreadsheet", response_class=HTMLResponse)
async def serve_spreadsheet():
    """Serves the Google Sheets style spreadsheet interface."""
    sheet_file = os.path.join(os.path.dirname(__file__), "templates", "spreadsheet.html")
    if os.path.exists(sheet_file):
        return FileResponse(sheet_file)
    return HTMLResponse("<h1>Spreadsheet View</h1>")


@app.get("/api/spreadsheet/data")
async def get_spreadsheet_data():
    """Returns all rows in the spreadsheet."""
    from sheets import HEADERS
    return {
        "headers": HEADERS,
        "rows": sheets_manager.get_all_rows(),
        "total_count": len(sheets_manager.get_all_rows())
    }


@app.get("/api/spreadsheet/download")
async def download_excel():
    """Directly download the Excel .xlsx spreadsheet file."""
    from sheets import XLSX_FILE
    if XLSX_FILE.exists():
        return FileResponse(
            str(XLSX_FILE),
            filename="Event_Bookings_Spreadsheet.xlsx",
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    raise HTTPException(status_code=404, detail="Excel spreadsheet file not generated yet")


@app.get("/api/spreadsheet/csv")
async def download_csv():
    """Directly download the CSV spreadsheet file."""
    from sheets import CSV_FILE
    if CSV_FILE.exists():
        return FileResponse(
            str(CSV_FILE),
            filename="Event_Bookings_Spreadsheet.csv",
            media_type="text/csv"
        )
    raise HTTPException(status_code=404, detail="CSV file not found")


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    print(f"Starting Event Booking App on http://localhost:{port}")
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)
