import os
from sys import argv
from dotenv import load_dotenv
from google import genai

def main():
    print("Hello from bootdev-ai-agent!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model = 'gemini-2.0-flash-001', \
        contents = f'{argv[1]}' \
    )

    print(f'{response.text}' \
        f'\nPrompt tokens: {response.usage_metadata.prompt_token_count}' \
        f'\nResponse tokens: {response.usage_metadata.candidates_token_count}' \
        )


if __name__ == "__main__":
    main()
