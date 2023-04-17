"""Constants for Vacuum Assistant Zones."""

import pathlib
import json

# Base component constants, some loaded directly from the manifest
_LOADER_PATH = pathlib.Path(__loader__.path)
_MANIFEST_PATH = _LOADER_PATH.parent / "manifest.json"
with open(_MANIFEST_PATH, encoding="Latin1") as json_file:
    data = json.load(json_file)
NAME = f"{data['name']}"
DOMAIN = f"{data['domain']}"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = f"{data['version']}"

STARTUP_MESSAGE = "Vacuum Google Assistant Zones started!"
