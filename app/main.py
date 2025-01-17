from fastapi import FastAPI, HTTPException
from app.gpt_handler import extract_meeting_details
from app.google_calendar import create_meet
from app.models import MeetingRequest
import datetime

app = FastAPI()

@app.post("/schedule_meeting/")
async def schedule_meeting(request: MeetingRequest):
    """Schedules a meeting based on user input."""
    meeting_details = extract_meeting_details(request.user_input)
    print(meeting_details)
    if not meeting_details:
        raise HTTPException(status_code=400, detail="Could not extract meeting details. Please try again.")

    start_time_str = meeting_details.get("start_time")
    end_time_str = meeting_details.get("end_time")

    try: 
        if start_time_str and end_time_str:
            start_time = datetime.datetime.fromisoformat(start_time_str)
            end_time = datetime.datetime.fromisoformat(end_time_str)

            event_id = create_meet(
                meeting_details.get("summary", "No Summary Provided"),
                meeting_details.get("description", "No Description Provided"),
                start_time,
                end_time,
            )
            if event_id:
                return {"message": "Meeting scheduled successfully", "event_id": event_id}
        else:
            raise ValueError("Start time or end time is missing.")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Error parsing date/time: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")