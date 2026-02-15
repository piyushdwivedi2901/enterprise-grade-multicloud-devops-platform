import os

class Config:
    CLOUD_PROVIDER = os.getenv("CLOUD_PROVIDER", "Local")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "Development")
    DEBUG = os.getenv("DEBUG", "False") == "True"
