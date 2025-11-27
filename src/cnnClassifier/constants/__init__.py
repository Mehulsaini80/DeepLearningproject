from pathlib import Path

# Resolve paths relative to the repository root (three levels up from this file)
REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_FILE_PATH = REPO_ROOT / "config" / "config.yaml"
PARAMS_FILE_PATH = REPO_ROOT / "params.yaml"


