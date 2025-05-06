from fastapi import FastAPI
from datetime import datetime
import zoneinfo

app = FastAPI()

@app.get("/api/time/{timezone}")
def get_time(timezone: str):
    try:
        tz = zoneinfo.ZoneInfo(timezone)
        now = datetime.now(tz)
        return {
            "timezone": timezone,
            "datetime": now.isoformat(),
            "utc_offset_hours": now.utcoffset().total_seconds() / 3600,
            "day_of_week": now.strftime("%A"),
            "day_of_year": now.timetuple().tm_yday,
            "unixtime": int(now.timestamp())
        }
    except Exception:
        return {"error": f"Invalid timezone: {timezone}"}

@app.get("/api/timezones")
def list_timezones():
    return sorted(zoneinfo.available_timezones())
