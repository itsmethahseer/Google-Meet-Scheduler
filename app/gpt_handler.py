import openai
import json

openai.api_key = "You API key here"

def extract_meeting_details(user_input):
    """Extracts meeting details using GPT."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": """
                    You are a helpful assistant designed to extract meeting details from user text.
                    Return a JSON object with the keys: 'summary', 'description', 'start_time', 'end_time'.
                 Example format:
                 {
                   "summary": "Project Update Meeting",
                   "description": "Discussing the progress of the Alpha project.",
                   "start_time": "2024-10-27T10:00:00",
                   "end_time": "2024-10-27T11:00:00"
                 }
                """},
                {"role": "user", "content": user_input},
            ],
            temperature=0,
        )
        generated_text = response['choices'][0]['message']['content'].strip('```json').strip('```')
        return json.loads(generated_text)
    except Exception as e:
        print(f"Error in GPT-4 interaction: {e}")
        return None 