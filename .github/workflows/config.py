"""ملف الإعدادات"""

import os

# Telegram
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID', '')

# AI APIs
OPENROUTER_API_KEY = os.environ.get('OPENROUTER_API_KEY')
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# Database (Supabase)
SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')

# Bot Settings
DEFAULT_MODEL = "google/gemini-2.5-flash-preview:thinking"
ADMIN_IDS = []  # سنعبئها لاحقاً
