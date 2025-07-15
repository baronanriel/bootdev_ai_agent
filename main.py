import os
import sys
from google import genai
from dotenv import load_dotenv
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    try:
        user_prompt = sys.argv[1]
    except:
        print("Fix your prompt")
        sys.exit(1)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model = 'gemini-2.0-flash-001', \
        contents = messages \
    )

    print(f'{response.text}')

    if "--verbose" in sys.argv:
        print(f'\nUser prompt: {user_prompt}' \
            f'\nPrompt tokens: {response.usage_metadata.prompt_token_count}' \
            f'\nResponse tokens: {response.usage_metadata.candidates_token_count}' \
            )


if __name__ == "__main__":
    main()
