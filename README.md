
# UbotX

A small collaborative AI chatbot starter project built in Python.

## Overview

UbotX is a minimal chatbot project designed to help you and your friend explore AI-powered conversational features together. The initial version focuses on a clean Python structure, environment-based configuration, a simple model interface, and automated checks through GitHub Actions.

## Features

- Terminal-based chatbot interface
- OpenAI-compatible model integration
- Environment-based configuration
- Conversation memory for a single session
- Simple test coverage
- GitHub Actions CI workflow

## Project structure

```text
UbotX/
├── .github/
│   └── workflows/
│       └── blank.yml
├── ubotx/
│   ├── __init__.py
│   ├── config.py
│   ├── chatbot.py
│   └── cli.py
├── tests/
│   └── test_chatbot.py
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── .gitattributes
