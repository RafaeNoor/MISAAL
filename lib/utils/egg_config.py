import os

try:
  misaal_env_var = "MISAAL_ROOT_DIR"
  value = os.environ.get(misaal_env_var)
  if value is None:
    raise EnvironmentError(f"MISAAL_ROOT_DIR '{misaal_env_var}' not set.")
  EGG_PKG_PATH = f"{value}/egglog"
except EnvironmentError as e:
  print(f"Error: {e}")