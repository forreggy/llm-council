"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

MAX_TOKENS_PER_RESPONSE = 600
MAX_TOKENS_CHAIRMAN     = 1000

# Council members - list of OpenRouter model identifiers
COUNCIL_MODELS = [
    "x-ai/grok-4.1-fast:free",
    "openai/gpt-oss-20b:free",
    "google/gemma-3-27b-it:free",
    "anthropic/claude-sonnet-4.5",
    "tngtech/deepseek-r1t2-chimera:free",
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "x-ai/grok-4.1-fast:free"

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
