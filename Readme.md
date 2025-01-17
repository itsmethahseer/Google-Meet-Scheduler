# Google Meet Scheduler

## Overview
The **Google Meet Scheduler** is a FastAPI-based application that allows users to schedule Google Meet events seamlessly. By leveraging OpenAI's GPT and Google Calendar API, the app extracts meeting details from natural language input and schedules the meeting automatically.

## Features
- Extracts meeting details such as summary, description, start time, and end time from user input using GPT.
- Schedules a Google Meet event on the user's Google Calendar.
- Provides reminders for scheduled events.
- Handles errors gracefully, such as invalid input or time format issues.

## Project Structure
```
Google Meet Scheduler
├── app
│   ├── google_calendar.py  # Handles Google Calendar API interactions
│   ├── gpt_handler.py      # Handles GPT-4 interactions for extracting meeting details
│   ├── main.py             # FastAPI application with endpoints
│   ├── models.py           # Pydantic models for request validation
├── myenv                   # Virtual environment folder
├── .gitignore              # Specifies files and directories to ignore in Git
├── credentials.json        # Google API credentials file
├── requirements.txt        # Python dependencies
├── token.json              # Stores user authentication tokens
```

## Prerequisites
1. Python 3.8 or higher.
2. Google Cloud Platform (GCP) account with access to the Google Calendar API.
3. OpenAI API key for GPT.
4. Virtual environment tool (e.g., `venv` or `virtualenv`).

## Setup

### 1. Clone the Repository
```
git clone <repository-url>
cd google-meet-scheduler
```

### 2. Set Up Virtual Environment
```
python3 -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Configure Google Calendar API
- Enable the Google Calendar API from the [Google Cloud Console](https://console.cloud.google.com/).
- Download the `credentials.json` file and place it in the project root directory.

### 5. Set Up OpenAI API Key
Replace the placeholder in `gpt_handler.py`:
```python
openai.api_key = "Your API key here"
```

### 6. Run the Application
Start the FastAPI server:
```
uvicorn app.main:app --reload
```
The server will be accessible at `http://127.0.0.1:8000`.

## API Endpoint
### `POST /schedule_meeting/`
**Description:** Extracts meeting details from user input and schedules a Google Meet event.

**Request Body:**
```json
{
  "user_input": "Schedule a meeting about project updates on Jan 20, 2025, from 3 PM to 4 PM."
}
```

**Response:**
- **Success (200):**
```json
{
  "message": "Meeting scheduled successfully",
  "event_id": "abcd1234jfi98e4gygjf"
}
```
- **Error (400):**
```json
{
  "detail": "Could not extract meeting details. Please try again."
}
```
- **Error (500):**
```json
{
  "detail": "An unexpected error occurred: <error_message>"
}
```

## Modules
### `google_calendar.py`
Handles Google Calendar API interactions:
- Reads and refreshes user credentials.
- Creates events with reminders and Google Meet links.

### `gpt_handler.py`
Uses GPT-4 to extract meeting details:
- Processes user input to identify summary, description, start time, and end time.
- Returns structured JSON data.

### `main.py`
Defines the FastAPI application:
- Contains the `/schedule_meeting/` endpoint.
- Validates requests and integrates the GPT and Google Calendar modules.

### `models.py`
Defines the Pydantic model for request validation:
```python
class MeetingRequest(BaseModel):
    user_input: str
```

## Error Handling
- **Invalid Input:** Raises an HTTP 400 error if meeting details cannot be extracted.
- **Date Parsing Issues:** Raises an HTTP 400 error if the provided dates are invalid.
- **Google API Errors:** Handles errors such as token expiration or calendar API issues.

## Future Improvements
- Support for custom time zones.
- Integration with additional calendar platforms.
- Enhanced natural language understanding for meeting details extraction.

## Contributing
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed explanation of your changes.

## License
This project is licensed under the MIT License.

## Acknowledgments
- [OpenAI GPT-4](https://openai.com/)
- [Google Calendar API](https://developers.google.com/calendar)

