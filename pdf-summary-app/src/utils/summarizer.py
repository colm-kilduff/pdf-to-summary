import os
from dotenv import load_dotenv
from together import Together

# Load the API key from the .env file
load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

client = Together(api_key=TOGETHER_API_KEY)


def summarize_text(text: str) -> str:
    """
    Summarize the given text using Together AI's Llama model.
    Try to keep the size of the summary to around 10% of the original text length.
    
    Args:
        text (str): The input text to summarize.
    
    Returns:
        str: The summarized text.
    """
        # Call the Together API with the Llama model
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
        messages=[
            {"role": "system", "content": "You are an AI assistant that summarizes text."},
            {"role": "user", "content": f"Summarize the following text:\n\n{text}"}
        ],
        max_tokens=5000,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        )
    

    return  response.choices[0].message.content