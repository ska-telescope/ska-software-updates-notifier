"""Handles the parsing of the configuration file"""
import os

import yaml

config_dir = os.path.join("/root", ".config", "sun")
config_file = os.path.join(config_dir, "config.yaml")
config = {"metrics": {"port": 9099}, "packages": {"apt": []}}

# Create Config Folder
if not os.path.exists(config_dir):
    os.makedirs(config_dir)

# Create Config File
if not os.path.exists(config_file):
    print(f"Creating default config file in {config_file}")
    with open(config_file, "w", encoding="UTF-8") as yamlfile:
        data = yaml.dump(config, yamlfile)

# Read Config File
with open(config_file, "r", encoding="UTF-8") as yamlfile:
    print(f"Reading config file at {config_file}")
    config = yaml.load(yamlfile, Loader=yaml.FullLoader)

# Validate Config File
if not config.get("metrics"):
    config["metrics"] = {}

if not config["metrics"].get("port"):
    config["metrics"]["port"] = 9099

if not config.get("packages"):
    config["packages"] = {}

if not config["packages"].get("apt"):
    config["packages"]["apt"] = []

if not config["packages"].get("delay"):
    config["packages"]["delay"] = 3600
