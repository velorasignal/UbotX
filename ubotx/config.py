
import os
from dataclasses import dataclass

from dotenv import load_dotenv


def load_environment() -> None:
    """Load variables from a local .env file if present."""
    load_dotenv()


@dataclass
class Settings:
    model_api_key: str
    model_name: str = "gpt-4o-mini"
    model_base_url: str = "https://api.openai.com/v1"
    system_prompt: str = "You are UbotX, a helpful assistant."

    @classmethod
    def from_env(cls) -> "Settings":
        load_environment()
        return cls(
            model_api_key=os.getenv("MODEL_API_KEY", ""),
            model_name=os.getenv("MODEL_NAME", "gpt-4o-mini"),
            model_base_url=os.getenv("MODEL_BASE_URL", "https://api.openai.com/v1"),
            system_prompt=os.getenv(
                "SYSTEM_PROMPT",
                "You are UbotX, a helpful assistant.",
            ),
        )

    def validate(self) -> "Settings":
        if not self.model_api_key:
            raise ValueError(
                "MODEL_API_KEY is missing. Add it to your .env file or environment."
            )
        return self
