import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI



def main():

    #getting command line arguments
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()



    #My variables
    role = "user"
    content = args.user_prompt

    my_messages = [
        {"role": role, "content": args.user_prompt},
    ]


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
        messages=my_messages,
    )


    #Printing prompt response and usage to console
    if args.verbose:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
        print("\n------")
        print(f"User prompt: {content}")
        print("\n------\n")

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
