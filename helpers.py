from typing import Dict

import tomli


def get_toml_data(full_path: str) -> Dict:
    with open(full_path, mode="rb") as fp:
        return tomli.load(fp)