
from __future__ import annotations

import json

import requests


class OpenAICompatibleClient:
    """Simple client for OpenAI-compatible chat completion APIs."""

    def __init__(
        self,
        api_key: str,
        model_name: str,
        base_url: str = "https://api.openai.com/v1",
    ):
        self.api_key = api_key
        self.model_name = model_name
        self.base_url = base_url.rstrip("/")

    def generate(self, messages: list[dict[str, str]]) -> str:
        """Send conversation messages to the model and return its response."""
        url = f"{self.base_url}/chat/completions"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": self.model_name,
            "messages": messages,
            "temperature": 0.7,
        }

        response = requests.post(
            url,
            headers=headers,
            data=json.dumps(payload),
            timeout=60,
        )
        response.raise_for_status()

        data = response.json()
        return data["choices"][0]["message"]["content"].strip()


class Chatbot:
    """Chatbot that remembers messages during the current session."""

    def __init__(self, client: OpenAICompatibleClient, system_prompt: str):
        self.client = client
        self.messages: list[dict[str, str]] = [
            {
                "role": "system",
                "content": system_prompt,
            }
        ]

    def ask(self, user_message: str) -> str:
        """Send a user message and return the chatbot response."""
        if not user_message or not user_message.strip():
            return "Please enter a message."

        if user_message.strip().lower() in {"exit", "quit", "bye"}:
            return "Goodbye!"

        self.messages.append(
            {
                "role": "user",
                "content": user_message,
            }
        )

        response_text = self.client.generate(self.messages)

        self.messages.append(
            {
                "role": "assistant",
                "content": response_text,
            }
        )

        return response_text
