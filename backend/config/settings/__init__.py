import os

env = os.getenv("mode", "development")

if env == "production":
    from .production import *
else:
    from .development import *