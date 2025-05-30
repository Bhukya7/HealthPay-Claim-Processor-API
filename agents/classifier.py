import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro")

async def classify_document(file_path: str, text: str) -> str:
    prompt = f"""
    Classify the following document as 'bill', 'discharge_summary', or 'id_card'.
    Filename: {file_path}
    Content (first 500 chars): {text[:500]}
    Return only the document type as a single word.
    """
    try:
        response = await model.generate_content_async(prompt)
        return response.text.strip()
    except Exception as e:
        raise Exception(f"Classification failed for {file_path}: {str(e)}")