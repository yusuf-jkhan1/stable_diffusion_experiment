import yaml
from pathlib import Path
import json

CONFIG_FILE = "src/configs/workspace_config.yaml"


def _get_config(config_file):
    with open(config_file) as f:
        config = yaml.load(f, Loader = yaml.FullLoader)
    return config

def _update_concepts_list(config_file):
    config = _get_config(config_file)
    concepts_list = [{
        "instance_prompt":      f"photo of {config['INSTANCE_NAME']} {config['CLASS_NAME']}",
        "class_prompt":         f"photo of a {config['CLASS_NAME']}",
        "instance_data_dir":    f"{Path(config['INSTANCE_DIR_ROOT']).joinpath(config['INSTANCE_NAME'])}",
        "class_data_dir":       f"{Path(config['INSTANCE_DIR_ROOT']).joinpath(config['CLASS_NAME'])}"
    }]
    with open("src/configs/concepts_list.json", "w") as f:
        json.dump(concepts_list, f, indent=4)    

def setup_workspace(config_file=CONFIG_FILE):
    config = _get_config(config_file)
    Path(config['INSTANCE_DIR_ROOT']).joinpath(config['INSTANCE_NAME']).mkdir(parents = True,exist_ok=True)
    Path(config['INSTANCE_DIR_ROOT']).joinpath(config['CLASS_NAME']).mkdir(parents = True,exist_ok=True)
    _update_concepts_list(config_file)
    print("=== Workspace Setup Complete ===")