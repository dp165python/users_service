import os


APP_ENV_DEV = "dev"
APP_ENV_PROD = "prod"
APP_ENV_TEST = "test"
AUTH_SERVICE_URI = os.environ.get("AUTH_SERVICE", 'http://localhost:5050/auth/smoke')
