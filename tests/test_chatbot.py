from ubotx.chatbot import Chatbot


class FakeClient:
    def __init__(self):
        self.calls = []

    def generate(self, messages):
        self.calls.append(messages)
        return "Hello from the fake model."


def test_chatbot_asks_and_remembers_context():
    fake_client = FakeClient()
    bot = Chatbot(
        client=fake_client,
        system_prompt="You are UbotX.",
    )

    first_reply = bot.ask("Hello")
    second_reply = bot.ask("How are you?")

    assert first_reply == "Hello from the fake model."
    assert second_reply == "Hello from the fake model."

    assert len(bot.messages) == 5
    assert bot.messages[0]["role"] == "system"
    assert bot.messages[1]["role"] == "user"
    assert bot.messages[1]["content"] == "Hello"
    assert bot.messages[2]["role"] == "assistant"
    assert bot.messages[3]["role"] == "user"
    assert bot.messages[3]["content"] == "How are you?"


def test_chatbot_returns_exit_message():
    fake_client = FakeClient()
    bot = Chatbot(
        client=fake_client,
        system_prompt="You are UbotX.",
    )

    result = bot.ask("exit")

    assert result == "Goodbye!"
    assert len(bot.messages) == 1


def test_chatbot_rejects_empty_input():
    fake_client = FakeClient()
    bot = Chatbot(
        client=fake_client,
        system_prompt="You are UbotX.",
    )

    result = bot.ask("   ")

    assert result == "Please enter a message."
    assert len(bot.messages) == 1
