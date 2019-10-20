import json
from pathlib import Path

CONFIG_PATH = Path("whitercanada.json")


def get_config(section):
    if not CONFIG_PATH.exists():
        print("Missing whitercanada settings file!")
        exit(1)

    with open(CONFIG_PATH) as config:
        config = json.load(config)

    if section in config:
        return config[section]
    else:
        print(f"Unknown section: {section}!")
        exit(2)
