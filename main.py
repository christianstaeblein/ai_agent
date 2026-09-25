import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI



def main():

    #getting command line arguments
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()


    role = "user"
    content = args.user_prompt

    #Getting environmental parameters
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key is None:
        raise RuntimeError("No API key found")


    #Initialising OpenRouter AI
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    #Sending prompt
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": role,
                "content": content,
            }
        ],
    )


    #Printing prompt response and usage to console
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
    print("\n------")
    print(f"\n{role} prompt: {content}")
    print("\n------\n")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
