import os
from google import genai


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def classify_content(text):

    if not text.strip():
        return "Others"

    prompt = f"""
You are a file classification agent.

Classify the content into exactly ONE category.

Allowed categories:
- Career
- DevOps
- Finance
- Documents
- Others

Content:
{text[:2000]}

Return ONLY the category name.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception as error:

        print(f"AI Classification Error: {error}")

        return None