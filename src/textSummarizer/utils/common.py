import os
from box import Box
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object

    Args:
        path_to_yaml (Path): Path to the yaml file

    Raises:
        BoxValueError: If the yaml file is empty

    Returns:
        ConfigBox: ConfigBox object containing the yaml file contents
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise BoxValueError("The YAML file is empty")
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as box_error:
        raise box_error
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list[Path], verbose=True) -> None:
    """Creates a list of directories

    Args:
        path_to_directories (list[Path]): List of paths to directories
        verbose (bool, optional): If True, prints the created directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of a file in KB

    Args:
        path (Path): Path to the file

    Returns:
        str: Size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    return f"{size_in_kb} KB"