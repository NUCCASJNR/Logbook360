import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


def get_settings_module():
    """
    Detects the environment based on the `MODE` environment variable
    and returns the appropriate Django settings module.
    """
    mode = os.getenv("MODE", "development").lower()
    print(f"MODE: {mode}")
    if mode == "production":
        return "config.settings.production"
    elif mode == "development":
        return "config.settings.development"
    else:
        raise ValueError(f"Unknown MODE: {mode}. Please set MODE to 'development' or 'production'.")
