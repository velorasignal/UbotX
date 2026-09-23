from ubotx.chatbot import Chatbot, OpenAICompatibleClient
from ubotx.config import Settings


def main() -> None:
    settings = Settings.from_env().validate()

    client = OpenAICompatibleClient(
        api_key=settings.model_api_key,
        model_name=settings.model_name,
        base_url=settings.model_base_url,
    )

    chatbot = Chatbot(
        client=client,
        system_prompt=settings.system_prompt,
    )

    print("UbotX chatbot ready. Type 'exit' to quit.")

    while True:
        try:
            user_input = input("You: ")
        except KeyboardInterrupt:
            print("\nUbotX: Goodbye!")
            break
        except EOFError:
            print("\nUbotX: Goodbye!")
            break

        if user_input.strip().lower() in {"exit", "quit", "bye"}:
            print("UbotX: Goodbye!")
            break

        try:
            response = chatbot.ask(user_input)
            print(f"UbotX: {response}")
        except Exception as error:
            print(f"UbotX: An error occurred: {error}")


if __name__ == "__main__":
    main()
